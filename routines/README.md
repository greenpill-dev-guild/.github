# Routines

> Markdown playbooks for guild-wide flows — bounties, check-ins, onboarding, retros, grants, workshops, meetings, and more.

These are **documentation, not enforcement**. Each playbook describes how the guild has agreed to handle a recurring flow. Anyone in the guild can adopt or adapt them; project teams can override locally as needed.

Distinct from [`claude/`](./claude/) — that subfolder holds source-of-truth prompts for **scheduled Claude automations** (daily synthesis, grant scouting, meeting-notes ingestion, weekly check-in digest). The playbooks here describe manual guild processes; the Claude routines automate specific slices of them.

## Index

### Working with the guild

- [bounty-intake.md](./bounty-intake.md) — End-to-end bounty flow from "I see an opportunity" to "I got paid"
- [weekly-checkin.md](./weekly-checkin.md) — How the 15-minute weekly check-ins work and what they're for
- [newcomer-onboarding.md](./newcomer-onboarding.md) — First-week path for new contributors

### Operations

- [grant-application.md](./grant-application.md) — Drafting and submitting grant applications (Octant, Gitcoin, Giveth, etc.)
- [workshop-prep.md](./workshop-prep.md) — Running a guild workshop end to end
- [meeting-notes.md](./meeting-notes.md) — Capturing, processing, and acting on meeting notes
- [retro-cadence.md](./retro-cadence.md) — Quarterly and annual retrospectives

### Tooling and process

- [drive-orchestration.md](./drive-orchestration.md) — Shared Drive folder taxonomy and sorting flow
- [responsible-disclosure.md](./responsible-disclosure.md) — How we handle security disclosures from external researchers

### Automated (Claude routines)

- [claude/guild-daily-synthesis.md](./claude/guild-daily-synthesis.md) — Daily 08:30 Discord synthesis across 6 guild channels; brief ready by 09:00
- [claude/guild-grant-scout.md](./claude/guild-grant-scout.md) — Weekly Wednesday 19:00 grant scouting across 5 active projects
- [claude/guild-meeting-notes.md](./claude/guild-meeting-notes.md) — Daily 20:00 Drive scan; extracts action items to repo issues
- [claude/guild-weekly-checkin.md](./claude/guild-weekly-checkin.md) — Sunday 20:00 cross-repo pulse digest

See [claude/README.md](./claude/README.md) for environment setup, schedule overview, and the manual-skill overlap policy.

## Conventions

- Each playbook is **self-contained** — readable without other context.
- Each starts with **when to use it** and ends with **common pitfalls**.
- Playbooks reference the guild workspace target (`greenpill.app/dev-guild`, coming soon — currently on Charmverse during migration) for operational state, and GitHub for execution.
- Updates to playbooks follow the [RFC process](../GOVERNANCE.md#rfc-process) for substantive changes; small clarifications can go through normal PR review.

## Promoting a project routine to the guild

If your project has a routine that other guild projects could benefit from:

1. Open an [RFC](https://github.com/greenpill-dev-guild/.github/issues/new?template=rfc.yml) describing the routine and why it generalizes.
2. Discuss in the weekly call.
3. On acceptance, open a PR adding it here.

## What does NOT belong here

- Project-specific runbooks (live in the project repo)
- Personal workflows (live in your own notes)
- Code or executable scripts at the top level (Phase 1 remains markdown-only; Phase 2 introduced reusable workflows under [../.github/workflows/](../.github/workflows/) and Claude routine prompts under [claude/](./claude/))
