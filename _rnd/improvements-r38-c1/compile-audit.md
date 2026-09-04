---
title: "improvements-r38-c1 — compile audit"
type: compile-audit
compile: improvements-r38-c1
project: improvements
owner: Johnny (Nortropic)
append_only: true
---

# Compile audit: improvements-r38-c1

## AUDIT-1
- auditor: independent semantic verification — fourteen fresh isolated reviewers, none of whom wrote the items they judged
- audited_at: 2026-09-04
- scope: ir_sha256=4a05fc361669cde154605a89604a4830f033e70082ddaabfd528e610dc86cc35 — SEMANTIC coverage against the frozen r38 falsification, not a re-review of structure. The structural/provenance layer is separately green (`validate` 0 FAIL / 0 WARN under RND contract v4.1, 30/30 source region hashes matching the IR, 0 RAW files modified). What is audited here is the claim this compile exists to make: that the 619 MATERIAL semantic omissions the external SOURCE→IR falsification found in `improvements-r38` are now carried. Method, in three passes, each by reviewers barred from writing what they judged. PASS 1 (six reviewers, 619 findings): does the item claiming a finding actually carry its meaning, judged against the blind reviewer's statement and verbatim anchor, with the raw source available? Verdicts CARRIED / PARTIAL / NOT_CARRIED / MISATTRIBUTED. Result 589 / 28 / 2 / 0. Every reviewer additionally ran mechanical checks over its whole batch — anchors located literally in the bound revision, item provenance overlapping the finding's message range, and owner-authority attributions cross-checked against the transcript role index; 0 misattributions were found, including on the pasted-agent-output findings where an owner-labelled turn carries agent text. PASS 2 (six reviewers, the 589 accepted): the bundle for PASS 1 omitted the adjudicator's `consequence_if_lost` through a defect in the harness, so PASS 1 judged against the finding's statement alone — a weaker criterion than the protocol specified. Rather than record that as a limitation, the 589 were re-judged against the consequence itself: would a rebuild reading only this item avoid the loss the adjudicator describes? Result 570 HOLDS / 19 SHORTFALL. PASS 3 (the 49 repaired findings, two reviewers): the same consequence criterion, applied by reviewers who did not write the repairs. Result 49 HOLDS / 0 SHORTFALL, with three marginal calls recorded in the reviewers' own words rather than resolved silently. 570 findings held at pass 2 and 49 at pass 3, so all 619 MATERIAL findings are verified carried and OPEN MATERIAL SEMANTIC OMISSIONS = 0. Repairs were made by workers who saw the reviewer's complaint but not each other's work: 30 findings in round one (15 claim extensions, 12 new items), 19 in round two. Two items — RND-430 and RND-431 — were diagnosed as over-compressed and split rather than stretched, since a single claim carrying twelve candidate business functions had lost the per-function operating content. That diagnosis is corroborated by the measured relationship between compression and loss: findings carried by an item holding 1–2 findings were not accepted at 1.1%, 3–6 findings at 6.3%, and 7+ findings at 19.4%. Over-compression, not under-compression, is where this corpus loses meaning.
- verdict: PASS

### Method limits, recorded rather than smoothed over
- The 30 unchanged source revisions were NOT blind-reviewed again; the 8,275 blind findings, their 4,611 match rows and the 619 materiality adjudications are frozen input, reused exactly. This audit therefore inherits whatever the original blind pass missed, and cannot detect a meaning no blind reviewer found.
- The PASS 1 bundle rendered only `claim`, `quote` and `provenance` of each item, hiding `evidence_refs` and `uncertainty`. Two reviewers caught this independently and noted items whose missing content was in fact present in those fields. PASS 2 and PASS 3 bundles carry the full item record, and the repair rounds were told the whole record is the unit.
- `consequence_if_lost` on some findings reads "Same as F-…"; reviewers resolved those cross-references against the named finding before judging, and said so.
- Reviewer counts are per finding, not per item: several items carry more than one finding and were judged separately against each, which is why one item can hold and fall short at the same time.

### Owner authority
- OWNER_ADJUDICATION_R38 (`OWNER_CHECK_R38=PASS`, STÄMMER 39 / FELTOLKAT 0 / VISA KÄLLAN 0) is bound to this compile as an executable guard: 195 assertions over the eleven critical authority consequences, **0 violations**. Every assertion is a ceiling on what the corpus may claim, never a grant.
- All 86 OWNER_DECISION items carry a typed `owner_authority_basis`; 33 of them (38%) are machine-readably NOT the owner's own words. In `improvements-r38` that distinction existed only as free-text caveat on 57 of 76 items.
- Three bases could not be settled inside any single source and were adjudicated against the whole corpus, with the ground recorded: RND-171 (`owner-authored` — the deciding sentence occurs exactly once in the corpus, in an owner turn), RND-179 (`owner-adoption-of-assistant-text`), RND-057 (`standing: PROPOSAL`, not DEFERRED — no owner turn defers it).
