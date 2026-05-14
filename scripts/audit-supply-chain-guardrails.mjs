#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
let mode = 'advisory';
let json = false;
let failOnWarning = false;
let rootArg = null;

for (const arg of args) {
  if (arg === '--help' || arg === '-h') {
    usage(0);
  } else if (arg === '--json') {
    json = true;
  } else if (arg === '--fail-on-warning') {
    failOnWarning = true;
  } else if (arg.startsWith('--fail-on-warning=')) {
    failOnWarning = parseBoolean(arg.split('=')[1]);
  } else if (arg.startsWith('--mode=')) {
    mode = arg.split('=')[1];
  } else if (arg === '--mode') {
    mode = args[args.indexOf(arg) + 1];
  } else if (!arg.startsWith('--')) {
    rootArg = arg;
  }
}

if (!['advisory', 'ci'].includes(mode)) {
  console.error(`Unsupported --mode=${mode}. Use advisory or ci.`);
  process.exit(2);
}

const root = path.resolve(rootArg || process.cwd());
const findings = { critical: [], warning: [], info: [] };
const skipDirs = new Set([
  '.git', 'node_modules', '.next', 'dist', 'build', 'coverage', '.turbo', '.cache',
  '.claude/worktrees', 'lib', 'dependencies', 'generated', '.tmp', 'broadcast'
]);

function usage(code) {
  console.log(`Usage: node scripts/audit-supply-chain-guardrails.mjs [--mode=advisory|ci] [--json] [--fail-on-warning] [root]\n\nRead-only audit for dependency release-age gates and high-risk GitHub Actions patterns.`);
  process.exit(code);
}

function parseBoolean(value) {
  return ['1', 'true', 'yes', 'on'].includes(String(value).toLowerCase());
}

function add(severity, code, location, message) {
  findings[severity].push({ code, location, message });
}

function rel(file) {
  return path.relative(root, file) || '.';
}

function exists(file) {
  try { return fs.existsSync(file); } catch { return false; }
}

function read(file) {
  try { return fs.readFileSync(file, 'utf8'); } catch { return ''; }
}

function shouldSkipDir(dir) {
  const parts = path.relative(root, dir).split(path.sep).filter(Boolean);
  for (let i = 0; i < parts.length; i++) {
    const suffix = parts.slice(0, i + 1).join('/');
    if (skipDirs.has(parts[i]) || skipDirs.has(suffix)) return true;
  }
  return false;
}

function walk(dir, files = []) {
  if (shouldSkipDir(dir)) return files;
  let entries = [];
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return files; }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full, files);
    } else if (entry.isFile()) {
      files.push(full);
    }
  }
  return files;
}

function findUp(startDir, names) {
  let dir = startDir;
  while (dir.startsWith(root)) {
    for (const name of names) {
      const candidate = path.join(dir, name);
      if (exists(candidate)) return candidate;
    }
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return null;
}

function parsePackageManagerVersion(lockDir, manager) {
  const pkgPath = findUp(lockDir, ['package.json']);
  if (!pkgPath) return null;
  const text = read(pkgPath);
  try {
    const pkg = JSON.parse(text);
    const spec = pkg.packageManager || '';
    if (spec.startsWith(`${manager}@`)) return spec.slice(manager.length + 1).split('+')[0];
    if (manager === 'pnpm' && pkg.engines?.pnpm) return pkg.engines.pnpm;
    if (manager === 'npm' && pkg.engines?.npm) return pkg.engines.npm;
  } catch {}
  return null;
}

function versionTuple(value) {
  const match = String(value || '').match(/(\d+)\.(\d+)\.(\d+)/);
  return match ? match.slice(1).map(Number) : null;
}

function versionLt(value, min) {
  const a = versionTuple(value);
  const b = versionTuple(min);
  if (!a || !b) return false;
  for (let i = 0; i < 3; i++) {
    if (a[i] < b[i]) return true;
    if (a[i] > b[i]) return false;
  }
  return false;
}

function checkReleaseAge() {
  const files = walk(root);
  const roots = new Map();
  for (const file of files) {
    const base = path.basename(file);
    const dir = path.dirname(file);
    if (base === 'bun.lock' || base === 'bun.lockb') addRoot(roots, dir, 'bun', file);
    if (base === 'package-lock.json') addRoot(roots, dir, 'npm', file);
    if (base === 'pnpm-lock.yaml') addRoot(roots, dir, 'pnpm', file);
    if (base === 'yarn.lock') addRoot(roots, dir, 'yarn', file);
  }

  if (roots.size === 0) {
    add('info', 'no-package-roots', '.', 'No package-manager lockfile roots found.');
    return;
  }

  for (const rootInfo of roots.values()) {
    for (const manager of rootInfo.managers) {
      const ok = hasReleaseAge(rootInfo.dir, manager);
      if (!ok) {
        add('critical', 'missing-release-age-gate', rel(rootInfo.dir), `${manager} root has a lockfile but no 3-day release-age gate in the nearest supported config.`);
      } else {
        add('info', 'release-age-gate-present', rel(rootInfo.dir), `${manager} release-age gate detected.`);
      }
      warnUnsupportedPackageManager(rootInfo.dir, manager);
    }
  }
}

function addRoot(roots, dir, manager, file) {
  const key = dir;
  if (!roots.has(key)) roots.set(key, { dir, managers: new Set(), files: [] });
  roots.get(key).managers.add(manager);
  roots.get(key).files.push(file);
}

function hasReleaseAge(lockDir, manager) {
  if (manager === 'bun') {
    const cfg = findUp(lockDir, ['bunfig.toml']);
    const text = cfg ? read(cfg) : '';
    return /minimumReleaseAge\s*=\s*(\d+)/.test(text) && Number(text.match(/minimumReleaseAge\s*=\s*(\d+)/)?.[1] || 0) >= 259200;
  }
  if (manager === 'npm') {
    const cfg = findUp(lockDir, ['.npmrc']);
    const text = cfg ? read(cfg) : '';
    return /(?:^|\n)\s*min-release-age\s*=\s*(\d+)/.test(text) && Number(text.match(/min-release-age\s*=\s*(\d+)/)?.[1] || 0) >= 3;
  }
  if (manager === 'pnpm') {
    const npmrc = findUp(lockDir, ['.npmrc']);
    const workspace = findUp(lockDir, ['pnpm-workspace.yaml']);
    const text = `${npmrc ? read(npmrc) : ''}\n${workspace ? read(workspace) : ''}`;
    const kebab = Number(text.match(/minimum-release-age\s*=\s*(\d+)/)?.[1] || 0);
    const camel = Number(text.match(/minimumReleaseAge\s*:\s*(\d+)/)?.[1] || 0);
    return kebab >= 4320 || camel >= 4320;
  }
  if (manager === 'yarn') {
    const cfg = findUp(lockDir, ['.yarnrc.yml']);
    const text = cfg ? read(cfg) : '';
    const match = text.match(/npmMinimalAgeGate\s*:\s*['"]?([^'"\n#]+)/);
    if (!match) return false;
    const value = match[1].trim();
    if (/^\d+\s*d$/.test(value)) return Number(value.match(/\d+/)[0]) >= 3;
    if (/^\d+$/.test(value)) return Number(value) >= 4320;
    return false;
  }
  return false;
}

function warnUnsupportedPackageManager(lockDir, manager) {
  const version = parsePackageManagerVersion(lockDir, manager);
  if (!version) return;
  const minimums = { bun: '1.3.0', pnpm: '10.16.0', yarn: '4.10.0', npm: '11.10.0' };
  if (minimums[manager] && versionLt(version, minimums[manager])) {
    add('warning', 'package-manager-version-may-not-enforce-release-age', rel(lockDir), `${manager} version ${version} may not enforce release-age gates. Config is present, but enforcement may require a future package-manager upgrade.`);
  }
}

function oidcExposedToPullRequest(text) {
  const beforeJobs = text.split(/\njobs\s*:/)[0] || '';
  if (/id-token\s*:\s*write/.test(beforeJobs)) return true;

  const lines = text.split(/\r?\n/);
  for (let index = 0; index < lines.length; index++) {
    if (!/id-token\s*:\s*write/.test(lines[index])) continue;
    const context = lines.slice(Math.max(0, index - 30), index + 1).join('\n');
    if (/github\.event_name\s*==\s*['"](?:push|workflow_dispatch|release)['"]/.test(context)) continue;
    if (/github\.event_name\s*!=\s*['"]pull_request['"]/.test(context)) continue;
    if (/github\.ref_type\s*==\s*['"]tag['"]/.test(context)) continue;
    if (/startsWith\(github\.ref,\s*['"]refs\/heads\/release\//.test(context)) continue;
    return true;
  }
  return false;
}

function checkWorkflows() {
  const workflowDir = path.join(root, '.github', 'workflows');
  if (!exists(workflowDir)) {
    add('info', 'no-workflows', '.github/workflows', 'No GitHub Actions workflow directory found.');
    return;
  }
  const workflows = walk(workflowDir).filter((file) => /\.ya?ml$/.test(file));
  for (const file of workflows) {
    const text = read(file);
    const location = rel(file);
    const hasPullRequest = /(^|\n)\s*pull_request\s*:/.test(text);
    const hasPullRequestTarget = /(^|\n)\s*pull_request_target\s*:/.test(text);
    const hasIdTokenWrite = /id-token\s*:\s*write/.test(text);
    const hasPublish = /(npm|pnpm|bun)\s+publish\b|yarn\s+npm\s+publish\b|twine\s+upload\b|poetry\s+publish\b|uv\s+publish\b/.test(text);
    const hasSecrets = /secrets\.[A-Z0-9_]+/.test(text);
    const hasActionsCache = /uses:\s*actions\/cache@|cache:\s*["']?(npm|pnpm|yarn|bun)["']?|hashFiles\s*\(/.test(text);
    const hasReleaseLike = /(^|\n)\s*(release|workflow_dispatch)\s*:|refs\/tags|github\.ref_type\s*==\s*'tag'/.test(text);

    if (hasPullRequestTarget) {
      add('critical', 'pull-request-target', location, '`pull_request_target` runs in the base repository context and must not process untrusted fork code.');
    }
    if (hasPullRequest && oidcExposedToPullRequest(text)) {
      add('critical', 'oidc-in-pr-workflow', location, '`pull_request` workflow grants `id-token: write` without an explicit non-PR job boundary; move OIDC to protected push/tag/release workflows.');
    }
    if (hasPullRequest && hasPublish) {
      add('critical', 'publish-in-pr-workflow', location, '`pull_request` workflow contains a package publish command. Publish must be restricted to protected release contexts.');
    }
    if (hasPullRequest && hasSecrets) {
      add('warning', 'secrets-in-pr-workflow', location, '`pull_request` workflow references repository secrets. Verify every secret-consuming job is unavailable to untrusted PR code or has safe fallbacks.');
    }
    if (hasPullRequest && hasActionsCache && hasReleaseLike) {
      add('critical', 'cache-shared-with-release-context', location, 'Workflow combines PR triggers, cache usage, and release-like context. Split untrusted PR cache from release/publish paths.');
    } else if (hasPullRequest && hasActionsCache) {
      add('warning', 'cache-in-pr-workflow', location, 'PR workflow uses dependency caches. Keep cache keys lockfile-scoped and separate from release/publish jobs.');
    }
  }
}

checkReleaseAge();
checkWorkflows();

if (json) {
  console.log(JSON.stringify({ root, mode, findings }, null, 2));
} else {
  printHuman();
}

const criticalCount = findings.critical.length;
const warningCount = findings.warning.length;
if (mode === 'ci' && (criticalCount > 0 || (failOnWarning && warningCount > 0))) {
  process.exit(1);
}
process.exit(0);

function printHuman() {
  console.log(`Supply-chain guardrails audit: ${root}`);
  for (const severity of ['critical', 'warning', 'info']) {
    const list = findings[severity];
    console.log(`\n${severity.toUpperCase()} (${list.length})`);
    if (list.length === 0) {
      console.log('  none');
      continue;
    }
    for (const finding of list) {
      console.log(`  - [${finding.code}] ${finding.location}: ${finding.message}`);
    }
  }
}
