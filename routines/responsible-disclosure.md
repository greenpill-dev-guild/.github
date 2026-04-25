# Responsible Disclosure

> How the guild handles security disclosures from external researchers and contributors.

**When to use this**: You received a security disclosure on behalf of the guild, or you're a researcher wanting to understand our process.

## For researchers (TL;DR)

- **Email**: `security@greenpill.builders`
- **Acknowledgment**: within 3 business days
- **Disclosure window**: please give us reasonable time to fix before public disclosure
- **Recognition**: we will credit you in the fix announcement unless you prefer otherwise
- **Public issues**: do **not** open public GitHub issues for security vulnerabilities

Full policy: [SECURITY.md](../SECURITY.md).

## Steward / maintainer flow

When a disclosure arrives:

### 1. Acknowledge (within 3 business days)

Reply to the researcher confirming receipt. Don't promise a fix timeline yet — promise a timeline for the **assessment**.

### 2. Triage (within 1 week)

Determine:

- **Severity** — critical / high / medium / low
- **Affected projects** — which guild repos? Any forks? Any deployed contracts?
- **Exploitability** — is this theoretical or actively exploitable?
- **Blast radius** — could this cause user funds loss? PII exposure? Ecosystem-level harm?

If the project is on our [supported list](../SECURITY.md#supported-projects), we own the fix. If it's a fork or dormant project, decide whether to upstream or close.

### 3. Stand up the fix

For **critical or high severity**:

- Form a small fix group (one steward + one maintainer + the researcher if helpful)
- Work in a private fork or branch with restricted visibility
- Coordinate with the researcher — they may have proof-of-concept code that helps

For **medium or low severity**:

- File an internal-only tracking issue
- Plan the fix into the normal release flow
- Communicate the timeline to the researcher

### 4. Coordinate disclosure

Pre-disclosure timeline depends on severity and exploitability. Standard windows:

- **Critical** — coordinate fix and disclosure within 30 days
- **High** — coordinate within 60 days
- **Medium** — coordinate within 90 days
- **Low** — disclose at next normal release; advisory if needed

Negotiate with the researcher if their timeline differs.

### 5. Ship the fix

- Merge through normal review (with sensitivity to not leaking the vuln in commit messages until disclosed)
- Tag a release
- Update the project changelog

### 6. Publish the advisory

Use **GitHub Security Advisory** on the affected repo:

- Vulnerability description
- Affected versions
- Patch versions
- Workarounds (if any)
- Credit to the researcher (with their consent)
- CVE if assigned

Cross-post to:

- Project's `CHANGELOG.md`
- Forum announcement
- Discord `#announcements` channel

### 7. Post-mortem (for critical issues)

Within 2 weeks of disclosure:

- Write a short post-mortem (private if it covers exploitation; public if it's about the bug class)
- Discuss in the next stewards meeting
- File any preventive issues (better tests, scanning, monitoring)
- Update [SECURITY.md](../SECURITY.md) if process gaps were exposed

## Common pitfalls

- **Slow acknowledgment** — researchers often go public if ignored for >2 weeks. Always reply within 3 business days even if you don't have answers yet.
- **Silently fixing without crediting** — burns bridges with the security community.
- **Public issues for vulnerabilities** — even "low severity" should not be public until patched.
- **Skipping advisories** — downstream users need to know to upgrade.
- **Underestimating severity** — when in doubt, treat as one tier higher than it looks.

## What is and isn't a security issue

**In scope** for this routine:

- Smart contract vulnerabilities (reentrancy, access control, etc.)
- Authentication or authorization bypass
- Sensitive data exposure
- Supply-chain compromise (typo-squatted deps, compromised maintainer keys)
- Server-side issues with exploitable consequences

**Out of scope** (treat as normal bugs, not security):

- UX confusion that doesn't expose data
- Missing rate limits without exploit path
- Deprecated dependencies without exploit path
- Self-XSS

## See also

- [SECURITY.md](../SECURITY.md) — public-facing policy
- GitHub's [Security Advisories docs](https://docs.github.com/en/code-security/security-advisories)
