# Grant Scout Linear/OAuth and Fabrication Incident

Date: 2026-06-02

## Summary

The 2026-05-28 `guild-grant-scout` run exposed two coupled failure modes:

- Linear access depended on an OAuth connector that can lapse in unattended cron runs.
- The routine treated prior proposal materials as prior awards, which let an unverified "Evidence Commons" / NLnet track-record claim enter grant-planning context.

The immediate routine prompt was later hardened in `routines/claude/guild-grant-scout.md`.

## Root Causes

- **Headless OAuth fragility.** Weekly unattended routines cannot rely only on periodic human OAuth re-consent when the output needs Linear continuity.
- **Wrong recall surface.** Funding recall must query the workspace-wide `funding:*` lifecycle, not only one team or one project.
- **Track-record ambiguity.** Proposal drafts and reusable application materials were not clearly separated from awarded/completed grants.
- **Weak claim verification.** The prompt did not require prior-funding, metric, partnership, or live-capability claims to trace to primary sources before entering a draft or Linear issue.

## Durable Fixes

- `guild-grant-scout` now treats prior grant files as **application materials, not awards**, unless the grants ledger proves completed status.
- The live routine requires factual claims to be verified against primary sources before they enter drafts, issues, or posts.
- `NLnet = Applied/pending, never awarded` is explicitly recorded in the routine prompt to prevent recurrence of the fabricated prior-award claim.
- Funding lifecycle tracking belongs in Linear `funding:*` saved views and accepted-award projects; GitHub issues are only for public execution work.

## Current Guardrail

See:

- `routines/claude/guild-grant-scout.md`
- `docs/linear-operating-model.md`
- `routines/grant-application.md`

## Model change (2026-07-26)

`guild-grant-scout` moved to `claude-fable-5`, chosen partly because of this incident: the failure mode here was fabrication under ambiguity, and that is the axis Fable is strongest on. The move does **not** retire any guardrail above. The existence gate and the verify-against-primary-source rule stay exactly as written, because they check third-party facts rather than the model's own reasoning, and no model tier makes them unnecessary.

It does introduce one new failure mode to watch on this routine specifically. Fable's safety classifiers can decline a request on an HTTP 200 with `stop_reason: "refusal"`, and the routines platform exposes no fallback parameter, so a declined run is a **silent no-op**: no post, no Linear write, no error. Grant scouting reads government, security-adjacent, and climate funding portals, which is where a false-positive decline is most plausible. If a Thursday passes with no `#funding` post and no failure line, check the run transcript before assuming a quiet week. Fable also requires 30-day data retention and returns a 400 on every request under zero-data-retention.
