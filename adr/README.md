# Guild ADRs

> Architectural Decision Records for guild-wide choices that durably shape how we build.

## What goes here

ADRs in this directory capture **guild-level** decisions — choices that affect more than one project, or that codify a shared standard.

Examples of guild-level decisions:

- "We adopt Bun as the default runtime for new guild repos"
- "We use Conventional Commits across all guild projects"
- "We standardize on EAS for attestations across guild projects"
- "We require signed commits on protected branches in every guild repo"
- "We run reusable Claude PR review workflows centrally rather than per-repo"

What does **not** go here:

- Project-specific architecture decisions (live in the project's own `docs/adr/` or equivalent)
- Personal preferences or one-off choices
- Things that can change without affecting other projects

## Process

1. **Open an [RFC](https://github.com/greenpill-dev-guild/.github/issues/new?template=rfc.yml)** describing the proposed decision.
2. **Discuss** in the weekly call and on the forum (7+ day comment window).
3. **Decide** — stewards close the RFC with a decision.
4. **Record** — open a PR adding an ADR file here using the [template](./ADR-template.md).
5. **Apply** — surface the decision in templates, READMEs, and copilot-instructions where relevant.

## Naming and numbering

Files: `NNNN-short-kebab-case-title.md` where NNNN is a 4-digit sequence number (e.g. `0001-bun-as-default-runtime.md`). Numbers are assigned at PR-merge time, not at draft time.

## Index

> ADRs are added here as they're accepted.

| ID | Title | Status |
| --- | --- | --- |
| — | — | _no ADRs accepted yet_ |

## Statuses

- **Proposed** — under RFC discussion
- **Accepted** — decided, in effect
- **Superseded** — replaced by a newer ADR (link to the replacement)
- **Deprecated** — no longer in effect, no replacement
- **Rejected** — explicitly decided against (kept for historical record)
