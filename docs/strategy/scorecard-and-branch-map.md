# Scorecard & Branch Map

> Canonical operating guide for outcomes and indicators (the balanced-scorecard layer). Companion to `docs/linear-operating-model.md`; where they overlap on routing, the operating model wins.

## The three tiers

| Tier | Changes | Home |
|---|---|---|
| **Theory of Change & Vision** | Yearly at most | `docs/strategy/theory-of-change.md` (this folder) |
| **Strategy** | A new edition each quarter | **Linear documents** on the `Guild Operating System` shelf (`Strategy — Q3 2026`, `Strategy — Q4 2026`, ...) |
| **Scorecard & Branch Map** | Rarely | this file |

Strategy is written fresh each quarter rather than edited forever, and it lives in Linear rather than here: it is an operating artifact that sits next to the initiatives it governs, not canon. Each edition supersedes the last without overwriting it, so the series is the version history. Reading the editions in order shows how the thinking shifted.

## The cascade

- **Strategy**: the current quarterly edition (Linear doc on the Guild Operating System shelf).
- **Outcomes**: Linear initiatives with Lean Outcome Cards (Outcome + Success signals + Target). The card's `Target:` line must match the initiative's target-date field.
- **Indicators**: each outcome initiative's `Indicator Register` Linear document, the canonical value table (`Indicator | Type | Target | Current | As-of | Source`). The June 2026 Google Sheet register is archived in Drive `Strategy/Indicators/`.
- **Outputs**: projects (each with `## Outcome`) and issues.

## The quarterly ritual

At each quarter's kickoff:

1. Write the new edition (`Strategy — Q4 2026`) as a Linear document on the Guild Operating System shelf.
2. Hold every live initiative against it: continue, close, or create.
3. **Re-point each initiative's strategy resource** at the new edition. An initiative nobody re-points is an initiative nobody confirmed still aligns, so the relinking is the alignment pass rather than overhead around it.

The Theory of Change gets the same treatment yearly, if at all. The scorecard-pulse flags a missing edition for the current quarter.

## Branches, teams, labels

Branch labels sit directly on initiatives (`branch:*`); issues roll up through `protocol:*` and `activity:*`.

| Branch | Issue-label rollup | Primary teams | Outcome initiatives |
|---|---|---|---|
| impact | `protocol:green-goods` | PRD, RESR | Product Health · Impact Methodologies · Env & Energy Data · Accessible Participation |
| capital | `activity:capital` + `protocol:pgsp` | PRD, RESR | Sustainability & Monetization · PGSP: Operators to Mainnet |
| social | `protocol:greenwill` | PRD | GreenWill Reputation & Identity |
| network | `protocol:network` | COM, MAR, PRD | Season Two Cohort Activation |
| growth | GROW team + `funding:*` (`activity:growth` retired; Growth is a team) | GROW | Growth & Funding |
| research | `activity:research` | RESR | Impact Methodologies (+ embedded across arcs) |
| ops | `activity:ops` | all | Guild Operating System (shelf, not an outcome) |

## Indicator rules

1. **Auto-derivable first.** An indicator earns a register row only if a routine can read it: Linear (issue/cycle/label queries), PostHog (funnel, MAU), on-chain (squads, badges, TVL), or Karma GAP (CIDS records, Hypercerts). Metrics only a human can supply (service revenue, event attendance) live as narrative in status updates instead.
2. **3-5 per outcome.** The vital few. If a signal matters but cannot be measured yet, it stays a Success signal on the card, not a register row.
3. **Every Current carries an As-of date.** A value without a date is treated as unknown.
4. **Registers are refreshed by the monthly scorecard-pulse** (1st of month): auto-derivable Currents updated, one status update per active outcome initiative, drift flagged (As-of over 30 days, card/field target mismatch, dead roadmap references, missing strategy edition for the current quarter).

## Exemptions

- **Status-only surfaces** (Coop Product Loop & Intent Clarity): no outcome card, no register; the pulse is the signal.
- **Completed and Canceled initiatives**: closed records with closed-register pointers.

## Cadences

- Product and research arcs: weekly light review (steward).
- Team arcs and Product Health: monthly scorecard review.
- Strategy: a new edition each quarter. Theory of Change: yearly.

## History

- 2026-06-21: first register built as a Google Sheet plus per-initiative docs. The sheet froze; it sat in nobody's workflow.
- 2026-07-18: Linear-first flip. Registers became the canonical value tables; the sheet was archived; slim sets adopted; the scorecard-pulse commissioned.
- 2026-07-19: strategy split into quarterly Linear editions (it is an operating artifact, not canon); the Theory of Change and this guide stay here as canon. Branch labels moved onto initiatives.
