# CLAUDE.md

This file gives Claude Code repo-specific guidance for `greenpill-dev-guild/.github`.

## Project

**Name**: greenpill-dev-guild/.github  
**Purpose**: Org defaults, public profile content, and shared guild contributor guidance  
**Status**: active

## Commands

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

## Architecture

This repo is documentation-first. Top-level community-health files and `.github/ISSUE_TEMPLATE/*` define org defaults. `.github/workflows/*` holds opt-in reusable workflows that consumer repos must call explicitly. `profile/README.md` renders on the public org page. `templates/` holds copy-into-repo starters, `routines/` holds guild playbooks, and `adr/` records guild-level architectural decisions.

## Key principles

1. Keep docs and default files lightweight; do not add new workflows, scripts, or automation config unless the user explicitly expands scope.
2. Treat shared wording as product surface: migration language, payout timing, disclosure SLA, and governance claims must stay consistent across files.
3. Keep the guild voice grounded in public goods, transparency, and building in public; avoid hype framing.
4. When process docs drift, fix the cross-reference at the same time instead of leaving two truths in the repo.

## Criticality matrix

- **`critical`**
  - `CONTRIBUTING.md`
  - `GOVERNANCE.md`
  - `SECURITY.md`
  - `SUPPORT.md`
  - `profile/README.md`
  - `.github/ISSUE_TEMPLATE/*`
  - `.github/PULL_REQUEST_TEMPLATE.md`
- **`sensitive`**
  - `templates/*`
  - `adr/*`
- **`routine`**
  - `routines/*`
  - `README.md`
  - `AGENTS.md`
  - `CLAUDE.md`

## Patterns to follow

- Use absolute GitHub URLs in `profile/README.md` for links back into this repo.
- Name Linear as the project-management source of truth; use GitHub for public execution/RFCs/code review, Drive for memos/evidence, and Discord/Telegram/calls for discussion.
- Use GitHub issue types (`Bug`, `Story`, `Epic`, `Task`) for work classification; avoid labels that duplicate issue type.
- If a doc tells someone to "open" an issue or RFC, link to the issue-creation flow, not just the source template file.
- When updating a directory's contents, update its index README in the same change.

## Investigate before answering

Read the actual files you reference. This repo is mostly cross-linked prose; small wording mistakes create real drift.

## Subagent discipline

Work directly for single-file or tightly related doc edits. Only split work when the user explicitly asks for parallel agent help.

## Scope discipline

- Do not add new workflows, scripts, or automation config without explicit approval.
- Do not introduce new contact emails, SLAs, or governance structures based on guesswork.
- For destructive edits to shared guidance, describe the change clearly in the PR or final summary.
