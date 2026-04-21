# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account (expense-reimbursable per the 2026-04-19 funding decision); the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` (markdown **playbooks** for manual guild processes like bounty intake, RFCs, retros). Playbooks are reference docs; routines are executable prompts.

## Files

- `guild-daily-synthesis.md` — Daily 08:30 synthesis of previous 24h Discord discussion across 6 channels (`#funding`, `#marketing`, `#social`, `#lead-council`, `#working-capital`, `#treasury`). Output: Drive doc + `#lead-council` TL;DR, ready by 09:00.
- `guild-grant-scout.md` — Weekly Wednesday 19:00 grant scouting across 5 active projects (primary: Green Goods + Coop; secondary: TAS-Hub, network-website, cookie-jar). Writes Drive drafts + `grant:*` lifecycle issues + `#funding` summary.
- `guild-meeting-notes.md` — Daily 20:00 scan of Drive for new meeting notes; extracts action items and creates issues on the relevant active-guild repo. Subsumes the manual `/meeting-notes` skill for Drive-sourced notes.
- `guild-weekly-checkin.md` — Sunday 20:00 pulse across the 5 active guild repos (commits, PRs, issues, CI, load distribution). Output: Drive weekly doc + `#lead-council` digest.

## Active repo scope

All four routines operate on the same set of 5 active guild repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| coop | greenpill-dev-guild |
| network-website | greenpill-dev-guild |
| cookie-jar | greenpill-dev-guild |
| TAS-Hub | Greenpill9ja |

Other guild repos (gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope — not the active set.

## Schedule

```
Mon–Fri  20:00  guild-meeting-notes
Wed      19:00  guild-grant-scout
Daily    08:30  guild-daily-synthesis (brief ready by 09:00)
Sun      20:00  guild-weekly-checkin
```

All day-and-evening cadence — distinct from the Green Goods 04:00–07:30 morning routine window.

## Environment

All four routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**
- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_MARKETING_CHANNEL_ID`
- `DISCORD_SOCIAL_CHANNEL_ID`
- `DISCORD_LEAD_COUNCIL_CHANNEL_ID`
- `DISCORD_WORKING_CAPITAL_CHANNEL_ID`
- `DISCORD_TREASURY_CHANNEL_ID`

**Connectors:** Google Drive, Google Calendar
**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch GG-specific secrets (Arbitrum RPC, Envio, Dune, PostHog, bot API tokens).

## Conventions

- All routine PRs target their repo's `develop` branch (or the repo's default branch if no `develop` exists).
- Routine branches use `claude/<routine-name>/<topic>` prefix.
- Every routine-authored issue/PR carries the `automated/claude` umbrella label.
- Dedupe issues by category label — grant lifecycle uses `grant:<state>`; other categories use the label taxonomy in `../../labels.yml`.
- Loop prevention: filter on `head_branch` starting with `claude/` (not on author — routine PRs carry the user's GitHub author).

## Rebuilding a routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading).
4. Configure repos, environment, connectors, and triggers as specified in the file's frontmatter.
5. Save.

## Manual skill overlap

The manual `/meeting-notes` skill (see user-level Claude Code skills) overlaps with `guild-meeting-notes.md`. The split:
- **Automated Drive flow** → `guild-meeting-notes` handles it nightly. Humans don't need to invoke the skill for Drive docs.
- **Pasted transcripts** → use `/meeting-notes` manually. The routine doesn't scan Discord or direct chat paste.

## Related

- `../../labels.yml` — guild-wide label manifest (consumed by the `labels-sync.yml` reusable workflow)
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes (distinct from routines)
