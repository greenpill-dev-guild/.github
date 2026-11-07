# Guild Claude Routines

Source-of-truth prompts for scheduled Claude automations operating at the guild level. Each routine's active configuration lives on [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's personal Anthropic Pro account; the files here exist so the setup is rebuildable if routines are lost or the research-preview API surface changes.

Distinct from `../*.md` markdown playbooks for manual guild processes like funded work intake, RFCs, retros, grants, and meeting notes. Playbooks are reference docs; routines are executable prompts.

## Portfolio

All cadences in **UTC**.

| File | Status | Cadence | Channel | Surface |
|---|---|---|---|---|
| `guild-grant-scout.md` | active (v3) | Fri 18:00 (= Fri 11:00 PT) | `#growth` + radar comment on the Growth radar issue + the `Grant scout shortlist` Linear document + Drive memo | Green Goods funding scout: weekly deadline radar, window watch on named programs, and a shortlist of verified leads across grants, prizes, accelerators, investment, partnerships and in-kind, filtered by the `Grant Scout Focus` Linear document; files a Growth issue only for a shortlist row a person ticked; reads the Weave funder catalog as a lead source; PGSP and Coop are out of scope |
| `meet-filer.md` | active | Tue–Sat 00:00 | Drive only | Files Gemini meeting notes + recordings into per-meeting Drive destinations; nothing to any tracker |

`drive-map.md` is a reference for the Drive queries these routines may run, not a routine.

The week, in order: meet-filer files meeting notes overnight Tue–Sat, and grant scouting lands Fri 18:00 UTC (Fri morning PT, right after the weekly usage window resets). The portfolio shrank to these two on 2026-11-07; [Retired routines](#retired-routines) says where the rest of the work went. **The 2026-07-30 quiet-Discord revamp** put every posting routine on house style v2: one message per post, a conversational lede, and a one-line all-clear on quiet runs.

The Green Goods routines (bug-intake, sync-triage-pulse, health-watch, growth-pulse, release-prep, research-synthesis, and research-week) live at [`greenpill-dev-guild/green-goods/docs/routines/`](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines).

## Retired routines

These specs left this folder on 2026-11-07; git history keeps every version.

| Routine | State before removal | Where the work went |
|---|---|---|
| `delivery-hygiene-pulse` | trigger paused since late August | No routine. Owners and team panels follow the Delivery Accountability rule directly |
| `scorecard-pulse` | monthly | The monthly scorecard review refreshes the registers ([scorecard guide](../../docs/strategy/scorecard-and-branch-map.md)) |
| `stipend-ledger` | monthly | Stewards review claims against the "Stipend Claims — This Month" saved view ([compensation playbook](../scoped-work-compensation.md)) |
| `profile-refresh` | weekly | The [org profile](../../profile/README.md) links to live sources instead of dated lists |
| `guild-weekly-synthesis` | no trigger since 2026-09-30 | Partnership and contact signal from calls belongs to the Green Goods research synthesis |
| `research-synthesis` (guild v3) | no trigger since 2026-09-30 | Replaced by the Green Goods research synthesis |
| `network-steward-intent-pulse` | no trigger found | No routine |
| `research-accountability-pulse`, `scope-review-pulse` | retired 2026-07-17 | Merged into `delivery-hygiene-pulse` |
| `coop-intent-pulse`, `software-ecology-pulse` | retired 2026-07-04 | Sunset |

## House style v2 (applies to every posting routine)

One style governs every Discord post a guild routine makes. The goal is a post a teammate would write: short, warm, and readable in one glance — with the full detail one click away in the durable artifact.

1. **One message, always.** Hard ceiling ~1,500 characters, target under ~900. Never chunk a post across messages; if it does not fit, cut content until it does. (The green-goods `release-prep` brief is the one stated exception, at two.)
2. **Lede first.** Open with 1–2 plain conversational sentences saying what the run means — "Quiet week; nothing needs you." or "Two things need attention: the Octant deadline and a stalled brief." — before any bullets. A reader who stops after the lede should still have the point.
3. **Then at most ~5 bullets total** across at most 2–3 sections. Bullets carry bold labels; blank line between blocks.
4. **A quiet run posts exactly one line** in the routine's home channel — `{emoji} {Routine} · {date}: all clear` (phrased per routine), plus the artifact link where one exists. Public-facing channels (`#community`) are exempt: they get no quiet-week post at all. Failures still post loudly; a failed run is never disguised as a quiet one.
5. **Lead with what needs a human** — a `🔴 Needs you` block goes first when it exists, and the afo `@`-mention fires only there (per the notification policy).
6. **A thing appears only if it moved or needs attention.** Never post a "quiet" bullet, a zero-count, or an empty section header. Numbers appear only when they changed meaningfully; fold them into the line they describe. No tables, no telemetry or coverage blocks in Discord (run stats go in the memo).
7. **One identity emoji in the header**, at most a couple of section markers (🔴 / 🤝 / 📋). No per-line emoji decoration.
8. **The durable artifact carries the detail** (Linear status update, Linear Document, Drive memo) and the post always links it.
9. Rank action items when there are several: P0 (past-due / decision owed) before P1 (stalled / SLA-breached) before P2 (watch).
10. **Get short by cutting content, not by compressing prose.** Drop anything that would not change what a reader does next, then write what remains in complete sentences. Never pad a post to look thorough, and never compress it into fragments, arrow chains, or invented abbreviations. In output text, prefer `·` and plain punctuation over em dashes.

## Active repo scope

The guild routines read these active project repos:

| Repo | Owner |
|---|---|
| green-goods | greenpill-dev-guild |
| network-website | greenpill-dev-guild |

Plus the central `greenpill-dev-guild/.github` for grant-related cross-project context, and PGSP (Public Goods Staking Protocol) where it surfaces in `#growth` or `#research` discussions.

**Coop, Cookie Jar, and TAS-Hub were dropped from routine scope on 2026-07-04** — Network Website remains first-class. Other guild repos (coop, cookie-jar, TAS-Hub, gardens, impact-reef, gg24-round-explorer, octant-v2(-core), regen-stack) are intentionally out of scope unless a routine prompt explicitly expands the active set.

## Schedule (UTC)

```text
Tue–Sat  00:00  meet-filer
Fri      18:00  guild-grant-scout        (= Fri 11:00 PT)
```

## Model tier

Each spec's `model:` frontmatter records the model its live routine runs. Editing the frontmatter does not change the running model, so change the routine and its spec together. This is the portfolio view after the 2026-09-30 move to Claude Opus 5.5 and Fable 5.1.

| Model | Routines | Why |
|---|---|---|
| `claude-fable-5-1` | guild-grant-scout | Open-ended grant discovery with real ambiguity to navigate, and historically the routine most prone to fabrication. It runs weekly, so a lost run costs one week. |
| `claude-opus-5-5` | meet-filer | The default. Cheaper per token than Opus 5, and Anthropic reports it is less likely than Opus 5 to state a figure its sources don't support. Pick this unless a routine clears the bar above. |

Fable runs draw on the account's weekly Fable usage allowance, and once it is spent a run stops within a second with "You're out of usage credits" and posts nothing. That cost `guild-grant-scout` its 2026-08-20 and 2026-08-27 runs.

To change a model:

- **Through the API, re-send the whole job config.** The routines API does not merge `job_config`, so a model change re-emits it with only the model swapped. The API also accepts any model string, so a typo only fails when the routine runs.
- **Confirm on the next run.** The run log from the routines API includes an `init: model=...` line naming the model that actually ran.
- **Expect declines to look quiet.** Both models run safety classifiers that can decline a request, and for a cron routine a decline looks like a quiet run rather than an error. Fable 5.1 also requires 30-day data retention, so a zero-data-retention org can use it only with Anthropic's express authorization.

Watch after the 2026-09-30 move:

- **`guild-grant-scout`** (Fri 18:00 UTC): the routine most likely to hit a classifier decline, because it reads government, security-adjacent, and climate funding portals. A Friday with no `#growth` post and no failure line needs its run log checked before it is read as a quiet week; a spent usage allowance looks the same.

## Channel mapping

| Channel | Used by | Purpose |
|---|---|---|
| `#growth` (renamed from `#funding`; `DISCORD_FUNDING_CHANNEL_ID` is unchanged) | guild-grant-scout | funding leads + pipeline (Growth team) |

## Notification policy

Routines @mention Afo only when his action is required (via `DISCORD_USER_ID_AFO`):

- `guild-grant-scout` — when a deadline is inside 7 days, an item is past due, a ticked shortlist row could not be filed, or a decision is owed (the `Needs you` block)

Discord notifications stay signal-heavy.

## Environment

All active routines use the `guild-routines` environment at claude.ai/code/routines.

**Required secrets:**

- `DISCORD_BOT_TOKEN` (shared bot token)
- `DISCORD_FUNDING_CHANNEL_ID`
- `DISCORD_USER_ID_AFO` — Afo's Discord snowflake ID for `<@${DISCORD_USER_ID_AFO}>` mentions
- meet-filer's webhook variables, as its spec lists them
- **Linear: OAuth connector only — no `LINEAR_API_KEY` is stored in the guild-routines env** (standing rule as of 2026-07-04). `guild-grant-scout`, the one Linear-touching guild routine, reaches Linear through the wired OAuth connector and fails closed when it lapses; re-authorize the connector rather than adding a key.

**Connector matrix:**

| Routine | Connectors | Why each |
|---|---|---|
| `meet-filer` | Google Calendar | Calendar = the `list_events` fallback for classifying meeting notes; file moves go through the Meet Recordings webhook (`MEET_FILER_WEBHOOK_URL`), not the Drive connector. No Discord, Linear, or GitHub. |
| `guild-grant-scout` | Google Drive, Linear | Linear = `funding:*` lifecycle on the Growth team, the `Grant Scout Focus` and `Grant scout shortlist` documents, and the `Grant deadline radar` issue · Drive = one memo per run in the Green Goods Growth folder · the `regen-commons/weave` repo is cloned read-only for its funder catalog · Calendar, Miro, Canva, PostHog stay wired on the trigger but are not used |

Gmail is intentionally NOT wired. Personal-inbox content carries too much pollution / noise / private information for any of these routines.

**Network access:** full (Discord API, GitHub API, Drive, Calendar, external web research)

Keep this environment separate from Green Goods product environments so a misbehaving guild routine cannot touch Green Goods-specific secrets such as Arbitrum RPC, Envio, Dune, PostHog, or bot API tokens.

## Surface model

The lean portfolio is anchored on three surfaces:

- **Linear** is the source of truth for actionable tracking — issues, customer signal, roadmap projects, and the funding lifecycle, organized across the five teams in the [team charters](../../docs/teams/README.md). `guild-grant-scout` writes Growth Issues labeled with `funding:*`, and only for shortlist rows a person ticked. No guild routine creates accepted work on its own: acceptance is human, via the brief flow and panel sign-off.
- **Drive memos** are memory substrate, not output destination. The grant scout writes a memo at run end so the next run's prior-recall can pick up open threads. The user is not expected to read Drive regularly; the routines do.
- **Discord** is the human-readable pulse channel — one house-style read per channel per run, scoped to that channel's audience.

GitHub is not a durable backlog — it stays in scope only for PRs and code review. Routines never file GitHub Issues, and no guild routine writes to a repository.

## Linear taxonomy

All Linear writes use the canonical label scheme (canonical statement: the [operating model](../../docs/linear-operating-model.md)):

- `protocol:*` — protocol/project (`protocol:green-goods`, `protocol:network`, `protocol:coop`, `protocol:pgsp`, `protocol:greenwill`)
- `package:*` — **code surface, keyed to the repo it lives in** — orthogonal to `protocol:*` (the product): one package can serve several products (e.g. GreenWill's contract work lives in green-goods `packages/contracts`, so `package:contracts` + `protocol:greenwill`). **green-goods repo:** `package:client`, `package:admin`, `package:agent`, `package:indexer`, `package:community`. **coop repo:** `package:app`, `package:api`, `package:extension`. **shared by both repos** (same name in each — the issue's `protocol:`/repo says which): `package:contracts`, `package:shared`, `package:docs`. Apply only to code-touching work (omit on research / funding / ops); a single-surface repo like `network` needs no `package:` at all.
- `activity:*` — work mode (`activity:build`, `activity:research`, `activity:design`, `activity:architecture`, `activity:qa`, `activity:maintenance`, `activity:marketing`, `activity:community`, `activity:ops`, `activity:capital`). **`activity:growth` is retired** — Growth is a team (`GROW`), not a work mode.
- **Estimate (Linear field)** — sizing signal for a scoped brief on the exponential scale (1/2/4/8 in live use; 16+ for a major integration). Replaces the retired `band:*` labels; a size, not a price — see the [compensation playbook](../scoped-work-compensation.md).
- `funding:*` — funding lifecycle (`funding:prospect`, `funding:drafting`, `funding:submitted`, `funding:active-award`), lives on the Growth team
- `source:*` — provenance of the originating signal (`source:discord`, `source:telegram`, `source:drive`, `source:plans`, `source:github`)
- `ai:*` — routine/authored provenance. Apply **`ai:routine`** to every routine-authored Issue/Customer Need (canonical for "scheduled routine" output, matches existing Linear convention). **Single-value**, like every grouped family: `ai:claude` / `ai:codex` *replace* `ai:routine`, they are never added alongside it. When both an originating and a delegated-to agent apply, the delegate wins the label and the origin goes in the body. Formerly written `agent:*`; the live group is `ai`, and `agent` exists only as `package:agent`, which is unrelated.

**Writing these through the API:** `group:child` is display shorthand, not accepted input. `save_issue` resolves labels by **bare child name or ID**, so pass `["green-goods", "qa", "routine"]`, not `["protocol:green-goods", "activity:qa", "ai:routine"]`. One unresolvable entry rejects the whole array and the routine files nothing, so a stale label name is a silent no-write rather than a partial write. Canonical statement: the [operating model](../../docs/linear-operating-model.md).

Old label vocabularies (`area:*`, `work:*`, `task:*`, `band:*`, `migration:*`, `automation:*`, `health:*`, `grant:*`, `source:linear`) are retired. Do not reintroduce them. Routines apply `ai:routine` to mark authored provenance — note this is provenance, not human priority. Cookie Jar and Story Board are not first-class protocols (Cookie Jar work routes to `protocol:green-goods` per Linear admin; Story Board is retired).

### Project routing

- **Customer Needs** = raw signal. They live unprojected and carry `source:*` for provenance.
- **Linear Issues** = accepted work, placed on the team that owns acceptance ([routing rules](../../docs/linear-operating-model.md#routing-model)): delivery → Product, investigation → Research, community/cohort → Community, funding → Growth, campaigns/creative → Marketing. Issues are unprojected by default and graduate into a bounded active project only when the match is clear.
- **Do not route new work into completed/staging projects** like `Green Goods`, `Coop`, `Network Website`, `Cookie Jar`, or `Story Board`. These remain as historical containers; new work goes unprojected on its acceptance team until a bounded active project owns it.
- The grant pipeline is **unprojected on Growth + saved views over `funding:*`** — the old Research `Grant Scouting` project is retired; delivery unlocked by an award is filed on Product and linked.
- Green Goods `.plans/` remains the execution truth for agent implementation details; Linear is the upstream backlog, `.plans/` is the per-feature plan.

## Conventions

- `meet-filer` moves Gemini meeting notes/recordings into per-meeting Drive folders. It posts to no Discord channel and writes nothing to Linear or GitHub; unclassifiable files land in `Meet Recordings — Review`.
- Grant lifecycle Issues live on the **Growth team** and are surfaced through saved views over `funding:prospect` / `funding:drafting` / `funding:submitted` / `funding:active-award`. They carry the active `funding:*` label plus the relevant `protocol:*`, and `ai:routine` **when routine-authored** (a human-filed grant Issue carries no `ai:*` label, since that family records authored provenance rather than lifecycle). Awards stay on Growth; delivery work is filed on Product by humans and linked.

## Rebuilding a routine

1. Log in to [claude.ai/code/routines](https://claude.ai/code/routines) under Afo's Pro account.
2. Click **New routine**.
3. Paste the prompt from the relevant `.md` file (everything after the `# Prompt` heading) — or, for thin-wrapper triggers, a pointer prompt that reads the spec from this repo's `main` at run start (the current pattern for every active guild routine).
4. Configure repos, environment, connectors, triggers, **and the model** as specified in the file's frontmatter. A rebuilt routine left on the platform default silently runs the wrong tier; see [Model tier](#model-tier).
5. Save.

## Scope discipline

Every routine's prompt declares a **scope contract** at the top:

- **Input channel(s)** — the Discord channel(s) and Drive folder paths it is allowed to read.
- **Output channel(s)** — the Discord channel(s) it is allowed to post to. A `Channel guard` block before each `POST` block enforces "post here or not at all" — never substitute an alternate channel.
- **Out-of-scope topics** — content owned by another routine or by people (grants belong to `guild-grant-scout`, for example). Even when such content surfaces in the routine's own folder, it is dropped.

This is in response to a real failure mode: a synthesis routine running on a quiet week reached into Drive, picked up grant/funding material, and posted it to a topic channel that does not own funding content. Fixes (built into every active routine):

- **Quiet short-circuits** — a quiet week/surface produces a short all-clear or nothing, never padded content.
- **Drive content reject step** on every Drive-reading routine — content keyword filtering alone is too loose. WEFA, personal-calendar artifacts, and out-of-scope topics are dropped on every candidate doc, not just at query time.
- **Cross-routine ownership tables** — declare which adjacent routine owns each topic; reject those topics in the current routine's synthesis.

## Meeting-note handling

Routine automation does not scan Drive meeting notes just to turn action items into issues.

- `guild-grant-scout` reads grant-relevant Drive docs (already its scope).
- The manual `/meeting-notes` skill remains the right tool when a human wants pasted transcripts or a specific meeting doc converted into action items.

## Related

- [Green Goods routines](https://github.com/greenpill-dev-guild/green-goods/tree/main/docs/routines): bug-intake, sync-triage-pulse, health-watch, growth-pulse, release-prep, research-synthesis, and research-week
- [Team charters](../../docs/teams/README.md) — the five Linear teams
- [Compensation playbook](../scoped-work-compensation.md) — the stipend model and its monthly claim review
- `../../labels.yml` — guild-wide label manifest consumed by the `labels-sync.yml` reusable workflow
- `../../.github/workflows/labels-sync.yml` — reusable workflow that syncs `labels.yml` to any opt-in guild repo
- `../../.github/workflows/claude-pr-review.yml` — reusable workflow that runs Claude PR review on any opt-in guild repo
- `../` — markdown playbooks for manual guild processes, distinct from routines
