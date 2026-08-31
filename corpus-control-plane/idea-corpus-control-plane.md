---
title: "Nortropic Corpus Control Plane V0 — corpus, portfolio and radar layer on top of frozen Intake, with Context Compiler"
type: idea-brief
status: idea
slug: corpus-control-plane
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: corpus-control-plane-full-chat.md
design_rationale: corpus-control-plane-design-rationale.md
intended_repo_path: corpus-control-plane/idea-corpus-control-plane.md
context_revision: 1
related: [project-corpus-intake, nortropic-recompile]
---

# Idea brief: Nortropic Corpus Control Plane V0

## 1. Summary

Build a corpus/portfolio/radar layer **on top of** the frozen Nortropic Intake v2.1 — never a rebuild of it — so that all current brainstorm chats are intaken into one deduplicated corpus, watches move out of brainstorm chats into a separate Radar lane, portfolio choice is separated from intake status, and a deterministic Context Compiler produces small context packs that give a fresh Claude Code session the right Nortropic without ChatGPT history. The key framing decision: discovery outrunning delivery is NORMAL, not debt — the system must sort, park and choose instead of trying to "code fast enough".

## 2. Context you need

Intake v2.1 is frozen (source episodes, context revisions, owner deltas, approved plans, `RELOAD_NOT_REMEMBER`). What is missing is the layer above it: a machine-readable catalog of all ideas and relations, an explicit portfolio answer to "what should we actually do with the ideas?", a home for watches/findings outside brainstorm chats, and a reproducible way to compile per-initiative context for fresh sessions. Four proposed capabilities: (1) Corpus Registry, (2) Portfolio Projection (`DISCOVERY/SHAPING/CANDIDATE/READY/ACTIVE/PARKED/DONE` with `strategic_value`/`readiness`/`appetite`), (3) Radar Lane (`WATCH → FINDING → DELTA`, only material deltas reach intake), (4) Context Compiler (~20–25KB packs, `CONTEXT_PACK_IS_AUTHORITY=NO`). Proposed home: `nortropic-knowledge` as a read-mostly derived layer, never execution authority.

This brief is the primary intake artifact for execution. Deeper design logic lives in the linked design rationale; the full chat is raw evidence — read targeted message ranges only if the rationale is insufficient. Current canonical repository authority beats all intake artifacts; within the intake package this brief wins over rationale and transcript. Once an owner-approved plan is bound (see the frontmatter), it carries execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Every relevant current chat accounted for in a corpus sweep with per-chat outcomes; same idea from five brainstorms = one idea with several source episodes.
- Archive / Knowledge / Portfolio / Plan / Context Pack held apart as five distinct concepts; Claude gets "the relevant projection of Nortropic", never all of Nortropic.
- Radar as a sensor system: watches produce findings, findings are compared against current state, only material deltas enter Innovation Intake.
- Three clocks (discovery/portfolio/delivery) plus a radar clock that never pull each other automatically; `DISCOVERY RATE > DELIVERY RATE = NORMAL`.
- Proven fresh-session continuity before any automation of it; target-repo authority always above knowledge/context.
- Verkstadsgolvet can later project this same data — no separate Scrum system with its own truth.

Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

D1. Intake the current chat corpus and use it for long-term Claude Code planning with context retained across new sessions — because context today lives scattered in chats and dies at session start (← msg 1).
D2. Watches/bevakningar shall be separated out of brainstorm chats into a structured lane the owner can actually follow — because inline watch results wreck the chats' information architecture (← msg 1).
D3. Build it — "Låt oss bygga detta då, hur går vi tillväga" adopts the msg 5 architecture: archive/knowledge/portfolio/plan/context-pack separation, Nortropic Radar with materiality classes, Shape-Up appetite over wholesale Scrum, and corpus intake + knowledge/portfolio baseline established **before** the big Organization OS planning (← msg 6; architecture msg 5).

R1. A giant `CLAUDE.md` / dumping all chats into permanent memory — because instructions should be a map, not an encyclopedia; oversized context degrades compliance (← msg 6 adopting msgs 3, 5 §2).
R2. Scrum wholesale — because Nortropic's three speeds (innovation, environmental sensing, limited build capacity) must not share one queue; borrow Shape Up's appetite/betting instead (← msg 6; msgs 4, 5 §10–11).

Note: further refinements arrived only in msgs 7–10, after the owner's last message — build-on-frozen-v2.1 rather than an "Intake v2" rebuild, markdown/JSON/git over vector/graph DBs, deferred watch consolidation, the name "Corpus Control Plane V0" and the `nortropic-knowledge` home. They are assistant proposals consistent with D3 but without itemized owner sign-off — see Q1/Q2 and the rationale §6.

## 5. Acceptance criteria (v1)

AC1. WHEN the corpus sweep runs over the selected chats, THE system SHALL account for 100% of them, each with an explicit outcome (`NEW_IDEA/CONTINUE_EXISTING/DUPLICATE/NON_MATERIAL/OUT_OF_SCOPE`) and no silent gaps (← msg 6; msg 10 step 2).
AC2. WHEN a completely fresh Claude Code session receives only the small entrypoint plus a compiled context pack, THE session SHALL correctly answer what is being built, why, what is decided, what is rejected, dependencies, current repo identity and next step — with no ChatGPT history needed after handoff (← msg 1; msg 10 steps 6, mållinje 9–10).
AC3. WHEN the Context Compiler runs twice on identical inputs, THE compiler SHALL produce the same pack, carrying exact SHA/path pointers and `CONTEXT_PACK_IS_AUTHORITY=NO`, and SHALL surface disagreements between old brainstorm and current repo as `CONTEXT_CONFLICT` instead of silently harmonizing (← msg 6; msg 10 step 5 and pack spec).
AC4. WHEN a watch produces a result, THE Radar lane SHALL record it as `WATCH → FINDING → DELTA` artifacts outside any brainstorm chat, and only material deltas SHALL proceed to Innovation Intake (← msg 1; msgs 5 §6–7, 10 step 7).
AC5. WHEN portfolio state is displayed, THE Portfolio Projection SHALL show `NOW / READY / SHAPING / DISCOVERY / PARKED` as an axis separate from intake status, with appetite/readiness/value fields and no single composite score (← msg 6; msg 10 step 3).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only — never copied here.
Suggestions: file contracts, validators and deterministic compilers before any UI/database/embeddings; treat source repos (`nortropic-intake`, `innovation-intake`, `nortropic-system`, Webbförvaltningen, `verkstadsgolvet`) as read-only inputs; keep `SessionStart` automation until after continuity is proven manually; any future SQLite/vector/graph index is a cache, never a source of truth; do not disturb the ongoing Webbförvaltningen.

## 7. Out of scope (v1)

- Rebuilding or modifying frozen Intake v2.1 ("Intake v2" as a new system is rejected in-source, msg 8 — assistant-argued).
- Closing/merging the six overlapping watches before a Radar contract exists (msg 10 step 7 — assistant-argued).
- A large UI or separate Scrum app; Verkstadsgolvet's projection comes later.
- Vector/graph databases as source of truth.
- The big Organization OS planning itself — this layer is sequenced before it.

## 8. Verification (how we know it works)

Run the msg 10 mållinje as a demonstration: full accounted corpus coverage, coherent duplicate/supersession/relation structure, a portfolio rendering, radar as separate stream, a reproducible context pack with verifiable pointer identities, and a fresh Claude Code session that resumes one initiative correctly without ChatGPT history — all captured as evidence an independent reviewer can confirm from the record alone.

## 9. Open questions (interview the owner before planning)

Q1. Exact home and naming: "Corpus Control Plane V0" in `nortropic-knowledge` was proposed after the owner's adoption (msgs 7–10) — does the owner ratify the name and home?
Q2. Which watches consolidate into which sensor tracks (Frontier AI Engineering / Organization–Aquarium / Web–Design were proposed), and when?
Q3. Does the Portfolio Projection extend or partially supersede the `innovation-inbox-idehantering` funnel? Pending owner review — deliberately **not** linked as related here.
Q4. When does the Context Compiler go behind `SessionStart` hooks (only after proven fresh-session continuity — what proof suffices)?

## 10. Process for this brief

1. Clarify: first send a subagent to read `corpus-control-plane-design-rationale.md` (its rejection and unresolved sections cover most §9 rationale) and report back what bears on §9; only if the rationale lacks the needed evidence, exact source wording matters, or a conflict/ambiguity remains, have it read the targeted message ranges in the source conversation via the rationale's retrieval map — never the whole transcript, and keep both out of main context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. On explicit owner approval, persist the exact approved plan as `corpus-control-plane-approved-plan.md`, validate it (`scripts/plan_contract.py validate`), bind it into this frontmatter and only then set `status: planned`.
4. Implement in a fresh session started from the approved plan: `plan_contract.py resume --slug corpus-control-plane --target-repo <repo>`; reconcile against current repository truth; after any compaction re-read the plan from disk; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the approved plan.
6. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `corpus-control-plane-full-chat.md` (same folder; 10 messages)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
