# NLnet Grant Strategy — Greenpill Dev Guild
### Deep-research + application approach for the three June-1 NLnet funds
**Date:** 2026-05-31 · **Sources:** Greenpill Shared Drive (funding corpus), GitHub `green-goods` + `coop` (+ `network`, `TAS-Hub`), NLnet public docs. · **Deadline for all three funds: 2026-06-01 12:00 CEST (noon).**

---

## 0. TL;DR — recommendation up front

You asked how to best approach the three NLnet funds (**NGI Zero Commons**, **NGI TALER**, **NGI Fediversity**). After cross-referencing our docs, code, and each fund's own criteria:

> **#1 — Lead with NGI Fediversity (Coop).** Strongest, cleanest, most defensible fit. Coop *is* federated, local-first, data-portable infrastructure — exactly what the fund exists for.
> **#2 — Submit NGI Zero Commons (Green Goods library-extraction)** — but only with a framing clearly distinct from the Commons app we *already have pending* from the April call.
> **#3 — Treat NGI TALER as opportunistic / probably defer.** There is genuinely no GNU Taler integration in our code and no draft; a weak fit hurts us with a funder we want long-term. Submit only if someone commits to a real Taler-integration scope, else target the Aug 1 call.

NLnet allows multiple submissions in one batch, judged independently — **two strong proposals beat three uneven ones.** No penalty for skipping TALER.

### Two findings that change the plan (see §2)
1. **We have NOT completed a prior NLnet "Evidence Commons" grant.** That claim exists only in an AI-drafted file; every primary source shows NLnet as *Applied/pending*. **Do not cite a prior NLnet relationship** — it's trivially checkable and would damage credibility with the exact funder we're courting.
2. **A Commons application is already pending** (the €48K "Interoperable Reporting Infrastructure", Hypercerts+ATProto, submitted ~Apr 1). A near-identical June Commons proposal reads as double-dipping — the June one must be **clearly different**, or hold it.

---

## 1. Verified fund facts (confirmed on nlnet.nl, May 2026)

All three are NLnet/NGI funds on the **same `/propose` form**, **same deadline (1 Jun 2026 12:00 CEST)**, **same band €5,000–€50,000**, first-time cap **€50K**, **hard rule: 100% of results published under a recognised FOSS license**, **English**, **R&D as primary objective**, **AI-use disclosure required**.

| Fund | Funds what | Our vehicle | Fit |
|---|---|---|---|
| **NGI Zero Commons** | Any internet commons — software, standards, data, P2P, middleware, end-user apps | Green Goods evidence/portability middleware | **Strong** (overlaps pending app) |
| **NGI Fediversity** | Decentralised, self-hostable, **federated** services; **data portability & user data ownership**; mix-and-match, no lock-in | **Coop** — local-first, Yjs CRDT P2P, ATProto/PDS, Filecoin | **Strongest + cleanest** |
| **NGI TALER** | Strengthen the **GNU Taler** privacy-preserving e-cash ecosystem (integrations, tools, use cases) | Green Goods funding rails | **Weak** — not Taler / not e-cash (§5) |

**NGI Zero scoring (Guide for Applicants):** Relevance/Impact/Strategic **40%** · Technical excellence/feasibility **30%** · Cost-effectiveness/value **30%**; must clear **>5.0/7**. → Spend the most words on **impact & strategic relevance**, then prove it's technically real, then a budget that's obviously honest.

**Top rejection triggers (verbatim themes):** weak differentiation from existing work · unsubstantiated claims · vague sustainability · budget rates disconnected from task value · ignoring the European dimension · not committing to open access/OSS.

**European dimension:** not a hard gate (worldwide eligible; EU/Horizon-associated get priority "given equal proposals"). We're US-led, so we must **surface a real European hook** — and we have genuine ones: **live pilots in Spain and Italy**, plus ATProto/Fediverse and GNU Taler are both European-rooted. Lead with these.

**AI disclosure:** our April submission already has a clean disclosure section (Claude + ChatGPT, structural editing only, applicant-reviewed, prompt dates) — **reuse verbatim.**

Sources: [Commons](https://nlnet.nl/commonsfund/) · [Commons Guide](https://nlnet.nl/commonsfund/guideforapplicants/) · [Eligibility](https://nlnet.nl/commonsfund/eligibility/) · [TALER](https://nlnet.nl/taler/) · [Fediversity](https://nlnet.nl/fediversity/) · [Fediversity Guide](https://nlnet.nl/fediversity/guideforapplicants/) · [Funding index](https://nlnet.nl/funding.html).

---

## 2. Critical findings (read before writing)

### 2.1 No prior NLnet "Evidence Commons" grant exists in our records
The €50K VLET draft asserts *"Prior delivered work: NLnet NGI Zero Commons 'Evidence Commons' (completed)."* Contradicted by every primary source:
- Grants ledger `database-export.csv`, verbatim: `Nlnet Foundation … Apr 1 https://nlnet.nl/propose/ afo.eth **Applied**` — *Applied*, not completed; **no** "Evidence Commons" row exists.
- Schneider briefing (2026-05-12): *"OSV and NLnet are draft proposals in progress."*
- Grant-scout memo (2026-05-14): NLnet *"drafting … Deadline 2026-06-01."*
- The submitted proposal cites no NLnet grant number — a first-time applicant's profile.

**Action:** do not claim any prior NLnet relationship unless Afo can produce a grant agreement/acknowledgement email. Treat the VLET line as an AI hallucination.

### 2.2 A Commons app is already pending (April call)
The €48K "Interoperable Reporting Infrastructure" is in, status *Applied*. June's Commons submission must be a **clearly different scope** (the VLET "extract reusable libraries" angle qualifies — it's reuse/commons, vs the April app's interoperability-lexicon angle) **or we hold Commons** and let April run. **Verify April's exact call/status first.**

### 2.3 GreenWill/identity is triple-claimed → deconflict
The **GreenWill recognition + attestation** layer is scoped in the VLET Commons draft, the pending **Octant × Greenpill** proposal, *and* implicitly the April NLnet app. Pick one home. **Recommendation: GreenWill → Octant; keep the NLnet asks on infrastructure** (federation, portability, evidence middleware). Overlapping funding is an explicit NLnet rejection trigger.

---

## 3. NGI Fediversity — lead proposal (Coop)  ⭐ #1

**Why our best shot:** Fediversity funds decentralised, self-hostable services where **users own and can move their data between services** — and Coop is close to a textbook fit, backed by real code (not slideware).

**Verified technical substance** (from code audit, file-path-backed):
- **Genuine CRDT P2P:** `yjs`, `y-webrtc`, `y-websocket`, `y-indexeddb` wired in `coop/packages/shared/src/sync-config.ts` + `modules/coop/sync.ts`; an actual Hono+Bun WebSocket **signaling + Yjs doc-sync server** at `packages/api/src/ws/` — not a stub.
- **Local-first by architecture (ADRs 001-007):** raw captures live in IndexedDB and never auto-sync; **publish is an explicit human gesture** (ADR-005); encrypted-at-rest (ADR-007); browser-extension-primary, server minimized (ADR-004).
- **Data portability:** three-format artifact sync + board/proof/archive/receipt export paths (ADR-006) — directly answers the fund's "separate content from the service provider."
- **Passkey-first identity (ADR-003):** no wallet-extension or Big-Tech dependency.
- **Green Goods is a real downstream consumer** (`modules/greengoods/`, the Roost surface) — proves it generalises beyond one app.

**Framing:** *"Coop — a local-first, federated knowledge commons for community groups: capture, refine, and publish shared group memory across devices and peers with no central server and full data portability."* Federated group-knowledge infrastructure, **not** "a notes app."

**European dimension:** ATProto/Fediverse alignment + EU community pilots.

**Honest scoping (do not overclaim):** Coop's onchain/Safe, Storacha/Filecoin archival, Semaphore privacy, and session-keys are **mock-first by default** (`VITE_COOP_*_MODE=mock/off`). Scope the proposal to what's live today (local-first capture, CRDT sync, export/portability, passkey identity) and frame the gated rails as the **funded R&D deliverable** (e.g. "harden self-hostable signaling + live Filecoin archival to production").

**Fix before submit:** **Coop has no LICENSE file** (repo or per-package). NLnet requires an OSS license commitment — add one (AGPL-3.0 or MIT) as part of the application.

**Budget shape:** €45–50K @ ~€100/hr, 4–5 deliverables: (1) self-hostable signaling + federation hardening, (2) data-portability/export + PDS bridge, (3) reference self-host deployment + docs, (4) threat-model + audit-ready posture, (5) public retrospective. 6–12 mo, milestone-paced.

---

## 4. NGI Zero Commons — second proposal (Green Goods middleware)  ⭐ #2 (conditional)

**Condition:** only if clearly distinct from the pending April app (§2.2). Cleanest distinct scope = the **VLET "extract reusable libraries" angle**: lift the proven offline-capture + EAS-attestation + verification primitives out of the Green Goods monorepo into **standalone, documented, independently-published OSS packages** any community-tech project can adopt. That's a *commons/reusability* story (what Commons funds), distinct from April's *interoperability-lexicon* story.

**Verified technical substance** (file-path-backed):
- **Offline-first, real:** VitePWA+workbox service worker (`packages/client/vite.config.ts`); versioned **IndexedDB job/outbox queue** (`shared/src/modules/job-queue/db.ts`) with a `client_work_id → EAS attestation` mapping table; resumable drafts; sync-on-reconnect (`hooks/app/useOffline.ts`).
- **On-chain attestation, deployed:** EAS Work/WorkApproval/Assessment schemas with **live Arbitrum schema UIDs** in `contracts/deployments/42161-latest.json` (`workSchemaUID 0x43ebd37d…`, etc.).
- **Identity:** passkey/WebAuthn + ERC-4337 via Pimlico (`shared/src/config/{passkeyServer,pimlico}.ts`).
- **Hypercerts** minting + marketplace (`workflows/mintHypercert.ts`, `@hypercerts-org/sdk`).
- **i18n:** full **en/es/pt** (~3,393 keys each) — serves non-English regen communities.
- **Indexer:** Envio HyperIndex (`packages/indexer/config.yaml`).
- **MIT-licensed**, public monorepo, strong test/CI (per-package GH workflows, Playwright e2e incl. passkey-mock/anvil-fork projects, Foundry **audit-realism** harness) — directly supports NLnet's "R&D / audit-ready" framing.

**Framing:** *"A Verifiable Local-Evidence Toolkit — extract Green Goods' in-production offline-capture, on-chain attestation, and verification primitives into reusable MIT-licensed packages so any community-tech project can document, attest, and verify field work offline, on cheap phones, with no platform owner."*

**Why it scores:** high Impact/Strategic (reuse of *proven, in-production* code, named first adopter Coop, real Global-South deployments) + high feasibility (extraction/hardening, not greenfield).

**Deconfliction:** carve GreenWill out (→ Octant); in "other funding sources," state Green Goods platform/pilot work is Arbitrum-funded and this ask is *only* the OSS library-extraction R&D (reuse April's honest non-overlap framing).

---

## 5. NGI TALER — honest assessment: probably defer

**The fit is weak; a rushed submission risks our standing.** TALER funds the **GNU Taler** ecosystem — privacy-preserving **e-cash/payments** (customer anonymity, merchant transparency, CBDC/community-currency). Code audit is unambiguous: **there is no GNU Taler anywhere in our repos** (all "taler" greps are false positives in minified artifacts). What we have is **crypto-rails funding** — Octant ERC-4626 vaults + Aave yield (`contracts/src/vendor/octant/*`, `modules/Octant.sol`), the **Cookie Jar** allowance primitive (`modules/CookieJar.sol`), YieldSplitter, Thirdweb card donations. That's a real on-chain funding story but **not Taler, not e-cash, not privacy-payments.** Drive has **no TALER draft** (zero "Taler" content matches).

**The only credible path** is scoping an actual **GNU Taler integration** — e.g. *"accept GNU Taler as a donation/payment rail for regenerative community treasuries"* or a Taler merchant integration for garden vaults. Legitimate and fundable, but **net-new work** we haven't started; a strong 2-page R&D proposal for it in <48h is a stretch.

**Recommendation:** **skip TALER on June 1; target Aug 1** with a real Taler-integration scope and an owner — *or* only submit now if someone commits to that integration. Do **not** relabel the vault/yield story as Taler.

---

## 6. Evidence library (reusable across proposals)

**Production metrics — Arbitrum, "Funding the Commons Story Pack" snapshot, queried 2026-04-15 (verified in Drive):**
- **16 live gardens · 53 gardeners · 27 operators · 20 evaluators**; domains: **education 15 · agroforestry 13 · waste 10 · solar 8**.
- ⚠️ **Refresh before submission:** these are ~6 weeks old. The Story Pack contains the exact live indexer query (`https://indexer.hyperindex.xyz/0bf0e0f/v1/graphql`, chainId 42161) — re-pull current numbers the morning of submission. *(I could not run the live POST query from here — sandbox blocks it — so the figures above are the last verified snapshot, not today's.)*

**Named deployments (citable):** TAS HUB Awka (Nigeria) · Muizenberg Community Garden (Cape Town, ZA) · AgroforestDAO (Minas Gerais, BR) · Growecosystems (Rio Claro, BR) · Greenpill Kenya. Pilot countries claimed: **Nigeria, Brazil, South Africa, Uganda, Spain, Italy** (Spain + Italy = European dimension).

**Integrations/partners (verified in code):** Hypercerts, Karma GAP, Hats Protocol, Gardens V2, Envio, Pimlico, Storacha/Filecoin, ENS, EAS, Privy, Thirdweb, Octant V2 vaults; ATProto/Silvi (planned).

**Grants actually delivered (cite as track record — NOT NLnet):** Grant Ships R1/R2; Gitcoin GG20–24; Octant Epoch 5 & 10 (Epoch 12 accepted); ReFi-in-Arbitrum; Arbitrum DAO "Building Regenerative Impact" (active). **Pending:** NLnet (April), OSV. **Not selected (don't cite as wins):** EF ESP, Octant Epoch 8, Celo Prezenti.

**Reusable narrative lines (verbatim):** *"If communities cannot make their work legible, they cannot make it fundable."* · *"Green Goods is a local-first impact reporting and regenerative compliance layer."* · third-party hook: *"over 90% of rainforest carbon credits were found to be unreliable or overestimated"* (Guardian/Die Zeit/SourceMaterial).

**Licenses (state explicitly):** green-goods MIT at repo root (⚠️ per-package `license` fields missing); **coop has NO license file — must add one**; VLET draft proposed AGPL-3.0 (app) + MIT (libraries). **Confirm canonical split with team.**

---

## 7. Technical-evidence appendix (claim → proof → strength)

**Green Goods (Commons proposal):**
| Claim | Proof (path) | Strength |
|---|---|---|
| Offline PWA / service worker | `client/vite.config.ts` (VitePWA+workbox, `sw-custom.js`) + sw test | strong |
| IndexedDB job/outbox queue | `shared/src/modules/job-queue/db.ts` (v5, `client_work_id_mappings`) | strong |
| Resumable drafts / sync-on-reconnect | `shared/src/hooks/*/use*Draft.ts`, `hooks/app/useOffline.ts`, `SyncStatusBar` | strong |
| Passkey + ERC-4337 (Pimlico) | `shared/src/config/{passkeyServer,pimlico}.ts`; `permissionless ^0.2.57` | strong |
| EAS attestation + **live schema UIDs** | `utils/eas/encoders.ts`; `contracts/deployments/42161-latest.json` | strong |
| Hypercerts mint + market | `workflows/mintHypercert.ts`, `@hypercerts-org/sdk`; `modules/Hypercerts.sol` | strong |
| i18n en/es/pt | `shared/src/i18n/{en,es,pt}.json` (~3,393 keys each) | strong |
| Envio indexer | `packages/indexer/config.yaml` (`envio 2.32.3`, 42161+11155111) | strong |

**Coop (Fediversity proposal):**
| Claim | Proof (path) | Strength |
|---|---|---|
| Yjs CRDT P2P | `shared/src/sync-config.ts`, `modules/coop/sync.ts`; `yjs`/`y-webrtc`/`y-websocket`/`y-indexeddb` | strong |
| Signaling + doc-sync server | `packages/api/src/ws/*` (Hono+Bun WS, `yjs-sync.ts`) | strong |
| Local-first explicit-publish | ADR-005 + `writeCoopState()` in `modules/coop/sync.ts` | strong |
| Encrypted-at-rest | ADR-007 + `modules/storage/db-encryption.ts` | strong |
| Passkey-first identity | ADR-003 + `modules/auth/`, `member-account.ts` | strong |
| Data-portability export | ADR-006 three-format artifact sync + export paths | strong |
| Safe/ERC-4337 anchoring | `modules/onchain/*`; **default `ONCHAIN_MODE=mock`** | partial (gated) |
| Storacha/Filecoin archival | `modules/archive/storacha.ts` (`@storacha/client`); **default `ARCHIVE_MODE=mock`** | partial (gated) |
| Anonymous publish (Semaphore) | `modules/privacy/*` (`@semaphore-protocol/core`); **default `PRIVACY_MODE=off`** | partial (gated) |

**TALER:** no GNU Taler code anywhere; nearest = Octant vaults / Aave / Cookie Jar / Thirdweb (green-goods) — **funding rails, not e-cash.** Any TALER work is net-new.

**Honest gaps (so proposals don't overclaim):** Coop onchain/archive/privacy/session are mock-default (not shipping live); Coop has no LICENSE; green-goods packages lack per-package license fields; stale `grant`-module script reference in `coop/package.json` (live module is `permit`); green-goods passkey writes blocked in local-fork mode; `network`/`TAS-Hub` are early (cite only as supporting ecosystem).

---

## 8. Action checklist before June 1 (noon CEST)
1. **Confirm the pending April NLnet app's status & call-date** (Afo/portal email) → decides if a June Commons proposal is safe vs double-dip.
2. **Decide GreenWill's home** (recommend Octant) → keep NLnet asks non-overlapping.
3. **Green-light the two strong proposals** — Fediversity (Coop) + Commons (VLET) — assign a human owner each.
4. **Decide TALER:** defer to Aug 1, or commit an owner to a real Taler-integration scope.
5. **Add a LICENSE to coop** (and per-package license fields to green-goods) — required for OSS grants.
6. **Lock €100/hr, ≤€50K budgets** + a **named contributor list with hours** per workstream.
7. **Reuse April's AI-disclosure** verbatim; **add a PGP key** (April form left it blank).
8. **Re-pull live indexer metrics** the morning of submission (query in Story Pack) so numbers are current.

## 9. Open questions for the team
- Any *real* prior NLnet grant? (Nothing in Drive supports it.)
- Is the pending app the Apr-1 or Jun-1 (13th) call? (Determines whether June Commons is a 2nd or 3rd concurrent item.)
- Owner + named contributors (with hours) per proposal?
- Final license: MIT-only vs AGPL+MIT split?
- Appetite for a genuine GNU Taler integration, or defer TALER to August?
