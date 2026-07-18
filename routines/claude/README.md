# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like funded work intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Portfolio

All cadences in **UTC**.

| File | Status | Cadence | Channel | Surface |
|---|---|---|---|---|
| `guild-weekly-synthesis.md` | active | Tue 01:00 (= Mon 18:00 PT) | `#community` excerpt + `#lead-council` private digest | Drive memo; reads all five Linear teams; carries the 🔬 Research block (replaced the Friday research-synthesis digest) |
| `delivery-hygiene-pulse.md` | active | Mon & Thu 08:00 | `#scope-review` + Linear comments | All five teams: slippage (past-due / stalled / due-soon owned work) + scope hygiene (unscoped committed work; scoped briefs awaiting their team panel). Merges the retired accountability + scope-review pulses |
| `network-steward-intent-pulse.md` | active | Tue 16:00 | Linear only | Initiative status update on `Network Presence`; no Issues or Customer Needs |
| `guild-grant-scout.md` | active | Thu 02:00 (= Wed 19:00 PT) | `#funding` + Drive memo | The `funding:*` lifecycle on the **Growth team** (unprojected + saved views); awards stay on GROW, delivery links to Product |
| `stipend-ledger.md` | active | 1st of month 09:00 | `#lead-council` + one Linear Document | Monthly claims-review pack: accepted work per contributor across all five teams; no dollar math (see the [compensation playbook](../scoped-work-compensation.md)) |
| `profile-refresh.md` | active | Mon 20:00 | GitHub PR on `.github` | Opens a PR refreshing the three auto-managed `profile/README.md` sections (Now building, Recently shipped, team-shipping); PR only, never pushes `main` |
| `meet-filer.md` | active | Tue–Sat 00:00 | Drive only | Files Gemini meeting notes + recordings into per-meeting Drive destinations; nothing to any tracker |
| `research-synthesis.md` | **retired 2026-07-17** | — | — | Digest folded into guild-weekly-synthesis's 🔬 Research block; the automated `#research`→Issue path retired (acceptance is human via the brief flow) |
| `research-accountability-pulse.md` | **retired 2026-07-17** | — | — | Merged into delivery-hygiene-pulse (slippage lane, all five teams) |
| `scope-review-pulse.md` | **retired 2026-07-17** | — | — | Merged into delivery-hygiene-pulse (scope-hygiene lane, per-team panels) |
| `coop-intent-pulse.md` | **retired 2026-07-04** | — | — | Sunset (Coop dropped from routine scope); trigger disabled, spec kept for history |
| `software-ecology-pulse.md` | **retired 2026-07-04** | — | — | Sunset (meta-introspection, low signal); trigger disabled, spec kept for history |

The week, in order: the cross-project synthesis lands Tue 01:00 UTC (Mon evening PT) and primes the week; delivery-hygiene sweeps Monday and Thursday mornings; Tuesday checks Network steward intent; grant scouting lands Thu 02:00 UTC (Wed evening PT); profile-refresh closes Monday by opening its PR; meet-filer files meeting notes overnight Tue–Sat; the stipend ledger compiles the month on the 1st. **The 2026-07 streamlining cut the portfolio from 8 weekly-firing guild routines to 6** by merging the two hygiene pulses and folding research synthesis into the weekly digest — fewer, denser posts over more teams.

The Green Goods routines portfolio (product-scoped: bug-intake, qa-triage-pulse, health-watch, growth-pulse, pr-review) lives at [`greenpill-dev-guild/green-goods/docs/routines/`](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines).

## House style (applies to every posting routine)

One style governs every Discord post a guild routine makes:

- **Bold section headers**, a blank line between blocks, bullets with bold labels.
- **Lead with what needs a human** — a `🔴 Needs you` (or equivalent) block goes first, and the afo `@`-mention fires only there.
- **A thing appears only if it moved or needs attention.** Never post a "quiet" bullet, a zero-count, or an empty section header.
- **Fold metrics into the line they describe**; no telemetry or coverage blocks in Discord (run stats go in the memo).
- **One message** per channel per run (chunk only when Discord's 2000-char limit forces it).
- Rank action items when there are several: P0 (past-due / decision owed) before P1 (stalled / SLA-breached) before P2 (watch).

## Active repo scope

The guild routines read these active project repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| network-website | greenpill-dev-guild |

Plus the central `greenpill-dev-guild/.github` for grant-related cross-project context, and PGSP (Public Goods Staking Protocol) where it surfaces in `#funding` or `#research` discussions.

**Coop, Cookie Jar, and TAS-Hub were dropped from routine scope on 2026-07-04** — Network Website remains first-class. Other guild repos (coop, cookie-jar, TAS-Hub, gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope unless a routine prompt explicitly expands the active set.

## Schedule (UTC)

```text
Mon      08:00  delivery-hygiene-pulse
Mon      20:00  profile-refresh
Tue      01:00  guild-weekly-synthesis   (= Mon 18:00 PT)
Tue      16:00  network-steward-intent-pulse
Tue–Sat  00:00  meet-filer
Thu      02:00  guild-grant-scout        (= Wed 19:00 PT)
Thu      08:00  delivery-hygiene-pulse
1st/mo   09:00  stipend-ledger
```

## Channel mapping

| Channel | Used by | Purpose |
|---|---|---|
| `#community` | guild-weekly-synthesis (excerpt) | community-safe public post |
| `#lead-council` (private) | guild-weekly-synthesis (digest); stipend-ledger (monthly pack) | private leadership digest + claims review |
| Linear initiative `Network Presence` | network-steward-intent-pulse | weekly Network steward-hub intent check |
| `#funding` | guild-grant-scout | grant opportunities + pipeline (Growth team) |
| `#scope-review` | delivery-hygiene-pulse | slippage + scoping/panel queue across all five teams |
| `#research` | (manual discussion only) | no routine posts here since research-synthesis retired; research movement appears in the weekly synthesis 🔬 block |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO`):

- `guild-weekly-synthesis` — only on the `#lead-council` post when at least one risk/decision is overdue
- `guild-grant-scout` — when a grant deadline is < 7 days out, a new high-fit opportunity scores ≥ 4 on Green Goods, or a stale-prospect decision is needed
- `delivery-hygiene-pulse` — Discord: afo in the 🔴 Needs-you block, plus the **owner** tagged on past-due and ⚠️③ struck-out items (three pulse nudges in 30 days = a steward decision per the Delivery Accountability rule); Linear: `@`-mentions the owner on slippage and the team panel on briefs awaiting sign-off
- `stipend-ledger` — on the 🔴 Needs-you block (reopened / unassigned / unscoped completions, cap-relevant volume)

The `#community` excerpt from `guild-weekly-synthesis` never mentions. Discord notifications stay signal-heavy.

## Environment

All active routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**

- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_COMMUNITY_CHANNEL_ID`
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_SCOPE_CHANNEL_ID`
- `DISCORD_LEAD_COUNCIL_CHANNEL_ID`
- `DISCORD_RESEARCH_CHANNEL_ID` (kept for history; no active routine posts to `#research`)
- `DISCORD_USER_ID_AFO` — Afo's Discord snowflake ID for `<@${DISCORD_USER_ID_AFO}>` mentions
- `DISCORD_USER_ID_GUI` / `_NANSEL` / `_MATT` / `_KIT` / `_COI` / `_TARUN` — optional per-contributor snowflakes; `delivery-hygiene-pulse` uses them to tag owners on overdue work (2026-07-13 decision: automated tags replace manual notifications). An unset var degrades to name-only, never a broken mention
- **Linear: OAuth connector only — no `LINEAR_API_KEY` is stored in the guild-routines env** (standing rule as of 2026-07-04). Every Linear-touching routine (`guild-weekly-synthesis`, `network-steward-intent-pulse`, `guild-grant-scout`, `delivery-hygiene-pulse`, `stipend-ledger`, `profile-refresh`) reaches Linear through the wired OAuth connector and fails closed when it lapses; re-authorize the connector rather than adding a key.

**Connector matrix:**

| Routine | Connectors | Why each |
|---|---|---|
| `guild-weekly-synthesis` | Google Drive, Google Calendar, Miro, Figma, Canva, Linear, PostHog, Vercel | Linear = source of truth for cross-project work across all five teams · Drive/Calendar = meeting + scheduling context · Miro/Figma/Canva = design + asset movement · PostHog = link to growth-pulse digest (rare direct fallback) · Vercel = deploy activity counts in per-project bullets (color, never primary) |
| `network-steward-intent-pulse` | Linear | Linear = social truth for Network steward-hub status; the Network repo checkout provides `.plans` execution truth. No Discord, Drive, GitHub write, PostHog, Vercel, or design connectors. |
| `meet-filer` | Google Calendar | Calendar = the `list_events` fallback for classifying meeting notes; file moves go through the Meet Recordings webhook (`MEET_FILER_WEBHOOK_URL`), not the Drive connector. No Discord, Linear, or GitHub. |
| `guild-grant-scout` | Google Drive, Google Calendar, Miro, Canva, Linear, PostHog | Linear = `funding:*` lifecycle on the Growth team + saved views · Drive = drafts + reusable evidence · Calendar = deadlines · Miro = planning context · Canva = existing pitch decks to reference/reuse · PostHog = subtle grant-evidence signal (active gardens, action volume) |
| `delivery-hygiene-pulse` | Linear | Linear = read all five teams for slippage + scope hygiene, post idempotent owner/panel comments; Discord digest via the shared bot token; no Drive/Calendar/design/PostHog |
| `stipend-ledger` | Linear | Linear = read the closed month's completed issues across all five teams + write one ledger Document; Discord digest via the shared bot token; no other surfaces |
| `profile-refresh` | Linear, GitHub | Linear = the Now-building + team-shipping lists (workspace-wide, all five teams); GitHub = the Recently-shipped list from releases/merged PRs, plus the PR it opens on `.github`. PR only, never pushes `main`; touches only the marker blocks. |

Gmail is intentionally NOT wired. Personal-inbox content carries too much pollution / noise / private information for any of these routines.

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Surface model

The lean portfolio is anchored on three surfaces:

- **Linear** is the source of truth for actionable tracking — issues, customer signal, roadmap projects, and the funding lifecycle, organized across the five teams in the [team charters](../../docs/teams/README.md). `guild-grant-scout` writes Growth Issues labeled with `funding:*`. `delivery-hygiene-pulse` writes only comments. `stipend-ledger` writes one monthly Document. `network-steward-intent-pulse` writes one initiative status update and creates no work. `guild-weekly-synthesis` writes nothing to Linear — cross-project pulse is observation, not tracker work. No routine creates accepted-work Issues anymore: acceptance is human, via the brief flow and panel sign-off.
- **Drive memos** are memory substrate, not output destination. Synthesis/scout routines write a memo at run end so the next run's prior-recall can pick up open threads. The user is not expected to read Drive regularly; the routines do.
- **Discord** is the human-readable pulse channel — one house-style read per channel per run, scoped to that channel's audience.

GitHub is not a durable backlog — it stays in scope only for PRs and code review. Routines never file GitHub Issues. One routine, `profile-refresh`, opens a PR (never a direct push to `main`) to refresh the public profile's three auto-managed sections; it is the only routine that writes to a repo, and it still files no issues.

## Linear taxonomy

All Linear writes use the canonical label scheme (canonical statement: the [operating model](../../docs/linear-operating-model.md)):

- `protocol:*` — protocol/project (`protocol:green-goods`, `protocol:network`, `protocol:coop`, `protocol:pgsp`, `protocol:greenwill`)
- `package:*` — **code surface, keyed to the repo it lives in** — orthogonal to `protocol:*` (the product): one package can serve several products (e.g. GreenWill's contract work lives in green-goods `packages/contracts`, so `package:contracts` + `protocol:greenwill`). **green-goods repo:** `package:client`, `package:admin`, `package:agent`, `package:indexer`, `package:community`. **coop repo:** `package:app`, `package:api`, `package:extension`. **shared by both repos** (same name in each — the issue's `protocol:`/repo says which): `package:contracts`, `package:shared`, `package:docs`. Apply only to code-touching work (omit on research / funding / ops); a single-surface repo like `network` needs no `package:` at all.
- `activity:*` — work mode (`activity:build`, `activity:research`, `activity:design`, `activity:architecture`, `activity:qa`, `activity:maintenance`, `activity:marketing`, `activity:community`, `activity:ops`, `activity:capital`). **`activity:growth` is retired** — Growth is a team (`GROW`), not a work mode.
- **Estimate (Linear field)** — sizing signal for a scoped brief on the exponential scale (1/2/4/8 in live use; 16+ for a major integration). Replaces the retired `band:*` labels; a size, not a price — see the [compensation playbook](../scoped-work-compensation.md).
- `funding:*` — funding lifecycle (`funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`), lives on the Growth team
- `source:*` — provenance of the originating signal (`source:discord`, `source:telegram`, `source:drive`, `source:plans`, `source:github`)
- `agent:*` — routine/authored provenance. Apply **`agent:routine`** to every routine-authored Issue/Customer Need (canonical for "scheduled routine" output, matches existing Linear convention). Optionally add `agent:claude` or `agent:codex` to identify which agent ran the routine when that distinction matters.

Old label vocabularies (`area:*`, `work:*`, `task:*`, `band:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, `source:linear`) are retired. Do not reintroduce them. Routines apply `agent:routine` to mark authored provenance — note this is provenance, not human priority. Cookie Jar and Story Board are not first-class protocols (Cookie Jar work routes to `protocol:green-goods` per Linear admin; Story Board is retired).

### Project routing

- **Customer Needs** = raw signal. They live unprojected and carry `source:*` for provenance.
- **Linear Issues** = accepted work, placed on the team that owns acceptance ([routing rules](../../docs/linear-operating-model.md#routing-model)): delivery → Product, investigation → Research, community/cohort → Community, funding → Growth, campaigns/creative → Marketing. Issues are unprojected by default and graduate into a bounded active project only when the match is clear.
- **Do not route new work into completed/staging projects** like `Green Goods`, `Coop`, `Network Website`, `Cookie Jar`, or `Story Board`. These remain as historical containers; new work goes unprojected on its acceptance team until a bounded active project owns it.
- The grant pipeline is **unprojected on Growth + saved views over `funding:*`** — the old Research `Grant Scouting` project is retired; delivery unlocked by an award is filed on Product and linked.
- Green Goods `.plans/` remains the execution truth for agent implementation details; Linear is the upstream backlog, `.plans/` is the per-feature plan.

## Conventions

- Synthesis routines do not open PRs and do not file Issues. Research acceptance is human (brief flow + panel sign-off); no routine creates accepted-research Issues since research-synthesis retired.
- `network-steward-intent-pulse` is a status-only routine. It writes to the `Network Presence` initiative and does not create Issues, Customer Needs, projects, Discord posts, Drive docs, or GitHub artifacts.
- `meet-filer` moves Gemini meeting notes/recordings into per-meeting Drive folders. It posts to no Discord channel and writes nothing to Linear or GitHub; unclassifiable files land in `Meet Recordings — Review`.
- `delivery-hygiene-pulse` posts one `#scope-review` digest for all five teams and drops idempotent comments: owner nudges on past-due / stalled / due-soon owned issues (thresholds N=7 / X=3, grant pipeline excluded), and team-panel tags on scoped briefs awaiting sign-off. It honors the retired pulses' comment signatures for idempotency, never changes any issue field, and never moves an issue to Todo; acceptance remains a human panel decision. Canonical rule: the **Delivery Accountability** Linear Document (formerly "Research Accountability", same thresholds, now guild-wide).
- `stipend-ledger` compiles the monthly claims-review pack (accepted work per contributor) and computes no dollar amounts; the claim rule is claim-then-steward-review per the [compensation playbook](../scoped-work-compensation.md).
- Grant lifecycle Issues live on the **Growth team** and are surfaced through saved views over `funding:prospect` / `funding:drafting` / `funding:submitted` / `funding:active-award`. They carry the active `funding:*` label plus the relevant `protocol:*` and `agent:routine`. Awards stay on Growth; delivery work is filed on Product by humans and linked.
- `guild-weekly-synthesis` creates no GitHub or Linear issues. It produces a Drive memo + two Discord posts, and carries the 🔬 Research block sourced from Linear RESR movement.

## Rebuilding a routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading) — or, for thin-wrapper triggers, a pointer prompt that reads the spec from this repo's `main` at run start (the current pattern for every active guild routine).
4. Configure repos, environment, connectors, and triggers as specified in the file's frontmatter.
5. Save.

## Scope discipline

Every routine's prompt declares a **scope contract** at the top:

- **Input channel(s)** — the Discord channel(s) and Drive folder paths it is allowed to read.
- **Output channel(s)** — the Discord channel(s) it is allowed to post to. A `Channel guard` block before each `POST` block enforces "post here or not at all" — never substitute an alternate channel.
- **Out-of-scope topics** — content owned by adjacent routines (grants → `guild-grant-scout`, slippage/scoping → `delivery-hygiene-pulse`, claims → `stipend-ledger`). Even when adjacent content surfaces in the routine's own folder, it is dropped.

This is in response to a real failure mode: a synthesis routine running on a quiet week reached into Drive, picked up grant/funding material, and posted it to a topic channel that does not own funding content. Fixes (built into every active routine):

- **Quiet short-circuits** — a quiet week/surface produces a short all-clear or nothing, never padded content.
- **Drive content reject step** on every Drive-reading routine — content keyword filtering alone is too loose. WEFA, personal-calendar artifacts, and out-of-scope topics are dropped on every candidate doc, not just at query time.
- **Cross-routine ownership tables** — declare which adjacent routine owns each topic; reject those topics in the current routine's synthesis.

## Meeting-note handling

Routine automation does not scan Drive meeting notes just to turn action items into issues.

- `guild-weekly-synthesis` reads recent Drive docs (allow-listed by content + reject heuristics) to improve the weekly cross-project digest. No issues filed.
- `guild-grant-scout` reads grant-relevant Drive docs (already its scope).
- The manual `/meeting-notes` skill remains the right tool when a human wants pasted transcripts or a specific meeting doc converted into action items.

## Related

- [Green Goods routines](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines) — the product-scoped routines (bug-intake, qa-triage-pulse, health-watch, growth-pulse, pr-review)
- [Team charters](../../docs/teams/README.md) — the five Linear teams every routine now reads
- [Compensation playbook](../scoped-work-compensation.md) — the stipend model the stipend-ledger routine serves
- `../../labels.yml` — guild-wide label manifest consumed by the `labels-sync.yml` reusable workflow
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes, distinct from routines
