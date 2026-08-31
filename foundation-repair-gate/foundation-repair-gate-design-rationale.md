---
title: "Foundation Repair Gate — design rationale"
type: design-rationale
status: source-derived
slug: foundation-repair-gate
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: foundation-repair-gate-full-chat.md
execution_brief: idea-foundation-repair-gate.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Foundation Repair Gate

## 1. Core thesis
A factory whose measuring instruments can be redefined by the thing being measured
proves nothing. The campaign's central model: separate the measurer from the measured
at every layer — identity-verified factory checkout, byte-verified derived installs, a
pinned read-only verifier, external reviewed manifests — and make ignorance explicit:
UNKNOWN_UPSTREAM is a verdict, never a default pass (agent-authored architecture,
owner-commissioned ← msgs 226, 230; arc msgs 232–336).

## 2. Problem / current state / intended outcome
The specialkompetens design surfaced a real finding: vendored skills whose upstream
identity was unproven (← msgs 184–195). The owner refused to proceed to implementation
on an unaudited foundation: "Så nu är vi en riktig senior digital avdelning? det är
inget vi har missat? Analysera, granska, tänk kritiskt" (← msg 226), then commissioned
the executable closeout prompt (← msg 230). Intended outcome: a foundation where every
component's provenance is graded, measurement is pinned and read-only, and publication
of trust transitions is serialized and owner-present. The campaign ran R1–R6 with PR
#102–#115 merged; R7 was authorized but never executed (← msgs 232–336).

## 3. Reasoning chain
- The provenance finding generalized: if one vendored skill's upstream is unknown, the
  default mapping unknown→trusted is the actual defect. Hence the grading order BYTE
  MATCH > VERSION CLAIM > REPOSITORY SIMILARITY and "UNKNOWN_UPSTREAM must never
  silently equal TRUSTED" (agent arc ← msgs 236–238, 285–293).
- Provenance is only stable if the factory itself has identity: factory = an
  identity-verified git checkout; installed copies are derived artifacts, byte-verified
  against it; runtime state lives apart from professional knowledge (repo-native
  factory, S0; ← msgs 246–258).
- A verifier that can update what it verifies is an author, not a verifier: external
  reviewed integrity manifest + read-only verifier with no update flags + a pin on the
  verifier itself (← msgs 251–258).
- The measured must not define the measurer: a customer repo's node_modules could
  shadow the measuring engine — engine-substitution defense (← msgs 258–275).
- Failures during measurement are not evidence about the site: tri-state verdict
  algebra PASS/FAIL/ODÖMBART, "tool failure is never site pass" (← msgs 254–281,
  321–336).
- Host identity mattered when evidence conflicted across machines; OWNER DECISION: the
  Mac is canonical, the desktop at most forensic (← msg 259).
- Legacy fixtures embodied the old, distrusted measurement; OWNER DECISION: reject the
  evidence ("vi vill inte rädda den evidensen, den var dålig" ← msg 263), declare
  FIXTURE_REGIME_CHANGE rather than tune new fixtures toward old scores (← msgs
  242–243, 258–281).
- Authority questions during browser verification produced the five-layer authority
  stack; the agent refused a persistent wildcard harness permission in favor of
  interactive approval per run (← msg 326) and banned synthesizing INP_PASS from a TBT
  proxy — "truth repair is preferable to a fake green" (← msg 336). Both are ASSISTANT
  PROPOSALS pending owner ratification.
- Operationally, the owner bounded autonomy: session restart as sandbox rebuild
  (← msg 279) and auto mode only inside an R-box with owner-present publications
  (← msg 286).

## 4. Design decisions and why
D2 (Mac canonical host). Why: two hosts give two truths; forensics may read the old
    one, authority lives on one. Evidence: (← msg 259).
D3 (reject legacy evidence). Why: rescuing bad evidence launders it into the new
    regime. Evidence: owner's verbatim rejection; LEGACY_FIXTURE_RECOVERY=
    REJECTED_BY_OWNER recorded in the campaign. Source: (← msg 263; arc 264–281).
D5 (auto mode in R-box only). Why: speed where reversible, humans where trust changes
    hands. Evidence: "kan jag köra auto mode?" answered with the bounded-box shape.
    Source: (← msg 286; box definition in agent arc 282–290).
Five-layer authority stack (ASSISTANT PROPOSAL). Why: an external effect is legitimate
    only when owner policy, Nortropic capability, harness permission and OS capability
    all consent; bypassing the harness's own boundary invalidates the chain. Source:
    (← msgs 293–326).

## 5. Explicit rejections / anti-requirements
REJECTED: Tuning new fixtures to reproduce old scores.
WHY: it optimizes for continuity with distrusted numbers.
FAILURE IT WOULD CREATE: the new regime inherits the old regime's errors invisibly;
regressions hide behind matched baselines.
SOURCE: (← msg 263; msgs 242–243, 258–281).

REJECTED (ASSISTANT-RULED, ratification open): Persistent wildcard harness permission
for browser verification.
WHY: a standing wildcard is an unreviewed authority grant.
FAILURE IT WOULD CREATE: the harness boundary stops being an authority layer.
SOURCE: (← msg 326).

REJECTED (ASSISTANT-RULED, ratification open): Synthesizing INP_PASS from a TBT proxy.
WHY: a proxy verdict is a fabricated measurement.
FAILURE IT WOULD CREATE: fake green on the exact metric class the campaign exists to
make truthful. SOURCE: (← msg 336).

## 6. Explored but unresolved
- R7–R11 and the Foundation §A6 cut: authorized direction, unexecuted at thread end
  (← msgs 326–336).
- PR #105's twelve paper drafts (~40 open questions): explicitly non-authoritative;
  disposition open (← msgs 300–312 region).
- Which relayed agent-authored contracts (e.g. BROWSER_VERIFICATION_EXECUTION) the
  owner ratifies as standing (← msgs 285–336).
- PENDING OWNER REVIEW: the sequencing re-baseline (gate blocks S1–S5; 0A → S0 →
  R1–R11 → gate → S1..S54; DESIGN_FREEZE at plan approval, IMPLEMENTATION_VALIDATION
  at S54) appears only in agent-authored directives relayed by the owner (← msgs 238,
  246, 251–252); it is recorded here as unresolved, not as a decision.

## 7. Important trade-offs / tensions
- Repair depth vs momentum: the gate blocks product slices while it runs (← msgs
  232–252) against the owner's standing push for speed elsewhere in the thread.
- Truthfulness vs continuity: FIXTURE_REGIME_CHANGE accepts a visible discontinuity in
  scores to keep measurement honest (← msgs 242–243, 263).
- Autonomy vs presence: auto mode inside the R-box vs owner-present publications
  (← msg 286).

## 8. Metaphor / concept → technical principle
- "Fabrik med mätinstrument" → the measurer must be pinned, read-only and outside the
  measured artifact → do NOT copy: calibration bureaucracy; the principle is
  separation, not paperwork (← msgs 251–275).

## 9. External evidence mentioned in the conversation
All MENTIONED IN SOURCE, none independently verified: GitHub PRs #102–#115 (merged
during the campaign) and PR #105's paper drafts; axe (accessibility gate) and INP/TBT
web-performance metrics as the measurement surface (← msgs 232–336). Note: the ChatGPT
assistant claims to have executed GitHub actions itself (merges, review comments,
incl. a "human HÖGRISK" constitution commit reserved for the owner) — an anomaly for
owner review, recorded as claim, not fact (← msgs 258–335).

## 10. Evolution / pivots
- One provenance finding → whole-foundation audit campaign (← msgs 184–195 → 226–238).
- Implementation-next → foundation-first: the closeout prompt turned the freeze into
  R-rounds before any product slice (← msgs 230–238).
- Desktop+Mac ambiguity → Mac-canonical (← msg 259).
- Rescue-the-fixtures → reject-and-declare-regime-change (← msgs 242–243 → 263).

## 11. Retrieval map
| topic | message range |
|---|---|
| adversarial review commission; closeout prompt | 226–231 |
| campaign start; provenance doctrine | 232–241 |
| fixture ladder; FIXTURE_REGIME_CHANGE | 242–243, 258–281 |
| repo-native factory (S0); verifier pinning | 246–258 |
| Mac canonical host | 259 |
| legacy evidence rejected | 263 |
| session restart; auto mode / R-box | 279, 286 |
| authority stack; browser verification; wildcard refusal | 285–326 |
| verdict algebra; INP truth boundary; mid-R7 end | 321–336 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-foundation-repair-gate.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`foundation-repair-gate-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
