---
title: "improvements — review queue"
type: review-queue
project: improvements
owner: Johnny (Nortropic)
append_only: true
---

# Review queue: improvements

## RQ-001
- date: 2026-08-31
- issue: Reversal-kandidat i nortropic-organization-os: nya svansen (CONV-005 msg 63–66) låter Execution Master v3 SUPERSEDA msg-49-masterprompten, medan briefens §6 pekar ut msg-49-prompten som avsett Claude Code-kontrakt. Ägaren styrde riktningen (msg 63) men ratificerade aldrig supersessions-formuleringen explicit.
- affects: CONV-005, nortropic-organization-os
- recommendation: registrera ett ägardelta (ARCHITECTURE_DECISION) som antingen ratificerar Master v3-supersessionen eller behåller §6-pekaren, vid nästa aktivering av paketet
- evidence: msg 63, 66, 67, 71, 73 i CONV-005 (episod CHAT-002 i paketet)
- owner_judgment_required: yes

## RQ-002
- date: 2026-08-31
- issue: Reversal-kandidat i claude-design-watch: briefens D1 säger att den veckovisa /design-bevakningen är AKTIV; CONV-014 msg 6 rapporterar att bevakningen stängdes av automationen. Q4 i briefen berörs.
- affects: CONV-014, claude-design-watch
- recommendation: ägardelta som bekräftar nedstängningen (och därmed resolver Q4) eller återaktiverar bevakningen
- evidence: msg 6 i CONV-014 (episod CHAT-002 i paketet)
- owner_judgment_required: yes

## RQ-003
- date: 2026-08-31
- issue: Tre reversal-kandidater i nortropic-frontier-delta-lineagen ur CONV-015-deltat: (a) P1-sekvenseringen (S3→S13 utan avbrott) re-baselinerades löpande; (b) delegationsprincipen 'AI fattar inte authority-beslut' spänner mot senare max-autonomi-styrningar (msg 172/204/212); (c) D1/R1-andan (maximal extern autonomi) styrdes om i flera steg. Paketet är superseded av bevaka-frontier-ai-engineering — frågan berör efterträdarens tolkning.
- affects: CONV-015, nortropic-frontier-delta, bevaka-frontier-ai-engineering
- recommendation: hanteras vid nästa aktivering av bevaka-frontier-ai-engineering: ägardeltan som ratificerar eller förkastar respektive omsvängning; ingen brief ändras i svepet
- evidence: msg 27–48, 172, 204, 212, 226–336 i CONV-015 (episod CHAT-002 i nortropic-frontier-delta)
- owner_judgment_required: yes

## RQ-004
- date: 2026-08-31
- issue: Fyra reversal-kandidater i bootstrap-closeout-rebaseline ur CONV-016-deltat: (a) D1/D4 'rör inte pågående bootstrap / Claude förbereder separat' vs msg 78 där Claude tar över bootstrapen; (b) msg 108 flippar tillbaka ('codex tokens resettas'); (c) D5 'fetch+rebase, ingen push' vs closeout-pushar (msg 30/53); (d) D6 SUB-1-omfrysning vs senare numrering. Delar ratificerades i praktiken av ägarhandling men aldrig som uttryckliga beslut.
- affects: CONV-016, bootstrap-closeout-rebaseline
- recommendation: ägardeltan (SCOPE/ARCHITECTURE_DECISION) vid nästa aktivering som formaliserar vilka av D1/D4/D5/D6 som ändrats; jfr claude-bootstrap-takeover-protocol (nytt paket) som bär takeover-intentionen
- evidence: msg 23–56, 74–128 i CONV-016 (episod CHAT-002 i paketet)
- owner_judgment_required: yes

## RQ-005
- date: 2026-08-31
- issue: Assistant-only-kandidaten 'agentbygge-primitivkatalog' (CONV-001 msg 13–62: ~76 repos Gold Extraction till primitivkatalog) paketerades INTE — noll ägaradopterade primitiver. Rådatan är förlustfritt bevarad i källan och pekas ut som komparator-evidens i nortropic-recompile-rationalen.
- affects: CONV-001, nortropic-recompile
- recommendation: lämna som råevidens (Kernels Recompile konsumerar transkriptet); paketera endast om ägaren uttryckligen vill ha katalogen som eget evidenspaket
- evidence: msg 13–62 i CONV-001
- owner_judgment_required: yes

## RQ-006
- date: 2026-08-31
- issue: Assistant-only-trådar och paketeringspolicy: CONV-017 (brainstorma-jamforelser; ägarstyrning utan ägarbackade beslut) och CONV-002 (0 ägarmeddelanden) fick inga paket. Prejudikatspänning: agent-harness-priorities skapades tidigare ur en likadan 0-ägarmeddelande-bevakningstråd.
- affects: CONV-017, CONV-002, agent-harness-priorities
- recommendation: fastställ enhetlig policy: bevaknings-/assistanttrådar paketeras inte utan ägarbeslut i tråden; agent-harness-priorities behålls som historiskt undantag
- evidence: msg 1–9 i CONV-017; hela CONV-002
- owner_judgment_required: yes

## RQ-007
- date: 2026-08-31
- issue: Relation gold-extraction-overlay ↔ arbetsmetoder-innovation: Gold Extraction läggs uttryckligen OVANPÅ den bevarade Deep Brainstorm-definitionen (CONV-001 msg 18–21) — CONTINUE_EXISTING-episod eller distinkt paket är genuint tvetydigt; svepet levererade distinkt paket + related-länk (reversibelt).
- affects: CONV-001, gold-extraction-overlay, arbetsmetoder-innovation
- recommendation: behåll distinkt + related tills Kernel/ägare ev. mergar
- evidence: msg 16–24 i CONV-001
- owner_judgment_required: yes

## RQ-008
- date: 2026-08-31
- issue: Relation owner-attention-inte-owner-stop ↔ nortropic-organization-os: idén operationaliserar org-os-briefens D2 (~90/10-autonomi) och D10 (avvikelse förstklassig) — episod av org-os eller distinkt?
- affects: CONV-003, owner-attention-inte-owner-stop, nortropic-organization-os
- recommendation: behåll distinkt (levererad) + hantera kopplingen vid org-os-aktivering
- evidence: msg 3–13 i CONV-003
- owner_judgment_required: yes

## RQ-009
- date: 2026-08-31
- issue: Relation nortropic-evolution-foundations ↔ nortropic-organization-os: nio-lagers Organization-as-Code-designen (CONV-015 msg 112–117 + CONV-012 msg 9–18) överlappar org-os-arkitekturen; gränsen odefinierad.
- affects: CONV-012, CONV-015, nortropic-evolution-foundations, nortropic-organization-os
- recommendation: distinkt nu; gränsdragning vid aktivering
- evidence: msg 9–18 i CONV-012; msg 112–117 i CONV-015
- owner_judgment_required: yes

## RQ-010
- date: 2026-08-31
- issue: Relation corpus-control-plane ↔ innovation-inbox-idehantering (Portfolio Projection bygger nytt lager över trattens statusar) samt gräns mot project-corpus-intake — tre paket i samma korpusstyrningsdomän.
- affects: CONV-010, corpus-control-plane, innovation-inbox-idehantering, project-corpus-intake
- recommendation: distinkta nu; Kernel får föreslå merge i Recompile
- evidence: msg 1–10 i CONV-010
- owner_judgment_required: yes

## RQ-011
- date: 2026-08-31
- issue: Relation webbforvaltningen-capability-assurance ↔ gauntlet-wayfinder: challengers/falsifieringsfixturer ekar Gauntlet-kvalitetslagret — samma labb, angränsande subsystem; merge-djup oklart.
- affects: CONV-011, webbforvaltningen-capability-assurance, gauntlet-wayfinder
- recommendation: related-länk levererad; merge-frågan till aktivering
- evidence: msg 1–18 i CONV-011
- owner_judgment_required: yes

## RQ-012
- date: 2026-08-31
- issue: Relation verkstadsgolvet-v2-cockpit ↔ claude-design-watch: UI/designarbetet kan överlappa Visual Intent-paketet; osäkert.
- affects: CONV-015, verkstadsgolvet-v2-cockpit, claude-design-watch
- recommendation: ingen länk levererad; avgörs vid aktivering
- evidence: msg 118–122, 135 i CONV-015
- owner_judgment_required: yes

## RQ-013
- date: 2026-08-31
- issue: Gränsdragning nortropic-planning-wall ↔ nortropic-aquarium: båda är Verkstadsgolvet-ytor (planering/kontroll vs ambient TV-projektion); överlapp och gränssnitt odefinierade i källorna.
- affects: CONV-006, CONV-005, nortropic-planning-wall, nortropic-aquarium
- recommendation: related-länk levererad; gränssnittsdefinition är designarbete vid aktivering
- evidence: msg 1–6 i CONV-006; msg 69–79 i CONV-005
- owner_judgment_required: yes

## RQ-014
- date: 2026-08-31
- issue: Relation nortropic-recompile ↔ bootstrap-closeout-rebaseline: recompile utvecklar samma rebaseline-båge men flyttar exekveringen till Kernel (CONV-001 msg 11) — fortsättningsepisod eller distinkt evolution?
- affects: CONV-001, nortropic-recompile, bootstrap-closeout-rebaseline
- recommendation: distinkt levererad (skilda exekutorer: ägare/Claude vs Kernel); ägarens call vid aktivering
- evidence: msg 6–12, 63–76 i CONV-001
- owner_judgment_required: yes

## RQ-015
- date: 2026-08-31
- issue: WYSIWYG-staketstängningar vid capture: CONV-013 msg 217 och CONV-015 msg 160 öppnar kodstaket som källan aldrig stänger; renderarens implicita avslutare lades till per den frusna playbookens DOM-semantik. Bytesexakta råexporter bevarade i svepets arbetskatalog; transfern bevisad exakt (exportLen+JSON).
- affects: CONV-013, CONV-015
- recommendation: ingen åtgärd — dokumenterad mekanisk normalisering; auditens granskningspunkt
- evidence: msg 217 i CONV-013; msg 160 i CONV-015
- owner_judgment_required: no

## RQ-016
- date: 2026-08-31
- issue: 16 CONTINUE_EXISTING-episoder levererades till legacy-paket utan omdistillerade briefer/manifest (paketen saknar manifest; kontraktets regel är 'build one when this idea is next activated, never from guesses'). Deltan för de fem växta trådarna (CONV-005/013/014/015/016) är dokumenterade i analysunderlaget och i RQ-001–RQ-004.
- affects: CONV-005, CONV-013, CONV-014, CONV-015, CONV-016, nortropic-organization-os, bevaka-frontier-ai-engineering, claude-design-watch, nortropic-frontier-delta, bootstrap-closeout-rebaseline
- recommendation: omdistillering + manifest sker vid respektive pakets nästa aktivering (normal CONTINUE_EXISTING-flöde)
- evidence: episodfiler <slug>-full-chat-CHAT-002.md i respektive paket
- owner_judgment_required: no

## RQ-017
- date: 2026-08-31
- issue: CONV-012 har två råversioner (radartråden växte under svepet); paketepisoderna (nortropic-aquarium CHAT-002, nortropic-evolution-foundations) bygger på r1; r2:s tillägg (senare radarrapport) är obehandlat i idélagret.
- affects: CONV-012, nortropic-aquarium, nortropic-evolution-foundations
- recommendation: r2-deltat konsumeras vid nästa aktivering eller nästa svep
- evidence: revisions r1/r2 i projektmanifestet för CONV-012
- owner_judgment_required: no

## RQ-018
- date: 2026-08-31
- resolves: RQ-017
- question: Auditens FIND-001 falsifierade RQ-017:s berättelse — vad är den korrekta bilden av CONV-012:s två revisioner?
- owner_answer: none (mekanisk korrigering av svepets egen felaktiga notering, ej ägarfråga)

## RQ-019
- date: 2026-08-31
- issue: Korrigerad bild av CONV-012 (ersätter RQ-017): tråden växte INTE under svepet — r2:s enda skillnad mot r1 är transkriptbyggarens egen Syfte-rad (parafras, icke-deterministisk mellan körningar); alla 18 meddelandekroppar är byteidentiska, och msg 18 (radarrapporten) finns i r1 och ÄR behandlad av nortropic-evolution-foundations. r2 är en spuriös revision skapad av omfångst av oförändrat innehåll; rå-revisioner är orörliga och r2 kvarstår som ofarlig dubblett. Proving-run-observation: byggarens headerfält bör vara deterministiska (v3.1-kandidat, ändras INTE under frysen).
- affects: CONV-012, nortropic-aquarium, nortropic-evolution-foundations
- recommendation: ingen idélager-åtgärd; notera builder-determinism som post-freeze-förbättringskandidat
- evidence: revisions r1/r2 i projektmanifestet; auditens FIND-001 (AUDIT-29)
- owner_judgment_required: no

## RQ-020
- date: 2026-08-31
- issue: Auditens FIND-003: tio källor har inventerade men EJ innehållsfångade bilagor (endast noterade i transkripthuvudena): CONV-001 (54 st, sediment-bilder), CONV-005 (13, IMG-bilder), CONV-006 (2), CONV-007 (2, Inklistrad markdown), CONV-011, CONV-013 (5, Inklistrad text), CONV-015 (11), CONV-016 (4), CONV-022 (4, inkl. nortropic-knowledge-phase0-tgz), CONV-023-området — bilagoinnehåll är best-effort per den frusna playbooken, men luckan ska vara synlig på projektnivå, inte bara per transkript.
- affects: CONV-001, CONV-005, CONV-006, CONV-007, CONV-011, CONV-013, CONV-015, CONV-016, CONV-022
- recommendation: ägaren kan bifoga originalfiler till respektive paket vid aktivering om de är lastbärande; annars kvarstår de som icke-fångade referenser
- evidence: transkripthuvudenas bilagenoter i respektive CONV; auditens FIND-003 (AUDIT-29)
- owner_judgment_required: yes

## RQ-021
- date: 2026-08-31
- resolves: RQ-020
- question: Auditens FIND-004: RQ-020 namngav ett fantomgap (CONV-023, vars huvud säger 'Inga bilagor.') och utelämnade det verkliga (CONV-012, 'Inklistrad markdown.md') — vad är den korrekta bilagelistan?
- owner_answer: none (mekanisk korrigering av svepets egen felaktiga post; ägarfrågan omställs korrekt i RQ-022)

## RQ-022
- date: 2026-08-31
- issue: KORRIGERAD bilagelucka (ersätter RQ-020): tio källor har inventerade men EJ innehållsfångade bilagor, endast noterade i transkripthuvudena: CONV-001 (54, sediment-bild-/filreferenser), CONV-005 (13, IMG-bilder m.m.), CONV-006 (2), CONV-007 (2, Inklistrad markdown), CONV-011 (bl.a. Nortropic_100_dagar_manual_v2.3_verified.pdf), CONV-012 (1, Inklistrad markdown.md), CONV-013 (5, Inklistrad text-chips), CONV-015 (11), CONV-016 (4), CONV-022 (4, inkl. nortropic-knowledge-phase0-owner-review-tgz). Bilagoinnehåll är best-effort per den frusna playbooken; luckan ska vara ägarsynlig på projektnivå.
- affects: CONV-001, CONV-005, CONV-006, CONV-007, CONV-011, CONV-012, CONV-013, CONV-015, CONV-016, CONV-022
- recommendation: ägaren bifogar originalfiler till respektive paket vid aktivering om de är lastbärande; annars kvarstår de som icke-fångade referenser
- evidence: transkripthuvudenas bilagenoter i respektive CONV; auditens FIND-003/FIND-004 (AUDIT-29)
- owner_judgment_required: yes

## RQ-023
- date: 2026-08-31
- resolves: RQ-001, RQ-002, RQ-003, RQ-004
- question: Grupp A — hur hanteras de fyra reversal-kandidaterna (nya svansar som spänner mot tidigare briefbeslut)?
- owner_answer: Skjut till aktivering — posterna stängs med hanteringen 'hanteras med ägardeltan när respektive paket aktiveras'; inga briefer ändras nu. (Ägarval i granskningsbatch 2026-08-31: "Skjut till aktivering".)

## RQ-024
- date: 2026-08-31
- resolves: RQ-005, RQ-006
- question: Grupp B — assistant-only-material paketeras inte (primitivkatalogen förblir råevidens för Recompile; CONV-017/002 får inga paket; agent-harness-priorities behålls som historiskt undantag)?
- owner_answer: Ja, enligt rekommendation — policyn är att bevaknings-/assistanttrådar inte paketeras utan ägarbeslut i tråden. (Ägarval 2026-08-31.)

## RQ-025
- date: 2026-08-31
- resolves: RQ-007, RQ-008, RQ-009, RQ-010, RQ-011, RQ-012, RQ-013, RQ-014
- question: Grupp C — åtta relations-/gränsfrågor: behåll leveransen (distinkta paket + ömsesidiga related-länkar) och avgör merge/gränsdragning senare?
- owner_answer: Behåll som levererat — distinkt + related står; merge-frågor avgörs vid aktivering eller av Kernels Recompile. (Ägarval 2026-08-31.)

## RQ-026
- date: 2026-08-31
- resolves: RQ-022
- question: Grupp D — hur hanteras de tio källornas inventerade men ej infångade bilagoinnehåll?
- owner_answer: För denna proving-run: stäng RQ-022 och defer bilagehydrering. Inventerade bilagor ska inte blockera nuvarande sweep. Inför den slutliga optimerade Improvements-intaken/Recompile source cut ska alla fortfarande tillgängliga bilagor klassificeras; lastbärande original ska fångas och verifieras före Kernel-handoff, medan uttryckligen icke-lastbärande bilagor får lämnas som inventerade referenser. Saknad lastbärande bilaga ska redovisas som known source gap, inte döljas som komplett corpus.

## RQ-027
- date: 2026-09-01
- issue: CONV-028 r1 (Grok Bot-delta) innehåller fyra assistentsyntetiserade koncept nominerade "till Recompile" (Attention Compiler, Role Shell, Experience-to-Capability Compiler, Quiet Organization Contract) plus ADOPT/ADAPT/REJECT-tabellen. Ägaren drev tråden ("ta med oss allt guld", msg 21) men adopterade aldrig koncepten uttryckligen som Nortropic-idéer. Per den ägarratificerade policyn (RQ-024) paketeras assistentsyntes inte utan ägaradoption i tråden — därför mintades inget idépaket i det inkrementella svepet 2026-09-01.
- affects: CONV-028
- recommendation: låt materialet förbli råevidens för RND_COMPILE (som primitivkatalogen); om ägaren vill ha koncepten som egna idépaket är det ett explicit ägarbeslut vid aktivering eller före Recompile source cut
- evidence: CONV-028 r1 msg 3 (koncepten), msg 18/21 (ägarens riktningsstyrning), RQ-024 (policyn)
- owner_judgment_required: yes

## RQ-028
- date: 2026-09-01
- issue: CONV-007 r2 (msgs 102–103, 112–115) innehåller två skarpa exemplar av legitima ägarstopp (R26-värdkörningsgodkännandet med extern irreversibel effekt; H038-arkitekturvalet om OS-exklusiv cleanup-auktoritet) inklusive resonemanget "det här är den typ av stopp vi vill behålla långsiktigt". Det korroborerar owner-attention-inte-owner-stop-paketets stopptaxonomi men är exekveringshändelser, inte brainstorm. Deltat levererades INTE som episod till det paketet i det inkrementella svepet.
- affects: CONV-007, owner-attention-inte-owner-stop
- recommendation: behåll som råevidens i källan (exekveringslogg; repo-verkligheten bor i repot); om taxonomi-exemplaren bedöms designbärande vid aktivering av owner-attention-inte-owner-stop kan CONV-007 r2 då levereras som episod med ägardelta
- evidence: CONV-007 r2 msgs 102–103, 112–115; skillens regel "Implementation feedback is not brainstorm truth"
- owner_judgment_required: yes

## RQ-029
- date: 2026-09-01
- issue: Redovisning av det inkrementella svepets skip-policy (AUDIT-38 FIND-005): 19 källor (CONV-008..CONV-025 utom de återfångade, samt CONV-027) återfångades INTE 2026-09-01 utan bedömdes oförändrade via plattformens update_time-orakel (< 2026-08-31, föregående capture-dag; konservativ same-day-cutoff — alla poster med update_time ≥ 2026-08-31 återfångades, varav tre visade sig byte-identiska och blev no-ops). update_time är plattformsmetadata, inte byte-bevis; deras r1-bytes står orörda och hash-verifierade, men "oförändrad sedan 2026-08-31" vilar för dessa 19 på plattformens egen deklaration.
- affects: CONV-008, CONV-009, CONV-010, CONV-011, CONV-012, CONV-013, CONV-014, CONV-015, CONV-016, CONV-017, CONV-018, CONV-019, CONV-020, CONV-021, CONV-022, CONV-023, CONV-024, CONV-025, CONV-027
- recommendation: acceptera oraklet för inkrementella mellanrundor; inför den slutliga Recompile source cut bör samtliga källor återfångas eller byte-verifieras (i linje med den ägarbekräftade FINAL INCREMENTAL IMPROVEMENTS INTAKE-planen, CONV-001 r2 msg 115–116)
- owner_judgment_required: no
- owner_answer: none (mekanisk redovisning av svepets egen begränsning; ägarfrågan om slutlig återfångst hör till Recompile source cut-beslutet)

## RQ-030
- date: 2026-09-01
- resolves: RQ-029
- question: RQ-029 (redovisningen av det inkrementella svepets update_time-skip-policy) skrevs felformad — en issue-post utan obligatoriskt owner_judgment_required — vilket fällde validate (REVIEW_QUEUE_INCOMPLETE, AUDIT-38 FIND-007) och räknade posten som öppet ägaritem tvärtemot avsikten. Hur stängs den korrekt utan redigering?
- owner_answer: none (mekanisk stängning per RQ-021-prejudikatet; ingen ägarfråga kvarstår). Sakinnehållet i RQ-029 verifierades korrekt av den oberoende granskningen (AUDIT-38): exakt 19 källor — CONV-008..CONV-025, CONV-027 — återfångades inte 2026-09-01 utan bedömdes oförändrade via plattformens update_time-orakel (< 2026-08-31; konservativ same-day-cutoff, komplementet exakt: alla 11 poster ≥ 2026-08-31 fångades). update_time är plattformsmetadata, inte byte-bevis; de 19:s r1-bytes är orörda och hash-verifierade. Ingen ny ägarbedömning krävs nu: fullständig återfångst/byte-verifiering före Recompile source cut ingår redan i den ägarbekräftade FINAL INCREMENTAL IMPROVEMENTS INTAKE-planen (CONV-001 r2 msg 115–116).

## RQ-031
- date: 2026-09-04
- issue: CONV-013 r1:s deklarerade bilageyta motsäger dess egen kropp. Rubriknotisen deklarerar "5 bilagor inventerade (Inklistrad text 20260825–20260826, txt-chips)", men meddelande 141/149/152 namnger två YTTERLIGARE uppladdningar — `Inklistrad text.txt` 2026-08-24 19:38:58 och `Inklistrad text.txt` 2026-08-24 19:41:04 — vars datum ligger UTANFÖR det deklarerade intervallet. Den sanna okapade ytan är alltså minst 7, inte 5 (AMR-004, bekräftad mot frysta bytes). Bilagemanifestet `attachments-r1.json` beskriver nu alla sju, men motsägelsen kvarstår mekaniskt: `attachments`-kontraktet rapporterar ATTACHMENT_SURFACE_UNRECONCILED och FULL_SOURCE_CAPTURE=NO för källan. Detta kan INTE åtgärdas genom att rätta notisen: `conversation.md` är frusen r38-källa, och varje redigering — även av den härledda rubriken — bryter dess whole-file sha256 och immutabilitetsgrinden.
- affects: CONV-013
- recommendation: låt fyndet stå öppet och synligt. Bilagornas bytes är inte återvinningsbara (File Library exponerar läsbart innehåll men inte råbytes; den enda artefakt som bär innehållet, NORTROPIC_DIGITAL_MASTERPLAN_RECOVERED_2026-08-24.md, deklarerar i sitt eget manifest att den är "source-bound but not byte-identical" och får därför aldrig befordras till källa). Referensidentiteten ÄR återvunnen: File Library-id `file_00000000029881f6b64adaa932cbd86f` respektive `file_00000000824081f99f6eb3a69f4ff014`. Vid Recompile source cut avgör ägaren om en korrigerad r2-capture av CONV-013 ska göras (ny revision, gammal orörd) eller om ytan förblir dokumenterat oförenlig.
- evidence: CONV-013 r1 msg 141, 149, 152; `_projects/improvements/sources/CONV-013/attachments-r1.json`; ~/Downloads/RECOVERY_MANIFEST_NORTROPIC_DIGITAL.md. Nedströms beroende IR-poster i den icke-committade kandidaten improvements-r38-c1: RND-347, RND-190, RND-191 (nämnda som prosa — `affects` tar bara CONV-id och paketslugar).
- owner_judgment_required: yes

## RQ-032
- date: 2026-09-04
- resolves: RQ-031
- question: RQ-031 lade fram CONV-013:s deklarerade-mot-observerade motsägelse för ägarbedömning. Frozen r1 deklarerar 5 bilagor; oberoende bevis i samma frysta källa fastställer minst 7; den frysta källan får inte redigeras; den fullständiga historiska bilageytan är inte återvinningsbar ur nuvarande capture. Hur avslutas posten utan att vare sig redigera vittnet eller låtsas att luckan är lagad?
- owner_answer: ERKÄNNANDE, INTE LÖSNING. Ägaren erkänner motsägelsen som en känd, olöst historisk källyte-lucka och accepterar att den ska FÖRBLI olöst. Ägaren adjudicerar uttryckligen INTE att CONV-013 har exakt 7 bilagor — bevisen fastställer 5 deklarerade och minst 7 observerade, inget mer. Erkännandet finns till för att en sanningsenlig korpus ska kunna vara strukturellt frisk utan att påstå att den underliggande källuckan är reparerad. Det får inte ändra den frusna r1-konversationen, inte skriva om 5 till 7 i den gamla källan, inte hävda ett exakt historiskt antal bortom bevisen, inte göra CONV-013 till FULL_SOURCE_CAPTURE=YES, inte göra ATTACHMENT_SEMANTIC_R38 till PASS, inte göra FINAL_IMPROVEMENTS_CORPUS_QUALIFIED till YES, och inte dämpa eller nedgradera fynden om otillgängligt material. Resulterande semantik: DECLARED_ATTACHMENTS=5, OBSERVED_ATTACHMENT_EVIDENCE>=7, RECONCILIATION=KNOWN_UNRESOLVED, FULL_SOURCE_CAPTURE=NO. En ägare får erkänna att en historisk bevislucka måste bestå; en ägare får INTE få saknade historiska bevis att existera genom beslut. Mekaniskt representerat i `_projects/improvements/sources/CONV-013/attachments-r1.json` under `owner_acknowledgement`, som kontraktet vägrar acceptera om den försöker påstå mer än detta.
