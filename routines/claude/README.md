# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like bounty intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Portfolio

| File | Status | Cadence | Channel | Issue surface |
|---|---|---|---|---|
| `guild-weekly-synthesis.md` | active | Mon 18:00 weekly | `#community` excerpt + `#lead-council` private digest | Drive memo (no tracker) |
| `guild-grant-scout.md` | active | Wed 19:00 weekly | `#funding` + Drive memo | Linear `Funding Pipeline` project (`funding:*` lifecycle) |
| `research-synthesis.md` | active | Fri 17:00 weekly | `#research` + Drive memo | Linear `Research` team (unprojected, `work:research`) |

Three scheduled runs per week. Monday opens with the cross-project synthesis that primes the week. Wednesday handles grants midweek. Friday closes the week with research synthesis. No daily-cadence routines.

Anything else previously in this folder (`guild-daily-synthesis`, `weekly-insights`, `design-synthesis`, `guild-product-development-synthesis`, `guild-weekly-checkin`, `routine-issue-cleanup`, `routine-self-audit`) has been removed — folded into the surviving routines or cut as noise.

The Green Goods routines portfolio (4 GG-scoped routines, separate from this guild set) lives at [`greenpill-dev-guild/green-goods/docs/routines/`](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines).

## Active repo scope

The guild routines read these active project repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| coop | greenpill-dev-guild |
| network-website | greenpill-dev-guild |
| cookie-jar | greenpill-dev-guild |
| TAS-Hub | Greenpill9ja |

Plus the central `greenpill-dev-guild/.github` for grant-related cross-project context, and PGSP (Public Goods Staking Protocol) where it surfaces in `#funding` or `#research` discussions.

Other guild repos (gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope unless a routine prompt explicitly expands the active set.

## Schedule

```text
Mon  18:00  guild-weekly-synthesis
Wed  19:00  guild-grant-scout
Fri  17:00  research-synthesis
```

## Channel mapping

| Channel | Used by | Purpose |
|---|---|---|
| `#community` | guild-weekly-synthesis (excerpt) | community-safe public post |
| `#lead-council` (private) | guild-weekly-synthesis (digest) | private leadership digest |
| `#funding` | guild-grant-scout | grant opportunities + proposals |
| `#research` | research-synthesis | weekly research digest |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO`):

- `guild-weekly-synthesis` — only on the `#lead-council` post when at least one risk/decision is overdue
- `guild-grant-scout` — when a grant deadline is < 7 days out, a new high-fit opportunity scores ≥ 4 on Green Goods, or a stale-prospect decision is needed
- `research-synthesis` — when an action concretely maps to Green Goods active work

The `#community` excerpt from `guild-weekly-synthesis` never mentions. Discord notifications stay signal-heavy.

## Environment

All active routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**

- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_COMMUNITY_CHANNEL_ID`
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_RESEARCH_CHANNEL_ID`
- `DISCORD_LEAD_COUNCIL_CHANNEL_ID`
- `DISCORD_USER_ID_AFO` — Afo's Discord snowflake ID for `<@${DISCORD_USER_ID_AFO}>` mentions
- `LINEAR_API_KEY` — used by `guild-grant-scout` (Funding Pipeline) and `research-synthesis` (Research team)

**Connector matrix:**

| Routine | Connectors | Why each |
|---|---|---|
| `guild-weekly-synthesis` | Google Drive, Google Calendar, Miro, Figma, Canva, Linear, PostHog | Linear = source of truth for cross-project work · Drive/Calendar = meeting + scheduling context · Miro/Figma/Canva = design + asset movement · PostHog = link to growth-pulse digest (rare direct fallback) |
| `guild-grant-scout` | Google Drive, Google Calendar, Miro, Canva, Linear, PostHog | Linear = `Funding Pipeline` lifecycle · Drive = drafts + reusable evidence · Calendar = deadlines · Miro = planning context · Canva = existing pitch decks to reference/reuse · PostHog = subtle grant-evidence signal (active gardens, action volume) |
| `research-synthesis` | Google Drive, Linear, Miro, Google Calendar, Canva, PostHog, Mermaid Chart | Drive + Linear = primary signal · Miro/Calendar/Canva/PostHog = color enrichment (active week only, never on quiet/silent weeks) · Mermaid = generative for diagrams embedded in Linear Issue bodies |

Gmail is intentionally NOT wired. Personal-inbox content carries too much pollution / noise / private information for any of these routines.

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Surface model

The lean portfolio is anchored on three surfaces:

- **Linear** is the source of truth for actionable tracking. `guild-grant-scout` writes the `Funding Pipeline` project lifecycle. `research-synthesis` writes the `Research` team's actionable insights. `guild-weekly-synthesis` writes nothing to Linear — cross-project pulse is observation, not tracker work.
- **Drive memos** are memory substrate, not output destination. Each synthesis routine writes a memo at run end so the next run's Phase 0 prior-recall can pick up open threads. The user is not expected to read Drive regularly; the routines do.
- **Discord** is the human-readable pulse channel — a single weekly read per channel, scoped to that channel's audience.

## Conventions

- Synthesis routines do not open PRs. `research-synthesis` files Linear Issues for actionable insights (Research team, unprojected).
- Grant lifecycle Issues live in the Linear `Funding Pipeline` project (Product team, Sustainability & Monetization initiative). They carry `funding:prospect` / `funding:drafting` / `funding:submitted` / `funding:active-award` plus `automation:routine` + `agent:claude`.
- `guild-weekly-synthesis` creates no GitHub or Linear issues. It produces a Drive memo + two Discord posts.

## Rebuilding a routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading).
4. Configure repos, environment, connectors, and triggers as specified in the file's frontmatter.
5. Save.

## Scope discipline

Every routine's prompt declares a **scope contract** at the top:

- **Input channel(s)** — the Discord channel(s) and Drive folder paths it is allowed to read.
- **Output channel(s)** — the Discord channel(s) it is allowed to post to. A `Channel guard` block before each `POST` block enforces "post here or not at all" — never substitute an alternate channel.
- **Out-of-scope topics** — content owned by adjacent routines (grants → `guild-grant-scout`, research → `research-synthesis`, etc.). Even when adjacent content surfaces in the routine's own folder, it is dropped.

This is in response to a real failure mode: a synthesis routine running on a quiet week reached into Drive, picked up grant/funding material, and posted it to a topic channel that does not own funding content. Fixes (built into every active routine):

- **Quiet-week short-circuit** on `research-synthesis`: < 5 substantive channel messages → quiet-week post → exit. Do not widen via Drive.
- **Drive content reject step** on every Drive-reading routine — content keyword filtering alone is too loose. WEFA, personal-calendar artifacts, and out-of-scope topics are dropped on every candidate doc, not just at query time.
- **Cross-routine ownership tables** — declare which adjacent routine owns each topic; reject those topics in the current routine's synthesis.

## Meeting-note handling

Routine automation does not scan Drive meeting notes just to turn action items into issues.

- `guild-weekly-synthesis` reads recent Drive docs (allow-listed by content + reject heuristics) to improve the Monday cross-project digest. No issues filed.
- `guild-grant-scout` reads grant-relevant Drive docs (already its scope).
- `research-synthesis` reads research Drive content only.
- The manual `/meeting-notes` skill remains the right tool when a human wants pasted transcripts or a specific meeting doc converted into action items.

## Related

- [Green Goods routines](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines) — the 4 product-scoped routines (bug-intake, health-watch, growth-pulse, pr-review)
- `../../labels.yml` — guild-wide label manifest consumed by the `labels-sync.yml` reusable workflow
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes, distinct from routines
