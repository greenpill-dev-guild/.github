# Brave-First DevTools MCP Closeout

Date: 2026-05-24

## Current Posture

Use Brave first for local human/agent browser walkthroughs, WebMCP validation, extension review, and DevTools MCP proof. Keep Chrome/Chromium-compatible fallback paths for contributors and CI.

This applies to Codex, Claude, and other agents that read repo guidance. It does not mean CI requires Brave.

## Implemented

- Local Codex MCP now has a `brave-devtools` server pointing at `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`.
- The existing `chrome-devtools` server remains available as a Chrome for Testing fallback.
- Shared template guidance in `templates/agentic-modern-web.md` is Brave-first for local agent browser proof.
- Repo-local agent guidance was updated in:
  - `greenpill/network`
  - `greenpill/green-goods`
  - `greenpill/coop`
  - `wefa/app`
  - `portfolio`
  - `greenpill/TAS-Hub`
  - `greenpill/.github`

## Validation Completed

Network was the first concrete proof target.

Evidence:

- `greenpill/network` commit `cee52e2` records the Chrome for Testing and Brave DevTools MCP validation.
- Network validation proved MCP could open the page, capture desktop/mobile screenshots, inspect accessibility snapshots, list console/network activity, list WebMCP tools, run Lighthouse, and capture a performance trace.
- Brave run used isolated/headless/no-usage-stats/redacted-header MCP arguments.
- Runtime WebMCP was not enabled; the page correctly reported no WebMCP tools.

## Remaining Gaps

1. Confirm `brave-devtools` appears as direct callable tools after a fresh Codex session and in Claude/browser-extension workflows where applicable.
2. Run one Brave-backed DevTools MCP proof per major product repo, starting with public or low-risk surfaces:
   - Network homepage
   - Portfolio homepage/project route
   - TAS-Hub homepage/contact
   - Coop public app/extension-safe surface
   - Green Goods docs/public surface before admin/client authenticated surfaces
   - WEFA public/login/onboarding only with child-safety constraints
3. Fix Network findings surfaced by DevTools MCP:
   - local `/map/state` request logs `ERR_CONNECTION_REFUSED` when the website preview runs without the local agent service;
   - `llms.txt` exists but Lighthouse Agentic Browsing reports that it lacks links.
4. Add or standardize a short repo runbook for “Brave-first MCP browser proof” after direct tool exposure is confirmed.
5. Keep runtime WebMCP frozen until one public-safe read-only prototype passes:
   - discovery through Brave-backed DevTools MCP;
   - clear schema and parameter descriptions;
   - no private data exposure;
   - safe failure behavior;
   - confirmation boundaries for any write/navigation that changes user state.
6. Do not promote DevTools MCP to a hard CI gate yet. Keep it advisory until repeated Brave runs show low noise and clear value over existing Playwright/browser-proof lanes.

## Confidence

- DevTools MCP plumbing: high.
- Brave-first guidance consistency: high.
- Existing repo browser-proof lanes: good, still advisory-quality for visual polish.
- Runtime WebMCP readiness: early; strategy is ready, runtime rollout is not.

## Next Suggested Pass

Run a two-repo Brave proof comparison:

1. Re-run Network after fixing `llms.txt` links and deciding how `/map/state` should behave in website-only preview.
2. Run Portfolio or TAS-Hub as the second public-only proof target.

If both passes are clean and low-noise, make Brave-backed DevTools MCP a standard closeout checklist item for browser-facing changes.
