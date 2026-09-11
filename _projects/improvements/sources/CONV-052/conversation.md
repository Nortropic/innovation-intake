# Brainstorma Agentic OS — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Brainstorma Agentic OS
**URL:** https://chatgpt.com/c/6a9b0652-9764-83eb-81b8-45e2b03047ab
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 4 (1 användare, 3 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”Brainstorma https://www.instagram.com/raycfu?igsi=ODZ3YTI1eHdja21y” och avslutas med: ”You've reached your limit of 20 active tasks. To schedule more tasks, consider pausing some tasks.”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 0 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

---

## Meddelande 1 — Johnny (användare)

Brainstorma https://www.instagram.com/raycfu?igsi=ODZ3YTI1eHdja21y

---

## Meddelande 2 — ChatGPT (assistent)

Jag gör samma typ av **Nortropic-radar** här: först identifierar jag vad @raycfu faktiskt bygger/tänker kring, sedan separerar jag **inspiration från verifierbara mönster**, och till sist översätter jag guldkornen till sådant som kan påverka Nortropic, Digitala eller vår framtida recompile.

---

## Meddelande 3 — ChatGPT (assistent)

Den här träffar Nortropic **ovanligt väl**. Jag kunde inte på ett pålitligt sätt läsa hela Instagram-flödet direkt, men @raycfu har ett eget guidebibliotek som verkar vara långformsvarianten av samma innehåll. Där finns just nu material om agent-team, software factories, loop engineering, graph engineering, skills, persistent knowledge, Paperclip-liknande AI-organisationer och en hel guide om ett “Agentic OS”. citeturn920103view0turn494599view0

Min första klassificering blir därför: **Ray Fu bör vara discovery radar för Nortropic, inte authority source.** Han är bra på att paketera nya agentiska mönster till konkreta konstruktioner snabbt. Men många guider är pedagogiska förenklingar och ibland marknadsföringsdrivna. Guldet ligger därför mindre i hans exakta prompts och mer i vilka mönster han upptäcker, kombinerar och gör operativa. Där bör vi sedan gå till ursprungskällan och verifiera.

**Det mest slående är hans “Agentic OS”.** Hans system har en constitution, ett autonomy contract med “acts alone / queues for me / wakes me up”, en triage-funktion, en stark conductor som inte implementerar, billigare workers, en färsk separat verifierare, worktrees, ett deterministiskt `verify.sh`, ett trust ledger och stående mål som återkontrolleras över tid. citeturn968906view0turn968906view1

Det är nästan en förenklad kusin till det vi har byggt.

Men det viktiga är **inte** att dra slutsatsen att vi borde kopiera det. Tvärtom ger det oss ganska stark extern convergence evidence för flera av Nortropics redan framväxta idéer. Nortropic har gått djupare på exempelvis authority, confinement, candidate/verifier-separation, fail-closed-beteende och på att inte låta en prompt vara den egentliga säkerhetsgränsen. Ray uttrycker exempelvis “never touch X” i `CLAUDE.md`; Nortropic försöker göra “kan inte touch X utan rätt capability/authority” till en verklig systemsanning. Den skillnaden är enorm.

Samtidigt finns det flera saker hos honom som jag tycker att vi faktiskt kan lära oss av.

Den första är **earned autonomy som en explicit produktmekanism**. Ray har ett trust ledger där ett skill får mer autonomi när det har tillräckligt många lyckade verifierade körningar, och degraderas när kvaliteten försämras. Hans exakta regel, exempelvis 20 körningar och 95 procent, är alldeles för naiv som generell Nortropic-policy. Men principen är stark: autonomi kan vara något en capability **kvalificerar sig till empiriskt**, i stället för något vi manuellt konfigurerar en gång. citeturn968906view2

För Nortropic skulle jag tänka mer:

`unproven → supervised → verified → bounded autonomous → trusted autonomous`

men baserat på flera dimensioner: verifieringsstyrka, riskklass, reversibilitet, recency, sample size, failure severity och eventuell distributionsförändring. En capability som gjort 500 perfekta bildoptimeringar säger ingenting om dess rätt att ändra betalningslogik.

Det här känns väldigt nära vår framtida **Profession Qualification**. En förvaltning blir inte “autonom” för att vi säger att den är det. Den tjänar ihop självständighet genom evidence.

Den andra stora träffen är **standing goals**. Ray skriver i princip att ett mål som bara verifieras en gång är “an assumption with a timestamp”, och låter därför mål leva vidare som predicates som återtestas. citeturn968906view1

Det där tycker jag är ett riktigt guldkorn för Organization OS.

Vi har tänkt mycket:

`task → verification → done`

men organisationell verklighet är ofta:

`något blev sant → det måste fortsätta vara sant`

Till exempel att produktionen fortfarande fungerar, att en säkerhetsinvariant fortfarande gäller, att Digitalas kvalitetsbaseline fortfarande hålls, att en integration fortfarande fungerar eller att en kunds kritiska SLO inte har försämrats.

Jag skulle dock dela det i två koncept. **Standing invariants** är saker som faktiskt kan vara PASS/FAIL och kontinuerligt bevakas. **Outcome objectives** är saker som “öka qualified leads” eller “gör Digitala bättre”, där sanningen är statistisk och utvecklas över tid. Vi ska inte göra misstaget att försöka uttrycka hela företagets mål som shell commands.

Den tredje träffen är **graph engineering**, och här tror jag faktiskt att vi hittar något direkt användbart för hur Nortropic arbetar. Ray beskriver arbeten som noder och dependencies som edges, men har ett bra enkelt test: om output från A faktiskt inte behövs av B är kanten falsk och arbetet behöver inte vänta. Han lägger dessutom en checker mellan parallella fan-outs och convergence så att en dålig parallell output inte smälter in osynligt i slutsyntesen. citeturn753569view3turn753569view4

Det passar perfekt med både Kernel och vårt kommande Improvements Recompile.

Vår tidigare modell har varit ungefär multipass compilation. Ray lägger ett extra perspektiv ovanpå den:

`dependency graph → remove fake edges → parallel fan-out → independently check outputs → converge`

Det betyder att Recompile inte bara bör vara context-optimerad. Den kan också bli **dependency-optimerad**.

Och på sikt tycker jag detta pekar mot att Nortropics scheduler inte främst ska tänka “vilken agent kommer härnäst?” utan:

> Vilka verkliga dependencies finns just nu, och vilket arbete är eligible att starta samtidigt?

Det är mycket mer Organization OS än en agentkedja.

Den fjärde träffen är hans **“clone yourself”**-modell. Formuleringen gillar jag mindre, men processen är bra: kartlägg återkommande arbete, bedöm repeatability kontra human judgment, intervjua människan tills även tacit knowledge kommer fram, extrahera det till en skill, testa skillen mot riktiga uppgifter och korrigera skillfilen utifrån gapen. citeturn753569view2

Här tycker jag att Nortropic kan göra något mycket starkare.

För vår framtida organisatoriska Intake — precis den typ av undersökning vi skickade till Viktor — kan vi mäta minst fyra saker:

| Dimension | Fråga |
|---|---|
| Repeatability | Hur återkommande och strukturerat är arbetet? |
| Judgment | Hur mycket genuint mänskligt omdöme krävs? |
| Verifiability | Hur starkt kan ett korrekt resultat bevisas? |
| Risk / reversibility | Vad händer om systemet har fel? |

Då får Nortropic inte bara ett formulär om “vad företaget gör”. Det får ett **capability-discovery instrument**.

Det skulle kunna upptäcka:

> den här processen bör automatiseras direkt  
> den här bör bli human+AI  
> den här kräver bättre verifiering innan autonomi  
> den här bör förbli mänskligt owner judgment.

Det är i princip embryot till en riktig **Profession/Capability Foundry**.

Den femte träffen är hans software-factory-material. Han separerar researcher, story writer, project manager, backend, frontend, test verifier och validator för att skydda context och hindra samma modell från att skapa och godkänna sina egna antaganden. Hans enklare builder/checker-loop använder samma idé och kräver dessutom exakta failure reports, hårda stop rules och förbjuder buildern att försvaga tester. citeturn920103view1turn753569view0turn753569view1

Här skulle jag däremot **inte ta hans agentstruktur**.

Det vore lätt att se detta och tänka:

`Research Agent → PM Agent → Backend Agent → Frontend Agent → Test Agent`

och därmed hårdkoda en artificiell personalstyrka.

Nortropics starkare variant är:

`required capabilities → eligible workers → task-specific graph → ephemeral execution`

“Researcher” är då en **seat/capability**, inte nödvändigtvis en permanent person. Ett uppdrag kanske behöver två research-capabilities och ingen PM. Ett annat behöver security analysis + browser evaluation + frontend building. Organisationen formas efter jobbet.

Den sjätte träffen är kanske den mest spännande på lång sikt: **Karpathy-looparna och bilevel autoresearch**. Ray har tagit upp generator/verifier/memory-loopen och därefter bilevel-modellen där en yttre loop inte gör arbetet själv utan analyserar hur den inre loopen söker efter förbättringar och ändrar sökstrategin utan att få ändra själva måttet på framgång. citeturn133152view0turn133152view1

Den här gången går det dessutom att verifiera mot primärkällorna. Karpathys `autoresearch` använder ett litet, låst upplägg där agenten modifierar `train.py`, evaluationen ligger utanför dess kontroll och `program.md` styr experimenteringen. citeturn123781search0turn123781search7 Den efterföljande Bilevel Autoresearch-preprinten beskriver en outer loop som optimerar **hur** inner loop söker, och rapporterar ungefär fem gånger större förbättring på just den testade Karpathy-benchmarken. Författarna och Ray är också tydliga med att det är ett begränsat resultat, inte ett universellt 5×-löfte. citeturn956182academia36turn956182search4

Det där kan på sikt bli Nortropics **Level 3 learning**:

`arbete → förbättra capability → förbättra hur capabilityn förbättrar sig`

Men med en konstitutionell gräns:

> Meta-loopen får förändra search strategy, playbooks och experiments — **inte authority, verifierns definition eller vad som räknas som framgång.**

Det är väldigt Nortropic.

Sedan har vi kunskapsdelen. Ray återger Karpathys LLM Wiki-idé: råkällor hålls immutabla, medan en AI-underhållen derived wiki kontinuerligt assimilerar nya källor, uppdaterar koncept, markerar konflikter och gör kunskapen kumulativ. citeturn494599view2 Karpathys original beskriver explicit tre lager: immutable raw sources, LLM-maintained wiki och ett schema som styr hur den kompileras och underhålls. citeturn783505view0

Detta är nästan exakt den epistemiska arkitektur vi har börjat landa i för Improvements:

`RAW CORPUS ≠ CURRENT KNOWLEDGE`

utan:

`immutable evidence → compiled current knowledge → recompile when world/model/system changes`

Det stärker mig i att vår Improvements Recompile inte är överbyggd. Tvärtom ser vi en bredare convergence mot **knowledge as a maintained compiled artifact** snarare än bara retrieval.

Och slutligen finns Paperclip-spåret. Ray lyfter ett UI med org chart, tasks, budgets, heartbeats, audit trails, approval gates och mission traceability. citeturn494599view1 Det är mycket relevant som **Aquarium/Verkstadsgolvet-inspiration**, men vi ska hålla fast vid vår viktigaste skillnad: UI:t får aldrig bli organisationens source of truth. Paperclip-liknande visualisering är intressant; Paperclip-liknande “dashboard database = organization” är inte nödvändigtvis vår modell.

Så min syntes av hela @raycfu är ungefär:

> **Han bygger pedagogiska minibitar av många saker som Nortropic försöker förena till ett riktigt system.**

Software factory. Skills. Agent teams. Routing. Independent verification. Trust. Work graphs. Persistent knowledge. Organizational dashboards. Autonomous loops. Meta-improvement.

Hos honom är de ofta separata guider.

Hos Nortropic borde de, där evidensen håller, bli **olika manifestationer av samma få primitives**.

Det gör kontot mycket mer intressant än ännu en “10 prompts that change your life”-profil.

Jag skulle definitivt lägga @raycfu i vår **high-signal discovery radar**, och framför allt markera fem teman för Recompile-korpuset: `earned autonomy`, `standing goals`, `dependency/fake-edge graph optimization`, `process → capability qualification` och `bilevel capability evolution`. Däremot skulle jag **inte ändra Bootstrap nu** utifrån detta. De flesta kärnidéerna bekräftar snarare riktningen vi redan tagit; guldet bör assimileras som external evidence och vägas ordentligt i Recompile i stället för att skapa ännu en sidoförgrening precis innan Kernel är klar. memcite

genui{"suggest_automation":{"label":"Bevaka @raycfu för nya agent- och OS-mönster"}}

---

## Meddelande 4 — ChatGPT (assistent)

You've reached your limit of 20 active tasks. To schedule more tasks, consider pausing some tasks.

