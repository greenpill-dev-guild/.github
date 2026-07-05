# Linear-Aware Dev Day Launcher

This playbook describes an agent-agnostic flow for starting a local dev day
from Linear context. The executable launcher logic lives in the local
`dev-surfaces` workbench; this repo owns the shared operating model so another
developer or agent can rebuild the same flow without depending on one assistant
runtime.

## Boundary

- Linear is the professional Greenpill Dev Guild work source.
- The active agent or script reads Linear through approved access, such as MCP,
  a connector, an API client, a CLI export, or a manually saved snapshot.
- `dev-surfaces` resolves a normalized work snapshot into local launch, health,
  and smoke commands.
- The launcher does not store a Linear API key and does not call Linear
  directly in v1.
- Agent-specific skills, plugins, memories, or project instructions are
  convenience hints only. They are not the source of truth for launch behavior.
- Personal or non-Linear projects are manual chat overrides.

## Day-Start Flow

Use this prompt in a general agent chat:

```text
Start my dev day from Linear. Read the current Product and Research cycle work,
include my assigned or active issues, pass a normalized snapshot to dev focus,
show me the inferred launch/health/smoke plan, and wait for confirmation before
launching. Do not kill unknown processes.
```

The active agent should:

1. List Linear teams and current cycles for Product and Research.
2. Read current-cycle issues and active assigned work with the smallest
   supported Linear queries.
3. Normalize issues into JSON with `id`, `title`, `url`, `team`, `status`,
   `statusType`, `cycle`, `assignee`, `priority`, and `labels`.
4. Run `dev focus --from <snapshot.json>` or pipe the same snapshot with
   `dev focus --from-stdin`.
5. Present the exact inferred `dev launch`, `dev health --json`, and
   `dev smoke --json` commands.
6. Launch only after confirmation, then run health and smoke.

## Mapping Model

The local workbench owns the mapping in `registry/work-focus.json`.

Default v1 intent:

- `protocol:green-goods` and `protocol:greenwill` map to the safe Green Goods
  local core: Anvil Arbitrum fork, local indexer, docs, admin, client, agent,
  and Storybook.
- `protocol:network` maps to the local Network stack.
- `protocol:tas` and `protocol:pgsp` are context-only in v1.

Production-backed Green Goods, prod-mirror, public tunnel, live-wallet, and
device/browser-helper modes require explicit human intent. They should never be
inferred from Linear labels alone.

## Manual Overrides

The active agent may pass overrides when the human asks for them:

```sh
dev focus --from work-snapshot.json --include portfolio
dev focus --from work-snapshot.json --exclude green-goods:indexer-graphql
```

Examples:

- "Start my day, include Portfolio" adds `portfolio`.
- "Start my day, skip Green Goods indexer" removes
  `green-goods:indexer-graphql`.
- "Start my day for personal work on Portfolio" can bypass Linear and use the
  explicit `dev launch portfolio` path.

## Safety

- Propose before launch by default.
- Do not kill unknown processes.
- Use `dev status`, `dev health`, and `dev smoke` for proof.
- Use repo-specific browser/E2E lanes after the workbench proves services are
  running.
