#!/usr/bin/env node
// agents-doctor: checks that a repository follows the shared agent kit.
//
//   node agents-doctor.mjs [--json] [--strict | --advisory] <repo>...
//
// One file with no dependencies, so the same script runs locally through
// `dev agents doctor` and in CI through the guild's reusable workflow
// (greenpill-dev-guild/.github, .github/workflows/agents-doctor.yml). The
// source of truth is dev-surfaces/agents/kit/doctor/agents-doctor.mjs; the
// guild copy must stay byte-identical.
//
// Each check is "fail" (the kit's contract is broken) or "warn" (part of the
// kit not adopted yet). By default only failures set a non-zero exit, so a
// repository can adopt the kit step by step from its printed baseline; --strict
// fails on warnings too, and --advisory only reports. Under GitHub Actions each
// failure and warning is also printed as an annotation.
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const read = (file) => {
  try {
    return fs.readFileSync(file, 'utf8');
  } catch {
    return null;
  }
};
const lstat = (p) => {
  try {
    return fs.lstatSync(p);
  } catch {
    return null;
  }
};

function realDir(p) {
  try {
    return fs.realpathSync(p);
  } catch {
    return null;
  }
}

const EM_DASH = String.fromCharCode(0x2014);

export const CHECKS = [
  {
    id: 'agents-md',
    title: 'AGENTS.md is the repository guide',
    run(repo) {
      const text = read(path.join(repo, 'AGENTS.md'));
      if (text === null) return { status: 'fail', detail: 'no AGENTS.md at the repository root' };
      return { status: 'ok', detail: `${text.split('\n').length} lines` };
    },
  },
  {
    id: 'claude-md-import',
    title: 'CLAUDE.md only imports AGENTS.md',
    run(repo) {
      const file = path.join(repo, 'CLAUDE.md');
      const st = lstat(file);
      if (!st) return { status: 'ok', detail: 'no CLAUDE.md (Claude reads AGENTS.md)' };
      if (st.isSymbolicLink()) {
        const target = realDir(file);
        return target && path.basename(target) === 'AGENTS.md' ? { status: 'ok', detail: 'a link to AGENTS.md' } : { status: 'fail', detail: 'a link to something other than AGENTS.md' };
      }
      const lines = (read(file) || '').split('\n').map((l) => l.trim()).filter((l) => l && !l.startsWith('<!--'));
      if (lines.some((l) => /^@\.?\/?AGENTS\.md$/.test(l))) {
        const extra = lines.filter((l) => !/^@\.?\/?AGENTS\.md$/.test(l));
        return extra.length <= 20 ? { status: 'ok', detail: extra.length ? `imports AGENTS.md plus ${extra.length} Claude-only line(s)` : 'one-line import' } : { status: 'warn', detail: `imports AGENTS.md but adds ${extra.length} lines of its own` };
      }
      return { status: 'fail', detail: `a standalone ${lines.length}-line CLAUDE.md that does not import AGENTS.md` };
    },
  },
  {
    id: 'skills-single-copy',
    title: 'One skills folder: .agents/skills, with .claude/skills linking to it',
    run(repo) {
      const agents = path.join(repo, '.agents', 'skills');
      const claude = path.join(repo, '.claude', 'skills');
      const a = lstat(agents);
      const c = lstat(claude);
      if (!a && !c) return { status: 'warn', detail: 'no repository skills folder' };
      if (a && c) {
        if (realDir(agents) === realDir(claude)) return { status: 'ok', detail: `${a.isSymbolicLink() ? '.agents/skills links to .claude/skills' : '.claude/skills links to .agents/skills'}` };
        return { status: 'fail', detail: 'two real skills folders, .agents/skills and .claude/skills, which drift apart' };
      }
      if (c && !a) return { status: 'warn', detail: 'skills only in .claude/skills, so Codex cannot see them' };
      return { status: 'warn', detail: 'skills only in .agents/skills; add the .claude/skills link for Claude Code' };
    },
  },
  {
    id: 'rule-enforcer-table',
    title: 'AGENTS.md lists its rules with their enforcers',
    run(repo) {
      const text = read(path.join(repo, 'AGENTS.md')) || '';
      return /\|\s*Rule\s*\|\s*Enforcer\s*\|/i.test(text) ? { status: 'ok', detail: 'has a rule and enforcer table' } : { status: 'warn', detail: 'no "| Rule | Enforcer |" table' };
    },
  },
  {
    id: 'no-em-dash',
    title: 'Agent guidance has no em dash',
    run(repo) {
      const hits = ['AGENTS.md', 'CLAUDE.md'].filter((f) => (read(path.join(repo, f)) || '').includes(EM_DASH));
      return hits.length ? { status: 'warn', detail: `em dash in ${hits.join(', ')}` } : { status: 'ok', detail: 'none' };
    },
  },
  {
    id: 'policy-json',
    title: '.agents/policy.json is valid when present',
    run(repo) {
      const text = read(path.join(repo, '.agents', 'policy.json'));
      if (text === null) return { status: 'warn', detail: 'no .agents/policy.json (repository rules for the shared guards)' };
      let doc;
      try {
        doc = JSON.parse(text);
      } catch (error) {
        return { status: 'fail', detail: `invalid JSON: ${error.message}` };
      }
      const errors = [];
      if (doc.version !== 1) errors.push('version must be 1');
      for (const [i, r] of (doc.commands || []).entries()) {
        if (!r.id || !r.message || !['block', 'ask'].includes(r.action) || (!Array.isArray(r.prefix) && typeof r.pattern !== 'string')) errors.push(`commands[${i}] needs id, message, action block|ask and prefix or pattern`);
      }
      for (const [i, r] of (doc.paths || []).entries()) {
        if (!r.id || !r.message || typeof r.glob !== 'string' || !['block', 'notice'].includes(r.action)) errors.push(`paths[${i}] needs id, message, glob and action block|notice`);
      }
      return errors.length ? { status: 'fail', detail: errors.join('; ') } : { status: 'ok', detail: `${(doc.commands || []).length} command and ${(doc.paths || []).length} path rule(s)` };
    },
  },
  {
    id: 'hooks-read-stdin',
    title: 'Hooks read their event from stdin, not CLAUDE_* variables',
    run(repo) {
      const files = ['.claude/settings.json', '.codex/hooks.json'].map((f) => path.join(repo, f)).filter((f) => fs.existsSync(f));
      const scripts = [];
      for (const dir of ['.claude/hooks', '.codex/hooks']) {
        try {
          for (const name of fs.readdirSync(path.join(repo, dir))) scripts.push(path.join(repo, dir, name));
        } catch {}
      }
      const dead = [...files, ...scripts].filter((f) => /\$\{?CLAUDE_(TOOL_INPUT|FILE_PATH|TOOL_NAME)\b/.test(read(f) || ''));
      return dead.length ? { status: 'fail', detail: `reads variables current hooks never set: ${dead.map((f) => path.relative(repo, f)).join(', ')}` } : { status: 'ok', detail: `${files.length + scripts.length} hook file(s) checked` };
    },
  },
  {
    id: 'codex-profiles',
    title: 'Codex config has no legacy [profiles.*] tables',
    run(repo) {
      const text = read(path.join(repo, '.codex', 'config.toml'));
      if (text === null) return { status: 'ok', detail: 'no .codex/config.toml' };
      if (/^\s*\[profiles\./m.test(text)) return { status: 'fail', detail: 'legacy [profiles.*] tables, which Codex 0.167 refuses with --profile' };
      return { status: 'ok', detail: 'no legacy profiles' };
    },
  },
  {
    id: 'pr-template',
    title: 'The PR template asks for Why, Measured, Verification, Not verified',
    run(repo) {
      const candidates = ['.github/pull_request_template.md', '.github/PULL_REQUEST_TEMPLATE.md', 'pull_request_template.md', 'docs/pull_request_template.md'];
      const text = candidates.map((f) => read(path.join(repo, f))).find((t) => t !== null);
      if (text === undefined) return { status: 'warn', detail: 'no pull request template' };
      const missing = ['Why', 'Measured', 'Verification', 'Not verified'].filter((s) => !new RegExp(`^#+\\s*${s}\\b`, 'im').test(text));
      return missing.length ? { status: 'warn', detail: `template lacks: ${missing.join(', ')}` } : { status: 'ok', detail: 'all four sections' };
    },
  },
  {
    id: 'codeowners',
    title: 'CODEOWNERS covers the critical paths',
    run(repo) {
      const found = ['.github/CODEOWNERS', 'CODEOWNERS', 'docs/CODEOWNERS'].find((f) => fs.existsSync(path.join(repo, f)));
      return found ? { status: 'ok', detail: found } : { status: 'warn', detail: 'no CODEOWNERS' };
    },
  },
  {
    id: 'merge-policy',
    title: '.agents/merge-policy.json states the merge tiers',
    run(repo) {
      const text = read(path.join(repo, '.agents', 'merge-policy.json'));
      if (text === null) return { status: 'warn', detail: 'no .agents/merge-policy.json' };
      try {
        const doc = JSON.parse(text);
        const tiers = Object.keys(doc.tiers || {});
        return ['critical', 'sensitive', 'routine'].every((t) => tiers.includes(t)) ? { status: 'ok', detail: `merge method ${doc.mergeMethod}, auto-merge ${doc.autoMerge}` } : { status: 'fail', detail: 'tiers must name critical, sensitive and routine' };
      } catch (error) {
        return { status: 'fail', detail: `invalid JSON: ${error.message}` };
      }
    },
  },
  {
    id: 'skill-adapter',
    title: 'Kit skills have their repository adapter',
    run(repo) {
      // A kit skill is one of the five shared skills that reads .agents/adapter.md;
      // a repository's own skill of the same name does not count.
      const kit = ['review', 'debug', 'plan', 'ship', 'research'].filter((name) =>
        ['.agents/skills', '.claude/skills'].some((dir) => /\.agents\/adapter\.md/.test(read(path.join(repo, dir, name, 'SKILL.md')) || '')));
      if (!kit.length) return { status: 'ok', detail: 'no kit skills, so no adapter needed' };
      const text = read(path.join(repo, '.agents', 'adapter.md'));
      if (text === null) return { status: 'warn', detail: `${kit.join(', ')} read .agents/adapter.md, which is missing, so they run on their defaults` };
      const missing = ['checks', ...kit].filter((section) => !new RegExp(`^## ${section}\\s*$`, 'm').test(text));
      return missing.length ? { status: 'warn', detail: `.agents/adapter.md has no ${missing.map((s) => `## ${s}`).join(', ')}` } : { status: 'ok', detail: `sections for ${kit.join(', ')}` };
    },
  },
];

export function doctor(repo) {
  const root = path.resolve(repo);
  if (!fs.existsSync(root)) return { repo: root, missing: true, results: [] };
  return { repo: root, results: CHECKS.map((check) => ({ id: check.id, title: check.title, ...check.run(root) })) };
}

export function summarize(reports) {
  return reports.map((r) => ({
    repo: r.repo,
    missing: Boolean(r.missing),
    fail: r.results.filter((x) => x.status === 'fail').map((x) => x.id),
    warn: r.results.filter((x) => x.status === 'warn').map((x) => x.id),
  }));
}

export function main(argv = process.argv.slice(2)) {
  const json = argv.includes('--json');
  const strict = argv.includes('--strict');
  const advisory = argv.includes('--advisory');
  const repos = argv.filter((a) => !a.startsWith('--'));
  if (!repos.length) repos.push('.');
  const reports = repos.map(doctor);
  if (json) {
    console.log(JSON.stringify({ reports, summary: summarize(reports) }, null, 2));
  } else {
    for (const report of reports) {
      console.log(`\n${report.repo}${report.missing ? ': not on this disk' : ''}`);
      for (const r of report.results) console.log(`  ${r.status === 'ok' ? 'ok  ' : r.status === 'warn' ? 'warn' : 'FAIL'} ${r.id}: ${r.detail}`);
    }
    if (reports.length > 1) {
      console.log('\nBaseline');
      for (const s of summarize(reports)) console.log(`  ${path.basename(s.repo).padEnd(22)} fail ${String(s.fail.length).padStart(2)}  warn ${String(s.warn.length).padStart(2)}${s.fail.length ? `  (${s.fail.join(', ')})` : ''}`);
    }
  }
  if (process.env.GITHUB_ACTIONS === 'true') {
    for (const report of reports) {
      if (report.missing) console.log(`::error title=agents-doctor::${report.repo} is not on this disk`);
      for (const r of report.results) if (r.status !== 'ok') console.log(`::${r.status === 'fail' ? 'error' : 'warning'} title=agents-doctor ${r.id}::${r.detail}`);
    }
  }
  if (advisory) return 0;
  const failed = reports.some((r) => r.missing || r.results.some((x) => x.status === 'fail' || (strict && x.status === 'warn')));
  return failed ? 1 : 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(fs.realpathSync(process.argv[1])).href) process.exitCode = main();
