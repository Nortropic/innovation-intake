---
title: "Autonomy without self-certification — design rationale"
type: design-rationale
status: source-derived
slug: autonomi-utan-sjalvcertifiering
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: autonomi-utan-sjalvcertifiering-full-chat.md
execution_brief: idea-autonomi-utan-sjalvcertifiering.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Autonomy without self-certification

## 1. Core thesis
Autonomy and trust stop being opposites once the stop conditions are typed: an agent
should flow through every normal workflow transition on its own, and must halt without
exception at the small set of transitions where trust changes hands — above all, any
change to its own authority. The dual invariant: fix defects freely, never certify
yourself, never expand yourself (owner demand ← msg 89; taxonomy and invariant in the
R113–R122 arc ← msgs 91–117).

## 2. Problem / current state / intended outcome
The bootstrap stalled twice: first on Codex quota (← msgs 74, 78), then on ceremony —
the agent stopped and asked at transitions that needed no human ("why is it stopping?
i want it to work autonomous towards the end goal", ← msg 89). Meanwhile
cross-provider review of R115 found five causally-confirmed security defects that
same-provider review had missed (← msg 102). Intended outcome: an operating doctrine
where the machine moves continuously, humans appear only at typed hard stops, and the
review that certifies work is structurally independent of the work's author.

## 3. Reasoning chain
- Quota exhaustion forced a provider handoff (OWNER DECISION ← msg 78, anticipated
  ← msg 74); a handoff can only be sound if state lives outside the model — hence
  provider handoff via Git/effect evidence, never model memory (assistant doctrine
  ← msgs 79–82, 95, 117), and the owner added the end goal to the handoff prompt so
  direction survives the transfer (← msg 83).
- The owner's msg 89 demand split stops into classes: NORMAL_WORKFLOW_TRANSITION ≠
  HUMAN_STOP, plus an explicit hard-stop taxonomy and the maxim "autonomy does not
  mean self-certification" (assistant design ← msgs 91, 95).
- R115 needed a genuinely new capability (dirfd unlink), i.e. a trust-authority
  expansion; routing it review-first produced the owner-authority invariant: agents
  fix defects autonomously but never expand their own authority — expansions require
  owner review of the exact allowlist/inventory/design diff, frozen to the exact call
  form with negative controls (← msgs 96–98).
- Codex's cross-provider review then falsified R115's safety with five real
  filesystem-effect defects (← msg 102). Root cause: security had been resting on
  cleanup winning races. The correction: PREVENTION>RECOVERY provider confinement —
  deny the provider the ability to create the race at all; cleanup demoted to
  defense-in-depth (← msgs 102, 105; adopted via Codex's R116 ruling, owner relay
  ← msg 106).
- The same round hardened adjacent seams: PROVIDER_RETURNED ≠
  PROVIDER_ATTEMPT_FINISHED (quiesce the owned process family on all terminal paths),
  atomic CREATE_IF_ABSENT/NEVER_OVERWRITE publication, the candidate-materialization
  trust boundary (candidate = deterministic function of authoritative base + validated
  result + frozen contract; provider scratch never becomes authority), immutable
  failed candidates, and authority retirement — confinement made the dirfd authority
  unnecessary, so it is dropped, not kept (← msgs 102, 105–107).
- With Codex quota returning, the owner made provider assignment operational: reserve
  first (← msg 92), then switch back to maximize usage (← msg 108).
- Scaling: the owner probed parallel Codex instances (← msg 118); the settled shape is
  one canonical coordinator terminal that spawns agents itself (← msgs 121, 123 "Den
  kunde starta själv"), with safe vs speculative parallelism (N independent builders
  on one frozen task, adversarial comparison, pick not merge) and model/effort routing
  by epistemic risk (assistant design ← msgs 117–128; owner corrects the real effort
  tiers "high, extra high och ultra" ← msg 127, assistant self-corrects ← msg 128).

## 4. Design decisions and why
D1/D6 (provider fluidity under quota). Why: idle quota is wasted factory time; Git is
    the durable state carrier. Evidence: (← msgs 74, 78, 92, 108). PENDING OWNER
    REVIEW: contradicts the closeout brief's separation decisions; recorded as
    unratified.
D3 (autonomy redesign). Why: every needless stop costs a human round-trip and teaches
    the agent to over-ask. Evidence: (← msg 89; design msgs 91, 95).
D5 (review-first authority expansion). Why: an authority diff reviewed after mutation
    is a fait accompli. Evidence: the executed flow — scope menu, then full design
    with exact diffs, "Stopping here for your approval, as instructed" (← msgs 96, 98).
D7 (single coordinator). Why: one authoritative terminal keeps ordering and blame
    assignment simple; the coordinator can spawn what it needs. Evidence: (← msgs 118,
    121, 123).

## 5. Explicit rejections / anti-requirements
REJECTED: Cleanup-as-security-boundary.
WHY: the provider can outrace or redirect path-based cleanup (TOCTOU, cross-parent
moves, surviving descendants).
FAILURE IT WOULD CREATE: exploitable races exactly at the trust boundary; false
"no residue" reports (defects 1–4). SOURCE: (← msgs 102, 105; ruling relayed
← msg 106; R116 contract ← msg 107).

REJECTED: Patching a failed candidate in place.
WHY: a failed candidate is forensic evidence; mutation destroys it.
FAILURE IT WOULD CREATE: unreviewable history, ambiguous provenance for the fix.
SOURCE: owner relay "e167fc0 och R115 förblir immutable" (← msg 106; practice msgs 86,
89; design msgs 88, 95).

REJECTED: Agent Teams for parallelism.
WHY: the coordinator + fresh context-isolated reviewer subagents model preserves
review independence and one authoritative terminal.
FAILURE IT WOULD CREATE: shared context between builders and reviewers — precisely the
independence the doctrine exists to protect. SOURCE: (← msgs 91, 95, 117; owner
confirmation ← msg 121).

REJECTED: Retaining R115's dirfd-unlink authority after confinement.
WHY: unused frozen authority is standing attack surface.
FAILURE IT WOULD CREATE: authority accretion justified by history rather than need.
SOURCE: (← msg 105; relayed contract "ingen generell dirfd- eller TMPDIR-auktoritet"
← msg 106).

## 6. Explored but unresolved
- Ratification of the R116 contract: ChatGPT subordinated its own draft to Codex's and
  declared the latter "binding owner-contract" via relay — no direct owner
  ratification visible (← msgs 106–107). OPEN.
- Standing status of the bounded host-execution authorization pattern (unsandboxed
  no-live runs under explicit approval) (← msgs 78, 82, 85, 95). OPEN.
- Where the doctrines freeze: the checkpoint was unreached at thread end (R122, H032
  148/4, ← msg 115); the doctrine currently lives in round evidence, not a gate. OPEN.
- Provider-fluidity as policy vs incident response (← msgs 78, 108). PENDING OWNER
  REVIEW.

## 7. Important trade-offs / tensions
- Autonomy vs certification: continuous flow (← msg 89) vs independent review at every
  trust transition (← msgs 95, 102).
- Prevention vs capability: confining the provider removes legitimate-looking
  conveniences (general TMPDIR writes) to kill race classes (← msgs 102, 105–106).
- Quota economics vs process purity: switching providers mid-campaign preserved
  momentum at the cost of the planned separation (← msgs 78, 108).
- Same-provider speed vs cross-provider depth: context-isolated same-provider review
  is cheaper; only cross-provider review caught the R115 defects (← msgs 89, 102).

## 8. Metaphor / concept → technical principle
- "Självcertifiering" (self-certification) → author and certifier must be different
  identities with disjoint context → do NOT copy: bureaucratic sign-off chains; one
  independent reviewer suffices (← msgs 91, 95, 102).

## 9. External evidence mentioned in the conversation
MENTIONED IN SOURCE, none independently verified: Codex usage/quota reset mechanics
(← msgs 74, 78, 92, 108); macOS sandbox-exec/Seatbelt semantics and POSIX dirfd/
unlinkat behavior underpinning the confinement design (← msgs 96–107); Claude Code
effort tiers — assistant's initial claim corrected by the owner to "high, extra high
och ultra" (← msgs 126–128); model names/eval figures in the routing discussion rest
on unresolvable search chips (← msgs 119–128).

## 10. Evolution / pivots
- Codex-only bootstrap → provider handoff via Git evidence (← msgs 74–83).
- Stop-and-ask agent → typed hard-stop taxonomy (← msgs 89–95).
- Cleanup-as-security → PREVENTION>RECOVERY confinement after five falsifying defects
  (← msgs 98 → 102 → 105–107).
- Authority kept-because-frozen → authority retirement (← msgs 105–106).
- "Fler terminaler?" → one coordinator that spawns agents (← msgs 118–123).

## 11. Retrieval map
| topic | message range |
|---|---|
| quota exhaustion; handoff to Claude Code | 74–83 |
| R112 blocked; immutable-candidate practice | 86–89 |
| hard-stop taxonomy; no self-certification | 89–95 |
| R115 scope; review-first authority expansion | 96–98 |
| five defects; cross-provider falsification | 102 |
| confinement doctrine; retirement; no-overwrite | 105–107 |
| provider switch-back; reserve decision | 92, 108 |
| R122 status relay | 115 |
| parallelism; coordinator; effort routing | 117–128 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-autonomi-utan-sjalvcertifiering.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`autonomi-utan-sjalvcertifiering-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
