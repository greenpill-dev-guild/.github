# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like bounty intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Portfolio (post-2026-05-08 reset)

The portfolio was reset on 2026-05-08 alongside the Green Goods reset. Goal: reduce noise so the surviving routines can be tuned to consistent quality. Daily-cadence routines were the loudest source of scope-creep and inconsistent output; they're now weekly.

| File | Status | Cadence | Channel | Issue surface |
|---|---|---|---|---|
| `guild-weekly-synthesis.md` | active (NEW) | Mon 18:00 weekly | `#community` excerpt + `#lead-council` private digest | Drive memo |
| `guild-grant-scout.md` | active | Wed 19:00 weekly | `#funding` + Drive | `.github` grant lifecycle issues |
| `weekly-insights.md` | active (NEW) | Fri 17:00 weekly | `#research` + `#design` | Linear (actionable insights) |
| `routine-self-audit.md` | active (Phase 3 upgrade pending) | Sun 23:00 weekly | `#engineering` | reads only — closes stale `automated/claude` issues as part of upgrade |
| `guild-daily-synthesis.md` | **paused** | (cron dropped) | (was `#community` + `#lead-council`) | (folded into `guild-weekly-synthesis`) |
| `research-synthesis.md` | **paused** | (cron dropped) | (was `#research`) | (folded into `weekly-insights`; insights now go to Linear, not `.github` issues) |
| `design-synthesis.md` | **paused (pending — concurrent edits)** | (cron drop pending) | (was `#design`) | (folded into `weekly-insights`) |
| `routine-issue-cleanup.md` | **paused** | (cron dropped) | (was `#engineering`) | (sweep folds into `routine-self-audit`) |
| `guild-product-development-synthesis.md` | **paused (pending — concurrent edits)** | (cron drop pending) | (was `#lead-council`) | (folded into Green Goods `growth-pulse` for Green Goods data; broader product-dev synthesis becomes a follow-up plan if needed) |
| `guild-weekly-checkin.md` | **paused (pending — concurrent edits)** | (cron drop pending) | (was `#community` excerpt + `#lead-council`) | (folded into `guild-weekly-synthesis` for cross-project; Green Goods numbers move to `growth-pulse`) |

Paused prompts remain in the repo as reference. Their cloud crons should be dropped via the routines surface at [claude.ai/code/routines](https://claude.ai/code/routines). Three paused entries are marked **(pending — concurrent edits)** because the prompt files had a concurrent quality-pass in flight on 2026-05-08; banners + cron drops on those land in a follow-up turn after the concurrent edits commit.

The Green Goods routines portfolio (7 GG-scoped routines, separate from this guild set) lives at [`greenpill-dev-guild/green-goods/docs/routines/`](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines).

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

## Schedule (post-2026-05-08)

```text
Mon      18:00  guild-weekly-synthesis
Wed      19:00  guild-grant-scout
Fri      17:00  weekly-insights
Sun      23:00  routine-self-audit
```

Four scheduled runs per week, down from eight. Monday opens with the cross-project synthesis that primes the week. Wednesday handles grants midweek. Friday closes the week with research + design synthesis. Sunday late-night runs self-audit (which now also handles the issue-cleanup sweep that was previously its own Friday routine). No daily-cadence routines.

Pre-reset cadence (for reference, all paused or pending-pause):

```text
Daily    08:30  guild-daily-synthesis             (paused — folded into guild-weekly-synthesis)
Wed      19:00  guild-grant-scout                 (unchanged)
Fri      17:00  research-synthesis                (paused — folded into weekly-insights)
Fri      18:00  design-synthesis                  (pending pause — concurrent edits)
Fri      22:00  routine-issue-cleanup             (paused — folded into routine-self-audit)
Sun      18:30  guild-product-development-synthesis (pending pause — concurrent edits)
Sun      20:00  guild-weekly-checkin              (pending pause — concurrent edits)
Sun      23:00  routine-self-audit                (unchanged; Phase 3 upgrade pending)
```

## Channel mapping (post-2026-05-08)

| Channel | Used by | Purpose |
|---|---|---|
| `#community` | guild-weekly-synthesis (excerpt) | community-safe public posts |
| `#lead-council` (private) | guild-weekly-synthesis (digest) | private leadership digest |
| `#funding` | guild-grant-scout | grant opportunities + proposals |
| `#research` | weekly-insights | weekly research digest (with cross-cuts to design) |
| `#design` | weekly-insights | weekly design digest (with cross-cuts to research) |
| `#engineering` | routine-self-audit | meta audit + issue cleanup |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO` env var):
- `guild-weekly-synthesis` — only on the `#lead-council` post when at least one risk/decision is overdue
- `weekly-insights` — when a Linear Issue is filed for active Green Goods work
- `routine-self-audit` — only when a rubric violation surfaces or routine output drifts
- `guild-grant-scout` — only when a grant deadline is < 7 days out

The `#community` excerpt from `guild-weekly-synthesis` never mentions. Discord notifications stay signal-heavy. The 2026-05-08 reset specifically removed the daily `guild-daily-synthesis` post that was the loudest @mention source — the surviving weekly post should feel like a useful read, not a notification stream.

## Environment

All active routines use the `guild-routines` environment at claude.ai/code/routines. Paused routines retain their environment field for reference but no longer run.

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

**Connector matrix (active routines only):**

| Routine | Connectors |
|---|---|
| `guild-weekly-synthesis` | Google Drive, Google Calendar |
| `guild-grant-scout` | Google Drive, Google Calendar, Miro |
| `weekly-insights` | Google Drive, Linear |
| `routine-self-audit` | none |

(Paused routines kept their original connector lists in their frontmatter for reference.)

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Conventions

- Synthesis routines do not open PRs. `weekly-insights` files Linear Issues for actionable insights (Green Goods Linear project; expand to other-project Linear projects when those exist).
- Grant lifecycle issues live in `greenpill-dev-guild/.github` and carry `grant`, one `grant:<state>` label, and `automated/claude` (`guild-grant-scout` continues this pattern).
- `research:insight` GitHub issues are **retired** post-2026-05-08. Actionable insights from `weekly-insights` go to **Linear**, not `.github`.
- `guild-weekly-synthesis` creates no GitHub or Linear issues. It produces a Drive memo + two Discord posts. Cross-project visibility belongs in the leadership digest, not in tracker artifacts.
- `routine-self-audit` is read-only on routine outputs but can close stale `automated/claude` GitHub issues as part of the absorbed cleanup pass. Closure is conservative — when in doubt, leave open.

## Rebuilding A Routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading).
4. Configure repos, environment, connectors, and triggers as specified in the file's frontmatter.
5. Save.

## Scope discipline

Every routine's prompt declares a **scope contract** at the top:

- **Input channel(s)** — the Discord channel(s) and Drive folder paths it is allowed to read.
- **Output channel(s)** — the Discord channel(s) it is allowed to post to. A `Channel guard` block before each `POST` block enforces "post here or not at all" — never substitute an alternate channel.
- **Out-of-scope topics** — content owned by adjacent routines (grants → `guild-grant-scout`, design → `design-synthesis`, research → `research-synthesis`, etc.). Even when adjacent content surfaces in the routine's own folder, it is dropped.

This is in response to a real failure mode: a synthesis routine running on a quiet week reached into Drive, picked up grant/funding material, and posted it to a topic channel that does not own funding content. The fixes (now built into the post-2026-05-08 portfolio):

- **Quiet-week short-circuit** on `weekly-insights` (and inherited from the paused `design-synthesis` / `research-synthesis`): < 5 substantive channel messages → quiet-week post → exit. Do not widen via Drive.
- **Drive folder allow-lists** on every Drive-reading routine — content keyword filtering alone is too loose. Both `guild-weekly-synthesis` and `weekly-insights` carry explicit folder allow-lists.
- **Cross-routine ownership tables** — declare which adjacent routine owns each topic; reject those topics in the current routine's synthesis. The 2026-05-08 reset reduced the routine count, which made these ownership tables shorter and easier to honor.

## Meeting-Note Handling

Routine automation does not scan Drive meeting notes just to turn action items into issues.

Current split (post-2026-05-08):

- `guild-weekly-synthesis` reads recent Drive docs (allow-listed folders only) to improve the Monday cross-project digest. No issues filed.
- `guild-grant-scout` reads grant-relevant Drive docs (already its scope).
- `weekly-insights` reads research/design Drive folders only.
- The manual `/meeting-notes` skill remains the right tool when a human wants pasted transcripts or a specific meeting doc converted into action items.

The previously-distinct `guild-product-development-synthesis` (paused-pending-edits) had its own meeting-note pass; that capability is being absorbed by `guild-weekly-synthesis` for cross-project + Green Goods's `growth-pulse` for Green Goods-specific product-dev signals.

## Related

- [Green Goods routine workflows + HITL diagrams](https://github.com/greenpill-dev-guild/green-goods/blob/main/docs/routines/workflows.md) — covers all 15 routines (cross-cutting), with mermaid diagrams of each pipeline
- `../../labels.yml` — guild-wide label manifest consumed by the `labels-sync.yml` reusable workflow
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes, distinct from routines
