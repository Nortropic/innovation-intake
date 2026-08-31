---
title: "Nortropic Owner Plane — design rationale"
type: design-rationale
status: source-derived
slug: nortropic-owner-plane
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-owner-plane-full-chat.md
execution_brief: idea-nortropic-owner-plane.md
authority: non-authoritative-rationale
fidelity: full
context_revision: 1
---

# Design rationale: Nortropic Owner Plane

## 1. Core thesis

The Owner Plane is the missing third layer of Nortropic. The bootstrap answers "how does Nortropic execute work safely?"; Organization OS answers "how does Nortropic represent itself as an organization?"; the Owner Plane answers "how does the owner express will to the organization — and receive back only real owner decisions — without becoming scheduler, prompt author and context shuttle?" (← msg 182). Its constitutional law is the bootstrap trust principle lifted to the organizational level: OWNER SPEECH ≠ MODEL INTERPRETATION ≠ ORGANIZATION STATE — the model proposes, a trusted layer decides (← msg 182 §5; msg 185 fas 2).

## 2. Problem / current state / intended outcome

The brainstorm began with the owner asking, in beginner terms, what the bootstrap actually is and how he will communicate with the system in the future (← msgs 172, 174). The assistant's diagnosis: today the owner is the orchestrator — project lead, prompt author, context shuttle, session starter, checkpoint handler (← msg 173). Intended outcome: the owner communicates in intent / priority / constraint / decision; the organization translates, works, and interrupts only at genuine authority boundaries; the morning experience is "Needs You: 0" (← msgs 175, 182 §23). SOURCE-DERIVED FACT: msgs 1–171 of this chat are bootstrap execution (H-032 refreeze, runner ceremonies), not part of this idea.

## 3. Reasoning chain

Owner asks how he will talk to the system (← msg 174) → three communication levels emerge: goal/direction, initiative, direct task (← msg 175) → owner sharpens the real constraint: "det är session usages och inte api usage" (← msg 176) → therefore the Owner Interface must be a control plane over authenticated session tools, not an API consumer; a Provider Capacity Manager is hypothesized (← msgs 177–178) → owner orders a deep brainstorm anchored in the frozen roadmap (← msg 179) → new external evidence (Codex App Server protocol with subscription auth, threads/resume, approvals, `account/rateLimits/read`/`account/usage/read`) makes a session-based Owner Plane a supported pattern rather than a workaround (← msgs 181, 182 §2) → the deep brainstorm concludes the Owner Plane is a protocol, not a dashboard: append-only Owner Gateway → Intent Interpreter (proposal only) → Authority Router → Organization OS, with a durable Attention Service on the return path (← msg 182 §19) → this forces a roadmap change: the Owner Plane contract must be frozen together with the Organization Architecture, and a thin Console V0 built right after Organization OS V0 Core, before the full Digital Twin — otherwise the organization's most important control system gets built in React components (← msg 182 §3–4, msg 185) → owner adopts ("Detta låter bra, låt oss planera för detta") (← msg 183) → owner asks for the concrete procedure (← msg 186) → 18-step controlled sequence with per-phase exit criteria, nothing built before `BOOTSTRAP_CHECKPOINT=PASS` (← msg 187).

## 4. Design decisions and why

D1. Session/plan usage, never API billing as base assumption.
    Why: the owner pays for ChatGPT/Claude plans; the Owner Plane must not silently convert governance into per-token spend. Rendering, reading status and responding to attention must cost zero model calls (← msg 182 §27).
    Evidence: owner's explicit framing (← msg 176); OpenAI's documented subscription-vs-API split and App Server usage endpoints (← msgs 178, 181–182).
D2. Protocol first, console second, rich UX last.
    Why: freezing OwnerUtterance/OwnerIntent/AttentionRequest/Delegation semantics makes the UI "nearly trivial"; the reverse order cements the wrong model (← msg 182 §29, §4).
D3. Owner Console V0 is deliberately tiny (ASK NORTROPIC / NEEDS YOU / NOW / PRIORITIES / CAPACITY) and local-first.
    Why: measure real owner behavior before building UI around assumptions; localhost keeps credentials with the authenticated CLIs and minimizes attack surface (← msgs 178, 182 §20–21, 185 fas 5).
D4. Attention is durable state with a budget.
    Why: "an owner stop must be state, not a message in a terminal" — it survives session death, restart, provider switch; interrupt classes range from INFO to immediate attention, minimizing interrupts without hiding real decisions (← msg 182 §8–10; msg 187 step 15).
D5. Conflicting owner decisions are superseding events, never edits.
    Why: Friday's intent supersedes Monday's as a new event, so "why did this change?" is answerable forever (← msg 182 §31).
D6. Explain and Preview join the Architecture Freeze.
    Why: after weeks of autonomy the owner will not remember why state is as it is; "Why?" must be answered by provenance, not model guesses, and large intents should preview their impact before applying (← msg 182 §25; msg 185).

## 5. Explicit rejections / anti-requirements

REJECTED: Chat directly to Supervisor as the authority path.
WHY: fast but structurally rotten. FAILURE IT WOULD CREATE: chat becomes authority with no provenance; back to "Johnny → chatbox → LLM → shell". SOURCE: (← msg 183; msg 182 §1, §28).
REJECTED: Codex App Server as replacement for H036.
WHY: it is a provider observation/session protocol, not Nortropic trust. FAILURE: execution boundary migrates into a vendor protocol; trusted code stops flowing through Supervisor → H036 → H032 → H031. SOURCE: (← msg 183; msg 182 §14).
REJECTED: Copying Munder Difflin's "GOD orchestrator" (and Agent Cockpit wholesale).
WHY: Nortropic already has a deeper trust stack (H036/H032/H031, gates, immutable candidates, evidence). FAILURE: a multi-agent program where one agent is the truth. Steal UX patterns only. SOURCE: (← msg 183; msg 182 §17–18).
REJECTED: Scraping ChatGPT/Claude web UIs for usage numbers.
WHY: fragile and unnecessary; clients expose real signals or they don't. FAILURE: scheduler decisions built on guessed capacity; `UNKNOWN` is the honest state. SOURCE: (← msg 183; msgs 178, 182 §12).
REJECTED: Building the Owner UI now, before `BOOTSTRAP_CHECKPOINT`.
WHY: the finished bootstrap's actual reality must inform the architecture ("we should not lock the next control plane hours before the first autonomous task runs"). FAILURE: architecture frozen against an imagined bootstrap. SOURCE: (← msg 186; msgs 185 fas 0, 187 step 1).
REJECTED (design guard, assistant-argued within the adopted architecture): provider permission prompts treated as owner decisions. FAILURE: today's permission spam rebuilt in a nicer dashboard. SOURCE: (← msg 183; msg 182 §37).

## 6. Explored but unresolved

- H036 later driving Codex App Server as the executed provider: "undersökas, inte antas" — a kernel-evolution question with a sketched adapter, explicitly not a V0 requirement (← msg 182 §15).
- Claude-side capacity signals: which stable CLI/session signals exist is an inventory task, not settled knowledge (← msg 182 §12, §16).
- The final typed-intent taxonomy and which write classes graduate beyond the reversible V0 set (← msg 182 §36; msg 187 step 13).
- Whether Owner Plane becomes its own intake lineage or an episode of `nortropic-organization-os` — the sequence requires coupling but defers identity to intake (← msg 187 step 3).

## 7. Important trade-offs / tensions

- Autonomy vs owner control: minimize interrupts without hiding real authority boundaries — resolved by attention classes and "ask only when ambiguity is materially consequential" (← msg 182 §9, §30).
- Rich observability vs micromanagement: a Digital Twin full of agent avatars invites "why is Codex 7 idle?"; work/outcomes must be the protagonist (← msg 182 §32).
- Provider convenience vs trust boundary: App Server offers steering/approvals that must remain observability, not authority (← msg 182 §14, §37).
- Speed vs sequencing: the Console is wanted now, but building before the bootstrap closeout would encode stale assumptions (← msgs 185, 187).

## 8. Metaphor / concept → technical principle

- "Kommunen"/kommunstyrelse → the owner speaks in goals; an organizational hierarchy translates to execution. DO NOT copy literally: no bureaucratic approval chain per delivery — reversible work flows without owner stops (← msgs 175, 182 §9).
- "Stadshuset" → the Owner Console surface only; it must not own state (← msg 182 §33).
- "Needs You: 0" → attention as the KPI of autonomy, not agent utilization (← msg 182 §23).

## 9. External evidence mentioned in the conversation

All MENTIONED IN SOURCE (none independently verified in this run): OpenAI Codex App Server protocol (embedding, threads/resume, approvals, `account/rateLimits/read`, `account/usage/read`, ChatGPT-plan auth) (← msgs 181–182); Codex CLI `/status` usage view (← msg 178); Claude Code CLI non-interactive `-p`, JSON/stream-json, `--resume`, `--permission-prompt-tool` MCP routing (← msg 182 §2, §16); Temporal durable workflows and LangGraph persistent interrupts as durability parallels — explicitly not adoption candidates (← msg 182 §10); Agent Cockpit, Munder Difflin, agent-dashboard as UX evidence (← msg 182 §17).

## 10. Evolution / pivots

- "Owner Interface = a UI" → "Owner Plane = architecture/authority protocol; Owner Console = the UI" (← msg 182 §4).
- Old roadmap (Digital Twin before any owner surface) → revised roadmap: Owner Plane contract inside the Architecture Freeze; Console V0 right after Organization OS V0 Core, before the Digital Twin (← msg 182 §3; msg 185).
- "Usage tracking" → Provider Capacity Manager with fail-closed `UNKNOWN` and capacity-as-scheduler-input, after the owner's session-not-API reframing (← msgs 176–178, 182 §12–13).

## 11. Retrieval map

| topic | message range |
|---|---|
| Bootstrap explained to owner (context only) | 172–173 |
| Three levels of owner communication; Owner Brief; Inbox | 174–175 |
| Session-usage constraint; Provider Capacity Manager | 176–178 |
| Deep-brainstorm order + roadmap anchor | 179–180 |
| Codex App Server discovery | 181 |
| Full architecture: laws, gateway, attention, rejections | 182 |
| Owner adoption | 183 |
| Revised roadmap + phases 0–10, exit criteria | 184–185 |
| 18-step controlled sequence | 186–187 |

## 12. What to load when

DEFAULT IMPLEMENTATION: read `idea-nortropic-owner-plane.md`.
IF DESIGN RATIONALE IS NEEDED: read this file.
IF EXACT SOURCE EVIDENCE IS NEEDED: read only the relevant message ranges in `nortropic-owner-plane-full-chat.md` (use §11).
Do not preload the raw transcript into the main implementing context.
