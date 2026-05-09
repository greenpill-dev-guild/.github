# Routines

> Markdown playbooks for guild-wide flows - funded scoped work, check-ins, onboarding, retros, grants, workshops, meetings, and more.

These are **documentation, not enforcement**. Each playbook describes how the guild has agreed to handle a recurring flow. Anyone in the guild can adopt or adapt them; project teams can override locally as needed.

Distinct from [`claude/`](./claude/) - that subfolder holds source-of-truth prompts for **scheduled Claude automations**. The playbooks here describe manual guild processes; the Claude routines automate specific slices of weekly synthesis, grant scouting, and research synthesis.

## Index

### Working with the guild

- [funded-work-intake.md](./funded-work-intake.md) - Scoping grant-dependent, sponsor-funded, or steward-approved paid work
- [weekly-checkin.md](./weekly-checkin.md) - How lightweight active-work check-ins work and what they're for
- [newcomer-onboarding.md](./newcomer-onboarding.md) - First-week path for new contributors

### Operations

- [grant-application.md](./grant-application.md) - Drafting and submitting grant applications (Octant, Gitcoin, Giveth, etc.)
- [workshop-prep.md](./workshop-prep.md) - Running a guild workshop end to end
- [meeting-notes.md](./meeting-notes.md) - Capturing, processing, and acting on meeting notes
- [retro-cadence.md](./retro-cadence.md) - Quarterly and annual retrospectives

### Tooling and process

- [drive-orchestration.md](./drive-orchestration.md) - Shared Drive folder taxonomy and sorting flow
- [responsible-disclosure.md](./responsible-disclosure.md) - How we handle security disclosures from external researchers

### Automated (Claude routines)

- [claude/guild-weekly-synthesis.md](./claude/guild-weekly-synthesis.md) - Monday 18:00 cross-project synthesis with public community excerpt, private lead-council digest, and Drive memo
- [claude/guild-grant-scout.md](./claude/guild-grant-scout.md) - Wednesday 19:00 grant scouting with Linear `funding:*` saved-view lifecycle, Discord funding summary, and Drive memo
- [claude/research-synthesis.md](./claude/research-synthesis.md) - Friday 17:00 research synthesis with Discord digest, accepted Research team Issues, and Drive memo

See [claude/README.md](./claude/README.md) for environment setup, schedule overview, and the manual-skill overlap policy.

## Manual Playbooks Vs Scheduled Routines

The top-level `routines/*.md` files are manual playbooks. They are not live Claude Code routines and they do not run on a schedule. The guild uses them as shared operating agreements for humans, onboarding references, and source context that Claude can read when a scheduled routine needs the relevant process shape.

The live scheduled automations are only the prompts under [`claude/`](./claude/). If a manual playbook should become automated, promote it deliberately into `claude/` with a clear trigger, connector set, output, and guardrails.

## Conventions

- Each playbook is **self-contained** - readable without other context.
- Each starts with **when to use it** and ends with **common pitfalls**.
- Playbooks follow the [Linear operating model](../docs/linear-operating-model.md): Linear owns project management, GitHub owns public execution/RFCs/code review, Drive owns memos and evidence, and Discord/Telegram/calls own discussion.
- Updates to playbooks follow the [RFC process](../GOVERNANCE.md#rfc-process) for substantive changes; small clarifications can go through normal PR review.

## Promoting A Project Routine To The Guild

If your project has a routine that other guild projects could benefit from:

1. Open an [RFC](https://github.com/greenpill-dev-guild/.github/issues/new?template=rfc.yml) describing the routine and why it generalizes.
2. Discuss in the weekly call.
3. On acceptance, open a PR adding it here.

## What Does NOT Belong Here

- Project-specific runbooks (live in the project repo)
- Personal workflows (live in your own notes)
- Code or executable scripts at the top level (reusable workflow YAML lives under [../.github/workflows/](../.github/workflows/); scheduled Claude routine prompts live under [claude/](./claude/))
