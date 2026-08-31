---
title: "Corpus freeze and synthesis method — design rationale"
type: design-rationale
status: source-derived
slug: korpusfrysning-och-syntesmetod
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: korpusfrysning-och-syntesmetod-full-chat.md
execution_brief: idea-korpusfrysning-och-syntesmetod.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Corpus freeze and synthesis method

## 1. Core thesis
A research corpus is only usable downstream if its identity is frozen and its claims
are graded. The method's two pillars: (1) durability — a campaign ends in exactly one
atomic commit, and that SHA, not any prose description, is the canonical input identity
for the next phase (← msgs 30, 40, 53); (2) epistemics — what a chat *contains* is not
what the owner *decided*, so every synthesized claim carries an evidence grade and an
authority attribution, verified both mechanically and semantically by independent
reviewers (← msgs 40, 43, 47).

## 2. Problem / current state / intended outcome
The improvements campaign produced 13+ intake packages and needed to become input for
cross-chat synthesis and later rebaseline (← msg 23). Risks observed live: briefs can
pass a rubric while still carrying vacuous motivations (← msgs 26–28); a synthesis can
mechanically cover everything yet be semantically wrong (the verifier itself had two
real bugs, ← msg 40); and assistant coinages masquerade as owner decisions — the
probes showed "nästan alla namngivna mekanismer är assistentmyntningar" while the
owner's real contributions are commissions, constraints, vetoes and
ratification-by-action (← msg 40). Intended outcome: a repeatable procedure where
freeze identity, grading and independent review are structural, not heroic.

## 3. Reasoning chain
- Closing the campaign without external eyes would be self-certification; the owner
  routed closeout through a fresh, no-context rubric reviewer first (OWNER DECISION
  ← msg 26; results ← msg 28).
- QA findings split by risk: surgical fixes (missing "— because", a dropped side
  track) are reversible and were fixed autonomously; length trimming can delete
  substance, so it was reserved for the owner — and not done ("Ingen nedkortning
  gjord, enligt beslut") (← msgs 28, 30).
- Supersede resolution + a read-only consistency audit + ONE atomic commit gave the
  corpus a single identity: 62e9fd4. The audit's first RED turned out to be bugs in
  the audit script itself — reinforcing that verifiers need verification (← msg 30).
- Phase 2 synthesis needed conventions: English (matching briefs and future agent
  readers) with verbatim Swedish owner quotes; rfcs/ because its contract is exactly
  "proposals before they become owner decisions", status proposed, authority none
  (routing menus ← msgs 34, 36; assistant recommendations ← msgs 35, 37; ratified by
  the delivered artifact ← msg 40).
- The synthesis probes falsified the owner's own layering hypothesis (Task Capsule ⊃
  Context Manifest): transcripts support synonyms; the chronology ("older term to
  retire") was inverted; the outer layer already had a corpus name (Canonical Work
  Order). Canonical naming was therefore left OWNER_CHOICE_REQUIRED instead of being
  silently resolved (← msgs 25, 33, 40, 43, 46).
- Grading vocabulary emerged to keep the synthesis honest: INDEPENDENT_CONVERGENCE /
  DEPENDENT_REFINEMENT / SHARED_PRIOR_CONTEXT / UNKNOWN, with guard rails
  (COHERENCE_IS_NOT_EVIDENCE, ELEGANCE_IS_NOT_AUTHORITY, REPETITION_IS_NOT_TRUTH,
  RECENCY_IS_NOT_SUPERSESSION, ASSISTANT_SPECIFICITY_IS_NOT_OWNER_INTENT) and an
  AUTHORITY column downgrading several brief-"decisions" to what transcripts actually
  support (assistant design ← msg 43; verified in artifact ← msgs 40, 47).
- Verification became two-tier by demonstration: Pass E (mechanical: 16/16 briefs,
  106/106 D/P/R/U entries, 42 citations, role attribution) plus an independent
  semantic reviewer, whose findings drove bounded remediation (4/4 fixed) before the
  freeze at 5c8a811 (← msgs 40, 47, 53).
- Pointer discipline closed the loop: when a memory note could not be written, the
  ruling was that the committed artifact's git identity IS the pointer — no shadow
  pointers (← msgs 40, 41).

## 4. Design decisions and why
D1 (independent rubric gate). Why: the author of a corpus cannot grade it. Evidence:
    (← msgs 26, 28).
D3 (ONE atomic commit + frozen SHA). Why: multiple commits give a corpus multiple
    identities; downstream phases need exactly one. Evidence: 62e9fd4 as sole
    canonical_sources of the RFC (← msgs 30, 40).
D4 (English + rfcs/ + status proposed). Why: language follows the readers; location
    follows the authority contract — proposals are not decisions. Evidence: (← msgs
    34–37, 40).
D5 (freeze only after two-tier verification). Why: mechanical coverage proves
    completeness, not truth; the semantic reviewer found what Pass E could not.
    Evidence: (← msgs 40, 47, 53).

## 5. Explicit rejections / anti-requirements
REJECTED: Task Capsule ⊃ Context Manifest unification (layered-hierarchy hypothesis).
WHY: falsified by the corpus — synonyms, inverted chronology, an existing outer-layer
name.
FAILURE IT WOULD CREATE: a canonical vocabulary built on a false history; later agents
"retiring" the newest term. Naming stays OWNER_CHOICE_REQUIRED.
SOURCE: (← msgs 25, 33, 40, 43, 46).

REJECTED: Memory pointers on synthesis artifacts.
WHY: git identity is durable and verifiable; memory notes drift and duplicate truth.
FAILURE IT WOULD CREATE: two pointers that can disagree, with the unverifiable one
winning by convenience. SOURCE: (← msgs 40–41).

## 6. Explored but unresolved
- Live-chat re-harvest cadence: policy shape adopted (immutable snapshots, new intake
  on material novelty, daily reports → Observatory), exact cadence undecided
  (← msgs 25, 30; msg 23's pending list).
- ContextPack / Context Manifest / Task Capsule canonical name: explicitly
  OWNER_CHOICE_REQUIRED (← msgs 40, 43, 46).
- Whether this method becomes the canonical procedure in the nortropic-intake skill /
  openai-anthropic-workflow package (this package's own Q2 — not decided in source).
- The msg-40 note that Phase 3's eight questions are reserved and rebaseline awaits
  the bootstrap checkpoint (← msg 40).

## 7. Important trade-offs / tensions
- Autonomy vs substance: surgical fixes autonomous, length trimming owner-reserved —
  precision beats tidiness (← msgs 28, 30).
- Coverage vs correctness: Pass E completeness vs semantic truth; both required, since
  each catches what the other cannot (← msgs 40, 47).
- Owner hypothesis vs corpus evidence: the method let the corpus falsify the owner's
  own layering theory rather than confirming it (← msgs 25, 40).
- Immutability vs freshness: frozen snapshots vs living watch-chats — resolved by
  routing novelty into new intakes, not edits (← msgs 25, 30).

## 8. Metaphor / concept → technical principle
Not applicable — the source range argues in direct procedural terms; no load-bearing
metaphors to translate.

## 9. External evidence mentioned in the conversation
MENTIONED IN SOURCE, none independently verified: the frozen corpus commit
Nortropic/innovation-intake@62e9fd44b6ea… and RFC commit 5c8a81181774… in
Nortropic/nortropic-knowledge (← msgs 30, 40, 53); GOVERNANCE.md's nine frontmatter
keys for nortropic-knowledge artifacts (← msgs 40, 53); the intake skill's
brief-rubric at `~/.claude/skills/nortropic-intake/evals/brief-rubric.md` (← msg 26).

## 10. Evolution / pivots
- "Klar kampanj" → gated closeout via independent rubric QA (← msgs 23 → 26–30).
- Owner layering hypothesis → falsified → OWNER_CHOICE_REQUIRED naming (← msgs 25 →
  40, 43, 46).
- Single verification pass → two-tier (mechanical + independent semantic) after both
  tiers caught real, disjoint errors (← msgs 40 → 47 → 53).
- Memory notes → git-identity pointer discipline (← msgs 40–41).

## 11. Retrieval map
| topic | message range |
|---|---|
| campaign report; three pending owner decisions | 23 |
| supersede + re-harvest policy proposal | 25 |
| independent rubric-QA gate | 26–28 |
| closeout: audit, ONE commit, freeze 62e9fd4 | 30 |
| language/location routing | 34–37 |
| Phase 2 report; falsified hypothesis; authority pattern | 40 |
| pointer discipline (git identity) | 40–41 |
| grading vocabulary; AUTHORITY column | 43, 46 |
| Pass E + semantic remediation | 47 |
| Phase 2 freeze 5c8a811 | 53 |

## 12. What to load when
DEFAULT IMPLEMENTATION: read `idea-korpusfrysning-och-syntesmetod.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in
`korpusfrysning-och-syntesmetod-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
