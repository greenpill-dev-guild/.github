# AGENTS.md

This repository is the org-level `.github` defaults repo for `greenpill-dev-guild`. Changes here can affect the contributor experience across the guild.

## Scope

- This repo is documentation-first: markdown docs, issue-form YAML, templates, and existing reusable workflow YAML are the normal edit surface.
- New `.github/workflows/` files, composite actions, executable scripts, or automation config require explicit user approval.

## Repo invariants

- Linear is the project-management source of truth. GitHub owns public execution/RFCs/code review, Drive owns memos and evidence, and Discord/Telegram/calls own discussion.
- Do not reintroduce the former dev-guild PM URL or old migration language for project-management state.
- Bun is the recommended default for new JavaScript repos, but inherited guidance must stay stack-neutral for existing repos.
- Use GitHub issue types (`Bug`, `Story`, `Epic`, `Task`) for work classification; labels are for cross-cutting dimensions, sources, routines, and automation state.
- Do not introduce guild-wide "Season" framing.
- Do not describe the dev guild as the entire Greenpill Network.
- Keep cross-references synchronized: `routines/README.md` must match `routines/`, and `adr/README.md` must match `adr/`.
- Avoid growth-hacking and trend-chasing voice: no FOMO, virality, leaderboards, streaks, or "AI-first" framing.
- Treat contact emails, disclosure SLAs, payout timing, and governance claims as sensitive public commitments. Do not change them casually.

## Supply-chain and agent safety

- Do not install or upgrade npm, Python, or package-manager dependencies unless the user explicitly approves that install in the current task.
- Prefer existing repo tooling, checked-in lockfiles, and standard library options over adding new packages.
- Treat `package.json`, lockfiles, package-manager config, `.github/workflows/**`, `AGENTS.md`, `CLAUDE.md`, `.codex/**`, and `.claude/**` as security-sensitive surfaces. Call out any changes to them in final summaries.
- Keep dependency installs on the checked-in lockfile path and preserve the repo's release-age gate configuration.

## Criticality

- **Critical**: `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `SUPPORT.md`, `profile/README.md`, `.github/ISSUE_TEMPLATE/*`, `.github/PULL_REQUEST_TEMPLATE.md`
- **Sensitive**: `templates/*`, `adr/*`
- **Routine**: `routines/*`, `README.md`

## Validation

Use the lightest honest checks that prove the docs still hold together:

```bash
rg -n "app\\.charmverse\\.io|greenpill\\.network/dev-guild|FOMO|virality|leaderboards|streaks|AI-first" .
# Also run a stale-term search for the former dev-guild PM URL,
# retired funded-work file names, old GitHub grant lifecycle labels,
# and retired Claude routine filenames.
python3 - <<'PY'
from pathlib import Path
import re

root = Path(".").resolve()
files = [p for p in root.rglob("*") if p.is_file() and p.suffix in {".md", ".yml"} and ".git" not in p.parts]
pat = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

for p in files:
    for match in pat.finditer(p.read_text()):
        target = match.group(1).split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (p.parent / target).resolve()
        if not resolved.exists():
            raise SystemExit(f"Broken relative link in {p.relative_to(root)} -> {target}")

print("relative links ok")
PY
```

## Working agreements

- Read the surrounding docs before changing shared language.
- If you change a process doc, update the index or cross-reference in the same pass.
- Prefer tightening wording over adding more prose.
- When a claim is uncertain, soften it or link the source instead of presenting it as settled fact.
- For browser-facing templates or repo guidance, require local agentic browser QA to use the user's authenticated Brave QA profile. Codex-facing guidance should use the Codex browser-extension path and claim the already-open Brave tab. Claude-facing guidance should use the Claude Code Chrome/Chromium extension path (`claude --chrome` or `/chrome`) and select the authenticated Brave profile/tab when the extension is installed and connected. Do not fall back merely because the extension is branded Chrome; use Claude computer-use/visible desktop control only when the Brave extension path is unavailable or not connected.
- Isolated Browser/Playwright/DevTools proof may be documented only as CI/clean-room proof, never as local authenticated QA. If QA-profile access is blocked, guidance should tell agents to report QA as blocked instead of substituting isolated proof.
