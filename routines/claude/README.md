# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like bounty intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Files (8 routines)

### Synthesis & coordination
- `guild-daily-synthesis.md` — Daily 08:30 Discord/Drive/Calendar/Figma/Miro pulse → urgent daily read, public-safe community post, private Drive appendix, `#lead-council` link/summary
- `guild-product-development-synthesis.md` — Sunday 18:30 synthesis of product-dev discussions from calls and working artifacts → private Drive memo + `#lead-council`
- `guild-weekly-checkin.md` — Sunday 20:00 guild-health pulse → private Drive check-in + `#lead-council` digest + `#community` excerpt

### Funding
- `guild-grant-scout.md` — Wednesday 19:00 grant scouting across active projects, using Miro when relevant → Drive proposal drafts + `#funding` summary + `.github` grant lifecycle issues

### Insight extraction (NEW)
- `research-synthesis.md` — Friday 17:00 reads `#research` last 7d, synthesizes themes into concrete actions per project + ecosystem → posts to `#research`, optionally files `research:insight` issues in `.github`
- `design-synthesis.md` — Friday 18:00 reads `#design` last 7d, synthesizes design feedback into actionable improvements → posts to `#design`, optionally files design issues in project repos

### Meta hygiene (NEW)
- `routine-issue-cleanup.md` — Friday 22:00 sweeps `automated/claude` issues across all active repos, closes already-fixed/recovered/stale/superseded → `#engineering` cleanup summary
- `routine-self-audit.md` — Sunday 23:00 produces weekly meta report on the routine system itself: ran/skipped/output count/issue→PR conversion rate per routine → `#engineering` audit summary

## Active Repo Scope

The guild routines read the same 5 active project repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| coop | greenpill-dev-guild |
| network-website | greenpill-dev-guild |
| cookie-jar | greenpill-dev-guild |
| TAS-Hub | Greenpill9ja |

Plus the central `greenpill-dev-guild/.github` for grant lifecycle and `research:insight` issues.

Other guild repos (gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope unless a routine prompt explicitly expands the active set.

## Schedule

```text
Daily    08:30  guild-daily-synthesis
Wed      19:00  guild-grant-scout
Fri      17:00  research-synthesis
Fri      18:00  design-synthesis
Fri      22:00  routine-issue-cleanup
Sun      18:30  guild-product-development-synthesis
Sun      20:00  guild-weekly-checkin
Sun      23:00  routine-self-audit
```

The Friday end-of-week cluster (research → design → cleanup) gives Afo a synthesized view of the week and a clean board going into the weekend. The Sunday cluster (product-dev synthesis → weekly checkin → self-audit) closes the week and primes Monday.

## Channel mapping

| Channel | Used by | Purpose |
|---|---|---|
| `#community` | guild-daily-synthesis (public pulse), guild-weekly-checkin (excerpt) | community-safe public posts |
| `#lead-council` (private) | guild-daily-synthesis (link/summary), guild-product-development-synthesis, guild-weekly-checkin | private leadership digests |
| `#funding` | guild-grant-scout | grant opportunities + proposals |
| `#research` | research-synthesis | weekly research digest |
| `#design` | design-synthesis | weekly design feedback synthesis |
| `#engineering` | routine-issue-cleanup, routine-self-audit | meta + cleanup reports |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO` env var):
- `research-synthesis` — when an action maps to Green Goods active work
- `design-synthesis` — when an action maps to Green Goods active work
- `routine-issue-cleanup` — when >10 closures or any risky-looking closures
- `routine-self-audit` — only when something is silently broken or low-converting

Other guild routines do not @mention — their audience is the team via shared channels and Drive docs.

## Environment

All eight routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**

- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_COMMUNITY_CHANNEL_ID`
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_RESEARCH_CHANNEL_ID`
- `DISCORD_DESIGN_CHANNEL_ID`
- `DISCORD_ENGINEERING_CHANNEL_ID`
- `DISCORD_LEAD_COUNCIL_CHANNEL_ID`
- `DISCORD_MARKETING_CHANNEL_ID`
- `DISCORD_SOCIAL_CHANNEL_ID`
- `DISCORD_WORKING_CAPITAL_CHANNEL_ID`
- `DISCORD_TREASURY_CHANNEL_ID`
- `DISCORD_USER_ID_AFO` — Afo's Discord snowflake ID for `<@${DISCORD_USER_ID_AFO}>` mentions

**Connector matrix:**

| Routine | Connectors |
|---|---|
| `guild-daily-synthesis` | Google Drive, Google Calendar, Figma, Miro |
| `guild-grant-scout` | Google Drive, Google Calendar, Miro |
| `guild-product-development-synthesis` | Google Drive, Google Calendar, Figma, Miro |
| `guild-weekly-checkin` | Google Drive, Google Calendar, Figma, Miro |
| `research-synthesis` | Google Drive |
| `design-synthesis` | Google Drive |
| `routine-issue-cleanup` | none |
| `routine-self-audit` | none |

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Conventions

- Synthesis routines do not open PRs. Insight-extraction routines (research-synthesis, design-synthesis) may open low-volume tracking issues with explicit caps.
- Grant lifecycle issues live in `greenpill-dev-guild/.github` and carry `grant`, one `grant:<state>` label, and `automated/claude`.
- `research:insight` issues live in `greenpill-dev-guild/.github` and carry `research:insight` + `automated/claude`.
- `guild-daily-synthesis` creates no GitHub issues. It separates public-safe community pulse from private appendix.
- `guild-product-development-synthesis` is synthesis-only — no issues, no boards, no repo mutations.
- `guild-weekly-checkin` is a guild-health routine. Engineering ops + calendar + meeting-note follow-ups + deadlines + contributor/community energy + design/board movement + next-week coordination needs.
- `routine-issue-cleanup` only closes; it never reopens. Closure is conservative — when in doubt, leave open.
- `routine-self-audit` is read-only — observes, never triggers other routines.

## Rebuilding A Routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading).
4. Configure repos, environment, connectors, and triggers as specified in the file's frontmatter.
5. Save.

## Meeting-Note Handling

Routine automation does not scan Drive meeting notes just to turn action items into issues.

Current split:

- `guild-daily-synthesis` reads recent Drive docs only to improve the daily pulse and private appendix.
- `guild-product-development-synthesis` reads call notes and working artifacts when they contain product-development context, then produces a synthesis memo only.
- The manual `/meeting-notes` skill remains the right tool when a human wants pasted transcripts or a specific meeting doc converted into action items.

## Related

- `../../labels.yml` — guild-wide label manifest consumed by the `labels-sync.yml` reusable workflow
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes, distinct from routines
