# Fullständigt transkript — Claude /design Watch

## Metadata

- **Källa:** ChatGPT, projekt "Improvements"
- **Chattitel:** Claude /design Watch
- **URL:** https://chatgpt.com/c/6a84969a-467c-83eb-a0e8-60cc5c88fc3e
- **Exportdatum:** 2026-08-20
- **Antal meddelanden:** 5 (1 användare / 4 assistent)
- **Fidelity:** verbatim (data-layer-capture; SHA256-verifierad transfer; fail-closed-verifierad)
- **Bilagor:** inga
- **Syfte (en rad):** Utvärdera Claude Codes nya /design-kommando (research preview) för Nortropic — landar i "Visual Intent"-konceptet och en aktiverad veckovis bevakning av /design-mognaden.

**Särskild form:** Chatten avslutas med att en VECKOVIS bevakningsautomation aktiveras
("Claude /design Watch") — framtida rapporter appendas i källchatten; detta är en
snapshot per exportdatumet.

**Om källhänvisningsmarkörer:** Sekvenser med Unicode-tecken i privata området
(U+E200–U+E202, synliga som `cite`/`turn…`/`memcite`) är ChatGPT:s käll-chips; de har
bevarats som de är i texten.

## Innehåll i korthet

Johnny delar nyheten om Claude Codes /design (artboard-workflow, research preview) och
frågar om Nortropic-nytta. Analys: värdet är inte "ännu ett designverktyg" utan ett
visuellt beslutssteg FÖRE kod som bryter första-versionens gravitation
(kod är dyrt att tänka med). Konceptet döps till Visual Intent: Need → UX intent →
/design-exploration (6 genuint olika förslag: konservativa/strukturellt annorlunda/
radikala) → välj/remixa → frys APPROVED_VISUAL_INTENT (med responsivitet, states,
komponentmappning, accessibility) → först då Builder-implementation → separat
verifiering. Reservationer: research preview, omoget för kärnworkflow. Beslut: veckovis
bevakning aktiveras som bara rapporterar meningsfulla förändringar (preview-status,
/design-sync, handoff-kvalitet, API/automation, mognad).

## Meddelande 1 — Johnny (användare)

ANTHROPIC 🔥: Claude Code got a new /design command in research preview! 

Design in Claude Code adds an artboard workflow from Claude Design to help users build editable UIs. 

Brainstorma är detta nåt användbart för Nortropic 
CCD 👀

---

## Meddelande 2 — ChatGPT (assistent)

Ja — **det här kan vara mycket mer relevant för Nortropic än det först låter**, särskilt för bron mellan brainstorming → UI-idé → faktiskt byggbar frontend. Jag kollar först exakt vad `/design` kan och var gränserna går, sedan mappar jag det mot ert workflow och testar om det bör bli en egen lane eller bara ett verktyg i befintliga loopar.

---

## Meddelande 3 — ChatGPT (assistent)

Jag har verifierat nyheten: Claude själva säger att `/design` är en **ny skill i research preview**. Den låter Claude Code skissa UI som **redigerbara artboards**, låta dig välja/justera riktning och sedan lämna tillbaka den valda designen till Claude Code för implementation. Det är alltså inte bara “gör frontend snyggare” — det lägger in ett **visuellt beslutssteg före kod**. 

Det är just den separationen som gör den intressant för Nortropic.

---

## Meddelande 4 — ChatGPT (assistent)

Ja. **Jag tror att `/design` kan bli väldigt användbart för Nortropic — men inte främst som ännu ett designverktyg.** Det intressanta är att det kan bli den saknade visuella länken mellan **idé/specifikation och implementation**.

Claude bekräftade i dag att `/design` är en ny skill i **research preview**: den skapar redigerbara UI-artboards direkt från Claude Code/desktop, låter dig välja och justera riktning och sedan lämna tillbaka den till Claude Code för implementation. citeturn405120view3 Det träffar ganska exakt problemet vi har diskuterat kring att gå från brainstorming → konkret beslut → byggande utan att informationen behöver översättas manuellt mellan flera verktyg.

## Det stora Nortropic-värdet

I dag är det lätt att göra ungefär:

**idé → prompt → Claude Code börjar bygga → första UI:t blir ankare → iteration på kod**

Problemet är att kod är dyrt att tänka med. När Buildern redan har byggt version A får version A ett slags gravitation: arkitektur, komponenter och styling börjar anpassas runt den.

Figma beskriver exakt samma problem: när man går direkt in i byggandet tenderar första versionen att bli *versionen*. Deras argument för canvas är att man kan se flera lösningar sida vid sida och tänka mer divergent innan man låser riktningen. citeturn405120view1

Med `/design` kan Nortropic i stället få:

**Problem/brief → flera visuella hypoteser → jämför → välj → förfina → frys design-intent → Claude Code implementerar → verifiera**

Det är en ganska fundamental skillnad.

Jag skulle kalla konceptet **Visual Intent**, snarare än en separat “designfas”.

---

## Så här skulle jag använda det i Nortropic

Inte:

`task → /design → bygg`

utan:

`Need → UX intent → /design exploration → APPROVED_VISUAL_INTENT → implementation → verification`

För en designkänslig Verkstadsgolvet-task skulle flödet kunna vara:

1. **Brief först.** Claude får mål, användare, innehåll, affärsmål, informationshierarki, constraints och vilka komponenter som redan finns. Anthropic rekommenderar själva att tänka igenom målet före designprompten. citeturn405120view0

2. **Divergera med `/design`.** Be inte om “en bra sida”. Generera exempelvis sex genuint olika lösningar: två konservativa, två strukturellt annorlunda och två radikala.

3. **Välj riktning innan kod.** Du kan säga ungefär “B har rätt informationsarkitektur, D har bäst hero och F har bäst navigation — kombinera dessa”. Anthropic-designern bakom Claude Design beskriver just ett arbetssätt med många alternativ och sedan remix av de bästa. citeturn405120view0

4. **Frys Visual Intent.** Den valda artboarden blir inte bara inspiration. Den bör kompletteras med explicit intent: responsivitet, states, interaktioner, komponentmappning och accessibility-krav.

5. **Först nu Builder.** Claude Code implementerar den valda designen i sitt worktree.

6. **Verifiering är fortfarande separat.** Browser/verklig runtime, responsivitet, accessibility, funktionstester och visuella regressioner ska avgöra om implementationen motsvarar den godkända intentionen. Anthropic betonar själva verifiering som den viktigaste Claude Code-praktiken. citeturn686257view5

Det passar väldigt bra med Nortropics fail-closed-tänk: **Design får föreslå. Builder får implementera. Verifiering får avgöra om implementationen faktiskt uppfyller intent.**

## Och `/design-sync` gör det betydligt mer intressant

Det här är den del jag tycker är mest strategisk.

Claude Design kan läsa ett React-designsystem från repot genom `/design-sync`. Anthropic säger att Claude då använder de verkliga komponenterna och designmönstren, och kontrollerar sina resultat mot design-systemet innan de visas. citeturn539036view2turn539036view0

Det öppnar för något ganska kraftfullt i Verkstadsgolvet:

**Nortropic primitives**  
↓  
**client design system / tokens / components**  
↓  
**`/design` exploration med verkliga byggblock**  
↓  
**vald kunddesign**  
↓  
**Claude Code implementation med samma byggblock**

Då slipper vi mycket av:

> AI gör snygg mockup → Builder försöker återskapa den → komponenterna passar inte → CSS-specialfall → design driftar.

Designen och implementationen kan utgå från **samma primitives**.

Det är mycket närmare ett generativt produktionssystem än vanlig “AI gör en mockup”.

## Det kan även lösa Lovable-problemet vi pratat om

En anledning till att verktyg som Lovable känns snabba är att feedbackloopens latency är extremt låg:

**idé → se något → ändra → se igen.**

Claude Codes klassiska styrka är däremot repository awareness, implementation, terminal, tester och agentiskt arbete.

`/design` börjar slå ihop de två världarna:

**Claude Code intelligence + visuell canvas-latency.**

Claude Design kan dessutom exportera standalone HTML/ZIP/PDF och lämna över direkt till Claude Code, samt integrera vidare med bland annat Lovable, Vercel och andra verktyg. citeturn539036view0

Det betyder att jag **inte skulle införa Figma eller Lovable som obligatoriska steg i Nortropic just nu**. Vi bör först testa om Claude Code + `/design` kan ge oss den visuella explorationsloopen utan ytterligare handoffs.

---

## Men jag skulle INTE bygga in `/design` djupt i autonomin ännu

Här är min största reservation.

Det är uttryckligen **research preview**. Dessutom har den vanliga Claude Code-commandreferensen i skrivande stund ännu inte ens hunnit lista `/design`; där finns `/design-login` och `/design-sync`, medan dagens officiella Claude-announcement beskriver den nya `/design`-skillen. citeturn405120view3turn539036view2

Så jag skulle inte göra:

`Nortropic orchestrator → hard dependency on /design`

ännu.

Jag skulle göra:

`Nortropic UI task → optional DESIGN_EXPERIMENT lane`

och mäta den.

Det finns dessutom ett viktigt okänt: **hur mycket strukturerad design-intent överlever själva handoffen?** Färg och layout är en sak. Men överlever exempelvis responsiv logik, komponentidentitet, hover/focus/error states, accessibility, spacing rules och semantisk hierarki utan att Claude måste inferera dem igen? Det är precis den sorts sak Nortropic bör utvärdera, inte anta.

Anthropic säger att handoffen är avsedd att fortsätta från befintligt arbete snarare än från en screenshot och att design intent skickas till engineering, vilket är lovande. citeturn539036view0turn539036view1 Men jag skulle fortfarande kräva evidence.

## Ett experiment jag verkligen tycker vi ska göra

Ta **en verklig men avgränsad UI-feature i Verkstadsgolvet** och bygg den två gånger.

**Control:** vårt normala Claude Code-flöde direkt från specification.

**Treatment:** samma specification → `/design` → 5–8 artboards → välj/förfina → handoff → Claude Code.

Mät sedan endast några få saker: tid till första design vi faktiskt accepterar, antal mänskliga korrigeringar, antal implementation/rework-loopar, design→production-drift, funktionella/a11y/responsive-fel och total Claude-usage.

Om `/design` ger exempelvis:

**färre rework-loopar + bättre slutresultat + ungefär samma eller lägre total kostnad**

då har vi evidence för att göra Visual Intent till en riktig Nortropic capability.

Om det bara producerar snygga artboards som Claude Code sedan måste tolka om från början, då är det mest kosmetisk acceleration och ska **inte** in i kärnarkitekturen.

---

### En större idé

Det finns även en mer radikal utveckling här.

På sikt skulle Nortropic kunna ha tre olika generativa rum:

**Possibility Space** — brainstorming/research hittar *vad* vi skulle kunna bygga.

**Design Space** — `/design` producerar och jämför *hur det skulle kunna fungera och se ut*.

**Implementation Space** — Claude Code bygger endast det alternativ som överlevt de första två.

Sedan kommer **Verification Space**, som inte skapar något utan försöker falsifiera resultatet.

Det är betydligt bättre än att låta en enda Builder tänka, designa, implementera och sedan bedöma sitt eget arbete.

Och det är faktiskt den viktigaste konsekvensen jag ser av `/design`: **Nortropic kan bli bättre på att söka igenom lösningsrymden innan vi spenderar implementation.** Figma argumenterar för samma code+canvas-princip, och Anthropic beskriver Claude Design som främst ett medium för ideation, alignment och exploration före production coding. citeturn405120view1turn405120view0

**Min slutsats:** absolut värt att testa. Jag skulle ge `/design` **8/10 i potentiell Nortropic-relevans**, men bara **3/10 i mogenhet för autonom kärninfrastruktur** just nu. Börja som ett evaluerat experiment, inte som ny arkitektur. Om handoff-fidelity håller kan det däremot bli en väldigt viktig del av Verkstadsgolvet.

Eftersom `/design` precis kommit i research preview kan jag också bevaka när Anthropic dokumenterar handoff-formatet bättre, lägger till automation/API-stöd eller flyttar funktionen mot beta/stable.

genui{"suggest_automation":{"label":"Bevaka Claude /design-utvecklingen"}} memcite

---

## Meddelande 5 — ChatGPT (assistent)

Klart. Jag bevakar Claude Code `/design` **veckovis** och säger bara till när det finns en **meningsfull förändring** — särskilt kring preview-status, `/design-sync`, handoff-kvalitet, API/automation och om det börjar bli moget nog för Nortropics kärnworkflow.
