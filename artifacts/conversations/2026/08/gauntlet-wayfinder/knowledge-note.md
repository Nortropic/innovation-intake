# Nortropic Knowledge Note — Gauntlet, Wayfinding, Verification & Conversation Capture

**Date:** 2026-08-16  
**Status:** Knowledge / innovation context; not implementation authority.  
**Innovation Intake:** Issue #4, previously verified synced to `Nortropic Innovation` with `Status = INBOX`, `Area = VERIFICATION`.

## Executive summary

This conversation produced two connected outcomes.

First, a refined architecture for agentic quality and verification:

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

Second, a practical knowledge-capture workflow for valuable conversations: keep both a near-verbatim `full-chat.md` for provenance/context handoff and a distilled `knowledge-note.md` for fast agent orientation, and store both durably in Git under `Nortropic/innovation-intake/artifacts/conversations/**`.

The two ideas reinforce each other: explicit provenance and durable context reduce the risk that future agents silently reconstruct requirements, assumptions or reasoning from incomplete summaries.

## 1. Why a naive Gauntlet is insufficient

### Agent-controlled checking

If the main agent decides which critics exist, writes their prompts, chooses observations, interprets feedback and decides when to stop, the system under test also designs much of its own exam. This is structured self-critique, not independent verification.

At scale, failure causality becomes unclear: product failure, evaluator failure, orchestration failure, specification failure and prompt drift can become indistinguishable.

### Reference products hide specification work

A real comparison target can encode thousands of implicit decisions. Novel business logic usually has no finished target. If the agent invents requirements and then grades its implementation against those same invented requirements, more iterations can optimize the wrong objective more efficiently.

## 2. Wayfinding's role

Wayfinding is upstream of verification. It exposes and resolves important unknowns before they silently become implementation assumptions.

```text
KNOWN                 → authorized decision/fact
KNOWN UNKNOWN         → explicit question/ticket
NOT YET SPECIFIABLE   → fog
PROPOSED ASSUMPTION   → not authority
```

Core rule:

> **ASSUMPTION != REQUIREMENT**

A proposed assumption may become a requirement only through an authorized decision process: owner choice, domain evidence, research, prototype evidence, legal/technical constraints, etc.

## 3. Specification

Specification records what was actually decided and should distinguish:

- authorized requirements;
- assumptions;
- unresolved unknowns;
- invariants;
- exclusions / out-of-scope behavior;
- positive examples;
- negative examples / forbidden outcomes;
- edge-case semantics;
- provenance and authority for important decisions.

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

This keeps checks independent from the implementation they judge and makes later failures traceable.

## 5. Correct role of the Quality Gauntlet

Gauntlet is optimization, not authority.

> **Specification defines the search space. Verification defines its hard boundary. Gauntlet searches for better points inside it.**

A critic can help improve visual quality, usability, complexity, information design or other partially subjective dimensions among already-valid solutions.

If a critic discovers something outside the authorized requirements/quality model, classify it as a new requirement proposal/question and route it backward to wayfinding/specification instead of directly mutating implementation.

## 6. Critic / grader / authority separation

```text
CRITIC          → finding / hypothesis
GRADER          → measurement / score
TRUST AUTHORITY → permission for state transition
```

Prefer critic observations over prescriptions. A critic may correctly observe a symptom while diagnosing the root cause incorrectly.

Cross-provider diversity can reduce correlated blind spots, but model agreement is still not authority.

## 7. Three nested loops

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

Ralph primarily supplies persistence. Gauntlet supplies a quality gradient. Evaluators supply falsification. Deterministic graders supply reproducibility. Nortropic supplies authority.

## 8. Parallelism rule

> **Parallelize reading/search/falsification aggressively; parallelize writing only when independence is proven.**

Multiple read-only critics can inspect the same immutable candidate with different lenses. Parallel builders should require genuinely disjoint write surfaces and stable interfaces.

## 9. Requirements traceability

Desired long-term chain:

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

## 10. Safe self-improvement

When a real failure escapes existing verification:

```text
REAL FAILURE
→ immutable failure artifact / reproducer
→ verifier author
→ independent challenger
→ freeze stronger measurement
→ future regression protection
```

Nortropic should **self-propose stronger measurements**, not freely self-modify its own authority.

## 11. Conversation knowledge capture

The conversation then exposed a separate operational need: valuable ChatGPT/Claude/Codex conversations should be durable and reusable by future agents.

The agreed practical representation is:

```text
artifacts/conversations/<year>/<month>/<slug>/
├── full-chat.md
└── knowledge-note.md
```

### `full-chat.md`

Purpose: provenance and maximum context transfer.

It should preserve the user-visible conversation as completely and verbatim as possible:

- complete user messages;
- complete visible assistant responses where available from the active conversation context;
- chronological order;
- original nuance, objections, alternatives and evolution of the discussion.

It should exclude:

- system prompts;
- developer prompts;
- hidden chain-of-thought/private reasoning;
- tool calls and tool-internal protocol/output unless intentionally summarized as a user-visible result;
- credentials/secrets.

The file is a context handoff, not higher authority than Nortropic's actual code/contracts/evidence.

### `knowledge-note.md`

Purpose: fast agent orientation.

It should distill:

- executive summary;
- core insights;
- architecture principles;
- decisions and hypotheses;
- rejected/modified ideas;
- open questions;
- Nortropic implications;
- links/identities for related Innovation Intake items where applicable.

The knowledge note is derived from the source conversation and must not silently override it.

## 12. Claude Code context handoff

Recommended future prompt to a coding agent:

```text
Read this conversation archive first:
artifacts/conversations/<year>/<month>/<slug>/full-chat.md

Then read:
artifacts/conversations/<year>/<month>/<slug>/knowledge-note.md

Treat full-chat.md as the source conversation and knowledge-note.md as a
derived summary, not as higher authority than the source.

I want to continue the work from that conversation.
First summarize your understanding of:
1. the original problem,
2. conclusions reached,
3. unresolved questions,
4. implications for Nortropic.

Do not implement anything yet.
```

This gives Claude Code both compressed orientation and the longer provenance needed when nuance matters.

## 13. Current archive location

This conversation package is stored in:

```text
Nortropic/innovation-intake
artifacts/conversations/2026/08/gauntlet-wayfinder/
├── full-chat.md
└── knowledge-note.md
```

The archive currently lives in Innovation because that is the requested operational home for valuable conversation material at this stage.

## 14. Standard future command

The working standard is:

> **Arkivera den här chatten i Nortropic Innovation. Skapa `full-chat.md` som ett så komplett och ordagrant arkiv som möjligt av hela den användarsynliga konversationen — sammanfatta inte mina meddelanden eller dina synliga svar. Exkludera endast interna system/developer-prompter, hidden reasoning, tool-internals och secrets. Skapa dessutom `knowledge-note.md` som en detaljerad destillering för snabb agentorientering. Spara båda permanent i `Nortropic/innovation-intake` under `artifacts/conversations/<år>/<månad>/<slug>/` och verifiera dem genom att läsa tillbaka dem från GitHub. Om jag även ber att spara innovationen, skapa därefter Innovation Intake-issuet och verifiera INBOX.**

If the user does not explicitly ask to create/save an Innovation Intake item, archive only the Markdown files.

## 15. Canonical synthesis

> **Wayfinding discovers what must be decided.**  
> **Specification records what was decided.**  
> **Verification precommits how correctness will be judged.**  
> **Builders search for solutions.**  
> **Gauntlets optimize quality without redefining success.**  
> **Nortropic controls what becomes trusted reality.**

And for durable context:

> **Full chat preserves provenance; the knowledge note preserves orientation. Keep both.**
