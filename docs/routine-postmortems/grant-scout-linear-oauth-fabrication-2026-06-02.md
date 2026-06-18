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
