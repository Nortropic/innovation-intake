# Bedöm backloggens aktualitet — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Bedöm backloggens aktualitet
**URL:** https://chatgpt.com/c/6a8f256f-2aec-83eb-9d75-bf1476a2c03e
**Exportdatum:** 2026-08-31
**Antal meddelanden:** 18 (9 användare, 9 assistent)
**Syfte:** Bedömning av 100-dagarsbackloggens aktualitet mot nuvarande Webbförvaltning samt design av en framtida Capability Assurance-audit.

**Innehåll i korthet:** Samtalet öppnar med: ”Kopplat till webbförvaltningen som vi nuvarande uppdaterar allt på, detta var backloggen som vi skulle jobba på, är den fortfarande aktuell?” och avslutas med: ”Ja. **Nu tycker jag att vi är redo att sluta brainstorma brett och börja planera implementationen.** Vi har fått med de variabler jag hade velat ha innan vi fryser riktningen: gaml”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 1 bilagor inventerade (Nortropic_100_dagar_manual_v2.3_verified.pdf); innehållet ej infångat i svepet.

---

## Meddelande 1 — Johnny (användare)

Kopplat till webbförvaltningen som vi nuvarande uppdaterar allt på, detta var backloggen som vi skulle jobba på, är den fortfarande aktuell?

---

## Meddelande 2 — ChatGPT (assistent)

Ja — **men med en viktig distinktion**:

> **100-dagarsbackloggen är fortfarande mycket relevant som krav-, kontroll- och täckningsbacklogg. Den är däremot inte längre den aktiva exekveringsplanen för Webbförvaltningen.**

Det är faktiskt förenligt med manualen själv. Den är daterad **2026-07-29**, bygger på den historiska baslinjen `1aa1394…`, och säger uttryckligen att dagens repo/runtime måste **rebaselinas före implementation**. Den säger även att `NO-OP VERIFIED` är rätt utfall när dagens implementation redan löser uppgiften lika bra eller bättre. fileciteturn2file1

### Vad som har hänt sedan dess

Den nya DESIGN-FRUSNA Webbförvaltningen-masterplanen från 24 augusti har i praktiken **absorberat och vidareutvecklat** 100-dagarsplanen. Den sätter dessutom en tydlig auktoritetsordning: aktuell publicerad repo-verklighet först, därefter den frusna exekveringsplanen; äldre dokument och utkast får inte styra över senare implementerad sanning. fileciteturn3file4

Det är en ganska stor arkitektonisk evolution. Den gamla manualen utgick fortfarande mycket från en småföretags-/lokalservicefabrik med arketyper. Den nya planen säger i stället:

**vilken legitim webbkund som helst → förstå verksamhet/användare/mål → upptäck nödvändiga capabilities → skapa Site Quality Contract → välj rätt kompetens → bygg → verifiera → lansera → observera verkligheten → lär systemet.**

`lokal-se` blir då **första capability packet**, inte själva universella arkitekturen. Den introducerar också capability catalog, Site Quality Contract, Reality Layer, kunskapsbanan, professionell kompetens/Gym och senare Digital Department. fileciteturn2file0

Och jag kontrollerade även **dagens publicerade `main`**. Den står nu på `9ace2fb64c6760f641b28dbb7b15ee904627a051`, där PR #138 precis landat med **v4-rubrikens UTKAST som challenger / NOT_PRODUCTION**. Det är exakt den typ av triggerstyrd utveckling som den nya masterplanen föreskriver. fileciteturn14file0L1-L10

Vi har dessutom redan hunnit landa stora delar av den nya banan: S1-min/K4, research contract v3, S2-intake i Verkstadsgolvet, S3 planner/capability catalog/interventionsbeslut, S4 Site Quality Contract, K0–K3, S5-grindparameterisering samt de senare S9–S12-förbättringarna. Så att nu börja köra PDF:n som **Dag 1 → Dag 100** skulle både duplicera arbete och i vissa fall dra oss tillbaka till äldre arkitektur.

Jag skulle därför se relationen så här:

| 100-dagarsmanualen | Roll idag |
|---|---|
| Säkerhet, fail-closed, permissions, supply chain, injection, isolation | **Fortfarande bärande krav** |
| Control plane, resume, release, autonomy | **Till stor del flyttat till/separerat från Full Autonomy Bootstrap** |
| Research, design, evals | **Fortfarande centralt men ombyggt till S/K/Gym + capability packs + Quality Contract** |
| Browser, a11y, prestanda, CI | **Fortfarande centrala kvalitetskrav** |
| Migration, juridik, handover, Care/Growth | **Fortfarande mycket relevanta framtida/livscykelkrav** |
| Obsidian, NotebookLM, externa MCP:er, lokal LLM osv. | **Inte automatiska backlog-items längre; kandidat/trigger/named-consumer först** |
| Red-team, restore, readiness, jämförelse mot baseline | **Fortfarande slutbevis för mognad** |

Det sista är viktigt: vi ska **inte kasta manualen**. Den innehåller väldigt mycket som vi absolut inte vill råka tappa — exempelvis migration, faktagodkännande, användartestning, WCAG, restore, cross-client isolation, Care/Growth och oberoende slutgranskning. På första sidan beskriver den också just hela kedjan från stabilisering till Care och slutlig red-team/certifiering, vilket fortfarande är en bra coverage-modell. fileciteturn2file1

Min rekommendation är därför att behandla den som:

> **`LEGACY_REQUIREMENTS_AND_COVERAGE_SOURCE`**

medan:

> **aktuell repo-verklighet + den DESIGN-FRUSNA Webbförvaltningen-masterplanen = `ACTIVE_EXECUTION_AUTHORITY`.**

Och innan vi någon gång säger **“Webbförvaltningen v1 är färdig”** bör vi göra en sista mekanisk reconciliation mot hela 100-dagarsmanualen: varje gammal Dag 1–100 klassificeras som **IMPLEMENTED / SUPERSEDED / STILL REQUIRED / DEFERRED / SEPARATE_BOOTSTRAP**. Då får vi det bästa av båda världarna: **vi följer den nya mycket bättre arkitekturen utan att en enda bra idé från den gamla backloggen tappas bort.**

Så: **ja, backloggen är fortfarande aktuell — men den har blivit en coverage/backstop, inte vår kölista. Den nya masterplanen är dess evolution.**

---

## Meddelande 3 — Johnny (användare)

så om du går igenom hela planen 1 och 1 och jämför mot nuvarande?

---

## Meddelande 4 — ChatGPT (assistent)

Ja. Jag har nu gjort den jämförelsen på det sättet: **alla 100 dagar i originalmanualen, en efter en, mot den publicerade verkligheten i Nortropic just nu**.

Jag låser jämförelsen till `nortropic-system/main @ 49d0662429909b2071a3c26a3d6327a64d23bd65` och `verkstadsgolvet/main @ f10ef634d3699297e8c495b7a39b67c736947cb3`. Det är viktigt eftersom systemet rör sig snabbt. `nortropic-system`-SHA:n är dessutom nyare än den jag tittade på i mitt förra svar. fileciteturn20file0L1-L10 fileciteturn50file0L1-L10

Manualen själv säger att dess 2026-07-29-baslinje inte får behandlas som bevis för dagens runtime och att `NO-OP VERIFIED` är rätt resultat när dagens system redan löst ett steg lika bra eller bättre. Det är exakt den princip jag använder här. fileciteturn0file0

**Statusnyckel:** ✅ = målet är materiellt motsvarat; 🟡 = delar finns men gamla exitkriteriet är inte bevisat; 🔵 = den gamla lösningsformen har ersatts av en bättre nuvarande arkitektur; 🟣 = hör numera huvudsakligen hemma i Trust Kernel/Full Autonomy Bootstrap, inte Webbförvaltningen; ⚪ = triggerstyrt/senare, inte något vi bör bygga nu utan behov; 🔴 = verklig kvarvarande lucka.

---

## Fas 1 — Dag 1–10: Stabilisera kärnan

Den här fasen har påverkats enormt av allt bootstrap-/Foundation-arbete. Nuvarande system har bland annat repo-native identitet, en stor mekanisk kontrollapparat, fail-closed kontrakt, obemannat beslutssystem och vaktankare. Samtidigt finns fortfarande konkreta luckor i agentpermissions och extern-data-isolering. Root-`AUTOPILOT` är fortfarande `off`. fileciteturn22file0L1-L2 fileciteturn37file0L1-L6

| Dag | Ursprungligt steg | Dom nu | Jämförelse mot dagens system |
|---:|---|---|---|
| **1** | Frys en verifierbar baslinje | ✅ | Genomfört historiskt och dessutom långt överträffat av senare SHA-/tree-/candidate-/gate-frysning. **Ska inte göras om som D001.** Däremot behöver slutlig Webbförvaltningen-v1 få en ny releasebaslinje. |
| **2** | Inventera verklig runtime och trust boundaries | 🟡 | Stor inventering har skett genom Foundation/Bootstrap, men manualens krav gäller **effektiv runtime vid aktuellt tillfälle**. Plugins, MCP, permissions, credentials och laddningsprecedence bör därför få en slutlig aktuell reconciliation före v1. |
| **3** | Gör launchresultatet atomärt | ✅ | Detta är ett av de tydligaste avslutade områdena. Launch har freshness-grind, bounded fixloop och ett final sweep som kör om de icke-juridiska grindarna efter fix mot färsk preview. Det är NRT-001:s moderna lösning. fileciteturn33file0L1-L2 |
| **4** | Gör autobygg fail-closed och färsk | ✅ | Autobygg har nu explicit `CONTINUE / ATTENTION_CONTINUE / ROUTE / HARD_STOP`, oklassificerade utfall stoppar och S12 gör obemannat till default utan att låta felaktigt läge bli en autonom gissning. |
| **5** | Isolera writers och separera release | 🟡 | Trust Kernel har gått mycket längre med `allowed_write`, containment och candidate identity. Men kundbyggflödet är inte helt samma sak: exempelvis finns fortfarande en skyddad `git add -A`-kedja i scaffold-kontraktet. Därför är det gamla målet inte helt stängt för **kundwriters**. fileciteturn35file0L1-L2 |
| **6** | Skapa ett enda lead- och pulskontrakt | 🟡 | Lead semantics är betydligt mognare: env-styrd mottagare, honeypot, elapsedMs, riktig delivery-testning och puls finns. Men jag hittar inte det gamla målets **ett maskinläsbart lead-contract som är ensam gemensam källa för implementation + test + gate**. |
| **7** | Gör agentroller tekniskt sanna | 🟡 | Förbättrat men **inte klart enligt manualen**. Design-reviewer saknar Bash, men har fortfarande `Skill` och `memory: user`; `qa-launcher` har fortfarande både `Bash` och `Skill`. Den gamla ambitionen var tekniskt snävare. fileciteturn26file0L1-L6 fileciteturn40file0L1-L6 |
| **8** | Frys supply chain före exekvering | 🟡 | Vendoring och exakta web-quality-versioner är starkt utvecklade. Men jag ser inte ett komplett centralt `vendor-manifest.json` för **hela** exekveringsytan med samma ceremony som manualen beskrev. |
| **9** | Karantänisera opålitlig text | 🟡 | Regeln “extern data är inte instruktioner” och många mekaniska gränser finns. Men manualens rena **reader → schema → policy → minimal FixTask → action-agent**-separation är inte fullt materialiserad över web/PDF/SVG/MCP. |
| **10** | P0-red-team och bemannat GO/NO-GO | 🟡 | Enorma mängder adversariell verifiering har genomförts. Men det finns inte ett aktuellt sammanhållet `P0-CLOSURE-REPORT` på **dagens main** som återprövar hela gamla P0-mängden. Gör detta som v1-closure, inte som gammal D010. |

### Fas 1-dom

**Mycket av säkerhetsfundamentet är byggt, men Dag 7–9 ska inte försvinna ur den nya backloggen.**

Särskilt Dag 7 är intressant, för den gamla manualen såg faktiskt något vi fortfarande kan se idag: dokumenterad “read-only” och **faktisk verktygsbehörighet** är inte riktigt samma sak.

---

# Fas 2 — Dag 11–20: Kontrollplanet

Här är förändringen ännu större. Den gamla manualen ville bygga mycket av det som sedermera blev **Full Autonomy Bootstrap / Provider-Neutral Trust Kernel**. Det ska alltså absolut **inte byggas igen inne i Webbförvaltningen**.

Nuvarande ägarkontrakt är explicit: provider harness äger sessioner, reasoning, tool loops och interna retries; Nortropic äger Task IR, write policy, containment, candidate SHA, verifier identity, attestation, stale/fencing, recovery och promotion. fileciteturn29file0L1-L6

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **11** | Definiera fabrikens state machine | 🟣 | Principen har flyttat ner i Trust Kernel/task authority. Bygg **inte** ett nytt webbspecifikt parallellt workflow-state-machine-lager. |
| **12** | Standardisera alla workflowoutputs | 🟣 | Provider-neutral structured results + TaskContract är den moderna lösningen. Kundworkflows har dessutom schemas. Det gamla generella resultatkontraktet bör absorberas, inte dupliceras. |
| **13** | Inför NORTROPIC-RUN och append-only events | 🟣 | Den exakta filformen är ersatt. Kontrollplanet har faktiskt `events.jsonl` som sanning + `state.db` som projektion och kan rebuilda enbart ur eventloggen. Det är kärnan av D013, fast med bättre ansvarsfördelning. fileciteturn44file0L1-L6 |
| **14** | Ersätt LLM-parsning med deterministiska parsers | 🟣 | Väldigt mycket av detta är gjort i Trust Kernel och senare Webbförvaltningen-vakter. Den senaste utvecklingen har rentav byggt parse-gate och source-anchored guards. |
| **15** | Bygg en central policy engine | 🟣 | `allowed_write`, denied surfaces, authority, containment och frozen verification är nu Trust Kernel-ansvar. Ett nytt generellt web-policy-engine vore fel lager. |
| **16** | Bygg en deterministisk release runner | 🔵 | Delad i två bättre saker: Trust Kernel äger promotion/main-transition för systembygget, medan **kundens produktion fortfarande är mänsklig**. Vi ska inte återinföra ett agentägt releasekommando bara för att gamla D016 sa det. |
| **17** | Gör körningar återupptagbara | 🟣 | Bootstrapen äger resume/recovery och build-autopiloten har explicit resume. Detta är inte längre en Webbförvaltningen-feature. |
| **18** | Standardisera timeout, retry och idempotens | 🟣 | Provider-interna retries ligger hos providern; Nortropic äger bounded cross-attempt retries/fingerprints. Exakt den ansvarssplitten står i dagens Trust Kernel-kontrakt. |
| **19** | Skriv backup-, restore- och incidentrunbooks | 🟡 | Mycket restore/recovery-arbete finns i kontrollplanet och historiska arkiv, men manualens hela “system + kund + credentials + verklig restore drill”-exit är inte slutbevisad. |
| **20** | Fault-injection av kontrollplanet | 🟣 | Bootstraparbetet har gjort omfattande adversarial/failure testing. Den moderna slutgrinden bör vara Bootstrapens empiriska unattended closeout, inte en separat D020-implementation. |

### Fas 2-dom

Det här är den tydligaste delen att **ta bort från Webbförvaltningens aktiva backlogg**.

Inte för att den var dålig, utan för att den **redan födde ett bättre system**.

---

# Fas 3 — Dag 21–30: Mätbarhet, CI och QA

Här hittar jag däremot några av de **största riktiga kvarvarande hålen**.

Det finns redan mycket stark lokal mekanisk verifiering — dagens README räknar upp ett stort antal egna kontrollskript och systemet har precis fått externa vaktankare. Men `.gitignore` tillåter inte ens `.github/` som spårad systemyta, och den aktuella branch-protection-responsen visar inga required status checks. fileciteturn22file0L1-L2 fileciteturn30file0L1-L6 fileciteturn20file0L1-L10

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **21** | Aktivera dataminimerad OpenTelemetry | 🔴 | Jag hittar ingen aktuell OTel-implementation i repot. Kunskaps-/kompetenslagret är **inte** samma sak. |
| **22** | Bygg grundläggande CI för systemrepot | 🔴 | Mekaniska lokala vakter finns i mängd, men ingen GitHub Actions-CI motsvarande manualens mål. |
| **23** | Secret- och dependency-supply-chain-kontroller | 🟡 | Secret guards, vendoring och pinnade verktyg finns. Men dependency review/SBOM/push protection/repo-CI motsvarande D023 är inte komplett. |
| **24** | CodeQL och statisk säkerhetsanalys | 🔴 | Ingen CodeQL/Semgrep-pipeline motsvarande D024 syns i aktuell main. |
| **25** | Sammanför doctor och verify till ett registry | 🟡 | Systemet har doctor/verify + en stor familj kontrollskript, men inget enda `checks/registry.json` som äger alla kontroller och genererar konsumenterna. |
| **26** | Enhetstesta guards och policies | ✅ | Här är dagens system **klart starkare än manualens ursprungliga mål**: table-driven, negativa, adversariala och mutationstester används mycket aktivt. De senaste committerna visar hur nya guards själva falsifieras. |
| **27** | Playwright-harness över browsers | 🟡 | Playwright finns i QA-flödet, men jag ser inte en versionerad Chromium + Firefox + WebKit + mobilmatris som reproducerbar CI-harness. fileciteturn47file0L1-L5 |
| **28** | Visuell, ARIA och a11y regression | 🟡 | Axe är nu mycket starkt: pinnad runner, fail-closed och manuell accessibility. Men visual diff + stabila ARIA snapshots/baselines är inte fullt byggt. |
| **29** | Härda bild- och SVG-pipelinen | 🟡 | `nortropic-bild` och `brand.mjs` finns och området har härdats, men jag skulle inte ge hela gamla D029 EXIT=PASS utan en direkt negativtest-reconciliation av timeout/bytes/MIME/SVG/provenance. fileciteturn49file0L1-L5 |
| **30** | Gör CI och branch protection till releasegrind | 🔴 | `nortropic-system/main` är protected, men required status checks är inte på. Verkstadsgolvet är inte ens protected i den avläsningen. D030:s verkliga mål är därför **inte uppfyllt**. |

### Fas 3-dom

Det här är **inte gammal skuld vi ska ignorera**.

Jag skulle bära fram **21–24 och 30** som riktiga moderna backlog-items.

---

# Fas 4 — Dag 31–40: Research och design

Här är det blandat. **Researchdelen har blivit mycket bättre än originalplanen. Designdelen har inte gjort samma resa ännu.**

Researchkontraktet är nu v3.1.0, pinnat, fail-closed och universellt: 17 stabila sektioner plus capability packets. Det är ett stort steg framåt från den gamla manualens tänkta schema. fileciteturn32file0L1-L2

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **31** | Versionera ett rikare researchkontrakt | ✅ | **Överträffat.** Research Contract v3.1.0 + universalitetslag + packet-komposition + pinning är bättre än gamla D031-formen. |
| **32** | Bygg strukturerad kundonboarding | 🟡 | Verkstadsgolvet har S2-intake med de nya fältgrupperna och pakethypotes/read-only projektförståelse. Men full kedja till `CLIENT-ANSWERS`, rights/assets och deterministiskt research-output är inte bevisad. |
| **33** | FACT-LEDGER och ASSET-LEDGER | 🔴 | Jag hittar inte dessa artefakter i aktuell repo-verklighet. Idén är fortfarande stark och blir dessutom viktig för Care senare. |
| **34** | Fastställ källnivåer för designinspiration | 🟡 | Det finns ett tydligt nuvarande inspirationsregister med SiteInspire, Land-book, Mobbin, GoodUI, Baymard osv. Men den gamla planens mer formaliserade provenance/evidensroll per referens är inte fullt genomförd. fileciteturn53file0L1-L6 |
| **35** | Skapa reference-card-kontraktet | 🔴 | Inget `reference-card` hittas. Idén är fortfarande relevant, men bör förenas med dagens Site Quality Contract i stället för att bli en parallell sanning. |
| **36** | Bygg Nortropic Reference Compiler | 🔴 | Ingen Reference Compiler/REFERENCE-PACK finns ännu. Detta är fortfarande en av de mer intressanta kvarvarande designkapabiliteterna. |
| **37** | Inför mänskligt designgodkännande | 🟡 | Briefens designriktning godkänns av människa vid nod 3. Men ingen separat hashbunden `DESIGN-APPROVAL` motsvarande D037. |
| **38** | Konsolidera designkanonen | 🔴 | **Tydligt inte gjort.** Nuvarande design-reviewer beordras fortfarande att ladda alla: `web-design-guidelines`, `ui-ux-pro-max`, `taste`, `impeccable`, `soft-skill`, `emil-design-eng`, `find-animation-opportunities`, `frontend-design`. Detta är nästan exakt den överlappning D038 skulle avveckla. fileciteturn26file0L1-L6 |
| **39** | Routa design- och techskills explicit | 🟡 | Motion och vissa techval routas redan efter behov, men design-reviewern har fortfarande bred permanent kanon. D039:s princip är alltså bara delvis införd. |
| **40** | Pilotera Reference Compiler och reducerad kanon | 🔴 | Kan inte göras ordentligt innan 35–39 är klara. |

### Fas 4-dom

Här hittade vi något viktigt:

> **D35–40 är fortfarande mycket aktuell backlogg.**

Det nya Webbförvaltningsbygget har avancerat research-, capability- och quality-contract-sidan kraftigt, men **design intelligence-lagret är fortfarande betydligt mer legacy**.

---

# Fas 5 — Dag 41–50: Produktifiera bygggolvet

Dagens system har en stark `nortropic-stack`, Site Quality Contract och capability catalog. Men det har **inte** byggt den gamla planens separata starter-/modulprodukt rakt av. Det är delvis bra — capability-arkitekturen är bättre än ett stort generiskt modullager. fileciteturn35file0L1-L2 fileciteturn36file0L1-L6

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **41** | Designa `nortropic-starter` | 🟡 | Ett mycket detaljerat stack/scaffold-kontrakt finns, men inget separat versionerat `nortropic-starter`-repo. |
| **42** | Bygg starterkärnan | 🟡 | Många av basdelarna genereras redan reproducerbart, men de är inte paketerade/testade som en clean-room starterprodukt. |
| **43** | Bygg primärhandlingsmoduler | 🟡 | `profile.ts` har nu bred primärhandlingsmodell och Gate 1 är generisk. Men den gamla uppsättningen återanvändbara moduler finns inte som sådan; extern bokning är t.ex. fortfarande `DECLARED` i kapacitetskatalogen. |
| **44** | SEO- och local-business-moduler | ✅ för `lokal-se` | Det här är sedan länge en stark del av systemet: `nortropic-seo-lokal`, NAP, schema, ortslogik, paketstyrning. Ska inte byggas om. |
| **45** | Skapa modulregister och budgets | 🔵 | **Capability Catalog + packet contract är den bättre efterföljaren.** Bygg inte ett parallellt gammalt `module-manifest`-system om samma fråga redan ägs av capabilities. |
| **46** | Mappa kundarketyper till fabriken | 🔵 | **Explicit ersatt.** Universal core + packets + capability signals + intervention decision är bättre än en hårdkodad arketypmatris. Att återinföra åtta arketyper som routingauktoritet vore bakåt. |
| **47** | Ramverks- och dependency-policy | 🔴 | Viktigt kvar. Nuvarande `nortropic-stack` säger fortfarande fast **Next.js 15**. Det saknas en riktig current-support/security-policy som skiljer kontrakt från aktuell LTS. |
| **48** | Pilotera Next.js 16 separat | ⚪ | Fortfarande en bra metod, men versionsnumret är en daterad snapshot. Kör den först när D47/current framework-policy säger att migrationen bör prövas. |
| **49** | Tre testkadensnivåer | 🟡 | `full → diff → full` finns för review, men inte ett komplett `quick/diff/full`-registry över hela QA-kedjan. |
| **50** | Benchmarka starter mot scaffold | 🔴 | Ingen riktig starter ännu → ingen riktig benchmark. |

### Fas 5-dom

**D45–46 ska strykas i sin gamla form. D47 är däremot viktigare nu än den såg ut då.**

---

# Fas 6 — Dag 51–60: Evals och lärande

Det här området är **mitt i aktuell utveckling just nu**.

Den publicerade main har ett **v4-rubrik-UTKAST** som challenger/NOT_PRODUCTION, Case A + Case B backtest-fixtures som uttryckligen **inte har körts**, ett universaliserat contract, paketkontrakt och Gym v1 där endast kontraktet — inte själva körningen — är byggt. De senaste commitsen är föredömligt tydliga med skillnaden mellan “formen finns” och “beviset finns”. Det passar exakt mot gamla manualens anda. Current competence register säger också `VALIDATING`, ungefär `n≈1`, inte `PROVEN`. fileciteturn39file0L1-L6

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **51** | Designa evalarkitekturen | 🔵 | Just nu håller en bättre evalarkitektur på att växa fram: v4 delar kärna/paketslot och låter hårdfel styra domslut. Men den är **UTKAST**, production v3 gäller fortfarande. |
| **52** | Golden set över åtta arketyper | 🔵 | Den fasta 8-arketypmodellen bör inte vara auktoritet längre. Dagens **capability-/packet-falsifiering** med Case A + Case B är bättre. Men testportföljen behöver bli mycket bredare. |
| **53** | Fixtures: akut service + planerad offert | ⚪ | Exakta paret är inte längre heligt. Case A täcker lokal service, men det här ska nu härledas ur coverage gaps i stället för kalenderdag. |
| **54** | Fixtures: extern bokning + platsförfrågan | 🔴 | De här beteendena behöver fortfarande riktig fixture-/körningstäckning eftersom capabilityn extern bokning inte är PROVEN. |
| **55** | Fixtures: fysisk plats + varumärkeskonsult | 🔴 | Fortfarande relevant coverage-gap, men formulera dem som capability/falsification cases, inte “arketyper för arketypernas skull”. |
| **56** | Fixtures: bildfattig kund + migration | 🔴 | Särskilt migration är fortfarande mycket relevant och svagt täckt. |
| **57** | Svensk copy-evaluator | 🔴 | Jag hittar ingen dedikerad svensk evaluator. Legacy `content-humanizer` finns fortfarande i systemets bärande kanon. Detta är en riktig kvarvarande idé. |
| **58** | Skill Contribution Trace | 🟡 | Kompetensregister och kunskapslagret börjar mäta **vad som kan beläggas**, men exakt per-skill contribution/cost/finding-attribution finns inte. |
| **59** | Nortropic Lab / Karpathy-metoden | 🔵 | Dagens knowledge lane, Gym, kandidater och explicit falsifiering absorberar mycket av filosofin. Ett separat generiskt “Lab-system” bör bara byggas där dagens experimentkontrakt saknar något konkret. |
| **60** | Hård N2-readinessgrind | 🔵 | Självförbättringen har utvecklats till mycket striktare authority-/Trust Kernel-struktur. Root-`AUTOPILOT` är dessutom fortsatt `off`. Den gamla “N2 dag 60”-ceremonin ska inte återupplivas som separat system. |

### Fas 6-dom

Här skulle jag inte “fortsätta Dag 51, 52, 53…”.

Vi ska låta **den nuvarande S/Gym/backtest-planen** fortsätta och sedan göra coverage-reconciliation mot D51–60.

---

# Fas 7 — Dag 61–70: Professionell launch och migration

Här blir den gamla manualen återigen **väldigt viktig**.

Den nuvarande fabriken är stark på *prelaunch*, men betydligt mindre färdig på **kundlivscykeln runt launch**.

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **61** | siteLifecycle och migrationskontrakt | 🔴 | Ingen förstaklassmodell för `new-site / same-URLs / URL-changes / domain-move / hosting-move` motsvarande manualen. |
| **62** | Crawl och URL-inventering | 🔴 | Ingen komplett old-site inventory/crawler-pipeline syns. |
| **63** | Redirect-, canonical- och cutovergrindar | 🟡 | `nortropic-cutover`, noindex och GSC-preflight finns. Men migrationens redirect-map/compiler + chains/loops + post-cutover-schema är inte fullt. |
| **64** | Kundens faktagodkännande | 🔴 | Briefgodkännandet är **inte samma sak** som kundens sign-off på slutlig telefon, tjänster, bilder, claims osv. mot final SHA/URL. Den här idén bör tillbaka. |
| **65** | Juridik-, claims-, cookie- och rättighetspaket | 🟡 | Human-only Gate 6 är stark och korrekt, juridikflaggor finns. Men ett samlat `LEGAL-REVIEW-PACK` med rights/data/claims/cookies/öppna beslut saknas som förstaklassartefakt. |
| **66** | Lätt mänsklig användartestning | 🔴 | Automation är stark; **riktig människa försöker förstå och använda sajten** är fortfarande en lucka. |
| **67** | WCAG 2.2 AA och browserprotokoll | 🟡 | WCAG 2.2 + pinnad axe + manuella checks finns. Men det gamla kravet på verifierad Chromium/Firefox/WebKit-matris är inte fullt bevisat. fileciteturn34file0L1-L2 |
| **68** | Ägarskap, handover och exit | 🟡 | `HANDOVER.md` finns i launchkedjan, men full ownership-register/cost/export/exit-modell är inte färdig. |
| **69** | Stabiliseringsplan 1/7/30/90 | 🔴 | Cutover finns, men ingen tydlig förstaklass **1/7/30/90 feedback-loop med field CWV, redirects, leads, indexering och fakta**. |
| **70** | Komplett representativ launchpilot | 🔴 | **Viktig.** Current competence register säger uttryckligen VALIDATING och ungefär en datapunkt; riktiga kunder saknas för PROVEN. Vi har alltså inte rätt att kryssa D070 grönt. fileciteturn39file0L1-L6 |

### Fas 7-dom

Det här är sannolikt **den viktigaste delen av gamla 100-dagarsplanen att rädda in i den moderna Webbförvaltningen**.

För vi har blivit extremt bra på att bygga och verifiera själva fabriken — men *hela professionella kundlivscykeln* är inte lika färdig.

---

# Fas 8 — Dag 71–80: Operatörens lärsystem

Här har Organization OS/Verkstadsgolvet och Knowledge Lane förändrat riktningen.

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **71** | Dashboards från events + OTel | 🔴 | Events finns i Trust Kernel, men OTel/dashboarddelen saknas. |
| **72** | Run Journal med FTS | 🟡 | Trust Kernel har eventlogg/projektion, men inte samma sak som ett explicit sökbart **kundhistoriklager** med FTS. |
| **73** | Observation Sensor | 🟡 | Retro/LEARNING-RECORD/knowledge work ligger nära intentionen, men jag ser inte den gamla högsignal-Observation Sensor som ett explicit produktionsinstrument. |
| **74** | Read-only Skill Scout | ⚪ | Fortfarande användbar när en verifierad kapabilitetslucka uppstår. Men inte något vi behöver bygga bara för att D074 finns. |
| **75** | MCP-register + preflight | 🟡 | MCP:er används och är rollkopplade, men komplett maskinläsbart register med owner/version/auth/tools/data/kill switch/preflight är inte uppfyllt. |
| **76** | Obsidian som cockpit | ⚪ | Inte en blocker för Webbförvaltningen. Organization OS/Verkstadsgolvet är nu en mer naturlig väg för operatörscockpit. |
| **77** | NotebookLM som researchlabb | ⚪ | Bra kandidat vid rätt researchcase, men inte en kärnkapabilitet. |
| **78** | Firecrawl/Mobbin/Perplexity-piloter | ⚪ | Behåll som kandidatstyrda experiment. Ingen anledning att införa dem före ett mätt problem. |
| **79** | Interna widgets/MCP Apps | 🔵 | **Verkstadsgolvet/Digital Twin är den moderna efterföljaren.** Bygg inte ett separat A2UI-spår bara för att gamla manualen sa det. |
| **80** | Förenkla utifrån telemetry/contribution | 🟡 | Systemet har gjort imponerande förenklingar och anti-driftarbete, men inte utifrån full telemetry/contribution eftersom D21/D58 ännu inte finns. |

### Fas 8-dom

**71, 72 och 75** är de mest materiella.

**76–79** ska inte ligga som obligatoriska “dagar” längre.

---

# Fas 9 — Dag 81–90: Gör fabriken till en webbyrå

Här är gapet väldigt tydligt.

Nuvarande repo beskriver sig fortfarande i huvudsak som en **website factory**. Launch är långt utvecklad. **Care och Growth som reproducerbara tjänster är inte det.** Nuvarande capability catalog har dessutom ingen `PROVEN`-rad. fileciteturn36file0L1-L6

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **81** | Produktifiera Launch, Care och Growth | 🔴 | Launch finns. Care/Growth är inte en färdig reproducerbar produktmodell. |
| **82** | Care-hälsokontroller och rapport | 🔴 | Ingen komplett Care runner/CARE-REPORT motsvarande manualen. |
| **83** | Leadkvalitetsloop utan CRM | 🔴 | Leadleveransen verifieras starkt, men vad som blev **kvalificerad lead → offert → affär** återförs inte systematiskt. |
| **84** | Review- och lokal synlighetsloop | 🟡 | Lokal SEO finns före launch; den återkommande post-launch review/GBP/GSC/Bing/AI visibility-loopen är inte färdig produkt. |
| **85** | Content-/fact-freshnesskalender | 🔴 | FACT-LEDGER saknas → den här loopen saknar sitt naturliga fundament. |
| **86** | Ändringsförfrågningar och SLA | 🔴 | Ingen tydlig reproducerbar FAKTA/LITEN CONTENT/NY SIDA/STRATEGISK/INCIDENT-pipeline ännu. |
| **87** | Kommersiellt ägarskap, kostnad och exit | 🟡 | Handover finns, men inte hela den kommersiella lifecycle-matrisen med cost/ownership/DPA/exit. |
| **88** | Hårdvarubenchmark före Mac mini | ⚪ | Bara relevant när telemetry bevisar lokal compute som flaskhals. **Inte Webbförvaltningen-blocker.** |
| **89** | Lokal LLM och Glif-adapters | ⚪ | Optional provider experiment. Bör vara capability-triggered, inte calendar-driven. |
| **90** | Första Care/Growth-dry-run | 🔴 | Kan inte göras ännu eftersom 81–87 inte är färdiga. |

### Fas 9-dom

Det här är **fortfarande backlogg på riktigt**.

Och här blir kommunmetaforen väldigt användbar: just nu bygger vi kompetensen att **leverera webb**, men Webbförvaltningen ska så småningom också kunna **förvalta webb**.

---

# Fas 10 — Dag 91–100: Red-team, bevis och v1

Det här är inte “gammalt nice-to-have”. Det här är slutceremonin som gör skillnaden mellan:

> “vi har byggt mycket”

och

> “vi har bevisat Webbförvaltningen v1.”

| Dag | Ursprungligt steg | Dom nu | Jämförelse |
|---:|---|---|---|
| **91** | Full prompt-injection-red-team | 🟡 | Många injection guards finns, men inte ett komplett aktuellt corpus över web/PDF/SVG/MCP/journal/reports mot dagens hela system. |
| **92** | Fault-injection externa tjänster | 🟡 | Bootstrapen testar många failure classes, men komplett kundkedjeprov för GitHub/Vercel/Resend/browser/research providers saknas. |
| **93** | Cross-client/memory/telemetry-isolering | 🔴 | Fortfarande viktig. Att `design-reviewer` använder `memory: user` gör den här kontrollen extra relevant. Full canary-test över kunder är inte bevisad. fileciteturn26file0L1-L6 |
| **94** | Disaster recovery + credential rotation | 🟡 | Trust Kernel/recovery är starkare, men en full clean-machine/customer/credential-rotation-drill är fortfarande ett eget beviskrav. |
| **95** | Hela fabriken med avbrott/resume/rollback | 🔴 | **Stor slutgrind.** Inte genomfört för den moderna Webbförvaltningen från intake hela vägen till efterlaunch/Care. |
| **96** | Baseline vs v1 | 🔴 | Ingen modern empirisk jämförelse där samma uppgifter körs på gammal baseline och slutlig Webbförvaltningen-v1. |
| **97** | Operatörsmanual och runbooks | 🟡 | Dokumentationen är mycket bättre och har numera coherence-vakter, men v1-manual kan inte färdigställas innan v1 faktiskt är färdig. |
| **98** | Oberoende teknisk + småföretagargranskning | 🔴 | Vi har massor av oberoende teknisk review **under utveckling**, men inte slutlig systemreview plus faktisk kund-/småföretagarlins. |
| **99** | Production Readiness Board | 🔴 | Ingen slutlig modern verdictmatris för exempelvis Research/Build/Autobuild/Launch/Care/Trust Kernel. |
| **100** | Tagga v1.0 eller RC | 🔴 | Definitivt inte där ännu. Repo säger själv på flera håll `VALIDATING`, `ODÖMBART`, `UTKAST`, `NOT_PRODUCTION`. Det är korrekt. |

---

# Vad hela 1–100-genomgången förändrar

Efter att ha gjort detta skulle jag justera mitt förra svar lite.

Jag skulle **inte längre bara säga “gamla manualen är en coverage-backstop”**.

Den är mer värdefull än så.

Den består i praktiken av tre olika sorters saker:

**Första tredjedelen har till stor del blivit verklighet eller absorberats av Trust Kernel.** Framför allt Dag 1–20. Vi ska inte bygga dem igen.

**Mitten innehåller både gammal arkitektur som vi har överträffat och genuina kvarvarande kapabiliteter.** Exempelvis ska den fasta arketypmodellen bort, medan Reference Compiler/designcanon, CI, framework policy, cross-browser och svensk copy-eval fortfarande är mycket relevanta.

**Sista tredjedelen är förvånansvärt aktuell.** Migration, faktagodkännande, användartestning, Care, Growth, field learning, cross-client isolation, disaster recovery, full E2E och Production Readiness är exakt sådant som lätt hamnar bakom när man fokuserar på att förbättra själva byggmotorn.

Det är därför jag nu skulle formulera den nya relationen så här:

> **Den DESIGN-FRUSNA Webbförvaltningen-planen avgör HUR vi bygger framåt.**
>
> **100-dagarsmanualen används som krav- och completeness-orakel för ATT vi inte glömmer någon viktig del av hela webbyrålivscykeln.**

Och det finns en ytterligare viktig signal i dagens repo: `kompetensregister.md` vägrar kalla något `PROVEN`; de centrala rollerna ligger på `VALIDATING`, med ungefär en datapunkt och otillräcklig riktig kundevidens. Det innebär att systemet själv redan säger samma sak som den här reconciliationen:

> **arkitekturen börjar bli mycket stark, men den verkliga livscykeln är ännu inte slutbevisad.** fileciteturn39file0L1-L6

## Det jag skulle göra med detta nu

Nästa logiska steg är **inte** att säga till Claude “fortsätt från Dag 21”.

Jag skulle låta nuvarande Webbförvaltningen-plan färdigställas, men lägga ovanpå den en **100-Day Reconciliation Matrix v1** där exakt alla 100 rader får permanent disposition:

`SATISFIED` · `SUPERSEDED` · `OWNED_BY_TRUST_KERNEL` · `REQUIRED_LATER` · `TRIGGER_ONLY` · `OPEN`.

Då får vi ett riktigt systematiskt svar på frågan **“vad återstår innan Webbförvaltningen faktiskt är komplett?”**, och när S-planen förändras kan samma matris mekaniskt revideras i stället för att vi behöver försöka minnas två enorma planer parallellt.

Den mest värdefulla upptäckten från genomgången är att jag **inte skulle vilja släppa Webbförvaltningen v1 utan att D61–70 och D91–100 i moderniserad form har fått riktiga svar**. Där ligger mycket av skillnaden mellan en extremt avancerad hemsidegenerator och den riktiga förvaltning vi har pratat om.

---

## Meddelande 5 — Johnny (användare)

jag tänker att vi bygger klart webbförvaltningen vilket pågår i detta nu och sen kör vi nortropic intake och skriver väl som en jämförande prompt eller nåt liknande

---

## Meddelande 6 — ChatGPT (assistent)

Ja — **det är precis den ordningen jag tycker vi ska köra.** Och det är bättre än att störa det pågående Webbförvaltningen-bygget genom att försöka trycka in 100-dagarsmanualen nu.

Vi gör det i tre tydliga steg.

### 1. Bygg klart nuvarande Webbförvaltningen

Låt den nuvarande DESIGN-FRUSNA planen fortsätta hela vägen till sin naturliga slutpunkt. Vi ska inte ändra dess roadmap baserat på den gamla manualen mitt under bygget.

Det är extra viktigt eftersom dagens arkitektur redan har ersatt flera gamla idéer med bättre konstruktioner: universal core + packets, Site Quality Contract, capabilities, knowledge lane, Gym, Trust Kernel osv. Att mata in 100-dagarsplanen nu riskerar att få Claude att börja “lösa” saker som redan är lösta på ett modernare sätt.

### 2. När Webbförvaltningen är klar: kör **Nortropic Intake på jämförelsen**

Då blir intake-idén ungefär:

> **Reconcile the completed Webbförvaltningen against the historical Nortropic 100-day web-agency plan and identify any capabilities, lifecycle requirements, verification requirements or valuable ideas that remain materially unaddressed.**

Det är alltså **inte**:

> “implementera det som saknas från 100-dagarsplanen”.

Utan först:

> **“jämför två generationer av Nortropic och ta reda på vad vi faktiskt fortfarande behöver.”**

Det är en mycket bättre fråga.

Den gamla manualen ska då behandlas som ett **historiskt krav-/idé-/coverage-corpus**, inte som ny authority. Manualen säger dessutom själv att dagens repo/runtime måste rebaselinas och att `NO-OP VERIFIED` är korrekt när ett mål redan är löst lika bra eller bättre. fileciteturn0file0

### 3. Intake-resultatet blir en ny modern backlog, inte “Dag 1–100 igen”

Jag skulle vilja att jämförelsen klassificerar **varenda D001–D100**, men också bryter ner dem på kravnivå när en dag innehåller flera separata idéer.

Till exempel:

`D038 Konsolidera designkanonen`

kan efter jämförelsen bli:

- `SUPERSEDED` — någon gammal routingmodell behövs inte längre.
- `STILL_REQUIRED` — reducering av permanent designkanon återstår.
- `ABSORBED_BY_NEW_ARCHITECTURE` — vissa delar har flyttat in i capability/Gym.
- `REJECT` — något skulle skapa parallell sanning.

Det är bättre än att ge hela D038 en enda färg.

Jag skulle använda ungefär dessa dispositioner:

| Disposition | Betydelse |
|---|---|
| `SATISFIED` | dagens system bevisar samma krav eller starkare |
| `SUPERSEDED` | behovet finns men löses nu av bättre arkitektur |
| `TRUST_KERNEL_OWNED` | hör hemma i bootstrap/control plane, inte Webbförvaltningen |
| `STILL_REQUIRED` | verklig kvarvarande Webbförvaltningskapabilitet |
| `PARTIAL` | delar finns, men ursprunglig outcome är inte bevisad |
| `TRIGGER_ONLY` | bygg först när verkligt behov/kund uppstår |
| `REJECT` | gammal idé bör uttryckligen inte återinföras |
| `UNKNOWN` | dagens evidens räcker inte för att döma |

Och **`UNKNOWN` får vara ett riktigt resultat**, inte automatiskt bli “lägg till backlog”.

---

## Den jämförande prompten bör vara ganska hård

När det är dags skulle jag ge Intake tre huvudsakliga auktoritetskällor:

**A. Den färdigbyggda Webbförvaltningen**
- final `main` SHA
- aktuell dokumentation
- aktuella contracts
- capabilities
- packets
- Gym/evals
- gates
- launch/lifecycle
- slutrapporten från bygget

**B. Den DESIGN-FRUSNA planen som ledde fram till den**
- så att systemet kan förstå avsikten bakom nuvarande arkitektur.

**C. `Nortropic_100_dagar_manual_v2.3_verified.pdf`**
- som historisk coverage- och idékälla, **inte authority över A/B**.

Sedan får den explicit instruktion att inte premiera gammalt bara för att det står i manualen.

Jag skulle exempelvis kräva:

> För varje gammalt krav, fråga först:  
> **Vilket problem försökte detta lösa?**  
> Därefter:  
> **Har dagens Nortropic redan löst problemet på samma eller starkare sätt?**  
> Inte:  
> **Finns filen/komponenten med samma namn?**

Det är en väldigt viktig skillnad.

`FACT-LEDGER.json` saknas kanske — men om samma funktion senare skulle ha fått en bättre förstaklassbärare ska vi inte skapa `FACT-LEDGER.json` bara för att gamla planen använde det namnet.

Samma med `NORTROPIC-RUN.json`, state machine, module registry, starter osv.

---

## Och sedan skulle jag låta Intake göra en andra syntes

Efter D001–D100-reconciliation ska den inte lämna oss med typ:

> 37 saker saknas.

Den ska deduplicera dem till **moderna capability gaps**.

Exempelvis skulle flera gamla dagar kunna kollapsa till:

**Lifecycle / Migration**
- site lifecycle
- old-site inventory
- redirects/cutover
- post-launch stabilization

**Client truth & approvals**
- final fact approval
- rights
- legal review pack
- ownership/handover

**Quality infrastructure**
- CI
- CodeQL
- dependency/security scanning
- cross-browser
- accessibility regression

**Design intelligence**
- reference contract/compiler
- reduced canon
- skill routing
- Swedish copy evaluation

**Care & Growth**
- Care runner
- fact freshness
- lead-quality feedback
- change requests
- recurring reports

**v1 proof**
- cross-client isolation
- disaster recovery
- full E2E
- independent external review
- readiness board

Då kanske 100 gamla dagar egentligen blir **8–15 moderna gaps**.

Det är det vi vill veta.

---

Och först **efter den syntesen** bestämmer vi vad som ska implementeras.

Alltså:

**Webbförvaltningen färdig**
→ **freeze/current-state evidence**
→ **Nortropic Intake: historical-vs-current reconciliation**
→ **D001–D100 disposition matrix**
→ **deduplicated modern gap analysis**
→ **prioritering**
→ **ny execution plan**
→ Claude Code.

Det fina är att vi då använder den gamla 100-dagarsplanen exakt till det den är bäst på: **att försöka fånga saker vi kan ha glömt**, samtidigt som den nya Webbförvaltningen får vara arkitektonisk source of truth.

Jag skulle därför **inte göra något mer med PDF:en just nu**. När det pågående Webbförvaltningen-bygget rapporterar färdigt tar vi dess slutliga SHA/slutrapport, och då kan jag skriva den kompletta Intake-prompten för den här reconciliationen. memcite

---

## Meddelande 7 — Johnny (användare)

behöver du brainstorma nåt mer ytterligare kring detta? kanske vi ska göra

---

## Meddelande 8 — ChatGPT (assistent)

Ja. Jag tycker faktiskt att vi ska **brainstorma ett lager till nu**, inte för att ändra det pågående bygget utan för att göra eftergranskningen riktigt bra när Webbförvaltningen är färdig.

Det finns en risk annars att vi gör en enkel:

> gamla 100-dagarsplanen ↔ nya Webbförvaltningen

…och missar att **båda planerna kan ha luckor**. Jag skulle därför göra efterarbetet betydligt starkare.

## Jag skulle göra det till en fyrdubbel slutrevision

När Webbförvaltningen är färdig fryser vi först dess exakta `main`-SHA. Sedan granskar vi fyra saker mot samma frysta system:

**1. Historical reconciliation**  
100-dagarsmanualens D001–D100 jämförs mot det faktiska färdigbyggda systemet.

**2. Masterplan reconciliation**  
Den DESIGN-FRUSNA Webbförvaltningen-planen jämförs mot vad som faktiskt blev byggt. Inte bara “Claude sa klar”, utan: blev varje tänkt capability, packet, contract, reality-lager, Gym-del osv faktiskt materialiserad eller medvetet avstådd?

**3. Fresh completeness/frontier audit**  
Vi frågar från noll:

> Om vi idag skulle designa en världsklass Webbförvaltning, finns det något viktigt som **varken gamla 100-dagarsplanen eller den nya masterplanen fångade?**

Här gör vi en färsk omvärldsgranskning mot aktuella primärkällor och utvecklingen vid tidpunkten: web standards, accessibility, browsers, security, Search, AI-agent engineering, design systems, observability, Care/Growth osv.

**4. Real-world lifecycle audit**  
En separat lins frågar inte “är arkitekturen elegant?” utan:

> Kan Nortropic verkligen ta en okänd kund från problem → rätt intervention → research → bygge/förbättring → verifiering → launch → stabilisering → Care → Growth → förändringar → exit?

Det här är en viktig lins eftersom man kan ha en fantastisk hemsidefabrik och ändå sakna delar av en **webbförvaltning**.

---

# Och jämförelsen bör ske på atomnivå, inte bara “Dag 38 = klar”

Det här tycker jag är den största förbättringen jämfört med vad vi nyss pratade om.

En gammal dag kan innehålla sex olika idéer. Exempelvis kan D038 samtidigt innehålla:

- en bra princip som fortfarande behövs,
- en vendor som bör tas bort,
- en mekanism som ersatts av Gym,
- en routingidé som redan är implementerad,
- en idé som vi numera uttryckligen vill förkasta.

Så:

> **D038 kan inte bara få status `SUPERSEDED`.**

Vi bör först bryta varje dag i dess **atomära avsikter/krav**.

Ungefär:

```text
D038-R01
D038-R02
D038-R03
...
```

Varje sådan rad får:

- ursprungligt problem
- önskat outcome
- föreslagen gammal mekanism
- modern motsvarighet
- exakt evidens
- disposition
- evidensmognad
- kvarvarande risk
- nästa handling

Det gör jämförelsen betydligt säkrare.

---

# Två axlar, inte en

Jag skulle dessutom **separera disposition från evidensmognad**.

Exempel:

### Disposition

`SATISFIED`  
`SUPERSEDED`  
`PARTIAL`  
`STILL_REQUIRED`  
`TRUST_KERNEL_OWNED`  
`TRIGGER_ONLY`  
`REJECT`  
`UNKNOWN`

Men separat:

### Mognad

Använd gärna Nortropics nuvarande språk:

`DECLARED → BUILT → VALIDATING → PROVEN`

Då kan något exempelvis vara:

> `SATISFIED / VALIDATING`

Det betyder:

> Arkitekturen finns och motsvarar kravet, men vi har ännu inte riktig produktionsevidens nog för att kalla den PROVEN.

Det är **mycket bättre** än att `SATISFIED` råkar betyda både “kod finns” och “det här fungerar bevisligen i verkligheten”.

Det passar också väldigt väl med hur dagens kompetens- och kapacitetsregister redan tänker.

---

# Jag vill lägga till en särskild kategori: “Zombie prevention”

Det här tycker jag är viktigt.

Gamla planer ligger kvar. Om ett år kan en agent hitta:

> `NORTROPIC-RUN.json`  
> `module-manifest.json`  
> “åtta arketyper”  
> “bygg ett eget policy engine”  

…och börja återuppfinna saker vi redan medvetet ersatt.

Så slutrevisionen bör skapa ett litet **Supersession / Rejection Ledger**.

Exempel:

```text
LEGACY CONCEPT:
Eight fixed customer archetypes

DISPOSITION:
SUPERSEDED

REPLACED BY:
Universal Core
+ Capability Catalog
+ Packets
+ Site Quality Contract

DO NOT REINTRODUCE:
A fixed archetype router as authority.

WHY:
It hard-codes the customer model and duplicates capability selection.
```

Det blir ett slags **anti-regressionsminne för arkitektur**.

Väldigt värdefullt.

---

# Vi bör också leta efter motsatsen: saker moderniseringen tappat

Det är minst lika viktigt.

När man bygger en bättre arkitektur kan man råka kasta bort en bra gammal egenskap.

Så en särskild fråga bör vara:

> **Vilka egenskaper fanns som uttryckligt krav i 100-dagarsplanen men har ingen tydlig modern ägare?**

Inte:

> “finns samma fil?”

Utan:

> “vem äger nu problemet?”

Om svaret blir:

```text
Ingen.
```

då har vi hittat ett **orphaned requirement**.

Det är exakt de fynden jag vill ha ut.

Exempel på kandidater från vår preliminära genomgång är sådant som:

- final kundfaktaapproval
- 1/7/30/90-stabilisering
- cross-client canary
- full ownership/exit
- Care
- field learning
- mänskligt användartest

Inte för att de nödvändigtvis saknas när bygget är klart — utan för att sådana saker är lätta att göra hemlösa när kärnarkitekturen utvecklas snabbt.

---

# Och en annan viktig lins: “nya risker som gamla planen inte kunde känna till”

100-dagarsplanen kan bara varna för världen den såg i juli.

Den nya arkitekturen innehåller saker som inte fanns då eller inte hade samma betydelse:

- universal core / packets
- capability compilation
- Site Quality Contract
- Knowledge Lane
- Gym
- provider-neutral Trust Kernel
- owner-attention-taxonomin
- Organization OS-relationen
- mer avancerad autonomi

Varje sådan innovation skapar också **nya felmoder**.

Så slutrevisionen bör fråga:

> Vad har vi byggt sedan juli som introducerar en ny trust boundary, driftmöjlighet, Goodhart-risk, routingrisk eller falsk-PASS-risk som 100-dagarsmanualen omöjligen kunde innehålla?

Det är egentligen en **delta-threat-model för innovationen själv**.

---

# Jag skulle dessutom använda två motriktade reviewers

Inte tio agenter. Bara två tydliga adversariala linser efter huvudanalysen.

### Coverage Challenger

Hans jobb:

> Försök bevisa att något värdefullt från den gamla planen har tappats bort eller felaktigt klassats som SATISFIED/SUPERSEDED.

### Simplification Challenger

Hans jobb:

> Försök bevisa att föreslagna “saknade” saker egentligen duplicerar dagens arkitektur, bygger för hypotetiska behov eller återinför legacy-komplexitet.

Det ger en väldigt bra balans.

Den ena skyddar mot **glömska**.

Den andra skyddar mot **backlog-bloat**.

Och sedan kan en tredje, mycket smal lins vara:

### Real Customer Challenger

> Skiter i hur elegant arkitekturen är. Vad skulle fortfarande gå dåligt för en riktig kund?

Det skulle passa Webbförvaltningen perfekt.

---

# Intake bör därför egentligen vara en campaign, inte en vanlig idé

Jag skulle inte skapa:

> “Idé: jämför 100-dagarsplanen.”

Jag skulle behandla detta som en **reconciliation campaign / audit**.

Flödet blir:

```text
WEBBFÖRVALTNINGEN COMPLETE
          ↓
freeze final SHA
          ↓
COLLECT EVIDENCE
          ↓
100-DAY ATOMIC RECONCILIATION
          +
MASTERPLAN → SHIPPED RECONCILIATION
          +
FRESH FRONTIER / COMPLETENESS AUDIT
          +
REAL-LIFECYCLE AUDIT
          ↓
adversarial challengers
          ↓
DEDUPLICATION
          ↓
MODERN CAPABILITY-GAP MAP
          ↓
Intake candidates
          ↓
owner prioritization
          ↓
next execution programme
```

**Först längst ner skapar vi riktiga implementation candidates.**

Annars riskerar `innovation-intake` att få 73 issues som egentligen representerar samma sex luckor.

---

# Och vi behöver en stopregel

Annars kan detta bli “Nortropic granskar Nortropic för evigt”.

Jag skulle sätta slutvillkoret ungefär:

Webbförvaltningen v1 får betraktas som completeness-reviewed när:

- 100 % av de atomiserade historiska kraven har disposition.
- 100 % av masterplanens bindande delar har disposition.
- varje `SATISFIED`/`SUPERSEDED` har konkret evidens.
- inget `UNKNOWN` med hög konsekvens saknar ägare.
- inga kritiska orphaned requirements finns.
- alla kvarvarande gaps har `NOW / LATER / TRIGGER / REJECT`.
- en oberoende challenger har försökt fälla analysen.
- fresh frontier-rundan inte hittar någon okontrollerad high-risk-lucka.
- resten får bli **känd backlog**, inte anledning att hålla v1 gisslan.

Det sista är viktigt.

> **“Komplett granskad” betyder inte “allt vi någonsin kan bygga är byggt”.**

Det betyder att vi **vet vad som finns, vad som saknas, vad vi medvetet väntar med och varför**.

---

Så ja: jag tycker brainstormingen gav oss en bättre modell än bara “kör Intake på gamla PDF:en”.

Jag skulle nästan kalla den framtida operationen:

> **Webbförvaltningen — Post-Build Reconciliation & Completeness Audit**

Och då använder vi 100-dagarsplanen som **en av fyra linser**, inte som hela facit.

Det tycker jag är nästa nivå på upplägget. memcite

---

## Meddelande 9 — Johnny (användare)

låter bra, brainstorma som vanligt

---

## Meddelande 10 — ChatGPT (assistent)

Ja. När jag tänker ett varv till på det här tror jag faktiskt att vi kan göra något **betydligt större och mer användbart än en engångsjämförelse av två planer**.

Det intressanta är inte egentligen:

> “Vad från 100-dagarsplanen saknas?”

Det verkliga problemet är:

> **Hur bevisar Nortropic att en förvaltning är komplett för sitt definierade uppdrag, utan att gammal arkitektur återinförs, nya luckor missas eller “byggt” förväxlas med “bevisat”?**

Det skulle kunna bli en generell metod för **alla framtida Nortropic-förvaltningar**.

Och det passar förvånansvärt väl med hur Nortropic redan har börjat utvecklas.

---

# 1. Jag skulle ändra tankemodellen från “comparison” till **Assurance Compilation**

Vi har flera olika typer av information:

```text
100-dagarsplan
        ↓
gamla krav / idéer / risker

DESIGN-FRUSEN masterplan
        ↓
modern arkitektur / intention

färdig Webbförvaltning
        ↓
verklig implementation

riktig runtime / riktiga kunder
        ↓
verklig evidens

omvärlden idag
        ↓
nya kandidatkrav
```

Vi vill inte att någon av dessa ska bli **den nya listan**.

Vi vill kompilera dem till något renare:

```text
                     SOURCES
                        │
              ┌─────────┼─────────┐
              │         │         │
            old       current    frontier
            plan       design     reality
              │         │         │
              └─────────┼─────────┘
                        ↓
              ATOMIC REQUIREMENTS
                        ↓
                CURRENT OWNERSHIP
                        ↓
                  EVIDENCE
                        ↓
                    DEFEATERS
                        ↓
                   DISPOSITION
                        ↓
          MODERN CAPABILITY / GAP MODEL
```

Alltså nästan:

> **historiska planer in → moderna proof obligations ut.**

Det tycker jag är den viktigaste utvecklingen av idén.

---

# 2. Vi bör aldrig fråga “finns komponenten?”

Vi ska fråga:

> **Är problemet löst?**

Exempel från gamla manualen:

`FACT-LEDGER.json`

Fel fråga:

> Finns `FACT-LEDGER.json`?

Rätt fråga:

> Kan Nortropic bevisa att affärskritiska fakta har källa, verifieringsstatus, freshness, ägare och konsistens över alla ytor där de publiceras?

Om det nya systemet löser detta bättre genom något helt annat:

```text
SATISFIED / SUPERSEDED
```

Om ingen idag äger problemet:

```text
ORPHANED REQUIREMENT
```

Det senare är den verkliga signalen.

---

# 3. **Orphan detection** tror jag blir en av de mest värdefulla linserna

Vi bör leta i **båda riktningarna**.

### A. Requirement → implementation

För varje gammalt eller nytt krav:

> Vem äger detta idag?

Exempel:

```text
REQUIREMENT:
En kund ska godkänna final faktarepresentation före launch.

CURRENT OWNER:
???

EVIDENCE:
???

RESULT:
ORPHANED
```

Det är en riktig lucka.

### B. Implementation → requirement

Men vi ska också fråga:

> Varför finns den här komponenten?

Om vi hittar:

```text
Component X
↓
ingen source need
ingen capability
ingen risk den löser
ingen customer outcome
ingen architectural requirement
```

då kan det vara **gold plating / legacy complexity**.

NASA:s systems-engineering-metodik använder just bidirektionell requirements traceability och varnar för att krav utan ett legitimt parent/source kan vara “gold plating” som bör elimineras. citeturn979027search4turn979027search2

Det här skulle göra vår revision både:

> **gap detector**

och

> **complexity detector**.

Väldigt Nortropic.

---

# 4. Jag tror vi behöver ett **Nortropic Assurance Graph**

Inte en stor ny runtimekomponent.

Första versionen kan bara vara en audit-artefakt.

Idén kommer från assurance cases: ett påstående ska inte vara “sant för att det står i dokumentationen”; man binder ett **claim → argument → evidence**, och anger även skäl att tvivla på slutsatsen. SEI beskriver assurance cases just som organiserad evidens och argument för varför ett systempåstående faktiskt håller. citeturn168835search0turn168835search6

Nortropic-version:

```text
CLAIM
Webbförvaltningen kan migrera en befintlig sajt
utan att tappa känd söksynlighet.

SUBCLAIMS
├─ lifecycle klassificeras
├─ gamla URL:er inventeras
├─ redirect map skapas
├─ chains/loops testas
├─ canonical/noindex verifieras
└─ post-cutover observeras

EVIDENCE
├─ implementation
├─ deterministic tests
├─ fixture
└─ real migration run

DEFEATERS
├─ ingen riktig migrering genomförd
├─ GSC-data saknas
└─ 90-dagars post-cutover ännu ej observerad

VERDICT
PARTIAL

MATURITY
VALIDATING
```

Det här är **mycket bättre än `Migration = ✅`**.

---

# 5. “Defeaters” passar Nortropic extremt bra

Det här var det mest intressanta jag hittade när jag jämförde vår metod med etablerad assurance-teori.

SEI:s modell för confidence bygger inte bara på att samla bevis, utan på att explicit fråga:

> **Vilka skäl finns att tvivla på detta claim?**

Och sedan försöka eliminera dem. citeturn168835search1turn168835search5

Det är nästan exakt den kultur vi redan har byggt:

```text
claim
↓
försök fälla
↓
hitta motexempel
↓
reparera
↓
falsifiera igen
```

Så varje `SATISFIED` skulle kunna bära:

```text
KNOWN_DEFEATERS:
none unresolved
```

medan:

```text
VALIDATING
DEFEATERS:
- only synthetic evidence
- no customer run
```

blir helt ärligt.

---

# 6. Vi bör lägga till en **proof class**

Alla bevis är inte samma sak.

Jag skulle vilja ha:

```text
P0 DECLARATION
P1 IMPLEMENTATION
P2 MECHANICAL VERIFICATION
P3 SYNTHETIC BEHAVIOR
P4 REAL-WORLD BEHAVIOR
P5 LONGITUDINAL REALITY
```

Exempel:

### Site Quality Contract

Kod + guards kanske ger:

`P2`

Fixture kan ge:

`P3`

Två verkliga kunder:

`P4`

Sex månader Care-data:

`P5`

Det skulle ligga väldigt nära dagens:

`DECLARED → BUILT → VALIDATING → PROVEN`

men mäta **vilken typ av bevis som faktiskt existerar**, inte bara maturity.

Vi kanske inte ens behöver införa namnen ovan permanent; principen är viktigare.

---

# 7. En tredje axel: **persistence class**

Det här är något jag tycker vi missat hittills.

Alla krav som upptäcks i audit ska **inte bli permanenta gates**.

Vi bör klassificera dem:

### `ONE_TIME_PROOF`

Behöver bara verifieras vid v1-ceremonin.

Exempel:
- baseline comparison.

### `PERMANENT_INVARIANT`

Måste skyddas vid varje ändring.

Exempel:
- en andra Site Quality Contract får inte uppstå.
- juridik får aldrig auto-godkännas.

### `RELEASE_GATE`

Kontrolleras på varje sajt.

Exempel:
- faktatrohet.
- primärhandling fungerar.

### `REALITY_SIGNAL`

Kan bara observeras efter launch.

Exempel:
- field CWV.
- lead quality.

### `PERIODIC_REVIEW`

Kontrolleras kvartalsvis/årligen.

Exempel:
- framework support.
- WCAG-version.
- vendor policy.

### `TRIGGER_ONLY`

Existerar först när verkligheten kräver det.

Exempel:
- Ring 2 package.
- lokal LLM.
- ny payment capability.

Det här hindrar oss från att efter audit skapa **300 permanenta tester**.

Thoughtworks idé om architectural fitness functions är användbar här: viktiga arkitekturegenskaper kan göras kontinuerligt testbara, men deras senaste enterprise-playbook betonar också att antalet bör hållas begränsat och användbart. citeturn307548search48turn307548search50

---

# 8. Auditens output bör alltså inte vara “100 saker”

Jag ser snarare fem slutprodukter.

### A. Coverage Matrix

Alla atomära claims får disposition.

### B. Assurance Case

De viktigaste påståendena om vad Webbförvaltningen faktiskt kan göra och vilket bevis som stödjer dem.

### C. Gap Map

Endast verkliga moderna luckor.

### D. Supersession Ledger

Vad som uttryckligen **inte ska återinföras**.

### E. Fitness-function candidates

Endast de upptäckter som är så viktiga och stabila att de förtjänar permanent mekaniskt skydd.

Sedan får Intake bara skapa implementation candidates från **C och eventuellt E**.

---

# 9. Supersession Ledger kan bli mycket kraftfullare än jag först tänkte

Exempel:

```text
LEGACY:
Fixed eight-archetype architecture

PROBLEM IT SOLVED:
Different customers need different requirements.

SUPERSEDED BY:
Universal Core
+ Capability Compilation
+ Packets
+ Site Quality Contract

REINTRODUCTION RISK:
HIGH

DO NOT:
Build a fixed archetype router as a new authority.

ALLOWED:
Use archetypes as fixtures / examples / discovery labels.

WHY:
Archetypes are useful observations but should not own runtime truth.
```

Det sista är viktigt.

Vi behöver inte säga:

> “arketyper är dåliga”.

Vi säger:

> **“arketyper får inte längre ha den auktoritetsroll de hade i den gamla arkitekturen.”**

Det är mycket mer precist.

---

# 10. Och några supersessions bör kunna få **tripwires**

Inte alla.

Men riktigt farliga gamla mönster kan få automatiska vakter.

Exempel:

```text
NO_SECOND_SITE_QUALITY_CONTRACT
NO_FIXED_ARCHETYPE_AUTHORITY
NO_PROVIDER_OUTPUT_AS_TRUST_VERDICT
NO_LATEST_MAIN_AS_RUNTIME_STANDARD
NO_AUTO_LEGAL_APPROVAL
```

Det blir nästan **architecture anti-bodies**.

När vi en gång har gjort ett kostsamt arkitekturmisstag ska inte Nortropic kunna återupptäcka samma “bra idé” två år senare utan att någon reagerar.

---

# 11. Vi ska också leta efter **semantic zombies**

Det finns en knepigare variant.

Vi kan ta bort:

```text
module-manifest.json
```

och tre månader senare bygga:

```text
capability-module-registry.json
```

som egentligen är samma gamla dubbelsanning med nytt namn.

Därför räcker inte supersession med filnamn.

Varje superseded concept behöver beskrivas som:

```text
FORBIDDEN SEMANTIC ROLE:
"A second authoritative description of which
capabilities this customer build requires."
```

Då kan en framtida reviewer förstå **rollen** vi försöker undvika.

Det här blir extra viktigt när agenter utvecklar systemet.

---

# 12. Vi bör använda **current scope som nollpunkt**

Detta är avgörande.

“Komplett Webbförvaltning” får inte betyda:

> kan bygga allt som kan finnas på internet.

Current scope säger exempelvis att stateless är vallgraven och att vissa behov routas bort. Då är:

```text
egen CRM
databas
full e-handel
medlemssystem
```

inte automatiskt gaps.

En förvaltning är komplett om den:

1. kan leverera allt som ligger inom sitt deklarerade uppdrag,
2. kan känna igen när något ligger utanför,
3. kan route:a det korrekt,
4. inte låtsas kunna det.

Det ger en mycket bättre definition:

> **Completeness = capability coverage + truthful boundaries.**

Inte:

> feature count.

---

# 13. Därför behöver vi en separat **Boundary Audit**

För varje `ROUTE-OUT` eller trigger-only capability:

> Kan systemet faktiskt upptäcka behovet?

> Routar det innan det hunnit göra skada?

> Ger det en vettig nästa väg?

Exempel:

```text
Kund behöver medlemsdata
↓
research upptäcker
↓
capability compiler identifierar stateful requirement
↓
stateless-vakten fäller
↓
ROUTE
```

Om systemet däremot bara har:

```text
"vi bygger inte databaser"
```

i dokumentationen men kan ändå råka planera en medlemsportal, då är scopegränsen inte verklig.

Det här blir en viktig completeness-dimension.

---

# 14. “Fresh Frontier” får inte bli en genväg runt Knowledge Lane

Det här är en väldigt viktig integration med det vi just byggt.

När audit-rundan söker dagens värld och hittar:

> “Ny browser capability X borde Nortropic använda!”

ska det **inte** gå:

```text
web search
↓
STILL_REQUIRED
↓
build
```

utan:

```text
external observation
↓
Knowledge Lane
↓
candidate
↓
corroboration
↓
local replication
↓
possibly adoption
```

NIST SSDF betonar också att säkerhetskrav, risker och designbeslut bör spåras och att provenance för software components ska samlas, vilket passar väldigt bra med vår propose-only och source-bound metod. citeturn307548search7turn307548search8

Så:

> **Historical reconciliation får döma gammalt mot nytt.**
>
> **Fresh frontier får föreslå framtid.**

De två auktoritetsvägarna ska inte blandas.

---

# 15. Jag skulle lägga till ett **Reality Gap** som eget fynd

Vi tenderar annars att säga:

```text
implementation exists
tests pass
→ SATISFIED
```

Men dagens Nortropic har redan lärt oss något viktigt:

> syntetisk evidens ≠ verklig evidens.

Så vi behöver kunna hitta:

```text
ARCHITECTURE GAP
saknas i systemet
```

men också:

```text
REALITY GAP
systemet finns men vi vet inte om det fungerar i verkligheten
```

Exempel:

```text
Capability:
lokal-se

Implementation:
yes

Fixtures:
yes

Gates:
yes

Real customers:
insufficient

GAP TYPE:
REALITY GAP

NEXT ACTION:
use on real customers, observe
```

Ingen kod behövs.

Det förhindrar att “gap analysis” automatiskt genererar programmering.

---

# 16. Samma sak med **Evidence Gap**

Ytterligare ett scenario:

```text
systemet gör förmodligen redan detta
men ingen kan bevisa det.
```

Det kanske kräver:

- ett test,
- instrumentation,
- en run,
- eller bara en tydligare trace.

Inte ny produktkod.

Därför skulle jag ha gaptyper:

```text
CAPABILITY_GAP
VERIFICATION_GAP
REALITY_GAP
OBSERVABILITY_GAP
OWNERSHIP_GAP
LIFECYCLE_GAP
DOCUMENTATION_GAP
SIMPLIFICATION_OPPORTUNITY
```

Det kommer göra den framtida backloggen **mycket mer intelligent**.

---

# 17. Det kan även finnas **negative gaps**

Det låter motsägelsefullt men är viktigt:

> något finns som inte borde finnas.

Exempel:

```text
DUPLICATE_AUTHORITY
OVERLAPPING_SKILL
UNUSED_CAPABILITY
PERMANENT_HUMAN_STOP_WITHOUT_NEED
UNBOUNDED_CONTEXT
LEGACY_PATH
```

Det är då ett **removal candidate**, inte ett build candidate.

Så gap analysis borde kunna säga:

```text
ADD
CHANGE
REMOVE
PROVE
OBSERVE
ROUTE
DO_NOTHING
```

Inte bara ADD.

---

# 18. Jag gillar också tanken på **Evidence Half-Life**

Inte som bokstavlig matematisk halveringstid, utan som modell.

Ett bevis kan bli gammalt.

Exempel:

```text
CLAIM:
Gate 4 accessibility is correctly implemented.

EVIDENCE_SHA:
abc123

OWNER_SURFACES:
skills/nortropic-prelaunch/**
agents/qa-launcher.md
scripts/run-axe-gate.mjs

INVALIDATES_ON:
change to any owner surface
change to WCAG baseline
change to axe runner
```

Om inget berört ändras:

> claim kan fortsätta vara valid.

Om en relevant yta ändras:

```text
SATISFIED
↓
STALE
```

SEI pekar uttryckligen på problemet med assurance/certifiering som bara blir snapshots och menar att evidensen bör gälla den **aktuellt släppta versionen** eller vara bevisat invariant mot senare förändringar. citeturn168835search6

Det är nästan exakt Nortropics stale/attestation-tänk applicerat på hela verksamhetskompetensen.

---

# 19. Det här öppnar dörren till **incremental re-audit**

Det betyder att vi inte behöver göra:

> “Läs om alla 118 sidor varje kvartal.”

Efter första compilationen har vi kanske:

```text
R-0001 → owned by A, B
R-0002 → superseded
R-0003 → owned by C
...
```

Vid en senare förändring:

```text
changed paths
↓
affected assurance claims
↓
only those become stale
↓
targeted revalidation
```

Det är väldigt elegant.

---

# 20. Och då blir Aquarium plötsligt relevant längre fram

Inte nu som implementation.

Men tänk vad Aquarium senare skulle kunna visa.

Inte:

```text
Webbförvaltningen
█████████ 94%
```

Det skulle jag ogilla.

Utan något mer organiskt:

```text
WEBBFÖRVALTNINGEN

Capabilities
18 VALIDATING
6 PROVEN
2 DECLARED
0 unknown high-risk

Assurance
42 current claims
3 stale
1 unresolved defeater

Reality
2 capabilities awaiting real-customer evidence

Frontier
4 candidates under observation

Drift
1 supersession tripwire triggered
```

Det hade varit **ambient organizational observability på riktigt**.

Inte health theater.

---

# 21. Samma modell fungerar sedan för nästa förvaltning

Det här är varför jag tycker idén har blivit större.

När Nortropic senare bygger exempelvis Automation:

```text
Vad betyder en bra automation?
↓
definition of excellent
↓
requirements
↓
implementation
↓
evidence
↓
assurance case
↓
reality
```

Research:

```text
Vad betyder bra research?
```

Support:

```text
Vad betyder bra kundservice?
```

Software:

```text
Vad betyder en bra produkt?
```

Så Post-Build Reconciliation kan bli en **förvaltningsskapande institution**.

---

# 22. Jag skulle nästan formulera en generell Nortropic-lag

> **En förvaltning är inte komplett när alla planerade komponenter finns.**
>
> **Den är komplett när varje kritiskt verksamhetspåstående antingen är bevisat, uttryckligen avgränsat eller har en namngiven kvarvarande osäkerhet och ägare.**

Det är mycket mer robust.

Och det motsvarar egentligen NASA:s klassiska Verification Matrix-tänk: varje requirement får unik identitet, källa, verifieringsmetod och resultat; spårbarheten ska hållas genom livscykeln. citeturn979027search0turn979027search1

Vi skulle bara göra en mycket mer agent-native version av det.

---

# 23. Auditens egna resultat måste också kunna falsifieras

Det här är viktigt efter allt vi precis lärt oss med Nortropics guards.

Anta att audit-agenten producerar:

```text
100% coverage
86 SATISFIED
9 SUPERSEDED
5 TRIGGER
```

Det ser fantastiskt ut.

Men hur vet vi att den inte bara **missade 40 krav under atomiseringen?**

Så själva reconciliationen behöver mekaniska kontroller:

```text
alla source sections consumed
alla D001–D100 represented
ingen atom saknar source pointer
ingen SATISFIED saknar evidence
ingen SUPERSEDED saknar replacement
ingen REJECT saknar rationale
ingen high-risk UNKNOWN saknar owner
ingen duplicate atomic ID
```

Och challenger ska försöka hitta:

```text
unparsed requirement
mixed-status requirement
wrong replacement
weak evidence
stale evidence
semantic zombie
```

Audit av audit.

Naturligt vid det här laget.

---

# 24. Vi kan till och med skapa ett litet **falsification set för reconciliationen**

Några planterade fall:

### Case 1
Gammal fil saknas men ny arkitektur löser problemet bättre.

Rätt svar:
`SUPERSEDED`, inte `MISSING`.

### Case 2
Gammal fil finns fortfarande men beteendet finns inte.

Rätt svar:
`NOT SATISFIED`.

### Case 3
En gammal dag innehåller fyra olika krav.

Rätt svar:
atomisera.

### Case 4
Implementation finns, bara syntetiska tester.

Rätt svar:
`SATISFIED / VALIDATING`, inte `PROVEN`.

### Case 5
Ny komponent saknar source/problem.

Rätt svar:
`UNTRACED COMPLEXITY`.

### Case 6
Out-of-scope funktion saknas.

Rätt svar:
`ROUTE-OUT`, inte `CAPABILITY GAP`.

### Case 7
En historisk mekanism är numera farlig.

Rätt svar:
`REJECT + supersession tripwire`.

Om audit-processen klarar de fallen litar jag mer på dess slutsatser.

---

# 25. Jag skulle vara försiktig med “completeness score”

Jag tror **inte** på:

> Webbförvaltningen 93.7 % complete.

Det skapar Goodhart direkt.

Ett enda:

```text
customer facts can silently drift after approval
```

kan vara viktigare än 50 mindre gröna saker.

Jag föredrar:

```text
NO UNRESOLVED CRITICAL CLAIMS
NO HIGH-RISK ORPHANS
NO HIGH-RISK UNKNOWN WITHOUT OWNER

14 REQUIRED_LATER
7 REALITY_GAPS
4 TRIGGER_ONLY
```

Det säger mycket mer.

---

# 26. Prioritering efter audit bör vara **consequence-first**

När gap map finns ska vi inte bara fråga hur lätt något är.

Jag skulle prioritera ungefär:

```text
1. trust / factual / legal / irreversible harm
2. customer lifecycle failure
3. inability to know whether we're right
4. repeated operator burden
5. quality capability
6. efficiency
7. optional frontier upside
```

Det betyder exempelvis att:

> final fact approval

förmodligen går före:

> nytt snyggt researchverktyg.

Precis som det borde.

---

# 27. En annan spännande idé: **Mission Coverage**

För varje Webbförvaltningen-uppdrag kan vi till slut uttrycka något som:

```text
UNDERSTAND
Can we correctly understand the organisation/problem?

DECIDE
Can we choose the right intervention?

DESIGN
Can we determine what good should mean here?

BUILD
Can we deliver it?

VERIFY
Can we prove the intended experience works?

LAUNCH
Can we transition safely?

OPERATE
Can we keep it healthy?

IMPROVE
Can we learn from real outcomes?

EXIT
Can the customer leave cleanly?
```

Detta är kanske den verkliga **top-level completeness model**.

Gamla D001–100, masterplanen och current implementation projiceras mot dessa uppdrag.

Om vi upptäcker:

```text
BUILD = extremely mature
OPERATE = weak
EXIT = weak
```

förstår vi förvaltningen mycket bättre än med 100 checklistpunkter.

---

# 28. Jag skulle lägga till **INTERVENE** före BUILD

Dagens Nortropic har redan gjort ett viktigt framsteg här.

Kunden kommer inte nödvändigtvis för att behöva en ny webbplats.

Så hela mission-modellen blir egentligen:

```text
UNDERSTAND
      ↓
DIAGNOSE
      ↓
INTERVENE
      ↓
DESIGN
      ↓
DELIVER
      ↓
VERIFY
      ↓
TRANSITION
      ↓
OPERATE
      ↓
IMPROVE
      ↓
EXIT
```

Det är mycket mer som en **professionell förvaltning** än en hemsidegenerator.

---

# 29. Och “Outcome” måste ligga utanför Quality

Det här knyter tillbaka till vår gamla diskussion om vad en bra hemsida är.

Vi har ungefär:

```text
INTEGRITY
Does it work correctly?

EXPERIENCE
Is it good to use?

OUTCOME
Does it achieve the intended real-world result?
```

Audit ska kontrollera att förvaltningen kan hantera **alla tre**.

Annars kan vi få:

```text
perfect Lighthouse
perfect accessibility
beautiful design

qualified lead rate: terrible
```

och ändå kalla sajten fantastisk.

Det ska Nortropic aldrig göra.

---

# 30. Det kanske viktigaste: **Post-Build Audit bör generera mindre system, inte större**

Efter allt detta låter det som att vi bygger ett stort compliance-monster.

Jag vill motsatsen.

Auditens framgångsmått bör vara:

```text
better certainty
+
fewer orphaned requirements
+
fewer duplicated authorities
+
fewer unnecessary components
+
smaller modern backlog
```

Inte:

```text
more governance files
```

Om 100 historiska dagar + masterplan + frontier-research resulterar i:

> **11 moderna gaps**

är det ett mycket bättre resultat än:

> **143 nya tasks**.

---

# Min nuvarande favoritmodell

Om jag kokar ned hela brainstormingen skulle jag göra framtida operationen i **sju pass**:

**Pass A — Freeze**  
Frys exakt färdig Webbförvaltningen-SHA och runtimebild.

**Pass B — Atomize**  
Bryt 100-dagarsplan + masterplan i små problem/outcome-claims med source IDs.

**Pass C — Trace both ways**  
Requirement → current owner/evidence och current component → source/need.

**Pass D — Assure**  
Claim + evidence + maturity + known defeaters + freshness.

**Pass E — Challenge**  
Coverage Challenger + Simplification Challenger + Real Customer Challenger + några fasta falsification cases.

**Pass F — Compile**  
Deduplicera allt till mission/capability gaps, supersessions, reality gaps och removal candidates.

**Pass G — Intake**  
Skapa endast accepterade moderna candidates och permanenta fitness-function candidates.

Sedan kan vi kasta bort själva “arbetsytan” för analysen och behålla de få permanenta resultaten.

---

## Och då skulle jag byta namn på hela idén

Inte bara:

**Post-Build Reconciliation & Completeness Audit**

utan kanske internt:

# **Nortropic Capability Assurance**

Med första körningen:

> **Webbförvaltningen Capability Assurance — v1**

Det är egentligen vad vi håller på att uppfinna.

Inte certifiering i marknadsföringsbemärkelse.

Utan ett sätt för Nortropic att svara på:

> **Vad påstår den här förvaltningen att den kan göra?**

> **Vilket bevis har den?**

> **Vad kan fälla påståendet?**

> **Vad vet vi fortfarande inte?**

> **Vad ska vi inte bygga igen?**

> **Vad behöver verkligheten lära oss härnäst?**

Det känns väldigt mycket som nästa naturliga steg efter **Capability Catalog + Knowledge Lane + Gym + Trust Kernel**: de beskriver och utvecklar kompetensen; **Capability Assurance bevisar hur långt kompetensen faktiskt räcker.** memcite

---

## Meddelande 11 — Johnny (användare)

Det låter bra, du kollade inget mot person of interests, webbyråer, litteraturen, openai, anthropic osv brainstorming

---

## Meddelande 12 — ChatGPT (assistent)

Precis. **Det var den stora saknade linsen i min förra brainstorming.** Jag jämförde framför allt Nortropic mot Nortropic: gamla planen, nya masterplanen, dagens repo, assurance-/systems-engineering-idéer. Jag gjorde inte en ordentlig **outside-in benchmark mot hur de bästa människorna, agentlabben, webbstudiorna och litteraturen tänker 2026**.

Jag har börjat göra den jämförelsen nu, och den förändrar faktiskt upplägget på ett bra sätt.

## Vi bör lägga till ett femte huvudspår: External Comparator Audit

När Webbförvaltningen är färdig ska vi alltså inte bara ha:

1. 100-dagarsplan → färdigt system
2. DESIGN-FRUSEN masterplan → färdigt system
3. fresh frontier scan
4. real customer/lifecycle audit

utan också:

> **5. External Comparator Audit — vad skulle de bästa externa referensramarna se som Nortropic inte ser själv?**

Och jag skulle medvetet hålla **olika skolor separata**, eftersom de optimerar för olika saker.

---

# 1. OpenAI-linsen: eval-driven verksamhetsutveckling

OpenAI:s riktning är väldigt relevant för det vi precis formulerade.

Deras agentplattform har gått mot built-in **guardrails, tracing och observability**, och senare Evals-utvecklingen lägger till **datasets, trace grading, human annotations och prompt optimization**. OpenAI beskriver dessutom eval-arbetet på affärsnivå som:

> **Specify → Measure → Improve.** citeturn536698search0turn536698search2turn536698search11

Det ligger nästan kusligt nära vår tanke:

```text
Vad betyder excellent?
↓
gör det explicit
↓
observera verkligt beteende
↓
mät
↓
förbättra
```

### Vad jag skulle ta in i Nortropic

Inte OpenAI:s agentframework — det behöver vi inte.

Utan principen att varje större **business capability bör ha ett eval surface**.

Alltså inte bara:

```text
KAP-MIGRATION = BUILT
```

utan kanske:

```text
CAPABILITY
Migration

SPECIFY
What must be true?

DATASET
Which cases exercise it?

TRACE
What actually happened through the workflow?

GRADERS
Deterministic
Agentic
Human
Real-world

IMPROVE
What does failure teach?
```

Det ger oss en viktig ny fråga i Capability Assurance:

> **Har varje kritisk capability ett sätt att systematiskt mäta verklig prestation — eller bara en implementation och några tester?**

---

# 2. Anthropic-linsen är kanske ännu mer träffsäker

Här händer väldigt mycket som direkt berör Nortropic.

Anthropic skriver 2026 uttryckligen att **harnesses kodar antaganden om modellernas begränsningar, och de antagandena blir gamla när modellerna förbättras**. Deras Managed Agents-arbete går därför mot stabila gränssnitt medan implementationen bakom får förändras. citeturn536698search5

Det validerar Provider-Neutral Trust Kernel nästan exakt.

Men det föreslår också något nytt för vår framtida audit:

## **Harness Assumption Audit**

För varje Nortropic-mekanism:

> Varför existerar den?

Exempel:

```text
CUSTOM RETRY LOGIC
↓
Behövs fortfarande?
↓
eller kom den från en tid när providern inte kunde göra X?

CUSTOM CONTEXT SYSTEM
↓
verklig trust boundary?
eller historiskt workaround?

EXTRA AGENT
↓
unik kompetens?
eller modellsvaghet från 2025?
```

Det är **supersession fast mot modellutvecklingen själv**.

---

Anthropics nya arbete med long-running application development är också väldigt relevant. De beskriver en struktur med **planner → generator → evaluator**, konkreta gradable criteria även för subjektiv design, strukturerade artefakter mellan sessioner och verklig end-to-end-browserverifiering. citeturn536698search6turn536698search16

Det stärker flera Nortropic-idéer:

- separera skapare och domare
- kriterier före bedömning
- test som verklig användare
- strukturerad handoff framför chatminne
- designkvalitet kan operationaliseras utan att låtsas vara helt deterministisk

Och deras containment-arbete gör en annan poäng: när agentkapabilitet ökar ökar också potentiell **blast radius**, så frågan blir inte bara “hur ofta gör modellen fel?” utan **“hur mycket kan ett fel påverka?”**. citeturn536698search8

Det skulle jag lägga in som:

### **Capability × Blast Radius**

En capability kan vara:

```text
PROVEN
```

men fortfarande kräva hård containment om dess möjliga skada är stor.

Det är en annan axel än kompetens.

---

# 3. Boris Cherny / Claude Code-linsen

Boris Cherny och Claude Code-teamet är en självklar Person of Interest-grupp för oss, just eftersom Claude Code avsiktligt varit ganska **low-level och opionionated** snarare än ett färdigt processframework. Anthropic beskriver också deras arbetssätt som att integrera Claude i verkliga befintliga codebases snarare än att lägga en stor abstraktion ovanpå. citeturn536698search3turn271807search17

Jag skulle ha en permanent POI-fråga:

> **Bygger Nortropic något som provider-harnessen nu gör bättre själv?**

Det ska vår Frontier Radar kunna flagga.

Inte automatiskt ta bort något.

Men:

```text
PROVIDER CAPABILITY SHIFT
↓
affected Nortropic assumption
↓
candidate simplification
↓
Gym / falsification
↓
keep or retire
```

Det här skulle förhindra att Nortropic blir ett fossil av Claude Code 2025.

---

# 4. Karpathy-linsen: experiment, inte övertygelse

Den vi redan har plockat mycket från.

Men i Capability Assurance skulle jag göra hans inflytande ännu tydligare:

> **Ingen arkitekturdiskussion får vinna bara för att den låter elegant.**

Istället:

```text
hypothesis
one meaningful change
fixed budget
measurement
guards
keep / revert
```

Det gäller inte bara modeller och prompts.

Det kan gälla:

- ny designcanon
- ny researchmetod
- ny capability
- ny reviewer
- nytt verktyg
- borttagning av en agent
- ny onboarding

Alltså:

> **Architecture by falsifiable experiment där det går.**

---

# 5. Martin Fowler / Neal Ford / Rebecca Parsons: Evolutionary Architecture

Här tycker jag att Nortropic och litteraturen möts väldigt fint.

*Building Evolutionary Architectures* beskriver arkitektur som **guided, incremental change across multiple dimensions**, där fitness functions skyddar viktiga egenskaper samtidigt som systemet får utvecklas. citeturn160324search2turn160324search84

Detta är i princip:

```text
Nortropic invariants
+
guards
+
tripwires
+
stale evidence
+
revalidation
```

Men deras perspektiv gör att jag skulle ändra en sak:

### Capability Assurance ska inte bara hitta nya gates.

Den ska fråga:

> **Vilka egenskaper måste överleva förändring?**

Exempel:

```text
UNIVERSAL CORE MUST REMAIN CUSTOMER-AGNOSTIC
PACKETS MAY SHARPEN, NEVER RELAX
NO SECOND SITE QUALITY CONTRACT
REALITY EVIDENCE NEVER REPLACED BY SYNTHETIC EVIDENCE
```

Det är egentligen **architectural characteristics**.

Sedan väljer vi den tunnaste fitness function som kan skydda dem.

---

# 6. Nicole Forsgren / Jez Humble / Gene Kim / DORA

En sak vi fokuserat väldigt mycket på är:

> Hur bra blir sajten?

DORA skulle tvinga oss att även fråga:

> **Hur bra fungerar maskinen som förändrar sajten?**

DORA:s forskningsprogram fokuserar på capabilities som driver software delivery och organizational performance. citeturn160324search16

Så Webbförvaltningen borde kanske ha **två olika performance planes**:

### Customer Product Performance

- user outcomes
- conversion
- accessibility
- reliability
- SEO
- business outcomes

### Delivery System Performance

- lead time
- time to validated preview
- failure/rework rate
- recovery time
- human wait
- amount of repeated work
- cost
- failed autonomous attempts

Det här blir väldigt intressant för Aquarium senare.

---

# 7. Charity Majors / observability-skolan

Här är den principiella lärdomen viktigare än någon specifik produkt:

> Monitoring svarar på frågor du visste att du skulle behöva ställa.  
> Observability hjälper dig förstå systemtillstånd du inte förutsåg.

Det bör påverka Aquarium och Care.

Vi ska inte bara bygga:

```text
50 GREEN DASHBOARD METRICS
```

utan se till att:

```text
run
↓
trace
↓
events
↓
artifacts
↓
decisions
```

går att undersöka när något **konstigt och nytt** händer.

Det stärker också min idé om att Assurance Graph bör vara drillable till evidens istället för att visa en magisk score.

---

# 8. Google SRE är mycket viktigare för Webbförvaltningen än jag först tänkte

SRE:s kanske viktigaste princip för oss:

> **Definiera SLO:er så som användaren upplever tjänsten.**

Google ger exempel på att mätning vid klienten gav en mycket ärligare bild än servermått. citeturn394154search0

Översatt till Nortropic:

Fel:

```text
form endpoint = 200
```

Rätt:

```text
kunden fick faktiskt leadet
```

Och det gör Nortropic redan på Gate 1.

Det är **ren SRE-filosofi**.

Men vi kan gå längre i Care.

## Web Service SLO

Exempel:

```text
Primary journey success
99.x%

Lead delivery success
99.x%

Critical pages available
99.x%

Valid primary CTA journey
99.x%

Critical facts stale
0 high-risk

Known redirect failures
0
```

Inte för att jaga 100 %.

Google argumenterar uttryckligen för att **100 % reliability i regel är fel target**, och använder error budgets för att balansera förändring och stabilitet. citeturn394154search1turn394154search2

Det ger en väldigt intressant framtida princip:

> När en kundsajt bränner sin reliability/quality budget → Growth-experiment pausar och Care/reliability får företräde.

Det är mycket bättre än:

> “vi fortsätter lägga till saker samtidigt som formuläret är ostabilt.”

---

# 9. Lou Downe / *Good Services* är nästan skriven för vår kommunmetafor

Det här var en av de mest träffsäkra externa jämförelserna.

Lou Downe har 15 principer för bra tjänster, bland annat att en tjänst ska:

- vara lätt att hitta
- förklara sitt syfte
- låta användaren nå sitt faktiska mål
- inte exponera organisationens interna struktur
- minimera steg
- undvika dead ends
- vara användbar för alla
- reagera på förändring
- förklara beslut
- göra mänsklig hjälp lättillgänglig. citeturn271807search1

Två saker slår mig direkt.

### A. Nortropic ska utvärdera **tjänsten**, inte bara sajten

Kunden som skickar offertformuläret bryr sig inte om:

```text
website boundary
CRM boundary
email boundary
customer business boundary
```

Den vill få sitt problem löst.

Det stärker vår:

> **Solve the whole problem**

-lins.

### B. Kunden ska aldrig behöva förstå Nortropics kommun

Lou Downes princip säger uttryckligen att bra tjänster bör vara agnostiska mot organisationens interna struktur. citeturn271807search1

Det här är en fantastisk Organization OS-regel:

> **Kommunmetaforen är för Nortropics interna intelligens — aldrig kundens kognitiva belastning.**

Kunden ska inte behöva veta:

> “är detta Care-enheten eller Growth-enheten?”

Den ska säga:

> “mitt telefonnummer har ändrats.”

Och Nortropic routar resten.

Det tycker jag är en **ny värdefull designprincip**.

---

# 10. GOV.UK Service Standard är också nästan en extern Webbförvaltningen-spec

Den säger bland annat:

- understand users and their needs
- solve a whole problem
- joined-up experience across channels
- simple to use
- accessible
- multidisciplinary team
- iterate continuously
- security/privacy
- define success and measure it
- choose appropriate technology
- operate a reliable service. citeturn160324search3

Och januari 2026 uppdaterades deras standard med bland annat uttrycklig AI-kompetens när AI används i tjänsten. citeturn160324search0

Det här skulle jag absolut använda som **extern falsifieringslins**.

Inte importera standarden.

Men fråga:

> Om någon från GOV.UK Service Standard gjorde en assessment av Nortropics Webbförvaltning — vilka frågor skulle vi få svårt att besvara?

Det är exakt typen av outside-in challenge vi vill åt.

---

# 11. Team Topologies förändrar hur jag ser “förvaltningen”

Webbförvaltningen liknar i praktiken en **stream-aligned value-delivery function**.

Trust Kernel och gemensam infrastruktur liknar platform capabilities.

Gym/Knowledge Lane har mycket av rollen hos ett **enabling team**: de ska höja förmågan hos de som faktiskt levererar värde, inte själva bli ett parallellt produktlager.

Team Topologies betonar dessutom **Thinnest Viable Platform** och att plattformar ska minska consuming teams' cognitive load, inte skapa mer. citeturn154212search1turn154212search9

Det ger oss en ny auditfråga:

> **Minskar den här Nortropic-komponenten Webbförvaltningens kognitiva/operativa belastning — eller skapar den ytterligare koordinering?**

Det är ett väldigt bra filter mot governance-bloat.

Och det gäller Organization OS senare:

> Organisation OS får **inte kräva att varje worker förstår Organization OS**.

---

# 12. Brad Frost / design systems

D038 från gamla planen ser ännu mer relevant ut efter detta.

Brad Frost betonar att design systems behöver:

- tydligt ownership
- governance
- adaptation
- feedback från faktiska användare av systemet
- inte bli en rigid source of truth som tvingar fel lösning på alla produkter. citeturn271807search15

Det är nästan exakt risken med en för stark Nortropic Design Canon.

Jag skulle därför lägga till:

## **Canon Pressure Test**

Fråga kontinuerligt:

> Hjälper kanonen agenterna till bättre beslut?

eller:

> Har kanonen börjat skapa sibling convergence?

En designregel ska kunna:

```text
ADOPT
→
VALIDATE
→
EVOLVE
→
DEPRECATE
```

precis som andra capabilities.

---

# 13. Addy Osmani: performance **budgets**, inte bara thresholds

Det här är en subtil men bra skillnad.

Addy Osmani beskriver performance budgets som något man **medvetet spenderar och gör tradeoffs med**, inte bara som ett slutligt rött/grönt test. citeturn271807search14

Nortropic har redan performance gates.

Men vi skulle kunna ha:

```text
EXPERIENCE BUDGET

JS
images
fonts
third-party
motion
widgets
network requests
```

Om kunden vill ha:

> stor videohero

så blir frågan inte:

> “video förbjudet”.

Utan:

> “vilken budget kostar detta, och vad tar vi bort/optimerar för att bära det?”

Det är betydligt mer professionellt.

---

# 14. Webbyråerna säger också något ganska tydligt

Jag tittade på några etablerade digitala produkt-/webbstudior som jämförelse.

### Build in Amsterdam

De beskriver själva ordningen som **strategy → design → technology**, med research, KPI-alignment, design system, implementation och därefter **platform monitoring and optimization**. citeturn668619search0turn668619search1

Deras nyare “digital flagship”-modell beskriver dessutom:

> Foundation → Idea → Expression → Delivery → ongoing refinement. citeturn668619search16

### ustwo

Deras erbjudande är explicit livscykelorienterat:

> **Discover → Shape → 0–1 → Boost**

med user research, hypothesis testing, beta testing, business readiness och sedan fortsatt iteration/scaling. citeturn668619search2

### Instrument

Positionerar sig tvärdisciplinärt över **brand + product + marketing**, så att alla touchpoints hänger ihop, snarare än att webbplatsen lever som en isolerad artefakt. citeturn668619search13

### DEPT

Tänker ännu bredare kring **customer journey, technology/data, growth och measurement/learning**. citeturn668619search8turn668619search18

---

# Vad detta säger om Nortropic

Det är inte:

> “kopiera Build in Amsterdam.”

Tvärtom.

Men toppbyråerna bekräftar ett mönster:

```text
RESEARCH / STRATEGY
↓
DESIGN
↓
BUILD
↓
LAUNCH
↓
MEASURE
↓
OPTIMIZE
↓
LONG-TERM PARTNERSHIP
```

Och därför blir gamla **D61–90 plötsligt ännu viktigare**.

Om Nortropic bara blir världsklass på:

```text
research → plan → build → gate
```

har vi byggt en otroligt avancerad **production function**.

Inte ännu en komplett **webbförvaltning**.

---

# 15. Det ger oss en ny jämförelse: “Nortropic vs agency operating model”

Jag skulle lägga in en separat comparator-tabell i auditkampanjen:

| Dimension | Nortropic | Leading studio pattern | Gap? |
|---|---|---|---|
| Discovery | ? | research + stakeholder/user understanding | |
| Intervention choice | ? | ofta starkt | |
| Strategy | ? | starkt | |
| Brand/design | ? | starkt | |
| Prototyping | ? | ofta före full build | |
| Engineering | ? | starkt | |
| Accessibility | ? | varierande | |
| QA | ? | starkt | |
| Business readiness | ? | ofta explicit | |
| Launch | ? | | |
| Monitoring | ? | | |
| Optimization | ? | | |
| User research after launch | ? | | |
| Growth | ? | | |
| Ownership/exit | ? | | |

Och det spännande är:

**Nortropic kan mycket väl vara starkare än webbyråerna på vissa saker.**

Till exempel:

- traceability
- factual provenance
- adversarial testing
- reproducibility
- explicit autonomy boundaries
- synthetic falsification
- knowledge governance

Vi behöver alltså leta efter **både underskott och Nortropic advantages**.

---

# 16. Litteraturspåret bör vara mycket bredare än bara AI-böcker

Jag skulle skapa några “schools of thought” för auditkampanjen:

### Systems / architecture
- *Building Evolutionary Architectures*
- *Thinking in Systems*
- *The Fifth Discipline*
- cybernetics / feedback systems

### Software delivery
- *Accelerate*
- *Continuous Delivery*
- DORA
- Google SRE

### Organization
- *Team Topologies*
- *The Goal*
- Theory of Constraints
- socio-technical systems

### Product
- *Escaping the Build Trap*
- *Continuous Discovery Habits*
- *Inspired / Empowered*
- Jobs to Be Done

### Service design
- *Good Services*
- *This is Service Design Doing*
- GOV.UK Service Manual

### UX / design
- Don Norman
- Nielsen Norman
- Brad Frost
- Baymard
- accessibility practitioners

### Strategy
- *Good Strategy/Bad Strategy*
- Wardley Mapping
- optionality / real-options thinking

### Learning / safety
- SRE postmortem culture
- resilience engineering
- normal accident / complex-system thinking

Vi ska absolut **inte implementera böcker**.

Vi använder dem som olika adversarial perspectives.

---

# 17. Person of Interest-radarn bör inte bara följa “AI-kändisar”

Jag skulle dela den i roller.

### Agent / AI engineering
- Boris Cherny
- Claude Code/Anthropic engineering-teamet
- Andrej Karpathy
- OpenAI agent/evals-folk
- personer som jobbar med harnesses, evals och tool design

### Systems / reliability
- Charity Majors
- Nicole Forsgren
- Jez Humble
- Gene Kim
- Martin Fowler
- Neal Ford / Rebecca Parsons

### Organization
- Matthew Skelton
- Manuel Pais

### Service/product
- Lou Downe
- Teresa Torres
- Marty Cagan
- Melissa Perri

### Web quality
- Addy Osmani
- Brad Frost
- Sara Soueidan
- web.dev/W3C-practitioners
- Baymard researchers

### Human factors / complexity
- Donella Meadows
- Sidney Dekker
- John Allspaw / resilience engineering-skolan

Poängen är inte:

> “vad tweetade X idag?”

utan:

> **Vilken fråga är X ovanligt bra på att ställa som Nortropic borde utsättas för?**

---

# 18. Det här leder till något jag gillar mycket: **Council of Lenses**

Inte faktiska permanenta AI-agenter.

Mer som review perspectives.

När Webbförvaltningen är klar kan vi köra:

```text
ANTHROPIC LENS
Are we duplicating the harness?
Are assumptions stale?

OPENAI LENS
Can we actually evaluate the capability end-to-end?

SRE LENS
What does the user experience as reliability?

DORA LENS
How good is the delivery system?

TEAM TOPOLOGIES LENS
Where are we creating cognitive load?

GOOD SERVICES LENS
Do we solve the whole user problem?

AGENCY LENS
Could this operate as a real client service over years?

EVOLUTIONARY ARCHITECTURE LENS
Which qualities survive change?

DESIGN SYSTEM LENS
Has standardization become constraint?

CUSTOMER LENS
Do I care about any of this, or can you just solve my problem?
```

Det är **mycket starkare** än en enda generisk “expert reviewer”.

---

# 19. Och challengers ska få hitta *novel requirements*

Det här är viktigt.

100-dagarsplanen innehåller redan kända requirements.

Masterplanen innehåller kända requirements.

Men External Comparator Audit får svara:

```text
NOVEL_REQUIREMENT
```

Exempel på möjliga sådana som jag redan ser från första researchrundan:

### `HARNESS_ASSUMPTION_FRESHNESS`
Custom infrastructure måste kunna motivera varför provider-native capability inte räcker längre.

### `SERVICE_NOT_ORG_STRUCTURE`
Kunden får aldrig behöva förstå Nortropics interna förvaltningsstruktur.

### `DELIVERY_SYSTEM_PERFORMANCE`
Förvaltningen behöver mäta sin egen förändringsförmåga, inte bara sajtens kvalitet.

### `USER-CENTRIC_SERVICE_SLO`
Care/reliability bör mätas från användarens affärskritiska journey.

### `CAPABILITY_BLAST_RADIUS`
Kompetens och authority/risk är separata dimensioner.

### `CANON_ADAPTABILITY`
En designcanon måste kunna degraderas/deprekeras när den själv orsakar likriktning.

### `EXPERIENCE_BUDGET`
Motion, JS, media och third-party-kostnad bör vara en budgeterad tradeoff, inte bara slutgrind.

### `WHOLE_SERVICE_OUTCOME`
Webbplatsens tekniska boundary får inte definiera användarens outcome-boundary.

Det här är exakt varför outside-in-linsen behövs.

---

# 20. Och det finns ett ännu mer radikalt comparator-spår: **“What would kill the agency?”**

Inte bara best practices.

Fråga etablerade byråmodeller indirekt:

> Varför går webbyråprojekt dåligt?

- dålig scope
- fel kundproblem
- endless revisions
- väntan på kundmaterial
- design utan outcome
- migrationsmiss
- ansvar efter launch oklart
- support som äter marginal
- osynliga recurring costs
- senior kunskap fastnar i individer
- custom tech blir maintenance burden
- ingen verklig lead/outcome feedback
- kunder lämnar för att de inte ser värdet

Sedan:

> **Vilka av dessa byråfailure modes har Nortropic gjort strukturellt omöjliga?**

och:

> **Vilka kan fortfarande hända?**

Det är en fantastisk slutreview.

---

# Så jag skulle nu uppgradera modellen igen

Det framtida arbetet blir:

```text
               WEBBFÖRVALTNINGEN COMPLETE
                          │
                          ▼
                     FREEZE SHA
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
 HISTORICAL          MASTERPLAN         CURRENT REALITY
 RECONCILIATION      RECONCILIATION
        │                 │                 │
        ├─────────────────┼─────────────────┤
                          │
                   EXTERNAL COMPARATORS
                          │
     ┌────────────┬───────┼────────┬────────────┐
     ▼            ▼       ▼        ▼            ▼
  OpenAI      Anthropic   POIs   Literature   Agencies
     │            │       │        │            │
     └────────────┴───────┼────────┴────────────┘
                          ▼
                   NOVEL CHALLENGES
                          │
                  REAL CUSTOMER LENS
                          │
                     ADVERSARIAL
                          │
                          ▼
                CAPABILITY ASSURANCE
                          │
                 MODERN GAP COMPILER
                          │
                 ┌────────┼────────┐
                 ▼        ▼        ▼
                ADD     REMOVE    PROVE
                 │        │        │
                 └────────┼────────┘
                          ▼
                  NORTROPIC INTAKE
```

Och **Fresh Frontier/Kunskapsbanan ligger bredvid**, så aktuella externa förändringar blir candidates och inte direkt authority.

---

## Min slutsats efter den här första outside-in-rundan

Det här förstärker snarare än försvagar det vi byggt.

Jag ser framför allt fyra stora saker:

**Nortropics Trust/assurance-tänk ligger ovanligt långt fram** jämfört med vanlig webbbyråpraktik.

**Webbförvaltningens research/capability-arkitektur ligger väldigt rätt i tiden** jämfört med moderna agentprinciper: stable interfaces, explicit evals, structured handoffs, provider/harness separation.

Men **den verkliga service lifecycle-delen måste bli lika stark som byggmotorn**. GOV.UK, Good Services, SRE, ustwo och de bättre byråmodellerna pekar alla åt samma håll: discovery → outcome → delivery → live operation → learning → evolution. citeturn160324search3turn271807search1turn668619search2

Och vi bör lägga till en permanent princip som jag inte tycker vi formulerat tillräckligt tydligt tidigare:

> **Nortropic ska inte optimera för att bygga webbplatser.  
> Nortropic ska optimera för att lösa och långsiktigt förvalta det användar- och verksamhetsproblem där webben är rätt intervention.**

Där tycker jag att **Webbförvaltningen** verkligen går från “extremt avancerad website factory” till något som förtjänar ordet **förvaltning**. memcite

---

## Meddelande 13 — Johnny (användare)

Mycket bra, är nortropic intake nästa steg tillsammans med en prompt eller hur vill du gå tillväga? eller nåt du behöver göra mer mot nuvarande etc? vill du brainstorma djupare på något?

---

## Meddelande 14 — ChatGPT (assistent)

Ja. Efter att ha tittat på **hur den uppdaterade Nortropic Intake faktiskt fungerar nu** tycker jag att vi har ett väldigt bra upplägg — och det är lite bättre än att vänta tills Webbförvaltningen är klar och då börja från noll.

Den nya Intake-modellen är nästan skräddarsydd för detta. Den är byggd för att en idé ska kunna få **flera källepisoder över tid**, därefter en ny context revision, ett intellektuellt delta, ny destillation/audit och först därefter planering. Den skiljer dessutom uttryckligen mellan råmaterial, varför, vad, ägarbeslut, planförslag och godkänd plan. fileciteturn60file0L1-L2

## Jag skulle använda Intake i två omgångar

**Omgång A gör vi nu:** fånga det vi har tänkt fram som ett eget långlivat Intake-paket, exempelvis:

**`webbforvaltningen-capability-assurance`**

Det paketet ska **inte säga “bygg dessa saker”**. Dess VAD är ungefär:

> Genomför efter färdigställandet av Webbförvaltningen en read-only, evidensbunden Post-Build Reconciliation & Capability Assurance för att fastställa vad förvaltningen faktiskt kan, vad som saknas, vad som ersatts, vad som endast saknar verklighetsevidens, vad som bör tas bort och vilka externa nya krav som är värda att föra vidare.

Där kan vi fånga **hela den här brainstormingen nu**: 100-dagarsreconciliation, masterplan reconciliation, assurance graph, orphan detection, supersession ledger, external comparators, OpenAI/Anthropic/POI/litteratur/webbyråer, real-customer-linsen, challengers, proof maturity, reality gaps osv.

Sedan ligger paketet still.

**Omgång B sker när pågående Webbförvaltningen verkligen är färdig.** Då lägger vi inte upp en ny idé. Intake-modellen säger uttryckligen att när samma grundidé återkommer med en ny brainstorm, ett dokument eller webbresearch ska det bli **en ny källepisod under samma slug**, inte en ny parallell idé. fileciteturn60file0L1-L2

Då tillför vi exempelvis:

- final `nortropic-system/main` SHA
- final `verkstadsgolvet/main` SHA där relevant
- slutrapporten från Webbförvaltningen
- den slutliga DESIGN-FRUSNA planen
- final current docs/contracts/capability catalog/packets/Gym/evals
- eventuell runtime-inventering
- 100-dagarsmanualen
- vår nya external-comparator-research, färsk vid just den tidpunkten

Och Intake gör en **ny context revision**. Den befintliga mekanismen kräver då context delta, omdestillation och ny distillation audit innan planering får börja. Det är precis den säkerhetsventil vi vill ha. fileciteturn60file0L1-L2

---

# Jag vill däremot inte starta själva jämförelse-auditen nu

Det är den viktiga gränsen.

Webbförvaltningen ändras medan vi pratar. Det senaste `nortropic-system/main` jag läste tidigare idag var redan överspelat några timmar senare. Om vi börjar döma:

> SATISFIED / PARTIAL / OPEN

nu, kommer vi auditera ett rörligt mål och sedan behöva göra om mycket av arbetet.

Så:

**capture nu — evaluate senare.**

Det är också filosofiskt rätt enligt Intake. Den säger att **VERKLIGHETEN läses färskt varje gång**, och att Intake bevarar intention/proveniens men aldrig ska bli exekverings- eller runtime-authority. fileciteturn60file0L1-L2

---

# Jag skulle inte heller låta assurance-paketet implementera sina egna fynd

Det här tycker jag är en viktig designförbättring.

Vi separerar:

### Campaign 1 — Capability Assurance

Read-only.

Producerar exempelvis:

- atomic coverage matrix
- mission coverage
- assurance claims
- orphaned requirements
- supersession/rejection ledger
- gap map
- reality/evidence gaps
- removal candidates
- fitness-function candidates
- novel external requirements
- unresolved/high-risk unknowns

Men **ändrar inte Webbförvaltningen**.

Sedan granskar du resultatet.

### Campaign 2 — Implementation Intake

Endast de fynd du faktiskt accepterar får bli riktiga implementation candidates.

Om audit hittar:

> 31 historiska avvikelser

men de efter deduplicering egentligen är:

> 6 moderna capabilities  
> 2 saker att ta bort  
> 3 reality gaps som bara behöver riktiga kunder  
> 4 trigger-only  
> 16 superseded/no-action

då bygger vi **inte 31 saker**.

Det är väldigt viktigt för att undvika att assurance-systemet producerar governance-bloat.

---

# Jag vill också lägga till ett explicit “No-build contract” för första kampanjen

Auditplanen bör säga ungefär:

```text
READ_ONLY_TARGET_REPOS=YES
IMPLEMENT_FINDINGS=NO
CREATE_NEW_RUNTIME_AUTHORITY=NO
CHANGE_GATES=NO
CHANGE_BASELINES=NO
CHANGE_CAPABILITY_STATUS=NO
PROMOTE_EXTERNAL_IDEA=NO
```

Den får alltså säga:

> “D64:s finala kundfaktagodkännande verkar sakna modern ägare.”

Men inte:

> “Jag byggde CLIENT-FACT-APPROVAL.json.”

Det beslutet kommer **efter** assurance.

---

# Något jag vill brainstorma lite djupare innan vi fryser själva auditdesignen

Ja — det finns några områden där ytterligare tänkande är värt mödan. Inte mer generell idéspåning, utan några **konkreta designfrågor**.

### 1. Vad betyder exakt “Webbförvaltningen complete”?

Det här är den viktigaste.

Vi behöver skilja:

**Build Complete**  
den DESIGN-FRUSNA exekveringsplanen är genomförd.

från:

**Capability Complete**  
alla in-scope verksamhetsförmågor har ägare och implementering eller explicit boundary.

från:

**Assurance Complete**  
vi har granskat claims/gaps och vet vad som är bevisat, validating, trigger-only osv.

från:

**Proven**  
verkligheten har faktiskt gett tillräcklig evidens.

Dagens Nortropic gör redan rätt genom att kalla centrala kompetenser `VALIDATING`, inte `PROVEN`, när riktig kundevidens saknas.

Så vi får inte låta:

> “Claude byggde klart masterplanen”

betyda:

> “Webbförvaltningen är verklighetsbevisad.”

Jag tror alltså vi vill ha:

```text
BUILD_COMPLETE
       ↓
CAPABILITY_ASSURANCE
       ↓
V1_READY / GAPS_KNOWN
       ↓
REAL CUSTOMER EVIDENCE
       ↓
PROVEN grows capability-by-capability
```

Det känns robust.

---

### 2. Auditens top-level mission model

Jag tycker vi ska frysa en semantisk toppmodell, eftersom den hjälper oss att inte drunkna i 100 dagar.

Min nuvarande favorit:

```text
UNDERSTAND
↓
DIAGNOSE
↓
INTERVENE
↓
DESIGN
↓
DELIVER
↓
VERIFY
↓
TRANSITION
↓
OPERATE
↓
IMPROVE
↓
EXIT
```

Varje atom från gamla planen, nya planen, current repo och externa comparators kan mappas mot en eller flera av dessa.

Då kan vi till slut säga något mycket mer meningsfullt än:

> 87/100 gamla dagar lösta.

Exempelvis:

```text
UNDERSTAND    strong
DIAGNOSE      strong
INTERVENE     strong
DESIGN        partial
DELIVER       strong
VERIFY        strong
TRANSITION    partial
OPERATE       weak
IMPROVE       validating
EXIT          partial
```

Inte som score — som strukturell bild.

Det kan avslöja asymmetrier mycket snabbt.

---

### 3. Vilka externa comparator-skolor ska verkligen vara kanon för audit?

Inte authority — **challenger lenses**.

Jag tror ungefär följande räcker:

- Anthropic / Claude Code — harness assumptions, long-running agents, containment
- OpenAI — evals, trace grading, datasets, agent lifecycle
- Karpathy — falsifiable experiments
- Google SRE — user-visible reliability, SLO/error-budget-tänk
- DORA / Accelerate — delivery-system performance
- Evolutionary Architecture — fitness functions
- Team Topologies — cognitive load / thin platform / enabling capability
- Good Services / GOV.UK — whole-service/user-outcome lens
- service/product discovery — continuous discovery / build-trap
- web UX/accessibility/performance — W3C, Baymard, web.dev, Brad Frost etc.
- selected high-end agencies — actual agency lifecycle/business model
- resilience/human factors — failure handling, learning, brittle automation

Jag skulle hellre ha **12 skarpa linser** än 80 personer.

Sedan kan POI-radarn ge färska personer/artiklar inom varje lins.

---

# En sak till som jag skulle lägga till nu: Counterfactual Audit

Den har vi inte riktigt pratat om.

Efter att systemet är klart frågar en reviewer:

> **Om vi byggde Webbförvaltningen från noll idag, med all kunskap vi nu har, vilka delar av dagens system skulle vi INTE bygga?**

Det är en väldigt stark simplification-lins.

För normalt frågar vi:

> Vad saknas?

Counterfactual-reviewern frågar:

> Vad har vi kvar bara för att historien råkade gå den vägen?

Exempel:

- agent som inte längre har unik uppgift
- två överlappande design skills
- historical workaround för modellbegränsning
- duplicated docs surface
- gammal local-SE assumption som överlevt universalisation
- manual approval som numera inte bär judgement
- tool som blivit provider-native

Output kan bli:

```text
KEEP
SIMPLIFY
MERGE
RETIRE
```

Det tror jag blir väldigt värdefullt.

---

# Och en “Agency economics” lins

Det här är en annan sak vi bör lägga till när vi pratar om en **förvaltning**, inte bara system engineering.

Fråga:

> Kan den här verksamheten levereras ekonomiskt hållbart?

Det handlar inte om att bestämma priser i kod.

Men assurance bör kunna se:

- var mänsklig tid återkommer
- var kunden blockerar
- hur många reworkrundor normalt krävs
- kostnad per build
- kostnad per Care-kund
- vilka capabilities som skapar dyr support
- vilka external vendors som ger återkommande kostnad
- vilka kundtyper som är dålig fit
- vilka “premium”-features som förstör marginal
- om Care faktiskt är lönsamt
- om ett väldigt sofistikerat kvalitetssystem blir dyrare än kundvärdet

Det är ett perspektiv jag tycker både vår gamla plan och mycket av den nya tekniska arkitekturen lätt kan underskatta.

> **World-class men ekonomiskt ohållbar är inte en bra förvaltning.**

Så mission model kanske får en tvärgående dimension:

```text
QUALITY
TRUST
CUSTOMER VALUE
OPERABILITY
ECONOMICS
LEARNING
```

Inte för att varje sajt ska få ett economics score, utan för att förvaltningen som verksamhet måste hålla.

---

# En sista lins: “Operator independence”

Gamla D097 var inne på det.

Men med Organization OS blir den större:

> Om du försvinner från tangentbordet en vecka, vad slutar fungera för att Nortropic egentligen fortfarande bor i ditt huvud?

Inte credentials eller juridiska beslut som medvetet ska vara mänskliga.

Utan dold kunskap såsom:

> “när den där grinden säger X brukar jag egentligen göra Y.”

eller:

> “Claude ska få den här extra instruktionen som inte står någonstans.”

Det borde Capability Assurance aktivt leta efter.

Kalla det:

**Tacit Dependency Audit**

Resultat:

```text
legitimate human judgment
vs
undocumented operator workaround
```

De två får inte blandas ihop.

---

# Så här skulle jag gå tillväga praktiskt

**Nu, medan bygget fortsätter:**

1. Vi stör inte Webbförvaltningen.
2. Vi använder Nortropic Intake för att **fånga den här audit-idén och brainstormingen** som ett nytt paket.
3. Status hålls som `idea`. Ingen implementation.
4. Eventuellt fortsätter vi brainstorma och lägger det som fler CHAT-/WEB-/GITHUB-episoder i samma paket.

Det här passar Intake exakt: samma idé kan få nya källepisoder, medan råmaterialet bevaras separat och senare revisioner bara destillerar den aktuella förståelsen. fileciteturn60file0L1-L2

**När Webbförvaltningen rapporterar BUILD_COMPLETE:**

5. Verifiera verkligen final main.
6. Frys exact SHA(s).
7. Lägg slutrapport + final repo snapshot som nya source episodes.
8. Gör färsk external-comparator research **då**, inte från en veckogammal snapshot.
9. Revidera Intake-context.
10. Kör distillation audit.
11. Planera **auditkampanjen**, inte implementationen.
12. Du godkänner auditplanen.
13. Kör Capability Assurance read-only.
14. Granska fynden.
15. Endast accepterade gaps går tillbaka genom Intake som riktiga förändringskandidater.

---

Och den nuvarande Intake-korpusen visar att det **inte redan finns någon särskild `webbforvaltningen-capability-assurance`-idé**; närliggande paket är bland annat Organization OS, Frontier Observatory, workflow/orchestration och engineering-spåren. fileciteturn61file0L1-L7

Så jag skulle **inte** lägga detta som en episod under exempelvis Organization OS. Det här har ett eget mål och bör ha en egen lineage.

### Därför är min rekommendation:

**Ja — Nortropic Intake är nästa steg redan nu, men endast för att fånga och strukturera Capability Assurance-idén.**

**Själva jämförelsen väntar tills Webbförvaltningen är BUILD_COMPLETE och vi kan binda den till ett finalt main-SHA.**

Och innan dess tycker jag inte vi behöver göra någon mer analys av den **nuvarande halvfärdiga Webbförvaltningen**. Det skulle mest producera stale conclusions.

Däremot tycker jag absolut att vi kan göra **ett sista riktigt djupt designpass på själva Capability Assurance-metoden** — framför allt mission model, comparator council, counterfactual/minimality, agency economics och tacit dependency — och sedan stoppa brainstormingen och skicka in den till Intake. Där har vi fortfarande hög hävstång utan att störa bygget. memcite

---

## Meddelande 15 — Johnny (användare)

det låter bra och jag vill vara säker på att vi har kontroll över alla variabler, nåt som är viktigt att vi verkligen bygger hemsidor utifrån vad litteraturen och proffsen säger är hur man gör hemsidor samtidigt som vi har utvinnit emil kowalski, taste, impeccable och de här populära från github så vi gör icke ai slop hemsidor med super b quality etc

---

## Meddelande 16 — ChatGPT (assistent)

Ja — och det här tycker jag är **en av de viktigaste sakerna att få rätt innan vi fryser Capability Assurance-idén i Intake**.

Det finns egentligen två separata mål som lätt blandas ihop:

> **1. Nortropic ska bygga objektivt bra webbplatser enligt webbforskning, standarder, UX-litteratur och professionell praxis.**

och

> **2. Nortropic ska bygga webbplatser med ovanligt hög craft, smak, särart och polish — utan den konvergerande AI-estetiken.**

Det ena får aldrig ersätta det andra. En extremt vacker Emil/Impeccable-sajt som människor inte förstår är dålig. En perfekt WCAG-/Lighthouse-sajt som ser ut som AI-template #418 är inte heller nivån vi vill åt.

Och när jag kontrollerar **dagens fortfarande pågående `main`** ser jag att vi faktiskt har mycket av råmaterialet men ännu inte den slutliga syntesen. Main har redan hunnit gå vidare till `9e85d7ba...`, där extern bokning precis gått från `DECLARED` till `BUILT`. fileciteturn63file0L1-L10 Samtidigt laddar dagens `design-reviewer` fortfarande **alla åtta designkällorna samtidigt**: `web-design-guidelines`, `ui-ux-pro-max`, `taste`, `impeccable`, `soft-skill`, `emil-design-eng`, `find-animation-opportunities` och `frontend-design`. fileciteturn64file0L1-L2

Det betyder för mig:

> **Vi har ingredienserna. Efter bygget måste vi verifiera att vi har gjort dem till ett kök — inte bara ställt åtta väldigt duktiga kockar vid samma kastrull.**

## Jag skulle bygga ett “Nortropic Web Excellence Model”

Inte nu som ny runtime. Detta blir en viktig del av Capability Assurance-auditen.

Jag skulle dela vad “världsklass webb” betyder i ungefär dessa områden:

| Domän | Frågan Nortropic måste kunna besvara |
|---|---|
| **Problem / intervention** | Behöver kunden ens en ny webbplats? |
| **User needs / jobs** | Vad försöker riktiga människor åstadkomma? |
| **Business outcome** | Vilket verksamhetsresultat ska sajten påverka? |
| **Information architecture** | Hittar människor rätt information och väg? |
| **Content** | Är innehållet användbart, konkret, idiomatiskt och faktatroget? |
| **Conversion / action** | Kan användaren faktiskt slutföra primärhandlingen? |
| **Trust** | Finns verkliga, korrekt attribuerade skäl att tro på företaget? |
| **Brand expression** | Känns sajten specifik för just den verksamheten? |
| **Visual hierarchy** | Förstår ögat vad som är viktigt utan instruktion? |
| **Typography** | Är typografi, rytm, längd och hierarki professionellt hanterade? |
| **Composition / grid / spacing** | Finns avsikt och rytm snarare än templatesektioner? |
| **Color** | Bär färg funktion, brand och hierarki snarare än trend? |
| **Imagery** | Är bilder relevanta, autentiska, rättighetsklara och väl komponerade? |
| **Interaction** | Finns rätt feedback, states, affordances och felbeteenden? |
| **Motion** | Förklarar/förstärker rörelse eller är den bara dekoration? |
| **Mobile** | Är mobilen designad som egen upplevelse, inte krympt desktop? |
| **Accessibility** | Kan människor med olika förutsättningar använda tjänsten? |
| **Performance** | Upplevs sajten snabb och responsiv i verkligheten? |
| **Findability / SEO** | Kan rätt människor hitta rätt innehåll? |
| **Security / privacy** | Är användaren och kunden skyddade? |
| **Technical quality** | Är implementationen robust, semantisk och reproducerbar? |
| **Maintainability** | Kan sajten ändras utan att allt faller ihop? |
| **Lifecycle / migration** | Kan vi säkert ersätta/flytta en befintlig sajt? |
| **Outcome / learning** | Vet vi efter launch om den faktiskt fungerar? |
| **Distinctiveness** | Skulle denna sajt kunna byta logotyp med fem andra AI-sajter utan att märkas? |

Det här är mycket närmare vad jag menar med **“kontroll över alla variabler”**.

Inte att vi kan bevisa att vi listat varje tänkbar variabel i universum — det kan ingen. Utan att vi har en **coverage-modell där en viktig webbdimension inte kan försvinna bara för att ingen agent råkade tänka på den**.

---

# Sedan måste källorna ha olika auktoritet

Det här tycker jag är avgörande.

Vi ska **inte** göra:

> Emil + Impeccable + Taste + Baymard + WCAG → stor Markdownfil → “designcanon”.

De svarar på helt olika frågor.

### W3C / WCAG

Detta är standards-/accessibilityplanet. WCAG 2.2 har testbara, teknikoberoende success criteria och är inte något Taste eller en referenssajt får rösta bort. citeturn258112search10turn258112search20

### web.dev / browser-/performancekällor

De äger frågor som LCP, CLS, INP och praktisk webperformance. Web.dev beskriver exempelvis LCP som laddningsupplevelse, CLS som visuell stabilitet och INP som respons på användarinput. citeturn258112search8

### Baymard / empirisk UX

Baymard är extremt värdefullt där deras forskning faktiskt gäller. Deras material bygger på stora mängder användartestning och benchmarking och betonar bland annat tydlig navigation, tillgänglighet, mobile UX, välplanerade formulär och återkommande användartestning. citeturn258112search0turn258112search2

Men:

> Baymards e-commerce-fynd får inte automatiskt bli lag för en en-sides VVS-sajt.

**Evidence måste vara domain-applicable.**

### GOV.UK / Good Services

Detta äger en högre abstraktionsnivå:

> förstå människans verkliga behov och lös hela problemet, inte bara den digitala skärmytan.

GOV.UK säger uttryckligen att man ska utgå från användarbehov, inte från en förvald teknisk lösning, och att användaren inte ska behöva förstå organisationens interna struktur. citeturn624351search0turn624351search1

Lou Downes *Good Services* går ännu tydligare på att tjänsten ska låta användaren slutföra det resultat de gav sig ut för att uppnå. citeturn624351search13turn624351search14

Det här är egentligen filosofin bakom Nortropics interventionsbeslut.

### Klassisk UX-/designlitteratur

Här skulle jag vilja att vi inkluderar sådant som:

**Don Norman — *The Design of Everyday Things***  
feedback, signifiers, conceptual models, constraints.

**Steve Krug — *Don't Make Me Think***  
självförklarande gränssnitt och låg kognitiv belastning.

**Refactoring UI — Adam Wathan / Steve Schoger**  
praktisk visuell hierarki, spacing, typography, color, depth och layout.

**Practical UI — Adham Dannaway**  
ett logikdrivet sätt att bygga intuitiva, tillgängliga och visuellt bra interfaces; boken beskriver själv målet på just det sättet. citeturn624351search5turn624351search8

Och jag skulle sannolikt lägga till renare grafisk-designkällor för typografi, grid, färg och komposition — så att AI:n inte bara tränas i **web UI fashion**, utan i faktisk design.

---

# Sedan kommer Emil Kowalski — men i rätt roll

Jag tittade särskilt på detta nu eftersom du nämnde honom.

Hans officiella skillrepo har vuxit ordentligt och beskriver sig uttryckligen som en genväg till att stå ut “in a sea of slop”. Det innehåller nu bland annat `emil-design-eng`, strikt animation review, animation improvement, animation-opportunity discovery, animation vocabulary, Apple-design-principer och library selection. citeturn450039search5turn450039search7

Det viktigaste från hans huvudskill tycker jag inte ens är “använd snygga animationer”.

Det är:

> **taste is trained**  
> **unseen details compound**  
> **beauty is leverage**

och sedan väldigt konkreta mikroprinciper om easing, transitioner, interaction feedback, transform origin, interruptions, defaults och edge cases. citeturn450039search0

Så jag skulle placera Emil som:

> **DESIGN ENGINEERING / MOTION / INTERACTION CRAFT**

Inte:

> “så här ska en hel webbplats se ut.”

Det är en viktig begränsning.

---

# Taste har också en väldigt specifik styrka

Taste-skillens nuvarande beskrivning säger att den reverse-engineerar en riktig sajt till både konkreta design tokens och ett slags **Taste DNA: Trigger → Decision → Reason → Evidence**, alltså varför vissa designval fungerar snarare än bara vilka hexvärden de använder. citeturn258112search18

Det gör Taste perfekt för:

> **reference analysis före design freeze**

Inte som permanent global domare som alla sajter ska följa.

Exempel:

```text
Kunden gillar Site X
        ↓
Taste analyserar
        ↓
inte "kopiera Site X"
        ↓
WHY:
editorial density
asymmetric composition
tight type scale
quiet surfaces
one expressive transition
        ↓
Nortropic översätter till kundens egen direction
```

Det är en enorm skillnad.

---

# Impeccable är kanske vår bästa anti-slop-critic

Impeccable är uttryckligen byggt kring problemet att modeller tenderar mot samma visuella defaults: generiska sans-fonts, gradienter, card-on-card, icon tiles osv. Projektet har utvecklat en stor designvokabulär, specialiserade referenser, critique/polish-lägen och deterministiska anti-pattern checks. citeturn258112search9turn258112search13

Det gör den väldigt värdefull.

Men även här:

> **Impeccable ska vara ett instrument, inte Nortropics smak.**

Om vi följer varje Impeccable-antimönster mekaniskt kan vi skapa nästa konvergens:

> alla Nortropic-sajter blir “anti-Impeccable-slop” på exakt samma sätt.

---

# Det finns nämligen en farligare variant: **anti-slop slop**

Det här tycker jag vi verkligen ska skriva in i assurance-designen.

AI-slop är inte bara:

- purple gradients
- bento
- Inter
- cards
- center everything

Efter att tusentals AI-agenter lärt sig “undvik AI-slop” kommer nästa slop kunna bli:

- serif display + neutral sans
- editorial whitespace
- off-white background
- terracotta/mässing accent
- huge typography
- tasteful grain
- asymmetrical hero
- “artisanal” photography
- subtle fade-up
- no cards

Alltså:

> **AI lär sig anti-AI-estetiken och den blir nästa template.**

Det är därför jag tycker dagens Nortropic redan gjort något ganska smart: reviewern har en separat **gestalt-syskonlikhetskontroll mot tidigare kunder**, inte bara en blocklist. Den försöker hitta om den nya sajten faktiskt ser ut som ett syskon till tidigare sajter och skiljer uttryckligen kvalitet från distinktion. fileciteturn64file0L1-L2

Det är ett starkt frö.

Jag skulle göra det till en grundlag:

> **ANTI-SLOP IS A CONSTRAINT, NEVER A STYLE.**

---

# Därför vill jag skilja mellan två saker som idag fortfarande sitter ganska nära varandra

## Nortropic Web Standard

Detta beskriver:

> **Vad som alltid måste vara bra.**

Till exempel:

- begriplighet
- användbarhet
- accessibility
- performance
- trust
- faktatrohet
- responsiveness
- interaction feedback
- technical quality

Det ska **inte** tala om hur sajten ska se ut.

## Project Visual Intent

Detta beskriver:

> **Hur just den här sajten ska uttrycka sig.**

Här kommer:

- kunden
- brand
- målgrupp
- faktiskt bildmaterial
- marknad
- vald direction
- riktiga referenser
- Taste analysis
- signaturelement
- motion character
- typography genre
- composition language
- anti-references

in.

Alltså:

```text
GLOBAL QUALITY
        ×
PROJECT-SPECIFIC EXPRESSION
        =
NORTROPIC SITE
```

Inte:

```text
GLOBAL NORTROPIC STYLE
        ↓
alla kunder
```

---

# Och här tror jag vi hittar den rätta formen för den gamla Reference Compiler-idén

Jag skulle inte vilja ha en “AI som tittar på fem sajter och producerar en stil”.

Jag vill ha något mer rigoröst:

```text
CLIENT TRUTH
+
USER / BUSINESS OUTCOMES
+
BRAND MATERIAL
+
REAL MARKET
+
CURATED REFERENCES
+
TASTE EXTRACTION
+
CRAFT PRINCIPLES
        ↓
REFERENCE COMPILATION
        ↓
PROJECT VISUAL INTENT
```

Sedan fryser man **intent**, inte inspirationen.

Buildern får därefter:

> “Bygg detta.”

Inte:

> “gå ut och bli inspirerad lite till.”

Det minskar både varians och template drift.

---

# Hur vi “utvinner” GitHub-skillsen blir därför kritiskt

Jag skulle absolut inte bara låta Nortropic fortsätta ladda dem för evigt.

Efter Webbförvaltningen-build-complete bör Capability Assurance göra en **Design Knowledge Distillation** av varje bärande extern skill.

För varje regel/idé vill jag veta:

| Fält | Exempel |
|---|---|
| Source | `emilkowalski/skills@SHA` |
| Principle | Enter animation uses immediate response / suitable easing |
| Domain | Motion |
| Authority | Practitioner craft |
| Applicable when | Temporary UI enters |
| Not applicable when | reduced-motion / no-motion intent |
| Conflict | performance / brand restraint |
| Evidence | source + local experiments |
| Testability | deterministic / visual judgment / human |
| Nortropic destination | motion canon |
| Runtime loading | conditional |
| Status | KEEP / MERGE / DEFER / REJECT |

Gör samma sak med:

- Emil
- Impeccable
- Taste
- Anthropic frontend-design
- ui-ux-pro-max
- web-design-guidelines
- soft-skill
- find-animation-opportunities
- eventuellt nya relevanta toppskills

Sedan kan vi upptäcka:

```text
53 idéer totalt
→
21 duplicates
→
7 conflicts
→
6 too generic
→
4 wrong for Nortropic
→
15 genuinely valuable rules
```

**De 15 ska bli Nortropic-kunskap.**

Inte åtta samtidiga externa röster.

---

# Detta löser också supply-chain-frågan

Extern designkompetens får en bra livscykel:

```text
UPSTREAM
↓
observed
↓
candidate
↓
static review
↓
distill
↓
local experiment / eval
↓
ADOPT selected knowledge
↓
Nortropic first-party canon
```

Sedan kan vi fortsätta bevaka upstream för **deltas** utan att varje upstreamändring förändrar hur en kundsajt byggs.

Det passar perfekt med dagens Knowledge Lane.

---

# En annan variabel vi måste fånga: **smak ≠ usability**

Detta låter självklart men AI-system blandar dem lätt.

Vi måste kunna ha:

```text
VISUAL:
exceptional

USABILITY:
poor
```

och:

```text
USABILITY:
exceptional

VISUAL:
generic
```

och båda ska kräva förbättring.

GOV.UK:s standard kräver exempelvis att en tjänst är enkel, intuitiv och testad med riktiga användare. citeturn624351search2

Det betyder:

> En design reviewer kan inte ensam intyga en webbplats.

---

# Jag skulle därför ha fyra oberoende slutdomar

Inte en `94/100`.

### Integrity

Kan inget kritiskt vara trasigt?

Hard gates:

- facts
- accessibility
- primary journey
- security
- performance
- technical integrity

### Experience

Förstår och lyckas användaren?

- clarity
- IA
- copy
- friction
- trust
- mobile
- usability

### Craft & Distinction

Är den faktiskt exceptionellt välgjord?

- typography
- composition
- visual hierarchy
- imagery
- micro-interactions
- motion
- detail
- brand specificity
- no sibling/template convergence

### Outcome

Fungerade det i verkligheten?

- qualified leads
- task success
- search visibility
- support burden
- conversion
- field performance
- customer feedback

Ingen av dem får räddas av snittet från de andra.

---

# “Superb quality” kräver också mänsklig kalibrering

Det här tycker jag är viktigt att vara realistisk med.

Vi kan mekanisera väldigt mycket.

Men:

> **Taste kan inte helt bevisas med kod.**

Så det bör finnas ett litet mänskligt kalibreringslager.

Inte:

> “Johnny gillar den = PASS.”

Utan:

blind jämförelse när det behövs:

```text
A / B
Which feels:
more credible?
more specific?
more polished?
more memorable?
more appropriate?
```

gärna mot:

- riktiga premiumreferenser
- ett par externa personer
- ibland kunden
- ibland en oberoende designer

Det ger oss mänsklig signal utan att göra smak till helt godtycklig auktoritet.

---

# Professionella byråer stärker också samma idé

Build in Amsterdam beskriver sin metod som **strategy + design + in-house development**, där brandens emotionella kärna kopplas till KPI:er och en skräddarsydd strategisk ram. citeturn624351search6

ustwo beskriver **hypothesis-driven testing, rapid prototyping, data collection och iterative refinement** före och under produktbyggandet. citeturn624351search3

Det betyder att “high-end agency quality” inte bara är pixels.

Det är:

> **understanding → direction → craft → implementation → testing → refinement.**

Det är exakt den kedja Nortropic bör operationalisera.

---

# Och litteratur måste få en egen “Literature Corpus”

Jag skulle vilja att Capability Assurance har en särskild fråga:

> **Vilka kunskapsområden kräver etablerad litteratur snarare än GitHub-skills?**

För exempelvis:

**typografi**  
en GitHub-prompt är ett sämre fundament än faktisk typografiteori.

**grid/komposition**  
bör hämta från grafisk design, inte bara AI-landningssidor.

**färg**  
bör förstå perception, kontrast, relationer och brand — inte bara palette generators.

**interaction**  
Norman + etablerade HCI-principer.

**usability**  
Krug, Nielsen/Norman, empirisk forskning.

**service design**  
Good Services / GOV.UK.

**motion**  
Emil är extremt relevant här.

Det blir:

> **books teach principles; research tests behavior; practitioners teach craft; GitHub skills operationalize; real sites calibrate taste.**

Det är en väldigt bra kunskapshierarki.

---

# En ny assurance-lins: `SOURCE_DIVERSITY`

Vi kan kontrollera om något viktigt bara vilar på en enda “skola”.

Exempel:

```text
MOTION:
Emil only
```

kanske okej för vissa craft-regler.

Men:

```text
WEB QUALITY:
Impeccable only
```

är absolut inte okej.

För varje kritisk kvalitetsdimension skulle jag vilja se en bra mix av:

```text
normative
empirical
professional craft
real-world
Nortropic evidence
```

Där det är relevant.

Det skyddar oss mot att en populär GitHub-skill blir religion.

---

# Ytterligare en ny lins: `CONFLICT REGISTER`

Det här tror jag behövs.

Exempel:

> Impeccable säger restraint.

> Kundreferensen kräver maximalistisk expression.

> Emil föreslår motion.

> Performance budget är pressad.

> WCAG/reduced-motion ställer krav.

Rätt system svarar inte:

> “Impeccable vinner.”

Det svarar:

```text
hard invariant:
accessibility

hard budget:
performance

project intent:
expressive

craft candidate:
motion

resolution:
expressive motion under reduced-motion +
performance budget
```

Alltså en **explicit conflict-resolution hierarchy**.

Det är mycket professionellare än att låta sista skillen i prompten vinna.

---

# Och vi ska inte bara extrahera vad proffsen GÖR

Vi ska extrahera deras **judgement process**.

Det är ännu mer värdefullt.

Emil:

> varför känns detta fel?

Taste:

> varför fungerar referensen?

Baymard:

> vilket användarbeteende stödjer regeln?

GOV.UK:

> vilket problem försöker användaren lösa?

High-end agency:

> hur översätts brand + strategy till design?

Nortropic behöver alltså inte bara:

```text
RULES
```

utan:

```text
HOW EXPERTS DECIDE
```

Det är där en riktig digital kompetens börjar uppstå.

---

# Jag tror detta bör bli ett eget delområde i framtida Capability Assurance

Jag skulle kalla det:

## **Web Excellence & Design Intelligence Audit**

Den frågar:

> Är Nortropics definition av “bra webb” komplett?

> Är varje del grundad i rätt sorts evidens?

> Har vi utvunnit extern designkompetens i stället för att stapla skills?

> Är global standard separerad från kundspecifik expression?

> Kan systemet producera olika högkvalitativa uttryck?

> Kan det upptäcka sin egen konvergens?

> Har craft-principerna trigger/anti-trigger?

> Finns contradictions och authority?

> Är externa skills fortfarande nyttiga eller har Nortropic lärt sig deras bästa delar?

> Kan våra resultat mäta sig med professionellt arbete?

---

# Och vi bör ha en riktig “Agency-grade blind benchmark”

Det här tycker jag blir viktigt senare.

Ta kanske:

- 3 Nortropic-sajter
- 3 professionella studiobyggen i jämförbar kategori
- 3 typiska AI-builder-sajter

anonymisera identitet där möjligt.

Bedöm:

```text
clarity
trust
craft
specificity
typography
composition
mobile
interaction
brand fit
memorability
slop tells
```

Om Nortropic bara slår AI-builders:

> inte tillräckligt.

Målet måste vara:

> **Nortropic belongs in the professional set.**

Sedan helst:

> konkurrerar med den övre delen av det.

Det tycker jag är en mycket bättre definition av “superb”.

---

# En sista viktig sak: designkvalitet måste compunda

Efter varje riktig kund:

```text
What did reviewers catch?
What did humans prefer?
What did users misunderstand?
Which motion choices worked?
Which references translated well?
Which canon rules caused sameness?
Which details survived production?
```

Men kunskapen får inte bli:

> “serif fungerade, använd serif nästa gång.”

Den ska bli:

> “i det här kontextläget gav stark typografisk kontrast snabbare comprehension; fontvalet i sig är inte principen.”

Annars lär systemet sig ytlig stil i stället för designkompetens.

---

## Så ja: jag skulle uppgradera vår framtida audit rejält

Vi har nu egentligen tre olika assurance-frågor:

**Capability Assurance**  
Kan Webbförvaltningen göra allt den påstår?

**Service Assurance**  
Löser den riktiga användar-/kundproblem genom hela livscykeln?

**Web Excellence & Design Intelligence Assurance**  
Vet den faktiskt vad professionell, högkvalitativ webb är — och kan den producera det utan AI-konvergens?

Och den sista ska specifikt jämföra mot:

**standarder + empirisk UX + litteratur + professionell webbpraktik + ledande byråer + Emil + Taste + Impeccable + Anthropic/frontend-design + övriga relevanta GitHub-signaler + Nortropics egen verkliga evidens.**

Det här är nog den viktigaste kompletteringen vi gjort till Capability Assurance-idén hittills.

Och jag skulle skriva in en väldigt kort Nortropic-princip som sammanfattar hela saken:

> **Learn principles from literature.  
> Learn behavior from research.  
> Learn craft from practitioners.  
> Learn taste from great work.  
> Learn truth from real users.  
> Then make it Nortropic — never a collage of its sources.**

Det är ungefär **exakt** hur jag vill att Webbförvaltningen ska lära sig bygga exceptionellt bra webbplatser.

---

## Meddelande 17 — Johnny (användare)

Bra, är vi redo att börja planera implementeringen?

---

## Meddelande 18 — ChatGPT (assistent)

Ja. **Nu tycker jag att vi är redo att sluta brainstorma brett och börja planera implementationen.** Vi har fått med de variabler jag hade velat ha innan vi fryser riktningen: gamla 100-dagarskraven, den nya Webbförvaltningen, verklig kundlivscykel, assurance/falsifiering, OpenAI/Anthropic/POI, litteratur, SRE/DORA/service design, professionella webbyråer, ekonomi/operatorberoende och nu särskilt **Web Excellence + Design Intelligence** med Emil, Taste, Impeccable och övriga designkällor.

Den viktiga distinktionen är bara: **vi implementerar nu ramen för Capability Assurance — vi kör inte själva slutrevisionen av Webbförvaltningen ännu.** Den fortsätter fortfarande att förändras; bara sedan vår tidigare kontroll har `main` hunnit vidare till `9e85d7ba...`. fileciteturn63file0L1-L10

### Så här vill jag gå vidare

1. **Nortropic Intake nu.** Skapa en egen lineage, förslagsvis `webbforvaltningen-capability-assurance`. Intake är väl lämpad eftersom den uttryckligen stödjer flera källepisoder, context revisions, delta, ny destillation och ny audit när mer material tillkommer; samtidigt läses repo-verkligheten färskt vid varje senare fas. fileciteturn60file0L1-L2
2. **Planera implementationen av assurance-metoden.** Vi definierar kontrakt, artefakter, validators, falsification cases, comparator-linser, design-intelligence-distillation och kampanjens stop conditions.
3. **Implementera endast det minimala read-only-ramverket.** Ingen förändring av den pågående Webbförvaltningen, inga nya produktkrav och inga remediation-fixar.
4. **Vänta på `WEBBFÖRVALTNINGEN_BUILD_COMPLETE`.** Då fryser vi final SHA, lägger in slutrapporten och current reality som nya Intake-källepisoder och gör färsk external research.
5. **Kör Capability Assurance.** Först då dömer vi D001–D100, masterplanen, current implementation, litteratur, proffs, webbyråer, OpenAI/Anthropic osv.
6. **Ägaren granskar resultatet.** Audit får inte implementera sina egna fynd.
7. **Endast accepterade gaps går tillbaka genom Intake** som nya implementation candidates.

Det finns några saker jag skulle göra till **hårda planeringskrav** redan från början: audit ska vara read-only mot målrepona; externa källor är challenger/evidens och aldrig direkt authority; `SATISFIED` kräver evidens; `SUPERSEDED` kräver namngiven modern ersättare; syntetisk evidens får inte bli `PROVEN`; out-of-scope får bli `ROUTE-OUT` i stället för falskt gap; ett auditfynd kan resultera i `ADD`, `CHANGE`, `REMOVE`, `PROVE`, `OBSERVE`, `ROUTE` eller `DO_NOTHING`; och hela processen ska optimera mot **färre, bättre moderna gaps**, inte större governance.

För webbkvalitetsdelen skulle jag särskilt kräva att planen implementerar **separationen mellan Web Standard och Project Visual Intent**. W3C/Baymard/litteratur/professionell praxis ska hjälpa Nortropic förstå vad en bra webbplats måste klara; Emil/Taste/Impeccable m.fl. ska destilleras till craft/judgement snarare än bli åtta samtidiga smakauktoriteter. Dagens reviewer laddar fortfarande hela åttakällorskanonen samtidigt, så just den här distillationsfrågan är verklig och värd att undersöka när bygget är klart. fileciteturn64file0L1-L2

## Prompten jag skulle börja med

> Använd den installerade `nortropic-intake`-processen och skapa en ny, långlivad idélineage med arbets-slug **`webbforvaltningen-capability-assurance`**.
>
> Detta är INTE en begäran att ändra eller auditera den pågående Webbförvaltningen nu. Målet i denna fas är att fånga, destillera och därefter planera ett framtida **read-only Post-Build Reconciliation & Capability Assurance-system** som ska köras först när Webbförvaltningen explicit är `BUILD_COMPLETE` och dess slutliga repo-SHA har frysts.
>
> Bevara följande centrala intention:
>
> **Nortropic ska efter färdigställandet kunna bevisa vad Webbförvaltningen faktiskt kan, vad som endast är byggt men ännu inte verklighetsbevisat, vad som saknas, vad som ersatts av modernare arkitektur, vad som bör tas bort, vilka gamla krav som blivit hemlösa, vilka nya risker moderniseringen själv skapat och vilka nya externa lärdomar som är värda att föra genom Knowledge Lane.**
>
> Assurance-kampanjen ska minst omfatta:
>
> - atomär reconciliation av `Nortropic_100_dagar_manual_v2.3_verified` mot finalt system, på problem/outcome-nivå och aldrig filnamnsmatchning;
> - DESIGN-FRUSEN masterplan → faktiskt skeppad implementation;
> - bidirektionell traceability: requirement → current owner/evidence och implementation → source/need;
> - orphaned requirements och untraced complexity;
> - dispositions såsom `SATISFIED`, `SUPERSEDED`, `PARTIAL`, `STILL_REQUIRED`, `TRUST_KERNEL_OWNED`, `TRIGGER_ONLY`, `REJECT`, `UNKNOWN`;
> - separat evidensmognad `DECLARED / BUILT / VALIDATING / PROVEN`;
> - capability gaps, verification gaps, reality gaps, observability gaps, ownership gaps, lifecycle gaps och simplification/removal opportunities;
> - explicit known-defeaters och stale/invalidation-semantik för viktiga assurance claims;
> - supersession/rejection ledger som hindrar semantic zombies och återinförande av övergivna arkitekturroller;
> - mission coverage över `UNDERSTAND → DIAGNOSE → INTERVENE → DESIGN → DELIVER → VERIFY → TRANSITION → OPERATE → IMPROVE → EXIT`;
> - real-customer/lifecycle challenge;
> - counterfactual/minimality challenge: “om Nortropic byggdes från noll idag, vad skulle vi inte längre bygga?”;
> - agency economics och tacit/operator-dependency audit;
> - external comparator council med färska challenger-linser från Anthropic/Claude Code, OpenAI/evals, Karpathy/experiment, Google SRE, DORA/Accelerate, Evolutionary Architecture, Team Topologies, Good Services/GOV.UK, UX/HCI/service-design-litteratur, web standards, tillgänglighet, performance, leading agencies och relevanta Persons of Interest;
> - fresh external findings får endast bli kandidater genom Knowledge Lane — aldrig direkt authority;
> - särskilt **Web Excellence & Design Intelligence Assurance**.
>
> Web Excellence-delen ska säkerställa att Nortropic lär sig webb från rätt källtyp:
>
> - normativa standarder för hårda krav;
> - empirisk UX/research för beteende;
> - etablerad litteratur för principer;
> - professionella webbyråer och verkliga världsklass-sajter för kalibrering;
> - practitioners för craft;
> - GitHub-skills för operationaliserbar kunskap;
> - verkliga användare och kunder för sanningen efter launch.
>
> Den ska särskilt inventera och destillera de nuvarande externa designkällorna, inklusive `emil-design-eng`, `taste`, `impeccable`, `ui-ux-pro-max`, `web-design-guidelines`, `frontend-design`, `soft-skill` och `find-animation-opportunities`. Målet är INTE en enda homogen Nortropic-stil och INTE att stapla alla källor permanent. För varje princip: identifiera källa/version, problem den löser, domän, authority class, applicability/anti-applicability, konflikter, testbarhet, lokal evidens och lämplig Nortropic-hemvist.
>
> Bevara principerna:
>
> **ANTI-SLOP IS A CONSTRAINT, NEVER A STYLE.**
>
> **GLOBAL QUALITY × PROJECT-SPECIFIC EXPRESSION = NORTROPIC SITE.**
>
> Nortropic ska kunna upptäcka både klassisk AI-slop och framtida “anti-slop slop”/gestalt-konvergens mellan egna kunder.
>
> Kvalitetsmodellen ska hålla isär minst:
>
> `INTEGRITY` — kritiska saker fungerar och är säkra/faktatroget verifierade.  
> `EXPERIENCE` — människor förstår och lyckas.  
> `CRAFT & DISTINCTION` — typografi, komposition, imagery, interaction, motion, detail, brand specificity och frånvaro av template/sibling convergence.  
> `OUTCOME` — verklig effekt efter launch.
>
> Ingen totalpoäng får kompensera bort ett kritiskt fel i en annan dimension.
>
> Kampanjen ska ha adversarial challengers för coverage, simplification och real customer reality samt fasta falsification fixtures som bland annat prövar:
>
> 1. gammal mekanism saknas men modern arkitektur löser problemet bättre → `SUPERSEDED`;  
> 2. gammal fil finns men beteendet saknas → inte `SATISFIED`;  
> 3. en historisk dag bär flera krav → atomisera;  
> 4. implementation + syntetiska tester men ingen riktig kund → aldrig `PROVEN`;  
> 5. komponent utan spårbart problem/source → `UNTRACED_COMPLEXITY`;  
> 6. out-of-scope capability → `ROUTE-OUT`, inte gap;  
> 7. farlig legacy-mekanism → `REJECT` + eventuell tripwire.
>
> Första kampanjen får **inte** ändra målrepon, implementera fynd, flytta capability-status, ändra gates/baselines eller skapa ny runtime authority.
>
> Slutoutputen ska vara liten och beslutsbar: atomic coverage matrix, assurance claims/evidence/defeaters, mission coverage, modern gap map, reality/evidence gaps, removal/simplification candidates, supersession ledger, Web Excellence & Design Intelligence report och en kort lista fitness-function candidates. Deduplicera aggressivt; 100 historiska punkter får gärna kompilera ned till ett fåtal moderna gaps.
>
> Planera också en tvåstegs-exekvering:
>
> **Stage A NOW:** implementera endast assurance-metoden/kampanjkontraktet och dess självvakter utan att köra revisionen mot ett rörligt mål.
>
> **Stage B TRIGGERED BY `WEBBFÖRVALTNINGEN_BUILD_COMPLETE`:** läs final `main` och runtime färskt, frys exakta SHAs, tillför slutrapport/current reality som nya source episodes, gör färsk extern comparator research, revidera intake-context och genomför därefter read-only Capability Assurance.
>
> Följ `Nortropic/innovation-intake` nuvarande kontrakt för source episodes, context revision, distillation audit, owner clarifications och approved-plan lineage. Intake bevarar intention/proveniens; gällande repo authority och faktisk runtime vinner alltid.
>
> Börja med att inventera om denna idé redan finns eller ska vara en ny lineage. Presentera sedan exakt vilka källor som behöver fångas nu, vilka frågor som verkligen behöver ägarbeslut före planering och ett föreslaget planeringsscope. **Bygg ingenting ännu.**

Det är där jag skulle sätta stopp för brainstormingfasen.

**Nästa verkliga steg är alltså Intake med den här riktningen → destillation → plan candidate → vi granskar planen tillsammans → först därefter implementation av Stage A.**

Jag tycker inte att vi behöver “komma på mer” innan vi gör det. Om Intake-/planeringsfasen hittar en verklig obesvarad arkitekturfråga tar vi den då; annars riskerar ytterligare fri brainstorming nu mest att öka korpusen utan motsvarande informationsvinst.

