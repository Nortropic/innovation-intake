---
title: "Nortropic Owner Plane — owner intent, authority, attention and organizational control"
type: idea-brief
status: idea
slug: nortropic-owner-plane
owner: Johnny (Nortropic)
created: 2026-08-31
source_conversation: nortropic-owner-plane-full-chat.md
design_rationale: nortropic-owner-plane-design-rationale.md
intended_repo_path: nortropic-owner-plane/idea-nortropic-owner-plane.md
context_revision: 1
related: [nortropic-organization-os, bootstrap-closeout-rebaseline]
---

# Idea brief: Nortropic Owner Plane

## 1. Summary

Create an Owner Plane: the layer through which Johnny expresses will to Nortropic (intent, priority, constraint, decision) and through which the organization returns real owner decisions — without Johnny acting as scheduler, prompt author and context shuttle. The single most important framing decision: the Owner Plane is built **protocol first, thin console second, rich Digital Twin UX last**, and it runs on the existing ChatGPT/Claude session-plan allowances, never on API billing as a base assumption. The idea was born in the tail (msgs 172–187) of an otherwise operational bootstrap-takeover chat; msgs 1–171 are execution-state material, not brainstorm truth.

## 2. Context you need

The Full Autonomy Bootstrap (Supervisor, H036/H032/H031, gates, evidence) is the Execution Plane; Organization OS is the planned Organizational Plane. The missing third layer: today the owner is himself the orchestrator between chats and terminals. Target: three planes — Owner / Organizational / Execution — where Stadshuset (Owner Console), Verkstadsgolvet (Digital Twin) and Aquarium are all projections of the same Organization OS state, none a source of truth. Nothing is implemented before `BOOTSTRAP_CHECKPOINT=PASS`.

This brief is the primary intake artifact for execution. Deeper design logic lives in the linked design rationale; the full chat is raw evidence — read targeted message ranges only if the rationale is insufficient. Current canonical repository authority beats all intake artifacts; within the intake package this brief wins over rationale and transcript. Once an owner-approved plan is bound (see the frontmatter), it carries execution order above this brief and below current repository authority.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- An event-sourced Owner Plane protocol: `OwnerUtterance → InterpretationProposal → typed OwnerIntent → Authority Router → OrganizationEvent`, governed by the 15 Owner Plane Laws (owner speech ≠ model interpretation ≠ organization state; UI never mutates canonical state; sessions disposable, organizational state durable).
- A durable Attention system where "Needs You: 0" is the key metric — real owner stops are state, not terminal messages.
- Typed Actuation V0 with few, understandable, largely reversible operations (`CAPTURE_INTENT`, `SET_PRIORITY`, `SET_CONSTRAINT`, `PAUSE/RESUME_INITIATIVE`, `RESPOND_TO_ATTENTION`).
- A Provider Capacity Manager over session/plan usage (Codex App Server observability, Claude CLI signals) reporting `AVAILABLE/DEGRADED/EXHAUSTED/RESET_AT/UNKNOWN` — scheduler information, never trust authority.
- A deliberately small local Owner Console V0 ("Stadshuset"): ASK NORTROPIC / NEEDS YOU / NOW / PRIORITIES / CAPACITY.
- Roadmap revision: the Owner Plane contract joins the Organization Architecture Freeze; Owner Console V0 is built right after Organization OS V0 Core, **before** the full Digital Twin.

Choose architecture, decomposition and tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

D1. An Owner Interface/Owner Plane shall be created to steer Nortropic, and it must run on the existing session/plan usage (ChatGPT/Claude subscriptions), not API billing — because the owner pays for sessions, and the control panel must not turn Nortropic into a large API consumer (← msg 176; elaboration msgs 177–178).
D2. The Owner Plane is brainstormed per the previously defined Deep-Brainstorm protocol, anchored in the agreed roadmap FULL AUTONOMY BOOTSTRAP → AUTONOMY KERNEL v1 → Organization OS → Digital Twin (← msg 179).
D3. Adopt the protocol-first architecture and revised roadmap — Owner Plane Laws, Owner Plane contract inside the Architecture Freeze, Console V0 before the full Digital Twin — because "Detta låter bra, låt oss planera för detta" (← msg 183; architecture msg 182).
D4. Deliver the path as a controlled sequence with per-phase exit criteria — the 18-step sequence from bootstrap closeout to Aquarium — because the owner asked for the concrete step-by-step procedure (← msg 186; sequence msg 187).

R1. Chat-directly-to-supervisor as authority — because chat becomes authority with no provenance (← msg 183; msg 182 §28).
R2. Codex App Server replacing H036 as trusted execution boundary — because App Server is an observation/session protocol; trusted work still flows Supervisor → H036 → provider → H032 → H031 (← msg 183; msg 182 §14).
R3. Copying Munder Difflin's "GOD orchestrator" trust model — because Nortropic's authority lives outside the model; steal UX ideas, never the trust model (← msg 183; msg 182 §18).
R4. Scraping the ChatGPT/Claude web UI for usage — because adapters must report only what clients actually expose, falling to `UNKNOWN` instead of guessing (← msg 183; msgs 178, 182 §12).
R5. Building the Owner UI now, before `BOOTSTRAP_CHECKPOINT` — because the finished bootstrap's reality must inform the architecture; capture as shaped initiative, implement after intake + current-reality inventory (← msg 186; msgs 185, 187 step 1).

## 5. Acceptance criteria (v1)

AC1. WHEN the owner submits a natural-language utterance, THE Owner Plane SHALL preserve it verbatim and append-only, record the model's interpretation as a separate proposal, and change organizational state only via a typed intent that passed the Authority Router (← msg 183; msg 182 §5, §38).
AC2. WHEN the owner runs the first real control test ("prioritize webbförvaltningen over Aquarium; Aquarium may continue shaping but no implementation until Organization OS V0 is green"), THE system SHALL prove the whole chain — utterance preserved → typed priority+constraint → canonical state updated → Supervisor obeys → Console reflects it → "Why?" returns exact owner intent and transition chain — without the owner writing a single provider prompt (← msg 186; msg 187 step 14, msg 185).
AC3. WHEN all provider sessions are exhausted, THE Owner Plane SHALL remain fully readable and decision-capable, parking model-requiring work as `WAITING_FOR_PROVIDER_CAPACITY`; idle UI consumes zero model usage (← msg 176; msg 182 §26–27).
AC4. WHEN a provider capacity state cannot be evidenced, THE Provider Capacity Manager SHALL report `UNKNOWN` rather than guess, and capacity SHALL never be used as trust authority (← msg 176; msgs 178, 182 §12).
AC5. WHEN a genuine owner decision is needed, THE Attention system SHALL persist a durable AttentionRequest (why owner is needed, recommendation, alternatives, consequence if unanswered) that survives session death, provider switch and machine restart (← msg 183; msg 182 §8, §10; msg 187 step 15).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants this must not violate: Nortropic's trust layer — constitution & rulebook (`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`). Pointer only — never copied here.
Suggestions: local-first (`localhost` on the owner's Mac, authenticated CLIs own their credentials); event-sourced owner intents with supersession, never edits; distinguish provider permission prompts from Nortropic owner decisions; "ask only when ambiguity is materially consequential"; Explain (provenance-backed "Why?") and Preview ("if applied: …") belong in the Architecture Freeze; run the Current-Reality Inventory (KEEP/ADAPT/ADD/SIMPLIFY/DEFER/REJECT/NEEDS_EVIDENCE) before building anything.

## 7. Out of scope (v1)

- Any implementation before `BOOTSTRAP_CHECKPOINT=PASS` and the bootstrap-closeout freeze (`AUTONOMY_KERNEL_V1=FROZEN_BASELINE`).
- Msgs 1–171 of the source chat (bootstrap execution) — execution learning, not brainstorm truth.
- The full Verkstadsgolvet Digital Twin and Aquarium (separate tracks; here only later projections of the same state).
- V0 non-goals from the chat: mobile app, 3D office, animated agents, voice, customer access, multi-tenant, public cloud deployment, automatic production risk approvals, generic workflow designer, hundreds of typed actions (← msg 185).
- Letting H036 drive Codex App Server as executed provider — an investigation question (Q2), not scope.

## 8. Verification (how we know it works)

Execute the 18-step sequence's step-14 first real control test (AC2) end-to-end on the real system and capture the mechanical evidence chain (preserved utterance, typed intents, organization events, supervisor eligibility changes, console projection, "Why?" provenance) so an independent reviewer can confirm `OWNER_PLANE_V0=OPERATIONAL` from the record alone.

## 9. Open questions (interview the owner before planning)

Q1. Package identity: own slug vs addition/episode under `nortropic-organization-os`? The assistant requires coupling ("inte leva som ett parallellt system") — the corpus check plus an owner call must decide (← msg 187 step 3).
Q2. May H036 later drive Codex App Server as the executed provider? Kernel-evolution question — investigate, never assume (← msg 182 §15).
Q3. Which stable capacity signals does Claude Code CLI actually expose today? (← msg 182 §12; msg 185 inventory)
Q4. Exact typed-intent taxonomy, and which actuation classes enter V0 versus later (approve publication, change delegation, accept risk…)? (← msg 187 step 13)
Q5. Exact Explain/Preview contracts to include in the Architecture Freeze (← msg 185).

## 10. Process for this brief

1. Clarify: first send a subagent to read `nortropic-owner-plane-design-rationale.md` (its rejection and unresolved sections cover most §9 rationale) and report back what bears on §9; only if the rationale lacks the needed evidence, exact source wording matters, or a conflict/ambiguity remains, have it read the targeted message ranges in the source conversation via the rationale's retrieval map — never the whole transcript, and keep both out of main context; then interview the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. On explicit owner approval, persist the exact approved plan as `nortropic-owner-plane-approved-plan.md`, validate it (`scripts/plan_contract.py validate`), bind it into this frontmatter and only then set `status: planned`.
4. Implement in a fresh session started from the approved plan: `plan_contract.py resume --slug nortropic-owner-plane --target-repo <repo>`; reconcile against current repository truth; after any compaction re-read the plan from disk; if it cannot be proven, STOP with `PLAN_IDENTITY_UNAVAILABLE`.
5. Adversarial review: fresh subagent checks the diff against this brief and the approved plan.
6. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `nortropic-owner-plane-full-chat.md` (same folder; idea content msgs 172–187)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
