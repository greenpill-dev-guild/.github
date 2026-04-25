# Templates

> Copy-into-repo starter files for new and existing guild projects.

These are **opt-in templates**, not org-wide enforcement. Anything in this directory is meant to be copied into a guild project repo and then customized for that project's specifics. Files in the parent `.github/` repo (community-health files, issue templates, PR template) propagate automatically; files here do not.

## Available templates

| Template | Use when |
| --- | --- |
| [`CLAUDE.md.template`](./CLAUDE.md.template) | Setting up a new repo for Claude Code, or formalizing existing AI-assisted work. |
| [`AGENTS.md.template`](./AGENTS.md.template) | Documenting agent invariants and working agreements for any AI coding assistant. |
| [`copilot-instructions.md.template`](./copilot-instructions.md.template) | Setting up `.github/copilot-instructions.md` for GitHub Copilot. |
| [`README.md.template`](./README.md.template) | Bootstrapping the README for a new guild project. |

## How to adopt

1. Copy the template into your project repo (rename to drop `.template`).
2. Replace every `{{PLACEHOLDER}}` with project-specific content.
3. Delete sections that don't apply to your project.
4. Commit and treat it as a living document — update as the project evolves.

## Stack assumption

These templates are written **bun-forward** — they assume Bun as the JS runtime and package manager unless your project has a specific reason to use something else. If your project is on pnpm, yarn, npm, or a non-JS stack, replace bun-specific commands with your equivalents.

## Contributing back

If you customize a template in a way that other projects could benefit from, open an [RFC](https://github.com/greenpill-dev-guild/.github/issues/new?template=rfc.yml) to discuss promoting your changes back into the template here.
