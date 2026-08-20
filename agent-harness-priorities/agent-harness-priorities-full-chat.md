# Fullständigt transkript — Nortropic agent harness priorities and experiments

## Metadata

- **Källa:** ChatGPT, projekt "Improvements"
- **Chattitel:** Nortropic agent harness priorities and experiments
- **URL:** https://chatgpt.com/c/6a7971a3-0aac-83eb-991f-57ae207766e3
- **Exportdatum:** 2026-08-20
- **Antal meddelanden:** 2 (0 användare / 2 assistent)
- **Fidelity:** verbatim (data-layer-capture, fail-closed-verifierad: exakt längd, JSON, balanserade kodstaket, första/sista meddelande)
- **Bilagor:** inga
- **Syfte (en rad):** Schemalagd bevakning av frontier-harness-utveckling (Anthropic/OpenAI) med implikationer för Nortropics reviewer-isolering, provenance och multi-agent-mönster.

**Särskild form:** Detta är en schemalagd bevakningschatt (ChatGPT scheduled task). Den
synliga chatten innehåller ENDAST assistentens rapporter — uppgiftsprompten är dold i
ChatGPT:s UI och ingår därför inte (WYSIWYG, korskollad mot renderade DOM:en).

**Om källhänvisningsmarkörer:** Sekvenser med Unicode-tecken i privata området (U+E200–U+E202,
synliga som `cite`/`turnNNN…`/`memcite`) är ChatGPT:s käll-chips; de renderas som små
källänkar i UI:t och har bevarats som de är i texten.

## Innehåll i korthet

Två automatiska bevakningsrapporter (10–20 aug 2026). Rapport 1: Claude Code-isoleringsfixar
validerar G20-riktningen; verifiering blir explicit/operatörsstyrd; bounded agent-DAG
snarare än fri rekursion; asymmetrisk challenger (Codex builder → Claude reviewer) slår
symmetrisk debatt enligt empiri; degraded-mode honesty vid multi-modell. Rekommendation:
ändra inte S1. Rapport 2: OpenAI gör agentidentitet/ursprung förstaklassigt (root_turn_id,
agent_name), hård reviewer-isolering (approval=never, read-only, tom extension registry),
gemensam privileged-action-pipeline, skills med forward-tests, shadow-utvärderad
skill-routering. Slutsats: nästa innovation är reviewer-isolering + lineage/provenance
("Operating Model v2"), inte fler debatterande modeller.

## Meddelande 1 — ChatGPT (assistent)

Det kom flera saker som är direkt relevanta för Nortropic, framför allt på **containment, verifiering och multi-agent review**. De viktigaste signalerna är dessa:

- **Claude Code har precis fått flera isoleringsfixar som starkt validerar vår G20-riktning.** Den 4 augusti fixade Anthropic att worktree-isolerade sessioner och subagenter kunde köra destruktiva Git-kommandon mot huvud-checkouten; den 6 augusti fixades bland annat ett Bash-permission-gap och möjlighet för workflow-kod att exekvera utanför workflow-sandboxen; den 7 augusti fixades en filesystem-deny-variant där trailing slash kunde göra regeln verkningslös; den 8 augusti fick `claude agents` dessutom samma workspace-trust-prompt som vanliga Claude Code. citeturn800993view3turn800993view2turn800993view0 **Implikation:** Nortropics K18R/G20 ska fortsätta vara en *extern effektmätning*, inte ett antagande om att “worktree isolation” eller en sandbox-flagga betyder säkerhet. Efter S1 bör vi överväga challenger-fixturer för `git -C`/`GIT_DIR`, symlink/path-kanonisering och policy-regelvariationer — men inte ändra den frysta h-017-grinden mitt i nuvarande slice.

- **Anthropic har gjort verifiering mer explicit och mindre modellstyrd.** Sedan Claude Code 2.1.215 den 19 juli kör Claude inte längre `/verify` eller `/code-review` på eget initiativ; operatören/workflowet måste uttryckligen anropa dem. Två dagar senare flyttades `/code-review` till en bakgrundssubagent för att hålla huvudkontexten ren. Den aktuella `/verify`-skillen är dessutom uttryckligen tänkt att bygga, köra och observera applikationen snarare än bara lita på tester/typechecks. citeturn723885view2turn307147view0turn103605search4 **Implikation:** det här ligger mycket nära Nortropics arkitektur: **controllern bestämmer när verifiering sker; buildermodellen får inte själv bestämma att verifiering är onödig.** Reviewer-/verify-agenter kan isolera kontext, men den mekaniska grinden förblir authority.

- **Claude Codes multi-agent-harness har blivit betydligt mer “fleet”-likt, men Anthropic sätter samtidigt uttryckliga gränser.** Den 24 juli fick nested subagents standarddjup 3 och dynamiska workflows en normal guideline på färre än 15 agenter; samma release lade till strict network allowlisting. Den 7 augusti kom cross-session `SendMessage`, `ListAgents` och self-hosted runners, inklusive explicit approval-policy för vissa inkommande meddelanden. citeturn307147view0turn800993view1 **Implikation:** när Nortropic når S11/S12 bör vi hellre bygga en **bounded agent-DAG** med explicit depth, concurrency, budget och agentidentitet än en fri rekursiv “agents spawn agents tills någon är nöjd”-modell. Agentmeddelanden bör vara typed envelopes med sender/recipient/task/base/candidate/provenance och kvitterad delivery.

- **OpenAI:s egna Codex-repo dogfoodar två mönster som nästan mappar direkt mot senare Nortropic-slices.** Deras `code-review`-skill fanar ut en separat subagent per `code-review-*`-specialist och kräver att alla fynd samlas tillbaka; `babysit-pr` övervakar däremot PR, CI, review-feedback och mergeability kontinuerligt, har begränsade flaky-retries och tydliga terminala/handoff-tillstånd. citeturn563800search2turn563800search1 **Implikation:** för S11 är “flera oberoende read-only challenger-lanes → aggregator” mer intressant än flera builders som röstar. För S5/S6/S7 är `babysit-pr` ett bra referensmönster för state machine + retry budget + “requires help”, men Nortropics egen attestation/promotion ska fortsatt baseras på vår mekaniska kedja, inte PR-watcherns omdöme.

- **Det finns nu faktiskt empirisk Claude↔Codex-data, och den talar *inte* för ett symmetriskt femvarvs-debate-upplägg.** En studie publicerad 22 juli körde 116 koduppgifter i sex review-konfigurationer. Där förbättrade Claude-review av Codex-utkast resultatet tydligt, medan Codex-review av Claude-utkast i experimentet försämrade resultatet; reviewern fick dessutom inte köra tester, så det är en ren review-signal och inte ett fullständigt harness-resultat. citeturn667655academia40 **Implikation:** om vi testar Claude↔Codex i Nortropic skulle jag nu prioritera **asymmetrisk challenger**: exempelvis Codex builder → Claude adversarial reviewer → targeted repair → mekanisk verifierare. Inte “Claude och Codex bollar fem gånger och majoriteten vinner”. Mät detta på vår egen task-suite innan det blir en permanent del av loopen.

- **Det närmaste aktuella “Claude + Codex + annan modell”-mönstret är fortfarande community, inte officiell OpenAI-best-practice.** `trinity`-förslaget i OpenAI/Codex använder Codex, Claude och Grok som separata review-lanes före implementation och på slutdiffen, med strikt JSON-schema, begränsad revisionsloop, provenance för fallback och explicit markering när verklig provider-diversitet saknas. Det är ännu bara ett communityförslag/discussion, inte en upstream-standard. citeturn827672search1turn827672search4 **Implikation:** den mest värdefulla idén för Nortropic är inte “tre modeller = sanning” utan **degraded-mode honesty**. Om vi senare använder flera modeller bör varje review bära exempelvis `provider`, `model`, `input_sha`, `candidate_sha`, `verdict`, `fallback_for`, `degraded`. En fallback får aldrig räknas som oberoende konsensus, och modellkonsensus får aldrig själv skapa attestation.

En separat signal kring **autonomous coding/auto-merge** är värd att hålla isär: Anthropic uppger att deras interna Claude Tag nu öppnar ungefär 65 % av deras PR:er och att 65 % av produktteamets kod skapas via Claude Tag; Tag arbetar även över timmar eller dagar och kan driva flera uppgifter parallellt. Däremot hittade jag **ingen officiell Anthropic-källa som säger att dessa PR:er automatiskt mergas utan en separat trust-/review-gate**. citeturn473407search0turn473407search1 För Nortropic är det alltså stöd för hög autonomi i **creation/execution**, inte argument för att låta buildern äga **promotion**.

En sista, lägre prioriterad signal för framtida S13/Verkstadsgolvet är MCP-specen från 28 juli: MCP går mot stateless request/response core och hårdare authorization. citeturn667655search1 Det talar för att vår framtida externa kontroll-/tool-yta bör vara explicit, stateless där det går och bära controller-state som identifierade snapshots/envelopes — men jag skulle **inte ändra något i nuvarande S1 för detta**.

Min sammanvägning för Nortropic just nu är därför: **ändra inte S1-planen.** De färska signalerna stärker snarare det vi precis gör: controller-owned runtime containment, frozen verifier authority, bounded retries, worktree/process hygiene och modell-agenter som workers/challengers snarare än root-of-trust. Den enda idé jag skulle lägga till i den senare backloggen är ett explicit experiment med **Codex builder → Claude challenger** och ett separat experiment med **parallel specialist review lanes**, båda mätta mot vår mekaniska verifierare innan de får påverka promotion. memcite

---

## Meddelande 2 — ChatGPT (assistent)

Det finns **flera tydliga nya signaler sedan förra bevakningen**, nästan alla från OpenAI/Codex den 12–15 augusti. De stärker Nortropics nya Builder → Reviewer → Owner-modell snarare än att tala för fri “agentdebatt”.

- **Codex gör nu agentidentitet och ursprung förstaklassiga.** OpenAI lade till `root_turn_id` som följer hela kedjan genom spawned agents, delegation, reviews och inter-agent-meddelanden; dessutom får varje turn ett kanoniskt `agent_name` som `/root/...`. Den 14 augusti flyttades även root/subagent-rollinstruktioner in i model catalog, och ett full-history-forkat barn får sin **egen** subagentroll utan att behålla förälderns rollinstruktioner. citeturn154938view0turn154938view9turn372126view0 **Implikation för Nortropic:** nästa version av evidence-kontraktet bör sannolikt bära något i stil med `ROOT_RUN_ID`, `AGENT_PATH`, `ROLE`, `MODEL` och `CANDIDATE_SHA`. Än viktigare: en reviewer som forkas från en builder ska inte ärva builderns rollprompt. Det är nu ett konkret officiellt harness-mönster, inte bara vår egen teori.

- **Den starkaste nya signalen är hur OpenAI isolerar reviewer-delegates.** Från 12 augusti måste delegerade Codex-sessioner vara non-interactive med approval policy `never`; permission requests får inte bubbla upp till parent utan nekas i delegaten. Guardian-reviewers begränsas dessutom till **read-only ∩ parentens befintliga filesystembehörigheter**, nekade paths bevaras, nätverk begränsas och environment-ID ingår i review-sessionens reuse identity. Den 14 augusti gick OpenAI längre: Guardian-reviewern startar med **tom extension registry** och Guardian stängs av inne i reviewern så att review inte rekursivt triggar review-av-review. Den 15 augusti testades dessutom att en read-only environment faktiskt blockerar writes även när själva threaden tillåter workspace-write. citeturn154938view1turn154938view2turn154938view3turn154938view4 **Implikation:** `$nortropic-reviewer` bör på sikt mekaniseras ungefär så här: `approval=never`, read-only execution profile, inga builder-plugins/extensions som default, ingen nested reviewer, och reviewer identity bunden till både `candidate_sha` **och** environment/profile identity. Det här är nästan en direkt blueprint för nästa generation av vår reviewer-harness.

- **OpenAI håller på att bygga ett gemensamt approval/review-plan i stället för separata tool-specifika tillstånd.** Permission requests går nu genom samma Guardian approval pipeline; nätverk, MCP och andra privilegierade handlingar styrs mot samma reviewmodell. Guardian v2 fick samtidigt konfigurerbar riskklassificering, review-threshold, reasoning effort och hårda transcript/token-budgetar. citeturn154938view5turn380250view0turn380250view1turn380250view2 **Implikation:** när Nortropic når auto-promotion/auto-merge bör vi undvika att varje verktyg själv bestämmer hur det eskalerar. Gör i stället en **enda controller-owned privileged-action pipeline** för push, merge, permission expansion, network escalation och promotion. En modellbaserad riskscore kan begära *mer* verifiering, men får aldrig få befogenhet att hoppa över frozen gates. Det passar vår fail-closed-modell mycket bättre än “AI:n bedömde risken låg → merge”.

- **Skills utvecklas i exakt riktning som vårt nya operating model-upplägg.** OpenAI ändrade `skill-creator` den 13 augusti mot korta, scoped instruktioner, progressive disclosure, optional resources, explicit invocation policy och **risk-based forward-testing**. Dagen efter fick skills ett `model`-fält i frontmatter och bounded model delegation: en skill kan begära ett särskilt model tier, men delegationen valideras och begränsas. citeturn154938view6turn154938view7turn154938view8 **Implikation:** våra tre Nortropic-skills ligger strukturellt rätt. Nästa förbättring borde inte vara större SKILL.md-filer utan snarare **forward-tests för varje skill**: kan builder-skillen råka ändra frozen gate? kan reviewer-skillen skriva? kan test-author råka implementera lösningen? Separat kan vi senare modell-pinna roller — exempelvis billigare builder-delsteg och starkare reviewer — men den faktiskt använda modellen ska rapporteras som evidence, inte betraktas som trust authority.

- **OpenAI shadow-evaluerar nu själva skill-routeringen i stället för att direkt byta strategi.** De lade till en LRU-baseline och därefter fusion mellan nyligen använda och lexikalt matchande skills som **shadow selection**, med ranking- och truncation-telemetri. citeturn380250view3turn380250view4 **Implikation:** mycket relevant först när Nortropic får många skills. Då ska vi inte låta en ny “smart router” börja styra produktionen direkt; kör den parallellt i shadow mode, jämför vilken skill den hade valt mot den riktiga körningen och promotera först efter mätt precision. Med bara våra nuvarande få roller är detta ännu inte värt ny komplexitet.

Den viktigaste sammanvägningen är därför: **nästa verkliga Nortropic-innovation är inte fler debatterande modeller utan hårdare reviewer-isolering + lineage/provenance.** Jag skulle prioritera en senare `Operating Model v2` med `root_run_id`, `agent_path`, `model`, `environment_profile_id`, immutable `candidate_sha`, non-interactive reviewer och extension-free read-only review. Därefter kan Claude läggas in som en alternativ challenger lane, men fortfarande under exakt samma candidate identity och mekaniska owner-gate.

Jag hittade däremot inget tillräckligt färskt officiellt Anthropic/Claude Code-släpp efter förra bevakningen som förändrar rekommendationen; den officiella changelog-feed som går att verifiera ligger fortfarande på äldre poster, så jag återupprepar inte de Claude Code-punkter vi redan tog förra gången. citeturn222966search0 memcite
