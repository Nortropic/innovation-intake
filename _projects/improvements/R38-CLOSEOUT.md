---
title: "Improvements r38 — terminal qualification closeout"
type: qualification-closeout
project: improvements
owner: Johnny (Nortropic)
append_only: true
---

# Improvements r38 — terminal closeout

This is the durable record of how the r38 attachment-semantic qualification campaign
ended. A future agent should be able to reconstruct the whole conclusion from this
file plus the artifacts it names, without any chat history.

    R38_CLOSEOUT   = COMPLETE_WITH_KNOWN_HISTORICAL_SOURCE_LOSS
    R38_RECOVERY   = TERMINAL_UNLESS_NEW_PRIMARY_EVIDENCE

The campaign is finished. The corpus is not perfect, and says so.

## What is bound

    FROZEN SOURCE CUT
      project improvements, inventory_revision 38, 30 sources, 36 revisions
      BODY_SOURCE_IDENTITY         994fa5b0aeff79741dcf43dee5c4039b204f96600dabe6d9509233c646da98f9
      FULL_SOURCE_SURFACE_IDENTITY 51311084d9e11f905797f2233cf410031c34bf43f031502d6a64f68e686d94a0

    CANDIDATE LINEAGE (each preserved byte-identically; none edited in place)
      improvements-r38             6816b133f97fa920258a1bebc039f619d59c736aace15aadb04ee0d767682a1d
      improvements-r38-c1          4a05fc361669cde154605a89604a4830f033e70082ddaabfd528e610dc86cc35
      improvements-r38-c2-rematch  b340122226a57bb4953e01677f13c623cc84d68e2fbbe2edbacd92aee099f196
      improvements-r38-c3-epistemic ac743f847227cd3ea685fd00ea54625c4addcb1431fa6fcf83dce0de6fe24d27
      improvements-r38-c4-epistemic d60f3e27c979d126be95de144acd054664e0d097c578ae7811e839259d3ad8cc   <- terminal

    TERMINAL ADJUDICATION
      CONV-001 primary-source-loss adjudication
      06d5abefa7dcf9fe17bf5afd5a5052871dbdf134bc9cf8f30af1147ccc9a9c6d

    FROZEN FALSIFICATION WITNESS
      attachment-semantic qualification scratch
      94da7113d70289642acc842c51e7fa381b15e99bc35fcd79650beee425c5d64f

c2, c3 and the rematch records are campaign evidence held outside the corpus; c4 is
published here because it is the terminal derived candidate. c1 remains the semantic
coverage compile and its audit is unchanged — c4's audit is scoped to epistemic status
only and says so.

## Result

    MATERIAL ATTACHMENT FINDINGS                 21
    RESOLVED_BY_SOURCE_BOUND_READABLE_EXTERNAL   19
    SOURCE_BOUND_BUT_INSUFFICIENT                 0
    MISMATCHED_SOURCE                             0
    STILL_UNRESOLVED                              2

    BOUND 16 · AMBIGUOUS 1 · NOT_BOUND 4

## The two that do not close

Both are CONV-001, and both are `KNOWN_IRRECOVERABLE_IN_CURRENT_HISTORICAL_SURFACE`.

**BAF-CONV-001-A-007 / B-015 — the Context Mesh image.** The surviving contemporaneous
observation at msg 23 hedges the flow it read off the diagram (*"Bilden visar ett flöde
ungefär:"*) and then asserts specific mechanics beyond that hedge (*"Den visar även hop
budgets, typed edges och dead-end traversal"*). Only the image could separate what the
diagram LABELLED from what the assistant SUPPLIED. The original adjudicator invoked the
semantic-redundancy escape and rejected it on exactly this ground.

**BAF-CONV-001-A-014 / B-024 — the msg-61 batch.** Msg 62 opens *"Först en liten
korrigering från din anteckning: författaren heter Jake Van Clief"* while the owner's
turn contains no note and no names. Only the artefact could settle whether that was the
owner's own words or a caption inside a forwarded image. Uploading is not authoring, and
the corpus's whole role-provenance contract turns on that distinction.

**Why no representation closes them.** Nineteen findings closed because a contemporaneous
derived observation preserved the *meaning* they protected. These two protect the missing
artefact's *primary falsification value* — the ability to check the observation against
the thing observed. A derived observation can carry meaning forward. It can never carry
forward the ability to falsify itself.

## What TERMINAL means, and does not mean

`R38_RECOVERY = TERMINAL_UNLESS_NEW_PRIMARY_EVIDENCE` means: do not run another broad
recovery sweep for these two unless genuinely new primary-source evidence or a new
discriminating locator appears. The basis is exhaustion, established mechanically:

- the frozen conversation proves the attachments existed (owner msgs 13, 22, 61, 77);
- CONV-001's own builder header records 55 attachments inventoried, content not captured;
- the attachment manifest carries no usable per-item identity — all 55 rows have `original_filename: null`;
- targeted File Library recovery failed across six successive recovery bridges;
- no discriminating primary-source fingerprint remains in the frozen locus.

It does **not** mean the sources never existed, that their content may be reconstructed,
that secondary synthesis may substitute for them, or that owner authority may close the
gap.

## Terminal states

    CORPUS_INTEGRITY                    = PASS
    SOURCE_CAPTURE_COMPLETENESS         = NO
    SEMANTIC_QUALIFICATION              = NOT_ESTABLISHED
    FULL_SOURCE_CAPTURE_CONV_013        = NO
    ATTACHMENT_SEMANTIC_R38             = FAIL
    FINAL_IMPROVEMENTS_CORPUS_QUALIFIED = NO
    POST_R38_CAPTURE_STARTED            = NO
    RECOMPILE_STARTED                   = NO
    NORTROPIC_SYSTEM_MUTATIONS          = 0

`CORPUS_INTEGRITY=PASS` coexisting with `ATTACHMENT_SEMANTIC_R38=FAIL` is the intended
shape: a corpus may be internally healthy while accurately declaring that its source
evidence is incomplete. CONV-013's source surface remains separately `KNOWN_UNRESOLVED`
and was not touched by this campaign.

## Failure canon

Eight distinctions this campaign paid for. They are lessons, not architecture authority.

1. **Assurance has a direction.** An IR→SOURCE check being green does not mean SOURCE→IR
   coverage holds. The original r38 compile passed its own validators while 619 MATERIAL
   semantic omissions sat in it.
2. **A green test needs activation evidence.** "0 false positives" over a population that
   never exercised the rule measures nothing.
3. **Unavailable to one harness is not unavailable to the organization.** Content this
   agent could not fetch was readable through another interface entirely.
4. **Semantic accessibility is not byte capture.** A source can be readable while its
   historical bytes are permanently unheld.
5. **Semantic completeness is not historical truth proof.** Preserving what was claimed,
   what supported it and what remains unverified is the job; re-proving the past is not.
6. **Semantic redundancy is not primary-evidence preservation.** A contemporaneous
   observation may carry the meaning and never the falsifiability.
7. **UNKNOWN / UNVERIFIED is positive information.** It must travel with the claim, and may
   be promoted to neither truth nor falsity.
8. **Owner-labelled is not owner-authored.** Uploading, pasting machine output, or carrying
   assistant prose inside an owner turn does not make the content the owner's.

## Handoff

    READY_TO_RETURN_TO_AUTONOMY_KERNEL = YES

meaning only that no further r38 work is justified before Kernel v1 is finished. It does
not authorize Recompile, and it does not authorize the post-Kernel Improvements sweep.
