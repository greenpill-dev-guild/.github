# AGENTS.md

This repository is the org-level `.github` defaults repo for `greenpill-dev-guild`. Changes here can affect the contributor experience across the guild.

## Scope

- This repo is documentation-first: markdown docs, issue-form YAML, templates, and existing reusable workflow YAML are the normal edit surface.
- New `.github/workflows/` files, composite actions, executable scripts, or automation config require explicit user approval.

## Repo invariants

- Every human-facing reference to the guild workspace uses `greenpill.app/dev-guild` with the qualifier `coming soon — currently on Charmverse during migration`, unless the field is URL-only.
- Do not conflate the workspace migration with the org's `charmverse` fork.
- Bun is the recommended default for new JavaScript repos, but inherited guidance must stay stack-neutral for existing repos.
- Use GitHub issue types (`Bug`, `Story`, `Epic`, `Task`) for work classification; labels are for cross-cutting dimensions, sources, routines, and automation state.
- Do not introduce guild-wide "Season" framing.
- Do not describe the dev guild as the entire Greenpill Network.
- Keep cross-references synchronized: `routines/README.md` must match `routines/`, and `adr/README.md` must match `adr/`.
- Avoid growth-hacking and trend-chasing voice: no FOMO, virality, leaderboards, streaks, or "AI-first" framing.
- Treat contact emails, disclosure SLAs, payout timing, and governance claims as sensitive public commitments. Do not change them casually.

## Criticality

- **Critical**: `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `SUPPORT.md`, `profile/README.md`, `.github/ISSUE_TEMPLATE/*`, `.github/PULL_REQUEST_TEMPLATE.md`
- **Sensitive**: `templates/*`, `adr/*`
- **Routine**: `routines/*`, `README.md`

## Validation

Use the lightest honest checks that prove the docs still hold together:

```bash
rg -n "app\\.charmverse\\.io|greenpill\\.network/dev-guild|FOMO|virality|leaderboards|streaks|AI-first" .
rg -n "greenpill\\.app/dev-guild" .
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
