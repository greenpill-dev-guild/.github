# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like funded work intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Portfolio

| File | Status | Cadence | Channel | Issue surface |
|---|---|---|---|---|
| `guild-weekly-synthesis.md` | active | Mon 18:00 weekly | `#community` excerpt + `#lead-council` private digest | Drive memo (no tracker) |
| `network-steward-intent-pulse.md` | active | Tue 16:00 weekly | Linear only | Initiative status update on `Network Presence`; no Issues or Customer Needs |
| `guild-grant-scout.md` | active | Wed 19:00 weekly | `#funding` + Drive memo | Linear Product (unprojected staging, `funding:*` lifecycle); accepted awards route into a dedicated `Grant Proposal / Award Stewardship` project |
| `research-synthesis.md` | active | Fri 17:00 weekly | `#research` + Drive memo | Linear Research team (unprojected, `activity:research`) |
| `research-accountability-pulse.md` | active | Mon & Thu 08:00 twice-weekly | `#research` + Linear comments | Flags Research team slippage (past-due / stalled / due-soon); comments + `@`-mentions the owner on each flagged issue (idempotent, ~weekly per issue) |
| `scope-review-pulse.md` | active | Mon/Wed/Fri 08:30 | `#scope-review` + Linear comments | Flags Triage / Backlog issues that need scoping or evaluator-panel acceptance before Todo; comments on scoped briefs only |
| `profile-refresh.md` | active | Mon 20:00 weekly (after synthesis) | GitHub PR on `.github` | Opens a PR refreshing the two auto-managed sections of the public `profile/README.md` (Now building, Recently shipped); PR only, never pushes `main`; no Issues |
| `meet-filer.md` | active | Tue–Sat 00:00 | Drive only (no Discord/Linear) | Moves Gemini meeting notes + recordings from the Meet Recordings folder into per-meeting Drive destinations; files nothing to any tracker |
| `coop-intent-pulse.md` | **retired 2026-07-04** | — | — | Sunset (Coop dropped from routine scope); trigger disabled, spec kept for history |
| `software-ecology-pulse.md` | **retired 2026-07-04** | — | — | Sunset (meta-introspection, low signal); trigger disabled, spec kept for history |

Five weekly runs, a twice-weekly research-accountability pulse, and a thrice-weekly scope-review pulse are active. Monday opens with the cross-project synthesis that primes the week; profile-refresh closes Monday at 20:00 by opening a PR to refresh the public profile. Tuesday checks Network steward-hub intent. Wednesday handles grants midweek. Friday closes the week with research synthesis. The research-accountability pulse runs Mon & Thu mornings (08:00) to surface Research-team slippage; the scope-review pulse runs Mon/Wed/Fri at 08:30 UTC to route pre-acceptance scoping/evaluation queues. The meet-filer routine files Gemini meeting notes into Drive on a Tue–Sat overnight cadence. **Coop Intent Pulse and Software Ecology Pulse were retired on 2026-07-04** (Coop dropped from routine scope; ecology folded out as low-signal).

Anything else previously in this folder has been removed — folded into the surviving routines or cut as noise.

The Green Goods routines portfolio (4 GG-scoped routines, separate from this guild set) lives at [`greenpill-dev-guild/green-goods/docs/routines/`](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines).

## Active repo scope

The guild routines read these active project repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| network-website | greenpill-dev-guild |

Plus the central `greenpill-dev-guild/.github` for grant-related cross-project context, and PGSP (Public Goods Staking Protocol) where it surfaces in `#funding` or `#research` discussions.

**Coop, Cookie Jar, and TAS-Hub were dropped from routine scope on 2026-07-04** — Network Website remains first-class. Other guild repos (coop, cookie-jar, TAS-Hub, gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope unless a routine prompt explicitly expands the active set.

## Schedule

```text
Mon      08:00  research-accountability-pulse
Mon      18:00  guild-weekly-synthesis
Mon      20:00  profile-refresh
Tue      16:00  network-steward-intent-pulse
Tue–Sat  00:00  meet-filer
Wed      19:00  guild-grant-scout
Thu      08:00  research-accountability-pulse
Fri      17:00  research-synthesis
M/W/F    08:30  scope-review-pulse
```

## Channel mapping

| Channel | Used by | Purpose |
|---|---|---|
| `#community` | guild-weekly-synthesis (excerpt) | community-safe public post |
| `#lead-council` (private) | guild-weekly-synthesis (digest) | private leadership digest |
| Linear initiative `Network Presence` | network-steward-intent-pulse | weekly Network steward-hub intent check |
| `#funding` | guild-grant-scout | grant opportunities + proposals |
| `#research` | research-synthesis | weekly research digest |
| `#research` | research-accountability-pulse | twice-weekly accountability flags (read-only) |
| `#scope-review` | scope-review-pulse | Mon/Wed/Fri pre-acceptance scoping and evaluator-panel queue |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO`):

- `guild-weekly-synthesis` — only on the `#lead-council` post when at least one risk/decision is overdue
- `guild-grant-scout` — when a grant deadline is < 7 days out, a new high-fit opportunity scores ≥ 4 on Green Goods, or a stale-prospect decision is needed
- `research-synthesis` — when an action concretely maps to Green Goods active work
- `research-accountability-pulse` — Discord: tags afo on past-due (🔴) items; Linear: `@`-mentions each flagged issue's owner in the accountability comment (v2)
- `scope-review-pulse` — Discord: tags afo on scoped briefs past the 3-day review SLA; Linear: `@`-mentions the discipline evaluator panel on scoped briefs awaiting sign-off

The `#community` excerpt from `guild-weekly-synthesis` never mentions. Discord notifications stay signal-heavy.

## Environment

All active routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**

- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_COMMUNITY_CHANNEL_ID`
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_RESEARCH_CHANNEL_ID`
- `DISCORD_SCOPE_CHANNEL_ID`
- `DISCORD_LEAD_COUNCIL_CHANNEL_ID`
- `DISCORD_USER_ID_AFO` — Afo's Discord snowflake ID for `<@${DISCORD_USER_ID_AFO}>` mentions
- **Linear: OAuth connector only — no `LINEAR_API_KEY` is stored in the guild-routines env** (standing rule as of 2026-07-04). Every Linear-writing routine (`guild-weekly-synthesis`, `network-steward-intent-pulse`, `guild-grant-scout`, `research-synthesis`, `research-accountability-pulse`, `scope-review-pulse`) reaches Linear through the wired OAuth connector; re-authorize the connector when it lapses rather than adding a key.

**Connector matrix:**

| Routine | Connectors | Why each |
|---|---|---|
| `guild-weekly-synthesis` | Google Drive, Google Calendar, Miro, Figma, Canva, Linear, PostHog, Vercel | Linear = source of truth for cross-project work (initiatives, projects, issues, customer needs) · Drive/Calendar = meeting + scheduling context · Miro/Figma/Canva = design + asset movement · PostHog = link to growth-pulse digest (rare direct fallback) · Vercel = deploy activity counts in per-project bullets (color, never primary) |
| `network-steward-intent-pulse` | Linear | Linear = social truth for Network steward-hub status; the Network repo checkout provides `.plans` execution truth. No Discord, Drive, GitHub write, PostHog, Vercel, or design connectors. |
| `meet-filer` | Google Calendar | Calendar = the `list_events` fallback for classifying meeting notes; file moves go through the Meet Recordings webhook (`MEET_FILER_WEBHOOK_URL`), not the Drive connector. No Discord, Linear, or GitHub. |
| `guild-grant-scout` | Google Drive, Google Calendar, Miro, Canva, Linear, PostHog | Linear = `funding:*` lifecycle saved views; accepted awards graduate to a bounded award/delivery project · Drive = drafts + reusable evidence · Calendar = deadlines · Miro = planning context · Canva = existing pitch decks to reference/reuse · PostHog = subtle grant-evidence signal (active gardens, action volume) |
| `research-synthesis` | Google Drive, Linear, Miro, Google Calendar, Canva, PostHog, Mermaid Chart | Drive + Linear = primary signal (Linear Research team, unprojected) · Miro/Calendar/Canva/PostHog = color enrichment (active week only, never on quiet/silent weeks) · Mermaid = generative for diagrams embedded in Linear Issue bodies |
| `research-accountability-pulse` | Linear | Linear = read Research team issues for slippage + post one accountability comment (`@`-mention owner) per flagged issue; Discord summary via the shared bot token; no Drive/Calendar/design/PostHog/Mermaid |
| `scope-review-pulse` | Linear | Linear = read Product and Research Triage / Backlog issues for pre-acceptance scoping and evaluator-panel queues + post one panel comment per scoped brief; Discord summary via the shared bot token; no Drive/Calendar/design/PostHog/Mermaid |
| `profile-refresh` | Linear, GitHub | Linear = the Now-building list from active initiatives/projects; GitHub = the Recently-shipped list from releases/merged PRs, plus the PR it opens to update `profile/README.md`. PR only, never pushes `main`; touches only the marker blocks. |

Gmail is intentionally NOT wired. Personal-inbox content carries too much pollution / noise / private information for any of these routines.

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Surface model

The lean portfolio is anchored on three surfaces:

- **Linear** is the source of truth for actionable tracking — issues, customer signal, roadmap projects, accepted research, and funding lifecycle saved views. `guild-grant-scout` writes Product Issues labeled with `funding:*` and routes won awards into bounded award/delivery projects. `research-synthesis` writes the Research team's accepted research insights, unprojected by default. `network-steward-intent-pulse` writes one initiative status update and creates no work. `guild-weekly-synthesis` writes nothing to Linear — cross-project pulse is observation, not tracker work.
- **Drive memos** are memory substrate, not output destination. Each synthesis routine writes a memo at run end so the next run's Phase 0 prior-recall can pick up open threads. The user is not expected to read Drive regularly; the routines do.
- **Discord** is the human-readable pulse channel — a single weekly read per channel, scoped to that channel's audience.

GitHub is not a durable backlog — it stays in scope only for PRs and code review. Routines never file GitHub Issues. One routine, `profile-refresh`, opens a PR (never a direct push to `main`) to refresh the public profile's two auto-managed sections; it is the only routine that writes to a repo, and it still files no issues.

## Linear taxonomy

All Linear writes use the canonical label scheme:

- `protocol:*` — protocol/project (`protocol:green-goods`, `protocol:coop`, `protocol:pgsp`, `protocol:greenwill`, `protocol:network`, `protocol:tas`)
- `package:*` — **code surface, keyed to the repo it lives in** — orthogonal to `protocol:*` (the product): one package can serve several products (e.g. GreenWill's contract work lives in green-goods `packages/contracts`, so `package:contracts` + `protocol:greenwill`). **green-goods repo:** `package:client`, `package:admin`, `package:agent`, `package:indexer`. **coop repo:** `package:app`, `package:api`, `package:extension`. **shared by both repos** (same name in each — the issue's `protocol:`/repo says which): `package:contracts`, `package:shared`, `package:docs`. Apply only to code-touching work (omit on research / funding / ops); a single-surface repo like `network` needs no `package:` at all.
- `activity:*` — activity type (`activity:research`, `activity:qa`, `activity:maintenance`, `activity:architecture`, `activity:build`, `activity:design`, `activity:marketing`, `activity:community`, `activity:growth`)
- **Estimate (Linear field)** — sizing for a paid scoped brief: set the issue's estimate on the exponential scale (Scout ~ 1, Brief ~ 4, Deep ~ 16). Replaces the retired `band:*` labels. See the scoped-work compensation playbook (`routines/scoped-work-compensation.md`).
- `funding:*` — funding lifecycle (`funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`)
- `source:*` — provenance of the originating signal (`source:discord`, `source:telegram`, `source:drive`, `source:plans`, `source:github`)
- `agent:*` — routine/authored provenance. Apply **`agent:routine`** to every routine-authored Issue/Customer Need (canonical for "scheduled routine" output, matches existing Linear convention). Optionally add `agent:claude` or `agent:codex` to identify which agent ran the routine when that distinction matters.

Old label vocabularies (`area:*`, `work:*`, `task:*`, `band:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, `source:linear`) are retired. Do not reintroduce them. Routines apply `agent:routine` to mark authored provenance — note this is provenance, not human priority. Cookie Jar and Story Board are not first-class protocols (Cookie Jar work routes to `protocol:green-goods` per Linear admin; Story Board is retired).

### Project routing

- **Customer Needs** = raw signal. They live unprojected and carry `source:*` for provenance.
- **Linear Issues** = accepted product work or accepted research. Issues are unprojected by default and graduate into a bounded active project only when the match is clear.
- **Do not route new work into completed/staging projects** like `Green Goods`, `Coop`, `Network Website`, `Cookie Jar`, or `Story Board`. These remain as historical containers; new work goes unprojected on the relevant team (Product or Research) until a bounded active project owns it.
- **Accepted grants** create or route into a bounded award/delivery project — never stay as loose pipeline noise.
- Green Goods `.plans/` remains the execution truth for agent implementation details; Linear is the upstream backlog, `.plans/` is the per-feature plan.

## Conventions

- Synthesis routines do not open PRs. `research-synthesis` files Linear Issues in the Research team for accepted research insights (unprojected).
- `network-steward-intent-pulse` is a status-only routine. It writes to the `Network Presence` initiative and does not create Issues, Customer Needs, projects, Discord posts, Drive docs, or GitHub artifacts.
- `meet-filer` moves Gemini meeting notes/recordings into per-meeting Drive folders. It posts to no Discord channel and writes nothing to Linear or GitHub; unclassifiable files land in `Meet Recordings — Review`.
- `research-accountability-pulse` posts one `#research` summary flagging overdue / stalled / due-soon owned Research issues (thresholds N=7 / X=3 / M=7, grant pipeline excluded), and (v2) adds one accountability comment `@`-mentioning the owner on each flagged issue — idempotent (~once/week per issue via a 6-day signed-comment skip), comments only. It never creates / edits / relabels / reassigns issues or changes any field. Canonical rule: the Research team's "Research Accountability — scope, due dates & escalation" Linear Document.
- `scope-review-pulse` posts one `#scope-review` summary for Product and Research Triage / Backlog Issues that either need scoping or are scoped and awaiting evaluator-panel sign-off. It comments only on scoped briefs awaiting evaluation, never on raw unscoped ideas, and never moves an issue to Todo; acceptance remains a human panel decision.
- Grant lifecycle Issues live in Linear's Product team and are surfaced through saved views over `funding:prospect` / `funding:drafting` / `funding:submitted` / `funding:active-award`. They carry the active `funding:*` label plus `activity:research`, the relevant `protocol:*`, and `agent:routine`. On award, an Issue receives `funding:active-award` and moves into a bounded award/delivery project when delivery, reporting, compliance, or funder follow-through needs project-level management.
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
