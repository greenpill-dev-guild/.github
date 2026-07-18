# How the Dev Guild Pays: the Stipend Model

> From Q3 2026, guild contributors are paid a monthly stipend claimed through a Cookie Jar and backed entirely by work tracked and accepted on Linear. Companion to [Funded Work Intake](./funded-work-intake.md), which covers how work is identified and scoped.

**When to use this**: you contribute to the guild and want to be paid, or you steward the treasury and review claims. Volunteer contributions use the normal issue and PR flow, and are always welcome outside this model.

## Principle

**No Linear record, no claim.** The stipend pays for work that is tracked on Linear and accepted there. Work that happens off-platform is invisible to this model on purpose: if it matters enough to pay for, it matters enough to scope as an issue first.

"Done" still means what it always has: acceptance criteria met, accepted by the team's evaluator panel or steward. Acceptance is what makes work claimable.

## The stipend

| Role | Cap | Period |
| --- | --- | --- |
| Contributor | up to **$400** | per month |
| Steward (currently afo) | up to **$2,400** | per month |

The steward cap is $400 across each of the six disciplines the steward covers (engineering, product, marketing, community, research, growth/BD), matching the per-discipline baseline set at the 2026-07-13 capital sync. **Contributors claim through the Cookie Jar; the steward settles directly from the treasury multi-sig** (not through the jar), reviewed against the same monthly ledger.

The cap is a ceiling, not a salary:

- A full month of accepted work: claim up to the cap.
- Less than that: claim proportionally less.
- Nothing tracked and accepted: claim nothing. The jar goes untouched.

Unearned and unclaimed amounts do not roll over; each month starts fresh.

## What backs a claim

An issue backs your claim for a given month when all of these hold:

- It is **assigned to you**, on any of the five teams (see the [team charters](../docs/teams/README.md)).
- It reached **Done in that month** and was accepted per the [operating model](../docs/linear-operating-model.md) (panel sign-off gated it into work; review accepted the result).
- It was **scoped**: the [Brief shape](../docs/linear-templates.md#brief) with an estimate set.

Estimates (1/2/4/8) and any stated allocation are reference points for judging how much of the cap a month's work fairly represents. There is deliberately no mechanical dollars-per-point formula; the judgment stays human, on both sides.

## Claiming: claim, then review

1. **Claim from the Cookie Jar** as the month closes, for the amount that fairly reflects your accepted, tracked work, up to your cap.
2. **Link your work in the claim note.** Every claim note must carry a Linear reference that backs it: the issue links themselves, the month's **Stipend Ledger** document, or the shared **"Stipend Claims — This Month"** saved view filtered to you (all teams · Done · completed this month · grouped by assignee). A claim without a Linear reference is invalid by convention and will be flagged.
3. **Steward review.** The steward reviews every claim against the Linear record, using the monthly stipend ledger as the reference pack. The review checks responsible usage; it does not re-litigate acceptance that already happened on the issue.
4. **Over-claims** are flagged by the steward and either offset against the next month or returned. Repeated over-claiming is grounds for removal from the jar allowlist, a steward decision under [GOVERNANCE.md](../GOVERNANCE.md).

## The stipend ledger

The `stipend-ledger` routine ([routines/claude/stipend-ledger.md](./claude/stipend-ledger.md)) compiles the review pack on the 1st of each month: every issue completed in the closed month across all five teams, grouped by contributor, with links, estimates, and payment-classification fields where present. It posts one digest for steward review and writes one Linear document, "Stipend Ledger — {month}". It computes no dollar amounts; it exists so the claim review takes minutes, not an evening.

## Payment classification, in the issue

Payable briefs may carry an explicit classification block (a pattern already in use on COM-10, MAR-1, and MAR-15, standardized in the [Brief template](../docs/linear-templates.md#brief)):

```markdown
## Payment classification
Classification: stipend-claimable | volunteer | grant-deliverable
Allocation: optional reference amount or points note
Envelope: the funding source this draws from
Guardrails: caps, splits across contributors, exclusions
```

Use it whenever the split, the envelope, or the expectation needs to be explicit up front. Absent the block, an accepted, assigned, estimated brief is stipend-claimable by default.

## Continuous roles

Ongoing coverage that is not a single deliverable (community support, ongoing maintenance, funding tracking) claims within the same monthly cap. Evidence it with **one coverage issue per month**: what was covered, moved to Done and accepted like any other issue. The [Continuous role Document](../docs/linear-templates.md#continuous-role-a-document-not-an-issue) defines the arrangement; the monthly coverage issue is the claimable record. This replaces the old "monthly role stipend plus hourly extras" arrangement.

## The Cookie Jar

Distribution runs through **one Cookie Jar for contributors** — the guild's own [cookie-jar](https://github.com/greenpill-dev-guild/cookie-jar) product (allowlist, NFT, POAP, Hypercert, and Hats gating), already deployed on Arbitrum. The steward does not claim from the jar: steward compensation settles directly from the treasury multi-sig, reviewed against the same ledger.

| Setting | Value |
| --- | --- |
| Jar | Guild cookie-jar deployment on Arbitrum (jar instance/address: steward fills in after deploy) |
| Jar admin | Working Capital multi-sig `0xe09315A86ED0A39862158f5631b928145987fE05` (an EOA may hold deploy-time admin only if the multi-sig can be set as admin after) |
| Chain | Arbitrum One |
| Token | USDC |
| Gating | **Green Goods Hats tree (Arbitrum): the team hat is the membership credential** — wearing it puts you on the jar; minting/toggling it is how the roster is managed. Plain allowlist is the fallback if hat minting lags. (The guild-level Hats tree lives on Optimism and is NOT used here; it would force a second jar deployment and cross-chain funding for no gain.) |
| Members | gui (gferreira525), nansel, matt, kit, coi, tarun — 6 contributors; steward excluded by design |
| Claim allowance | $400 per member per monthly window |
| Launch window | The first window opens once Artizen Season 6 funds land and covers **July + August combined ($800/member)**; monthly from then on |
| September | No September refill — September is funded by Artizen Season 7 and lands with the **October** refill ($400 for September + $400 for October). September work is still tracked and accepted normally; only payout timing shifts |
| Funding path | Artizen Season 6 → nonprofit fiscal routing (tax) → working-capital multi-sig → jar top-up in USDC |

Until the jar instance is live, claims follow the same rules and are settled manually from the treasury multi-sig.

## The exception path: grant-funded briefs

Some work is too large for a monthly cap: a major integration, or a deliverable a grant explicitly contracts. That work can be priced as a fixed-price brief outside the stipend when **all** of these hold:

- The steward signs off, and the team's evaluator panel accepts the brief.
- A named grant envelope funds it (the capped line-item inside the grant it supports).
- The price is fixed at scope time, recorded in the issue's payment-classification block (`Classification: grant-deliverable`), and paid on acceptance.

This is an exception, not a parallel track. Work that was not explicitly priced and enveloped up front is stipend work.

## What changed (2026-07)

The previous playbook priced every brief individually: Scout ($100–500), Brief ($500–1,800), and Deep ($1,500–3,000) tiers derived from a $30–60/hr impact-set rate, paid in 2–3 tranches. That model is retired for guild members, replaced by the stipend and the Cookie Jar.

What survives unchanged: the scoped-brief shape, estimates as the sizing signal (1/2/4/8, with 16+ marking integration-scale work), panel acceptance as the gate, grant-tied envelopes as the money that fills the jar, and the principle that the guild pays for accepted outputs, not time. Scout / Brief / Deep live on only as informal sizing vocabulary.

## Related

- [Funded Work Intake](./funded-work-intake.md) — how scoped work is identified and confirmed; this playbook is its payment layer.
- [Linear operating model](../docs/linear-operating-model.md) and [team charters](../docs/teams/README.md) — teams, acceptance, estimates.
- [Grant Application](./grant-application.md) — the funding-source side that fills the envelopes.
- **Delivery Accountability** rule (Linear Document) — scope → due date → pulse → escalation; the `delivery-hygiene-pulse` routine chases the same flow this playbook pays.

---

*Status: active from Q3 2026 (July). Caps: $400/month contributor, $2,400/month steward. Claims via Cookie Jar, backed by Linear-tracked accepted work, steward-reviewed monthly against the stipend ledger.*
