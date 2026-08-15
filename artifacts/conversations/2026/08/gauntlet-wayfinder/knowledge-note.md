# Nortropic Knowledge Note — Wayfinding, Verification & Quality Gauntlet

**Date:** 2026-08-16  
**Status:** Knowledge / innovation context; not implementation authority.  
**Innovation Intake:** Issue #4, verified synced to `Nortropic Innovation` with `Status = INBOX`, `Area = VERIFICATION`.

## Executive summary

A pure Gauntlet Loop is useful for quality optimization but is unsafe as the mechanism that defines correctness. Two failure modes dominate: the lead agent can dynamically invent its own critics/checks, and novel products often lack an external reference product, forcing the evaluator to invent its own definition of “good”. The resulting system can optimize confidently against a standard it created itself.

Nortropic should separate the lifecycle into:

```text
WAYFINDING
→ SPECIFICATION
→ VERIFICATION DESIGN
→ CONTRACT FREEZE
→ BUILD
→ VERIFICATION
→ QUALITY GAUNTLET
→ EMPIRICAL REALITY
→ TRUSTED PROMOTION
```

The Quality Gauntlet may improve a valid solution, but it must not redefine requirements or become trust authority.

## 1. Why a naive Gauntlet is insufficient

### Agent-controlled checking

If the main agent decides which critics exist, writes their prompts, chooses observations, interprets feedback and decides when to stop, the system under test also designs much of its own exam. This is structured self-critique, not independent verification.

### Reference products hide specification work

A real comparison target embeds thousands of implicit decisions. Novel business logic normally has no finished target. If the agent invents requirements and then grades its implementation against them, extra iterations merely optimize the wrong objective.

## 2. Wayfinding

Wayfinding is upstream of verification. It exposes and resolves important unknowns before they silently become implementation assumptions.

```text
KNOWN                 → authorized decision/fact
KNOWN UNKNOWN         → explicit question/ticket
NOT YET SPECIFIABLE   → fog
PROPOSED ASSUMPTION   → not authority
```

> **ASSUMPTION != REQUIREMENT**

A proposed assumption may become a requirement only through an authorized decision process: owner choice, domain evidence, research, prototype evidence, legal/technical constraint, etc.

## 3. Specification

Specification records what was actually decided:

- authorized requirements;
- invariants;
- exclusions / out-of-scope behavior;
- positive and negative examples;
- forbidden outcomes;
- edge-case semantics;
- provenance/authority;
- unresolved unknowns that still block implementation.

Specification defines the allowed search space for builders.

## 4. Verification design before build

Verification should be claim-first and precommitted:

```text
CLAIM
→ how could this claim be false?
→ observable falsification paths
→ deterministic/measurable checks
→ positive anchors + negative controls
→ freeze
→ builder begins
```

## 5. Quality Gauntlet

The Gauntlet's role is optimization, not authority.

> **Specification defines the search space. Verification defines its hard boundary. Gauntlet searches for better points inside it.**

If a critic finds something outside the authorized quality model, classify it as a new requirement/question and route it backward to wayfinding/specification.

## 6. Critic / grader / authority separation

```text
CRITIC          → finding / hypothesis
GRADER          → measurement / score
TRUST AUTHORITY → permission for state transition
```

Prefer critic observations over prescriptions. A critic may correctly observe a symptom while diagnosing the root cause incorrectly.

Cross-provider diversity can reduce correlated blind spots, but model agreement is still not authority.

## 7. Parallelism

> **Parallelize reading/search/falsification aggressively; parallelize writing only when independence is proven.**

Multiple read-only critics can inspect the same immutable candidate with different lenses. Parallel builders should require genuinely disjoint write surfaces and stable interfaces.

## 8. Requirements traceability

Desired chain:

```text
OWNER INTENT
→ DECISION
→ REQUIREMENT
→ CHECK / TEST
→ FROZEN CRITERION
→ CANDIDATE SHA
→ EVIDENCE
→ ATTESTATION / PROMOTION
```

A failure should be traceable backward through this chain.

## 9. Safe self-improvement

```text
REAL FAILURE
→ immutable failure artifact / reproducer
→ verifier author
→ independent challenger
→ freeze stronger measurement
→ future regression protection
```

Nortropic should **self-propose stronger measurements**, not freely self-modify its own authority.

## 10. Three nested loops

```text
OUTER — NORTROPIC TRUST LOOP
frozen contract → candidate identity → deterministic gates
→ independent falsification → attestation → promotion

MIDDLE — QUALITY GAUNTLET
actual artifact → critic/evaluator → evidence finding
→ remediation → improved candidate

INNER — PROVIDER / RALPH-LIKE LOOP
reason → tool → observe → edit → test → repeat
```

## 11. Implications for the Nortropic roadmap

This idea strengthens the conceptual role of the later intake/specification/verifier/evaluator capabilities:

- intake should distinguish requirements, assumptions, unknowns, references and constraints rather than merely turn prose into tasks;
- verifier authoring should derive checks from authorized claims before implementation;
- evaluator capability should remain advisory/falsificatory and must not become root of trust;
- discovered requirements should route backward to shaping/wayfinding instead of directly mutating implementation;
- Verkstadsgolvet can later expose this traceability and show why each check exists.

## 12. Canonical synthesis

> **Wayfinding discovers what must be decided.**  
> **Specification records what was decided.**  
> **Verification precommits how correctness will be judged.**  
> **Builders search for solutions.**  
> **Gauntlets optimize quality without redefining success.**  
> **Nortropic controls what becomes trusted reality.**

## 13. Innovation Intake record

Saved as:

- **Title:** Wayfinding → Specification → Verification → Quality Gauntlet
- **Area:** VERIFICATION
- **Issue:** #4 in `Nortropic/innovation-intake`
- **Project sync:** GitHub Actions `Innovation Intake` completed successfully
- **Verified Project state:** `Status = INBOX`, `Area = VERIFICATION`

This note is explanatory knowledge. The Innovation Intake item is a discovery record, not executable Factory authority.
