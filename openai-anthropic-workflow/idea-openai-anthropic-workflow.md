---
title: "Brainstorm extraction workflow: chat as working memory, harvest as durable artifact"
type: idea-brief
status: idea   # lifecycle: idea → clarified → planned → building → verified; terminal: superseded
slug: openai-anthropic-workflow
owner: Johnny (Nortropic)
created: 2026-08-20
source_conversation: openai-anthropic-workflow-full-chat.md   # reference only — this brief takes precedence
intended_repo_path: openai-anthropic-workflow/idea-openai-anthropic-workflow.md
related: [innovation-inbox-idehantering, brainstorming-arbetsfloden]
---

# Idea brief: Brainstorm extraction workflow — chat as working memory, harvest as durable artifact

## 1. Summary

The extraction problem: long brainstorms in ChatGPT/Claude are hard to turn into
buildable material. The researched answer, matching OpenAI's and Anthropic's own
practice: **the chat is working memory, never the system of record** — the flow is
conversation → extraction/compaction → durable artifact → execution, not "export the
transcript and hand it over". The chat's endpoint — Claude Code opening a chat URL in
the logged-in Chrome, reading it fully, and extracting `brainstorm-source.md` +
`idea-brief.md` under strict classification rules — **has since been implemented as
the `nortropic-intake` skill**. This brief preserves the rationale and the two
still-open threads: the Tana track and the native ChatGPT "project sources"
alternative.

## 2. Context you need

Evidence gathered in-chat: Anthropic's Legal and Growth teams brainstorm in Claude.ai
and let Claude condense the session into step-by-step implementation material;
OpenAI's agent-first team made repository knowledge the system of record (AGENTS.md is
a map); Codex practice is Ask-mode planning → issue-like tasks → queue; OpenAI's
brainstorming guide is wide → narrow → plan. As a ready-made store, Johnny acquired
**Tana** in this chat and set up an `#Idea` structure (initial transfer via plain
copy/paste). ChatGPT Projects can natively save an answer as a permanent **project
source**. The final workflow (msg 26) — `claude --chrome`, open chat URL, read all,
never modify, extract into an 11-section harvest with rules like "never classify an
assistant suggestion as a user decision without explicit acceptance" — is the seed
that became `nortropic-intake`.
Read the source conversation only if you need rationale. Where it conflicts with this
brief, this brief wins.
Invariants this must not violate: Nortropic's trust layer — constitution & rulebook
(`nortropic-system/docs/07-konstitution.md`, `03-regelverk.md`): trust contracts, frozen
gates, §-rules. Pointer only — read them there; never copied here.

## 3. Destination (goal, not implementation plan)

- Every valuable brainstorm ends in a durable, self-contained artifact (brief +
  linked source) in a permanent store — never as a chat left to memory. (Realized by
  `nortropic-intake` + idébanken; kept here as the standing principle.)
- Extraction preserves epistemics: user decisions vs assistant proposals vs rejected
  alternatives vs open questions are kept distinct; the user's latest explicit
  position wins; disagreements and uncertainty survive extraction.
- A decided role (or retirement) for Tana in the toolchain, and a decided stance on
  ChatGPT Projects' "save to project sources" for ChatGPT-side permanence.

Choose architecture/decomposition/tooling yourself, within §6.

## 4. Decisions already made (do not relitigate silently)

- D1. Chat is working memory; the durable artifact is the record — because both
  OpenAI's and Anthropic's own teams converged on conversation → compaction → artifact
  → execution (← msg 5–6, 21).
- D2. Don't build a custom extraction system when starting: use a ready-made store —
  Tana was chosen and acquired, with an `#Idea` structure and copy/paste as the first
  bridge (← msg 8–16).
- D3. The harvest workflow: Claude Code + Chrome integration reads the chat by URL
  (read-only) and produces source + brief with strict decision-classification rules
  — because no native cross-system chat API exists and the logged-in browser is the
  officially supported read path (← msg 24–26). [Since implemented as the
  `nortropic-intake` skill.]
- P1 (noted option). ChatGPT Projects' "Save to project / Add to project sources"
  turns an answer into a permanent source for future chats — a native ChatGPT-side
  alternative for pre-harvest permanence (← msg 21).

## 5. Acceptance criteria (v1 — for what remains)

- AC1. WHEN a brainstorm is harvested, THE artifact SHALL separate user decisions,
  assistant proposals, rejected alternatives and open questions, and SHALL prefer the
  user's latest explicit position.
- AC2. WHEN the owner decides Tana's role, THE toolchain documentation SHALL state
  what lives in Tana vs idébanken, or that Tana is retired.
- AC3. WHEN a ChatGPT-side note must persist before harvest, THE workflow SHALL name
  the mechanism (project source, or explicit none-needed).

## 6. Constraints & implementation notes (right altitude — suggestions, not orders)

Invariants: Nortropic's trust layer — constitution & rulebook (pointer, never a copy).
Most of this brief's machinery already exists in `~/.claude/skills/nortropic-intake/`;
any further work should extend that skill rather than reopen the architecture. The
msg-26 extraction rubric (11 sections, decision-classification rules) is a useful
cross-check against the skill's brief template.

## 7. Out of scope (v1)

- Rebuilding what `nortropic-intake` already does (capture, verification,
  distillation, corpus delivery).
- A custom extraction system (rejected in favor of ready-made tools at the start; now
  moot).
- Transcript-as-handoff (the anti-pattern this whole chat argues against).

## 8. Verification (how we know it works)

From the record alone: one harvested brainstorm shows the epistemic separation of AC1
(spot-check that no assistant proposal appears as an owner decision); the toolchain
doc answers AC2/AC3 unambiguously.

## 9. Open questions (interview the owner before planning)

- Q1. Tana: still in use for idea capture, or superseded by idébanken? If kept, what
  is its lane (personal notes vs corpus)?
- Q2. Should ChatGPT-side brainstorms be saved as project sources pre-harvest, or is
  harvest-on-demand (this campaign's model) sufficient?
- Q3. Should the msg-26 rubric's sections (e.g. "current thesis", "user hypotheses")
  be folded into the `nortropic-intake` brief template, or is the current template
  deliberately leaner?

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

- Source conversation: `openai-anthropic-workflow-full-chat.md` (same folder; msg 26
  is the seed of the nortropic-intake skill)
- The implemented result: `~/.claude/skills/nortropic-intake/`
- Related brief: `innovation-inbox-idehantering/` (idea-capture family)
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
