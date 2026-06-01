# How the Dev Guild Pays for Scoped Work

> How the guild values and pays for work across every discipline — engineering, product, marketing, community, research, and growth / BD / funding. Companion to [Funded Work Intake](./funded-work-intake.md), which covers how work is identified and scoped.

**When to use this**: You are a steward, maintainer, or contributor agreeing payment for guild work. Volunteer contributions use the normal issue / PR flow.

## Principle

We pay for **accepted outputs, not for time.** A scoped piece of work is the unit, and **"Done" (acceptance criteria met + accepted) is the payment event.** The bar is the acceptance criteria agreed *up front*, not a judgment call at review.

## Two ways we pay

- **Deliverable work → scoped brief + estimate (fixed price).** Most work: a feature, a campaign, a logo, a spec, a research memo, a grant application, an impact report. Scope it, size it, pay on acceptance.
- **Continuous work → a role / retainer per cycle.** Ongoing coverage that isn't a single artifact — community support, ongoing engineering maintenance, funding tracking. Paid as a **monthly role stipend**, with **extra scoped sessions tracked per hour** (e.g. a dedicated onboarding or support session beyond the baseline).

The per-discipline table says which mode each discipline uses. The stages, sizing, and acceptance flow below describe **deliverable** work.

## The unit (deliverable work)

A payable brief carries one named **Output** · 3–6 **Acceptance criteria** · a **Boundary** · a **Decision/exit** (done-when + the decision it feeds) · an **estimate** (its sizing tier). No clear artifact + criteria ⇒ not payable yet — it's still in scoping, which is itself paid (Stage 0). Research uses the RESR-4 issue template; the same shape works for any discipline.

## Two stages (deliverable work)

- **Stage 0 — Paid scoping (Scout tier, up front).** The deliverable *is the brief*: output + acceptance criteria + boundary + decision/exit + a proposed execution estimate. How a contributor gets "paid to explore" — but the money buys a reviewable output. If Stage 0 yields only vagueness, execution isn't funded: a small, bounded spend and a clean exit.
- **Stage 1 — Execution (sized + tranched).** Fund the accepted brief at its estimate tier, across 2–3 tranches on its milestones; the final tranche releases on decision/exit acceptance.

## Sizing — how much

Price **bounded effort at a guild rate set per brief by impact, sized at scope time by the scoper — not the contributor.** The rate is an internal sizing tool; **work is billed fixed-price per brief, never open hourly** (the exception is continuous-work hourly extras).

- **Guild rate: $30–60/hr, set per brief by impact.** Low end for routine work; top end for a high-impact sprint that materially moves the guild forward. An explicit early-stage discount below market; rises as grants grow.
- **Relativity ladder:** engineering / integration is the heaviest implementation lift → it anchors the top (a major integration is ~80–200h of senior work). Product, marketing, research, and growth size *at or below* comparable engineering effort.
- **Sizing tiers** — recorded as each issue's Linear **estimate** (price = estimated hours × the impact rate, fixed for the brief):

  | Tier | Estimate | Effort | Typical fixed price |
  |---|---|---|---|
  | **Scout** | 1 | 3–10 hrs | $100–500 |
  | **Brief** | 2 | 12–30 hrs | $500–1,800 |
  | **Deep** | 3 | 40–80 hrs | $1,500–3,000 |

  Most product / marketing / research briefs are **Scout–Brief** (clear scope, ~1–2 weeks). **Deep** is reserved for cross-cutting, load-bearing work and stays below a major integration.

## By discipline

| Discipline | Unit / output | "Accepted" means | How it's paid |
|---|---|---|---|
| **Engineering** | a shippable change — feature, fix, integration (PR-backed) | merged + meets AC + verified working | deliverable tiers; heaviest lift, anchors the top. Ongoing maintenance → continuous role. |
| **Product** | a scoped product artifact — spec, flow, UX design, brief | approved vs the brief + build-ready | deliverable tiers; clear scopes, ~1–2 weeks |
| **Marketing** | a campaign / content / brand asset (incl. logo, creative) | shipped + meets the brief | deliverable tiers; clear scopes, ~1–2 weeks |
| **Community** | supporting users + members — onboarding, support, engagement | coverage held / session delivered | **monthly support-role stipend** + **per-hour** for extra onboarding or dedicated support sessions |
| **Research** | a decision-ready artifact — memo, taxonomy, readiness plan | AC met + decision usable (incl. a rigorous "no-go") | deliverable tiers (Scout / Brief / Deep), sized below engineering |
| **Growth / BD / Funding** | grant application, impact report, partnership, funding tracking | submitted / delivered / partnership advanced | funding-pegged tiers (a fraction of the funding unblocked); grant **sourcing + tracking** are pipeline / continuous |

**Design is not a separate lane** — product / UX design is a Product artifact; brand / creative (logos, assets) is a Marketing artifact.

## Controlling total spend

The rate sizes a brief; it does not bound the budget. What keeps spend affordable:

- **Grant-tied envelope — the actual spend bound.** Paid work is funded as a capped line-item inside the grant or initiative it supports (a set amount / % per cycle), not an open pool — and we prefer work that helps unblock the funding it draws from.
- **WIP cap for focus.** Keep a small number of paid deliverable briefs active per lane (≤ 2–3) so work finishes; the envelope, not headcount, is what caps total spend.
- **Most exploration stays unpaid signal.** Discussion channels and the weekly synthesis capture raw exploration for free; a *paid* brief is the exception, reserved for scoped, decision- or ship-critical work.

## Accept, revise, escalate

- **Accepted = acceptance criteria met**, reviewed by the scoping steward or a **designated / external evaluator** — acceptance should not be one person's solo subjective call.
- Short of criteria → **one revision round** (request-changes + a short re-due).
- Still short → escalate: **re-scope / split** (partial credit for the accepted portion) **or reassign.** **Budget follows the output:** if someone else finishes it, the unearned tranche moves with it. The guild pays once, to whoever clears the bar.

## Trust over time

First engagement: more up front, more support. Future front-loading is **earned by delivery**; repeated misses mean quiet non-renewal, not confrontation. Cash isn't the whole package — recognition (GreenWill), credited overflow pickups (`reassigned:overflow`), and a rising track record all count. As budgets grow the **$30–60 range itself rises toward market** on a stated trigger (e.g. per major grant won), and proven delivery moves a contributor toward the top of the current range.

## In Linear

- A paid **deliverable brief** lives as an issue on its team (Product or Research), carrying the **scoped-brief shape** (the RESR-4 template), an **`activity:*` label** for its discipline (`build` / `design` / `research` / `architecture` / …), and its **estimate** set on the issue (Scout ~ 1 / Brief ~ 2 / Deep ~ 3).
- **Growth / BD / Funding** runs through the `funding:*` lifecycle labels + the Grant Scouting project (sourced by the `guild-grant-scout` routine).
- **Continuous roles** (community support, maintenance) are a recurring arrangement, tracked separately from per-brief issues.
- The **research-accountability pulse + rule** govern dated, owned deliverable issues — Research today, extendable to Product.

## Related

- [Funded Work Intake](./funded-work-intake.md) — how scoped paid work is identified and scoped; this playbook is its pricing / payment layer.
- [Grant Application](./grant-application.md) — funding-source-side process for the Growth / BD / Funding lane.
- **Research Accountability** rule (Linear Document, Research team) — scope → due date → pulse → escalation; this playbook prices and pays the same flow.

---

*Status: draft for steward review. Disciplines: engineering · product · marketing · community · research · growth/BD/funding. Deliverable work = scoped brief + $30–60/hr impact-set tiers (research sized below integration); community = monthly support role + hourly extras; product/marketing = artifact briefs, ~1–2 weeks. Spend bound = the per-grant envelope.*
