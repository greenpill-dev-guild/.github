# Scorecard & Branch Map

> Canonical operating guide for outcomes and indicators (the balanced-scorecard layer). Companion to `docs/linear-operating-model.md`; where they overlap on routing, the operating model wins.

## The cascade

- **Strategy**: this folder (`docs/strategy/`). Theory of Change & Vision reviewed yearly; Strategy reviewed quarterly (alignment pass over all initiatives, logged in strategy.md).
- **Outcomes**: Linear initiatives with Lean Outcome Cards (Outcome + Success signals + Target). The card's `Target:` line must match the initiative's target-date field.
- **Indicators**: each outcome initiative's `Indicator Register` Linear document, the **canonical** value table (`Indicator | Type | Target | Current | As-of | Source`). The June 2026 Google Sheet register is archived in Drive `Strategy/Indicators/`.
- **Outputs**: projects (each with `## Outcome`) and issues.

## Branches ↔ teams ↔ labels

Branches are the strategic lens (what kind of value); teams are who works; labels roll issues up.

| Branch | Issue-label rollup | Primary teams | Outcome initiatives |
|---|---|---|---|
| impact | `protocol:green-goods` | PRD, RESR | Product Health · Impact Methodologies · Env & Energy Data |
| capital | `activity:capital` + `protocol:pgsp` | PRD, RESR | Sustainability & Monetization · PGSP |
| social | `protocol:greenwill` | PRD | GreenWill Reputation & Identity |
| network | `protocol:network` | MAR, COM, PRD | Marketing & Story · Season Two Cohort Activation |
| growth | GROW team + `funding:*` (`activity:growth` retired; Growth is a team) | GROW | Growth & Funding |
| research | `activity:research` | RESR | Impact Methodologies (+ embedded across arcs) |
| ops | `activity:ops` | all | (operating docs shelf + status-only pulses; not an outcome arc) |

## Indicator rules

1. **Auto-derivable first.** An indicator earns a register row only if a routine can read it: Linear (issue/cycle/label queries), PostHog (funnel, MAU), on-chain (squads, badges, TVL), or Karma GAP (CIDS records, Hypercerts). Metrics only a human can supply (service revenue, event attendance) live as narrative in status updates instead.
2. **3-5 per outcome.** The vital few. If a signal matters but can't be measured yet, it stays a Success signal on the card, not a register row.
3. **Every Current carries an As-of date.** A value without a date is treated as unknown.
4. **Registers are refreshed by the monthly scorecard-pulse routine** (1st of month): it updates auto-derivable Currents, posts one status update per active outcome initiative, and flags drift (As-of over 30 days, card/field target mismatch, dead roadmap references, strategy.md unreviewed over ~100 days).

## Exemptions

- **Status-only surfaces** (Software Ecology & Agentic Workflow Health, Coop Product Loop & Intent Clarity): no outcome card, no register; their pulses are the signal.
- **Completed initiatives** (Linear Migration, GG Protocol Hardening, Network Presence): closed records; no live registers.

## Cadences

- Product/research arcs: weekly light review (steward).
- Team arcs (Growth & Funding, Season Two Cohort Activation, Marketing & Story) + Product Health: monthly scorecard review.
- Strategy: quarterly alignment review, logged in `strategy.md`; Theory of Change: yearly.

## History

- 2026-06-21: first register built as a Google Sheet + per-initiative docs. The sheet froze; it sat in nobody's workflow.
- 2026-07-18: Linear-first flip. Registers became the canonical value tables; the sheet was archived; slim sets adopted; the scorecard-pulse routine commissioned. Strategy canon moved to this folder (strategy is not an initiative; initiatives come from it).
