---
title: "Nortropic Corpus Control Plane V0 — design rationale"
type: design-rationale
status: source-derived
slug: corpus-control-plane
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: corpus-control-plane-full-chat.md
execution_brief: idea-corpus-control-plane.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Nortropic Corpus Control Plane V0

## 1. Core thesis

The owner's problem — "can Nortropic intake all current chats so Claude Code can plan long-term with retained context, and can the watches get out of the brainstorm chats?" (← msg 1) — is not an archiving problem. It is a missing **middle layer between brainstorming and coding**: a place where ideas, decisions, watches, backlog and execution are held apart yet traceable to their origin (← msg 2). Four media are currently mixed in the same chats (brainstorming, research/radar, planning, execution), and the fix is separation with compilation: full chats preserved as evidence, intake as the operative memory, portfolio as choice, and a context pack as the per-task projection — "organisationens minne bor utanför modellen" (← msg 5 §1–5).

## 2. Problem / current state / intended outcome

Current state: great ideas sit months from implementation in the same thread as strategy; watch results interrupt discussions; Claude Code loses history between sessions; the backlog grows faster than the usage budget allows (← msgs 1, 5). Intended outcome: discovery may produce 100 ideas while delivery builds two, without loss and without the feeling of being behind — the usage limit treated as capacity, not failure; the goal is no longer "code as fast as we brainstorm" but "absorb innovation faster than we implement it, losing nothing, extremely selective about what consumes Claude/Codex capacity" (← msgs 5 §9, 5 final section).

## 3. Reasoning chain

Owner names two pains plus a Scrum-like structuring wish (← msg 1) → the assistant reframes: this is an architecture problem, an operating system for idea → plan → build, not another archive (← msg 2) → preserve-full-chat/distill-for-work is confirmed as the right base pattern by Anthropic/OpenAI guidance (map, not encyclopedia) (← msg 3) → Scrum is too blunt because three different speeds should not share a queue (← msg 4) → the full architecture lands: archive/knowledge/portfolio/plan/context-pack, Radar as sensor system with materiality classes, appetite from Shape Up, three clocks plus radar clock, four planning horizons, initiatives as small "worlds", decision records, context retrieval per initiative — and a re-sequencing: corpus intake + knowledge/portfolio baseline **before** the big Organization OS planning, so Claude plans from institutional memory plus repo reality instead of a pile of prompts (← msg 5) → owner adopts: "Låt oss bygga detta då, hur går vi tillväga" (← msg 6) → repo inventory shows roughly half the foundation already exists (intake episodes/hashes, knowledge non-authority guard, a manual 16-package R&D synthesis as proof of concept), so the build becomes a **layer on top**, not "Intake v2" (← msgs 7–8) → the four capabilities are named (Registry, Portfolio Projection, Radar Lane, Context Compiler) (← msg 9) → final shape "Nortropic Corpus Control Plane V0" in `nortropic-knowledge`, a seven-step build plan whose step 2 is the full Corpus Sweep, a 20–25KB pack spec, and a ten-point V0 finish line ending in `CHATGPT_REQUIRED_AFTER_HANDOFF=NO` (← msg 10).

## 4. Design decisions and why

D1 (OWNER DECISION). Intake the corpus; keep planning context across sessions.
    Why: session restarts destroy continuity; chats are the wrong long-term memory. Evidence: owner's opening problem statement. Source: (← msg 1).
D2 (OWNER DECISION). Watches leave the brainstorm chats.
    Why: "kladdar ner" — the human flow and the sensor flow are different flows. Source: (← msg 1; design msg 5 §6–7).
D3 (OWNER DECISION). Build the msg 5 architecture.
    Why: separation of concerns at organizational level; appetite instead of estimates; portfolio before build. Source: (← msg 6; msg 5).
D4 (ASSISTANT INFERENCE, post-adoption). Layer on top of frozen Intake v2.1, home in `nortropic-knowledge`, read-mostly, never execution authority.
    Why: v2.1 already carries RAW/WHAT/WHY, episodes, revisions, approved plans; knowledge repo already forbids becoming a second source of truth. Source: (← msgs 8, 10).
D5 (ASSISTANT INFERENCE, post-adoption). Deterministic files first; DBs only ever as cache.
    Why: markdown/JSON/git + deterministic indexes are agent-readable and verifiable; a vector DB as truth would fork authority. Source: (← msg 10).
D6 (ASSISTANT INFERENCE, post-adoption). Prove fresh-session continuity manually before `SessionStart` automation.
    Why: automation of an unproven loop hides its failures. Source: (← msg 10 step 6).

## 5. Explicit rejections / anti-requirements

REJECTED: A giant `CLAUDE.md` / all chats in permanent memory.
WHY: Anthropic and OpenAI guidance both say map-not-encyclopedia; big instructions eat context and reduce compliance.
FAILURE IT WOULD CREATE: 500k tokens of everything ever brainstormed, degrading every session. SOURCE: (← msg 6 adopting msgs 3, 5 §2).
REJECTED: Scrum wholesale.
WHY: three speeds, one queue is structurally wrong; appetite ("how much capacity does this deserve?") fits usage-limited delivery.
FAILURE: a new GitHub-repo interrupting Webbförvaltningen; every idea becoming the next Claude task. SOURCE: (← msg 6; msgs 4, 5 §10–11).
REJECTED (assistant-argued, post-adoption): "Intake v2" as a new system.
WHY: v2.1 is frozen and already half the foundation. FAILURE: parallel intake truth. SOURCE: (← msg 8).
REJECTED (assistant-argued, post-adoption): vector/graph databases as source of truth.
FAILURE: unverifiable retrieval becomes authority. SOURCE: (← msg 10).
REJECTED (assistant-argued, post-adoption): closing/merging the six overlapping watches now.
WHY: consolidate only once the Radar contract exists. FAILURE: sensor loss with nothing to receive the streams. SOURCE: (← msg 10 step 7).

## 6. Explored but unresolved

- Naming and home ("Corpus Control Plane V0" / `nortropic-knowledge`) — proposed only after the owner's last message; needs ratification (← msgs 7–10).
- Watch consolidation into sensor tracks (Frontier AI Engineering / Organization–Aquarium / Web–Design) and its timing (← msg 10 step 7).
- Relation to the Innovation Inbox funnel: msg 5 §8 explicitly keeps the existing status model and adds value/readiness axes — evolution or partial supersession is an owner call.
- SessionStart automation threshold: what counts as "proven" continuity (← msg 10 step 6).

## 7. Important trade-offs / tensions

- Context richness vs context pollution: the pack must be small (~20–25KB) yet sufficient; pointers over copies (← msg 10).
- Preservation vs operability: everything is kept, almost nothing is read — "alla chattar ska in, men Claude ska nästan aldrig läsa dem" (← msg 5 §1).
- Sensing vs focus: radar must run continuously without pulling delivery; clocks are decoupled by design (← msg 5 §11).
- Honesty vs harmonization: the compiler must emit `CONTEXT_CONFLICT` rather than reconcile old brainstorm with current repo (← msg 10 step 5).

## 8. Metaphor / concept → technical principle

- "Karta, inte encyklopedi" → entrypoints are routing tables into knowledge; content loads on demand. Do not copy literally: a map that itself grows unbounded recreates the encyclopedia (← msgs 3, 5 §2).
- "Tre klockor" → discovery/portfolio/delivery run at different rates and never auto-advance each other; not a scheduling implementation, a coupling prohibition (← msg 5 §11).

## 9. External evidence mentioned in the conversation

All MENTIONED IN SOURCE: Anthropic Claude Code guidance (fresh context window per session; concise `CLAUDE.md` ~<200 lines; auto-memory `MEMORY.md` index model; `SessionStart`/`SessionEnd` hooks; subagents with project-scoped memory) (← msgs 3, 5 §2, §5, §16, 10 step 6); OpenAI Codex guidance (`AGENTS.md` as map; repository knowledge as system of record) (← msgs 3, 5 §2); Shape Up appetite/betting and Scrum backlog transparency (← msgs 4, 5 §10); continuous-discovery practice (← msg 5 §9); Lovelace and Orbit as repo-based agent-ADR evidence (← msg 5 §14); filecite chips to intake/knowledge repo files, incl. `RELOAD_NOT_REMEMBER=YES` and `CHATGPT_REQUIRED_AFTER_HANDOFF=NO` in frozen v2.1 (← msgs 8, 10).

## 10. Evolution / pivots

- "How do we save chats?" → "middle layer between brainstorming and coding" (← msgs 1–2).
- "Structure like Scrum" → three decoupled queues + appetite (← msgs 1, 4–5).
- "Design Nortropic Corpus Intake v2" (msg 5's closing direction) → after repo inventory: build the layer on top of the already-frozen v2.1 instead (← msgs 7–8, 10). The earlier framing must not be revived.
- Sequencing: corpus intake + baseline is inserted **before** the big Organization OS planning, without changing the big-build order (Webbförvaltningen → bootstrap → Organization OS) (← msg 5 final section; msg 10).

## 11. Retrieval map

| topic | message range |
|---|---|
| Owner problem statement | 1 |
| Middle-layer reframing; full-chat-as-evidence | 2–3 |
| Scrum rejection, three speeds | 4 |
| Full architecture (five concepts, radar, clocks, horizons, ADRs, context retrieval, resequencing) | 5 |
| Owner adoption | 6 |
| Repo inventory → layer-on-top, four capabilities | 7–9 |
| Corpus Control Plane V0: build plan, sweep, pack spec, finish line | 10 |

## 12. What to load when

DEFAULT IMPLEMENTATION: read `idea-corpus-control-plane.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in `corpus-control-plane-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
