# Security Policy

## Overview

The Greenpill Dev Guild is committed to the security and privacy of our projects and contributors. This document outlines how we handle vulnerability reports and our baseline security practices across guild repositories.

## Supported projects

Security updates are provided for the latest version of each actively maintained guild project. "Actively maintained" means the project has had commits within the last 6 months or is explicitly maintained by a steward.

| Project | Status | Notes |
| --- | --- | --- |
| [green-goods](https://github.com/greenpill-dev-guild/green-goods) | Active · supported | Latest version; critical-only patches for older releases |
| [coop](https://github.com/greenpill-dev-guild/coop) | Active · supported | Latest version |
| [cookie-jar](https://github.com/greenpill-dev-guild/cookie-jar) | Active · supported | Latest version |
| [network-website](https://github.com/greenpill-dev-guild/network-website) | Active · supported | Latest version |

For other guild repositories — including forks (`charmverse`, `gardens`, `octant-v2-core`, `opencred`, `greenpill-hypercerts`) and dormant projects (`greenwill`, `allo-yeeter`, `impact-reef`, `greenpill-commons`, `regen-rabbit-race`) — we do not actively patch. Critical issues affecting upstream may be reported to upstream maintainers; reports affecting guild forks specifically can still be sent to us via the channel below.

## Reporting a vulnerability

If you identify a potential security vulnerability in any guild repository, **do not open a public issue**. Instead:

1. **Email** the issue details to `security@greenpill.builders`.
   - Include a detailed description of the vulnerability, the affected component(s), and the potential impact.
   - Provide reproduction steps if possible.
   - Include any suggested mitigation.
2. **Acknowledgment** — we will acknowledge receipt within **3 business days** and begin assessment.
3. **Investigation and remediation** — we aim to address valid issues promptly. Critical issues receive immediate attention; minor vulnerabilities are addressed in due course. We will keep you updated.
4. **Responsible disclosure** — please give us a reasonable window to address the issue before disclosing publicly. We will credit you in the fix announcement unless you prefer otherwise.

For additional context on our disclosure approach, see [routines/responsible-disclosure.md](./routines/responsible-disclosure.md).

## Security practices

Across guild repositories we maintain:

- **Access control** — strict permissions; only authorized contributors can modify production-critical code; signed commits required on protected branches.
- **Two-factor authentication** required for all org members.
- **Dependency management** — Dependabot enabled; dependencies updated regularly; vulnerable versions patched promptly.
- **Code review** — all changes reviewed by a maintainer before merging to protected branches; CODEOWNERS routes high-risk paths to the appropriate reviewer.
- **Continuous monitoring** — GitHub security tooling (Dependabot, Secret Scanning, Code Scanning where applicable) on every active repo.
- **Open source only** — all dependencies must be open-source-licensed and auditable.

## High-risk paths

Across guild projects, the following paths warrant elevated review and steward sign-off:

- Deployment, verification, migration, and upgrade scripts
- Smart contract source code (`packages/contracts/src/**` and equivalents)
- Authentication and authorization providers
- Environment configuration (`.env*`)
- CI/CD configuration (`.github/workflows/**`)
- Dependency manifests for supply-chain-sensitive packages

Project-level `CLAUDE.md` / `AGENTS.md` may extend this list with project-specific high-risk paths.

## Contact

- **Security disclosures**: `security@greenpill.builders`
- **General contact**: `contact@greenpill.builders`
- **Stewards**: `steward@greenpill.builders`
