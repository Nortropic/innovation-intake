# Korpus-index — Nortropic innovation-intake

En rad per idé; upsertas vid varje leverans och vid varje statusbyte/korslänkning
(Phase 2.8/3/4 i skillen `nortropic-intake`). STATUS-kolumnen visar hela livscykeln:
`idea → clarified → planned → building → verified` (terminal: `superseded`) —
så syns både idébanken och det pågående i en blick.

`planned`, `building` och `verified` kräver en bunden godkänd plan
(`<slug>/<slug>-approved-plan.md` + `approved_plan_sha256` i briefen) — se `CLAUDE.md`.
Planfilen får ingen egen rad här: indexet är en idékatalog, inte en filförteckning.
Kontrollera hela korpusen mekaniskt med
`python3 ~/.claude/skills/nortropic-intake/scripts/plan_contract.py validate`.

| slug | title | status | created | links |
|---|---|---|---|---|
| build-fast-path | Build fast path: template repo + Content-phase split | clarified | 2026-08-16 | related: snabba-upp-loopar, claude-design-watch |
| gauntlet-wayfinder | Gauntlet quality layer inside the Nortropic trust loop | idea | 2026-08-16 | supersedes: gauntlet-quality-layer; related: webbforvaltningen-capability-assurance |
| agent-harness-priorities | Agent harness priorities: reviewer isolation, provenance, bounded multi-agent patterns | idea | 2026-08-20 | related: nortropic-frontier-delta, bevaka-frontier-ai-engineering, autonomi-utan-sjalvcertifiering, claude-bootstrap-takeover-protocol |
| snabba-upp-loopar | Middle-out loop compression: faster Nortropic loops without touching trust | idea | 2026-08-20 | related: build-fast-path, nortropic-frontier-delta, workflow-orkestrering, brainstorma-nortropic-engineering, bevaka-frontier-ai-engineering, unattended-overnight-execution |
| nortropic-frontier-delta | Nortropic Evolution Loop: autonomous frontier monitoring and self-improvement without touching trust | superseded | 2026-08-20 | superseded_by: bevaka-frontier-ai-engineering; related: agent-harness-priorities, snabba-upp-loopar, workflow-orkestrering, brainstorma-nortropic-engineering, digitalforvaltningen-webb-v2, foundation-repair-gate |
| workflow-orkestrering | Context & orchestration contract: kill copy/paste handoffs, operator portal, learning fabric | idea | 2026-08-20 | related: nortropic-frontier-delta, snabba-upp-loopar, innovation-inbox-idehantering, dokumentation-repo-struktur, brainstorming-arbetsfloden, brainstorma-nortropic-engineering, bevaka-frontier-ai-engineering, nortropic-organization-os, nortropic-planning-wall, verkstadsgolvet-v2-cockpit |
| innovation-inbox-idehantering | Innovation Inbox: a Discovery Plane funnel for frictionless idea capture | idea | 2026-08-20 | related: workflow-orkestrering, openai-anthropic-workflow, nortropic-planning-wall, project-corpus-intake |
| dokumentation-repo-struktur | Thin authoritative core, thick knowledge base: the nortropic-knowledge split | idea | 2026-08-20 | related: workflow-orkestrering, nortropic-organization-os |
| nortropic-som-kommun | Nortropic as a municipality: central governance, shared infrastructure, autonomous förvaltningar | superseded | 2026-08-20 | superseded_by: nortropic-organization-os |
| nortropic-organization-os | Nortropic Organization OS: trust-based autonomy above the Autonomy Kernel | idea | 2026-08-25 | supersedes: nortropic-som-kommun; related: workflow-orkestrering, dokumentation-repo-struktur, bevaka-frontier-ai-engineering, bootstrap-closeout-rebaseline, claude-bootstrap-takeover-protocol, nortropic-aquarium, nortropic-evolution-foundations, nortropic-owner-plane, nortropic-planning-wall, nortropic-recompile, nortropic-function-intake, nortropic-marknadsposition |
| openai-anthropic-workflow | Brainstorm extraction workflow: chat as working memory, harvest as durable artifact | idea | 2026-08-20 | related: innovation-inbox-idehantering, brainstorming-arbetsfloden, project-corpus-intake |
| arbetsmetoder-innovation | Deep Brainstorm protocol: evidence-driven R&D mode as the standing default | idea | 2026-08-20 | related: brainstorming-arbetsfloden, gold-extraction-overlay |
| brainstorming-arbetsfloden | Conversation compiler: BUILD IR, repo reconciliation and evals-before-code after intake | idea | 2026-08-20 | related: workflow-orkestrering, arbetsmetoder-innovation, openai-anthropic-workflow, nortropic-recompile |
| claude-design-watch | Visual Intent: a frozen visual decision step before code, powered by Claude /design | idea | 2026-08-20 | related: build-fast-path |
| brainstorma-nortropic-engineering | The Nortropic engineering stack: layer taxonomy, memory model and the missing layers | idea | 2026-08-20 | related: workflow-orkestrering, nortropic-frontier-delta, snabba-upp-loopar, bevaka-frontier-ai-engineering |
| bootstrap-closeout-rebaseline | Bootstrap closeout and rebaseline: finish narrow, observe, rebaseline, continue | idea | 2026-08-20 | related: nortropic-organization-os, autonomi-utan-sjalvcertifiering, claude-bootstrap-takeover-protocol, korpusfrysning-och-syntesmetod, nortropic-owner-plane, nortropic-planning-wall, unattended-overnight-execution |
| bevaka-frontier-ai-engineering | Nortropic Frontier Observatory: an autonomous technological intelligence and evolution system | idea | 2026-08-20 | supersedes: nortropic-frontier-delta; related: agent-harness-priorities, snabba-upp-loopar, workflow-orkestrering, brainstorma-nortropic-engineering, nortropic-organization-os, digitalforvaltningen-webb-v2, nortropic-evolution-foundations, nortropic-planning-wall, owner-attention-inte-owner-stop, nortropic-marknadsposition |
| project-corpus-intake | Nortropic Intake v3: Project Corpus Intake (PROJECT_SWEEP) + proving-run iteration | idea | 2026-08-31 | related: openai-anthropic-workflow, innovation-inbox-idehantering, nortropic-recompile, corpus-control-plane, korpusfrysning-och-syntesmetod, nortropic-function-intake |
| nortropic-recompile | Nortropic Recompile: the Kernel's first mission compiles Improvements into Concept/Constitution/Architecture/Roadmap | idea | 2026-08-31 | related: nortropic-organization-os, brainstorming-arbetsfloden, project-corpus-intake, corpus-control-plane, korpusfrysning-och-syntesmetod |
| gold-extraction-overlay | Nortropic Gold Extraction: standing lens + batch mining of external builds | idea | 2026-08-31 | related: arbetsmetoder-innovation |
| owner-attention-inte-owner-stop | Owner attention ≠ owner stop: Nortropic delegation order + surgical web-management patch | idea | 2026-08-31 | related: bevaka-frontier-ai-engineering |
| nortropic-planning-wall | Nortropic Planning Wall: AI-native scrum/planning layer on top of Factory Room | idea | 2026-08-31 | related: workflow-orkestrering, nortropic-organization-os, innovation-inbox-idehantering, bevaka-frontier-ai-engineering, bootstrap-closeout-rebaseline, nortropic-aquarium, verkstadsgolvet-v2-cockpit |
| claude-bootstrap-takeover-protocol | Provider failover: Claude takes over the bootstrap from Codex at the usage cap, under the same Nortropic work-form | idea | 2026-08-31 | related: bootstrap-closeout-rebaseline, nortropic-organization-os, agent-harness-priorities |
| nortropic-owner-plane | Nortropic Owner Plane — owner intent, authority, attention and organizational control | idea | 2026-08-31 | related: nortropic-organization-os, bootstrap-closeout-rebaseline |
| corpus-control-plane | Nortropic Corpus Control Plane V0 — corpus, portfolio and radar layer on top of frozen Intake, with Context Compiler | idea | 2026-08-31 | related: project-corpus-intake, nortropic-recompile |
| webbforvaltningen-capability-assurance | Webbförvaltningen Capability Assurance — post-build reconciliation & completeness audit | idea | 2026-08-31 | related: gauntlet-wayfinder |
| nortropic-aquarium | Nortropic Aquarium — calm, evidence-bearing diorama projection of the organization | idea | 2026-08-31 | related: nortropic-organization-os, nortropic-planning-wall |
| nortropic-evolution-foundations | Nortropic Evolution Foundations — semantic registry, causal lineage, principal identity, assumption expiry and the Evolution Loop | idea | 2026-08-31 | related: bevaka-frontier-ai-engineering, nortropic-organization-os |
| digitalforvaltningen-webb-v2 | Digitalförvaltningen: domain competency layer above the Trust Kernel | idea | 2026-08-31 | related: nortropic-frontier-delta, bevaka-frontier-ai-engineering |
| unattended-overnight-execution | Unattended multi-agent execution: overnight mandate, Round A trust protocol, bounded delegation | idea | 2026-08-31 | related: bootstrap-closeout-rebaseline, snabba-upp-loopar |
| foundation-repair-gate | Foundation Repair Gate: vendored-skill provenance, repo-native factory root, pinned measurement | idea | 2026-08-31 | related: nortropic-frontier-delta |
| verkstadsgolvet-v2-cockpit | Verkstadsgolvet v2: executive cockpit with representational compression | idea | 2026-08-31 | related: workflow-orkestrering, nortropic-planning-wall |
| autonomi-utan-sjalvcertifiering | Autonomy without self-certification: hard-stop taxonomy, owner-authority invariant, provider confinement | idea | 2026-08-31 | related: bootstrap-closeout-rebaseline, agent-harness-priorities |
| korpusfrysning-och-syntesmetod | Corpus freeze and synthesis method: evidence grading, authority attribution, two-tier verification | idea | 2026-08-31 | related: project-corpus-intake, nortropic-recompile, bootstrap-closeout-rebaseline |
| nortropic-function-intake | Nortropic Function Intake — dissect an organizational function until Nortropic can take responsibility for it | idea | 2026-09-01 | related: nortropic-marknadsposition, nortropic-organization-os, project-corpus-intake |
| nortropic-marknadsposition | Nortropic marknadsposition — eight simulated company futures, Luleå as laboratory, owner-endorsed initial path | idea | 2026-09-01 | related: nortropic-function-intake, nortropic-organization-os, bevaka-frontier-ai-engineering |
