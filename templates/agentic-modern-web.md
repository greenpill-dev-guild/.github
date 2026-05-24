# Agentic Modern Web Standard

Use this template when a Greenpill project has a public web, docs, PWA, extension, or browser-facing UI surface. Customize the repo-specific commands and forbidden WebMCP tools before adopting it.

## Defaults

- Baseline target: Baseline Widely Available.
- Enforcement: advisory scripts first; CI gates only after the proof loop is stable.
- `llms.txt`: public/docs surfaces only.
- WebMCP: strategy first; no runtime tools until explicitly approved.

## Repo Guidance Snippet

- Before frontend, UI, CSS, HTML, accessibility, browser proof, or web-design changes, search and retrieve current Chrome Modern Web Guidance and apply this repo's Baseline Widely Available target.
- Prefer semantic HTML, native controls, platform CSS, and browser primitives before custom JavaScript or new dependencies.
- Keep the DOM and accessibility tree legible: one clear `main`, meaningful headings, labels, accessible names, visible focus, keyboard paths, touch targets, loading/error/empty states, and reduced-motion behavior.
- Run `bun run agentic:check` as the advisory proof front door. Use `bun run agentic:browser-proof` for rendered proof when layout, interaction, motion, or public routes change. Keep `agentic:verify` as the repo's existing heavier lane when it already has that name.
- WebMCP is strategy-only until approved. Future tools must be visible, user-confirmable, public-safe, scoped to the page, and forbidden from exposing secrets, private data, hidden admin actions, destructive operations, onchain writes, or background-only actions.

## Suggested Scripts

Choose existing local commands; do not add new dependencies.

```json
{
  "scripts": {
    "agentic:check": "<existing light checks>",
    "agentic:browser-proof": "<existing rendered browser/playwright/lighthouse proof>",
    "agentic:verify": "<existing browser/storybook/playwright proof>"
  }
}
```

`agentic:browser-proof` should emit or preserve evidence an agent can cite: routes/surfaces checked, viewport matrix, screenshot or visual artifact, console/page errors, accessibility-tree or role assertions, reduced-motion state when relevant, `llms.txt` reachability for public/docs roots, and WebMCP tool discovery status (`not_configured` is acceptable before runtime WebMCP exists).

## `llms.txt` Scope

Only publish `llms.txt` from already-public app/docs roots. Keep it focused on project purpose, public routes/docs, agent guidance, and privacy exclusions. Do not include private API routes, admin-only docs, internal credentials, unpublished roadmaps, or operator-only procedures.

## WebMCP Strategy Checklist

- Candidate tools are visible on the page and map to normal user actions.
- Each tool has an explicit confirmation rule for writes, submissions, purchases, publishes, or navigation that changes user state.
- Forbidden tools are listed in the repo strategy doc.
- Browser proof includes screenshots or DOM checks, console health, accessibility-tree sanity, and reduced-motion behavior when motion is present.
- Before runtime rollout, use Chrome DevTools MCP or Puppeteer WebMCP to prove tool discovery, schema validity, graceful errors, and absence of forbidden tools. Add evals for wrong-tool, wrong-order, wrong-argument, stale-state, and confirmation-boundary cases.
