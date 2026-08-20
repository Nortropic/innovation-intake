---
title: "Innovation Inbox: a Discovery Plane funnel for frictionless idea capture"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: innovation-inbox-idehantering
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: innovation-inbox-idehantering-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: innovation-inbox-idehantering/idea-innovation-inbox-idehantering.md
related: [workflow-orkestrering, openai-anthropic-workflow]
---

# Idea brief: Innovation Inbox — a Discovery Plane funnel for frictionless idea capture

## 1. Summary

Ideas arrive faster than they can be implemented, so Nortropic needs a **Discovery
Plane** separate from the Control Plane: a frictionless inbox where capturing an idea
costs one sentence, a funnel (INBOX → SHAPING → CANDIDATE → READY → ACTIVE → DONE,
plus PARKED) that matures ideas without interrupting active coding, and an eventual
"Spara den här idén"-command from chat. The framing decision: **an INBOX item must
never automatically become executable factory work.** HISTORICAL CAVEAT: this chat
built a concrete v1 (GitHub Projects + issue bridge) that was later dismantled; the
idea-capture need has since partially been served by the idébank corpus and the
`nortropic-intake` skill — the owner must decide what of this brief remains live.

## 2. Context you need

At capture time (Aug 15) Nortropic's backlog was execution authority only — no home
for raw ideas. The chat hand-built the GitHub Project "Nortropic Innovation" (statuses,
board, fields `Area` [8 options], `Source / Context` [a pointer, never the content],
`Why it matters` [one sentence]) and a separate repo `Nortropic/innovation-intake`
where a second, parallel Claude Code session built the v1 bridge
(issue → GitHub Actions → Projects GraphQL → INBOX with fields set), proven
end-to-end. The remaining unsolved piece was a reliable ChatGPT→GitHub write path
(plugin writes blocked; a Custom GPT + Action route was scrapped). The intake repo has
since been repurposed as the idea corpus (idébanken) and chat capture is now done by
the `nortropic-intake` skill — several concepts from this chat (funnel states,
shaping, dedup commands) remain unimplemented ideas.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Capture is one sentence: "Ny idé? → skriv titel → INBOX → fortsätt arbeta."
  Metadata (Area, Source/Context, Why it matters) is optional at capture and can be
  filled later by a human or a shaping agent.
- A funnel that separates idea maturity from execution: INBOX (raw) → SHAPING
  (research/dedup/structure) → CANDIDATE → READY (implementable contract) → ACTIVE →
  DONE, with PARKED as a shelf — where only READY may feed the factory's canonical
  task authority, through the normal owner process.
- Chat-native commands: "Spara den här idén" (create INBOX item with inferred
  title/area/source/why), "Visa mina innovationsidéer" (read + summarize),
  "Shape:a I-023" (research + fill + move INBOX → SHAPING).
- Dedup/aggregation over the idea set ("we have 17 verification ideas, five are the
  same problem").
- The intake machinery lives OUTSIDE `nortropic-system` and can never touch the
  running factory.

Choose architecture/decomposition/tooling yourself, within §6 — including whether the
GitHub-Projects funnel or the current idébank corpus is the substrate.

## 4. Decisions already made (do not relitigate silently)

- D1. Ideas must be capturable without interrupting active work — one-sentence
  capture, metadata later — because the whole problem is that capture friction loses
  ideas (← msg 1–4, 16).
- D2. Discovery Plane ≠ Control Plane: an inbox item never automatically becomes
  factory work — because idea flow must not contaminate execution authority
  (← msg 4, 23, 39).
- D3. Intake infrastructure is built in a separate repo and a separate parallel
  Claude Code session — never inside `nortropic-system` — because the idea system
  must not be able to interfere with the running control-plane build (← msg 28–35).
- D4. Metadata model: `Area` (CONTROL PLANE / FACTORY-AGENTS / VERIFICATION /
  UX-VERKSTADSGOLVET / RESEARCH-SELF-IMPROVEMENT / PERFORMANCE / PRODUCT / OTHER),
  `Source / Context` as a pointer ("var hittar jag ursprunget?"), `Why it matters` as
  one sentence — chosen so a future AI can sort hundreds of ideas (← msg 18–23).
- D5. ChatGPT does the thinking (title, area, why, dedup, shaping); GitHub is just the
  database — because the intelligence layer is where capture friction is removed,
  while storage should stay dumb and inspectable (← msg 26).
- R1 (REJECTED, by owner). The Custom GPT + Action write path — "detta fungerade
  inte, vi skrotar denna idé" — because it hallucinated successful saves and Custom
  Actions did not work with Pro thinking (← msg 98–108).
- R2 (REJECTED). Importing existing repo items into the Project at creation —
  because the funnel must start as a clean idea surface, not inherit execution
  backlog items (← msg 8–9).
- R3 (REJECTED at the time). Building on custom MCP write from ChatGPT — write
  support was beta/not available on the Pro plan (← msg 26).
- U1 (UNRESOLVED). A working ChatGPT→GitHub write path: the chat ends with
  `create_issue` newly exposed but the session still blocking execution; proposed next
  step was a fresh chat (← msg 105–117).

## 5. Acceptance criteria (v1)

- AC1. WHEN the owner captures an idea (chat command or manual), THE system SHALL
  store it in INBOX with only a title required, in under ~10 seconds of owner effort.
- AC2. WHEN an intake record is malformed (unknown Area, missing required metadata at
  shaping time), THE bridge SHALL fail closed with a visible error and SHALL NOT
  mutate the idea store.
- AC3. WHEN the same idea source is submitted or edited again, THE system SHALL update
  the existing item idempotently — never a duplicate.
- AC4. WHEN an idea reaches READY, THE handover to the factory SHALL go through the
  existing canonical task authority — no direct execution from the idea store.
- AC5. WHEN intake automation runs, THE record SHALL show zero writes to
  `nortropic-system`.

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Suggestions from the chat: versioned intake contract (schema marker, strict Area
enum, whitespace-tolerant parsing, fail-closed on unknown values); least-privilege
auth (GitHub App / narrowly scoped credential; plain GITHUB_TOKEN cannot reach
Projects); issue-backed items over duplicate drafts; keep the v1 bridge's test suite
ideas (valid/invalid intake, idempotency, edit-updates). If rebuilt today, weigh the
GitHub funnel against extending the idébank corpus + `nortropic-intake` skill, which
already own capture and storage.

## 7. Out of scope (v1)

- Automatic promotion of ideas into factory tasks (D2 boundary).
- The Custom GPT + Action route (rejected, R1).
- Shaping/research automation beyond the command definitions (a later stage on top of
  a working inbox).
- Touching `nortropic-system` or the running build session in any way (D3).

## 8. Verification (how we know it works)

End-to-end: capture one idea via the chat command → confirm INBOX item with correct
fields from the store's own state (AC1); submit a malformed intake and show the
fail-closed rejection with no mutation (AC2); resubmit/edit the first idea and show
idempotent update (AC3); promote one idea to READY and show the handover lands as a
canonical task through the normal owner process (AC4) — all confirmed from the record
by an independent reviewer.

## 9. Open questions (interview the owner before planning)

- Q1. Supersession call: has the idébank corpus + `nortropic-intake` skill superseded
  this idea's storage layer, so the remaining live scope is the FUNNEL (shaping/
  candidate/ready lifecycle) and chat-capture commands on top of the corpus? Or do you
  still want the GitHub Projects funnel?
- Q2. Does the GitHub Project "Nortropic Innovation" still exist with captured ideas
  that need migrating into the corpus?
- Q3. U1: is a ChatGPT→write path still wanted at all, now that local Claude Code
  (nortropic-intake) can harvest chats directly?
- Q4. Should the corpus INDEX status lifecycle (idea → clarified → …) absorb the
  funnel states (SHAPING/CANDIDATE/READY/PARKED), or stay separate?
- Q5. Who runs shaping/dedup — a scheduled agent, on-demand command, or part of a
  future synthesis pass?

## 10. Process for this brief

1. Clarify: first send a subagent to read the source conversation and report back the
   rationale relevant to §9 (keeps the transcript out of main context); then interview
   the owner on §9 (AskUserQuestion); append answers here.
2. Plan in plan mode; owner reviews before any code ("address all notes, don't implement yet").
3. Implement in a fresh session from the approved plan.
4. Adversarial review: fresh subagent checks the diff against this brief; report only
   gaps affecting correctness or stated requirements.
5. Traceability: commit messages cite this brief's slug.

## References

- Source conversation: `innovation-inbox-idehantering-full-chat.md` (same folder)
- Related brief: `workflow-orkestrering/` (Discovery Plane over Control Plane; intake.submit in the operator portal)
- Repo history of `Nortropic/innovation-intake` (v1 bridge commits f9c6e82/afbb979, later removed)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
