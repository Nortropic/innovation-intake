# Fullständigt transkript — Arbetsmetoder för innovation

## Metadata

- **Källa:** ChatGPT, projekt "Improvements"
- **Chattitel:** Arbetsmetoder för innovation
- **URL:** https://chatgpt.com/c/6a831565-5568-83ed-a66d-e2c7a4816755
- **Exportdatum:** 2026-08-20
- **Antal meddelanden:** 8 (3 användare / 5 assistent)
- **Fidelity:** verbatim (data-layer-capture; SHA256-verifierad transfer; fail-closed-verifierad)
- **Bilagor:** inga
- **Syfte (en rad):** Ersätta de magiska orden ("Websearcha, best practices, think hard, iterate") med ett explicit evidensdrivet brainstormprotokoll — beslutat som stående default ("Deep Brainstorm").

**Om källhänvisningsmarkörer:** Sekvenser med Unicode-tecken i privata området
(U+E200–U+E202, synliga som `cite`/`turn…`/`memcite`) är ChatGPT:s käll-chips; de har
bevarats som de är i texten.

## Innehåll i korthet

Johnny frågar om hans brainstormfraser är praxis. Research av OpenAI/Anthropic:
"iterate" utan mätbar kvalitetsribba är svagt; reasoning-modeller ska få svårare
uppdrag, inte "think hard"; iterera mot en extern definition av bra. Ett
standardprotokoll etableras: Frame → Research → Diverge → Challenge → Synthesize →
Quality bar/Eval → Smallest experiment → Iterate, med epistemiska etiketter
FACT/EVIDENCE/INFERENCE/SPECULATION och regeln att grundpremissen alltid ska prövas
innan idén byggs vidare på. Johnny beslutar att Deep Brainstorm (full process) är
standardläge varje gång; endast explicita "snabbt"/"ingen research" lättar på det.

## Meddelande 1 — Johnny (användare)

När jag ska brainstorma så brukar jag skriva saker som Websearcha, best practices, think hard, iterate men är det praxis att göra så? Hur arbetar man på openai, anthropic när man ska ta fram nya saker eller förbättra?

---

## Meddelande 2 — ChatGPT (assistent)

Ja — dina fraser fungerar, men de är ganska “magiska ord”. Det som brukar ge störst kvalitetslyft är att ersätta dem med en **explicit arbetsprocess**: vad som ska undersökas, vilka källor som väger tyngst, hur idéerna ska jämföras, och vad som krävs innan något rekommenderas.

Jag kollar nu hur OpenAI och Anthropic själva beskriver research, evals, iteration och agentiskt utvecklingsarbete, och översätter det till ett bättre brainstorming-upplägg för dig.

---

## Meddelande 3 — ChatGPT (assistent)

Det offentliga materialet från båda bolagen pekar faktiskt åt samma håll: **“iterate” är rätt idé, men iteration utan en mätbar kvalitetsribba är svag**. OpenAI beskriver eval → körning → analys → förbättring, medan Anthropic uttryckligen rekommenderar att definiera framgångskriterier och evals innan man optimerar. 

Och en viktig detalj: för moderna reasoning-modeller rekommenderar OpenAI **inte** generiska uppmaningar som “think step by step”; raka och tydliga instruktioner fungerar bättre.

---

## Meddelande 4 — ChatGPT (assistent)

Ja. Men jag skulle ändra hur du gör det.

Det du brukar skriva:

> **“Websearcha, best practices, think hard, iterate.”**

är en bra *signal om ambitionsnivå*, men det är inte riktigt den arbetsmetod som OpenAI och Anthropic beskriver offentligt. Den tydliga trenden hos båda är snarare:

**problem → kontext/evidens → flera hypoteser → kritik → mätbar kvalitetsribba → experiment → eval → iteration**

Det är en ganska viktig skillnad.

### Dina fyra uttryck

**“Websearcha” — bra, men specificera varför.**  
För omvärldsanalys, teknik, nya metoder och konkurrenter är det helt rätt att söka. Men hellre:

> Sök aktuella primärkällor. Prioritera officiell dokumentation, engineering-bloggar och forskning. Separera etablerade fakta från slutsatser och spekulation.

Annars kan modellen samla ihop tio SEO-artiklar och kalla det “research”.

**“Best practices” — användbart, men lite farligt.**  
Best practice betyder i praktiken ofta *vad andra redan gör*. Om du försöker skapa något nytt vill du även fråga:

> Vad är nuvarande best practice? Varför ser den ut så? Vilka antaganden bygger den på? Vad skulle vi göra annorlunda om vi designade systemet från first principles idag?

Det ligger nära hur OpenAI beskriver sin problemlösningskultur: både first principles och etablerade best practices. citeturn345285search32

**“Think hard” — den skulle jag i princip sluta använda.**  
OpenAI säger uttryckligen att reasoning-modeller fungerar bäst med enkla, direkta instruktioner och att uppmaningar av typen “think step by step” inte behövs och ibland kan försämra resultatet. citeturn636170search0

Ge modellen ett **svårare uppdrag**, inte bara instruktionen att tänka hårdare.

Exempel:

> Identifiera de tre starkaste lösningshypoteserna. Försök därefter falsifiera var och en. Leta efter antaganden, second-order effects och failure modes innan du rekommenderar en lösning.

Det tvingar fram bättre arbete än “think hard”.

**“Iterate” — helt rätt, men definiera vad iterationen ska optimera mot.**

Det här är kanske den största lärdomen från både OpenAI och Anthropic.

OpenAI beskriver eval-arbetet ungefär som: definiera uppgiften → kör den på testfall → analysera resultat → förbättra → kör igen. citeturn636170search28turn636170search17

Anthropic säger på motsvarande sätt att man först bör definiera konkreta och mätbara framgångskriterier och därefter bygga evals mot dem. citeturn636170search10

Alltså:

> **Iterera inte tills AI:n “tycker att det är bra”. Iterera mot en extern definition av bra.**

Det här ligger väldigt nära det vi tidigare har diskuterat kring dina verification-/gauntlet-idéer.

---

## Hur OpenAI verkar arbeta

Vi ska vara försiktiga med att påstå att vi känner till någon hemlig “OpenAI brainstorming SOP”. Det gör vi inte. Men deras offentliga engineering-material visar ett ganska tydligt mönster.

OpenAI beskriver hur deras produkt-, engineering- och GTM-team studerar befintliga workflows, **definierar vad bra betyder** och därefter bygger och itererar. citeturn345285search6

I deras mer extrema Codex-experiment har ingenjörernas roll flyttats från att huvudsakligen skriva kod till att **specificera intention, skapa rätt miljö och konstruera feedback-loopar** där agenten kan arbeta och verifieras. citeturn345285search0

Och OpenAI använder evals tillsammans med traditionell produkt­experimentering/A/B-tester; evalen ersätter alltså inte verklig feedback utan blir ett sätt att systematiskt mäta förbättringen. citeturn345285search5

Det blir ungefär:

**Intent → Context → Prototype → Feedback loop → Eval → Improve → Ship/rollback**

Inte:

**Prompt → “think harder” → snyggt svar.**

---

## Hur Anthropic verkar arbeta

Anthropic är kanske ännu tydligare offentligt.

Deras grundrekommendation är att börja med den enklaste lösningen, optimera den med utvärderingar och först introducera mer avancerade agentiska/multi-agent-system när enklare lösningar inte räcker. citeturn636170search2

Claude Code är ett bra verkligt exempel. Anthropic beskriver hur det först utvecklades genom snabb iteration på feedback från egna medarbetare och externa användare. Därefter byggde de successivt evals för specifika beteenden och senare mer komplexa egenskaper. De läser dessutom regelbundet själva eval-transkripten i stället för att enbart titta på ett numeriskt score. citeturn345285search1

När Anthropic byggde sitt multi-agent research-system använde de också en snabb loop med **observability + test cases + iteration**, och fann att multi-agent framför allt var användbart när problemet faktiskt krävde bred parallell research. citeturn345285search7

Det är viktigt: **fler agenter är inte automatiskt bättre brainstorming.**

---

# Så skulle jag ändra din metod

Istället för:

> **Websearcha. Best practices. Think hard. Iterate.**

använd ungefär följande mentala modell:

### 1. Frame
Vad försöker vi egentligen förbättra?

Definiera:

**nuläge → problem → mål → constraints → vad betyder “bättre”?**

### 2. Research
Undersök världen.

Prioritera:

**primärkällor → forskning → frontier engineering → relevanta open-source-system → verkliga implementationer**

Inte bara “vad säger Google?”.

### 3. Diverge
Nu brainstormar vi på riktigt.

Be om lösningar från exempelvis:

- etablerad best practice
- first principles
- konkurrerande arkitekturer
- angränsande branscher
- radikala/okonventionella alternativ

Här vill du **inte välja vinnare ännu**.

### 4. Adversarial critique
Nu försöker vi förstöra idéerna.

För varje kandidat:

**Vad måste vara sant?  
Vad kan gå fel?  
Vilka second-order effects finns?  
Vad missar vi?  
Vad skulle få oss att förkasta idén?**

### 5. Synthesis
Först därefter kombinerar man det bästa.

Inte nödvändigtvis “välj idé 3”.

Ofta är svaret:

> 60 % från A + mekanismen från B + skyddsräcket från C.

### 6. Define the eval
Innan implementation:

> **Hur vet vi objektivt att den nya lösningen är bättre än den gamla?**

Det här är kärnan i både OpenAI:s och Anthropics moderna utvecklingsmetodik. citeturn636170search17turn636170search10

### 7. Smallest useful experiment
Bygg den minsta sak som kan falsifiera eller validera hypotesen.

Inte hela systemet.

### 8. Measure → learn → iterate
Och **nu** kommer `iterate`.

Men iterationen får ny evidens varje varv.

---

## Det ger en mycket bättre standardprompt

För något viktigt skulle jag istället skriva till mig ungefär:

> Undersök detta som ett research- och innovationsproblem.  
>   
> Börja med att tydligt formulera problemet, nuläget, målet och vad “bättre” betyder.  
>   
> Gör därefter aktuell research och prioritera primärkällor, officiell dokumentation, forskning och verkliga implementationer. Separera fakta, evidens och dina egna slutsatser.  
>   
> Identifiera nuvarande best practice, men stanna inte där. Analysera vilka antaganden den bygger på och undersök även lösningar från first principles och relevanta angränsande områden.  
>   
> Generera flera genuint olika lösningshypoteser innan du väljer riktning. Försök sedan aktivt falsifiera dem: hitta svagheter, failure modes, trade-offs, second-order effects och sådant vi sannolikt missar.  
>   
> Syntetisera därefter den starkaste lösningen och jämför den mot nuläget med explicita kriterier.  
>   
> Föreslå slutligen det minsta experimentet som kan avgöra om hypotesen faktiskt är bättre, vilka evals/mätetal som krävs och vilken evidens som skulle få oss att ändra uppfattning.

Det är betydligt närmare **hur ett bra R&D-arbete ser ut** än “think hard”.

Och det intressanta för det du håller på med är att samma princip återkommer hela vägen från brainstorming till autonoma agentsystem:

**Wayfinding → hypothesis → specification → build → verification/eval → evidence → learning.**

Det betyder att du egentligen kan ha **en och samma innovationsloop för hela Nortropic**, där brainstorming bara är första delen av en evidensdriven kedja i stället för en fristående ChatGPT-session. citeturn345285search0turn345285search1 memcite

---

## Meddelande 5 — Johnny (användare)

Detta låter bra, hur skulle jag kunna implementera detta i mitt framtida brainstormande så vi arbetar så här

---

## Meddelande 6 — ChatGPT (assistent)

Ja. Jag skulle göra det till ett **standardprotokoll mellan oss**, så att du inte längre behöver komma ihåg att skriva `websearcha`, `best practices`, `think hard`, `iterate` varje gång.

Jag har sparat detta som din default för framtida brainstorming.

## Så använder du det

Du ska i princip kunna skriva:

> **Brainstorma kring: [idé/problem]**

eller till och med:

> **Jag har en idé: …**

Då tolkar jag det som att vi går in i ett **evidensdrivet R&D-läge**, inte bara börjar kasta ur oss idéer.

Jag följer då denna kedja:

1. **Frame** — Vad är egentligen problemet? Nuläge, mål, constraints och vad “bättre” betyder.
2. **Research** — Om frågan gynnas av aktuell kunskap söker jag automatiskt primärkällor, dokumentation, forskning och relevanta implementationer. Du behöver inte skriva `websearcha`.
3. **Diverge** — Jag genererar flera genuint olika vägar: current best practice, first principles, alternativa arkitekturer och mer okonventionella idéer.
4. **Challenge** — Jag försöker sedan slå sönder våra egna idéer: antaganden, failure modes, trade-offs, second-order effects och blind spots.
5. **Synthesize** — Vi kombinerar det bästa till en starkare lösning i stället för att bara välja “idé A”.
6. **Quality bar / Eval** — Vi definierar hur vi faktiskt skulle kunna veta att den nya lösningen är bättre.
7. **Smallest experiment** — Vi identifierar minsta test som kan validera eller falsifiera hypotesen.
8. **Iterate** — Nästa iteration bygger på ny evidens, inte bara på att modellen försöker skriva ett “bättre svar”.

### En viktig förändring

Jag vill också separera fyra saker tydligare när vi brainstormar:

**FACT** — vad vi faktiskt vet.  
**EVIDENCE** — vad källor/data pekar mot.  
**INFERENCE** — vad jag drar för slutsats från evidensen.  
**SPECULATION** — intressanta idéer som ännu saknar stöd.

Det gör att en spännande AI-idé inte råkar förvandlas till “sanning” efter fem meddelanden.

## Du behöver alltså inte längre skriva

`Websearcha, best practices, think hard, iterate.`

Skriv hellre själva intentionen:

> **Brainstorma kring hur vi skulle kunna göra X bättre.**

Om du vill styra djupet kan vi ha tre väldigt enkla kommandon:

**“Brainstorma…”**  
→ normal full process.

**“Deep brainstorm…”**  
→ mycket bred research, fler alternativa hypoteser och hårdare adversarial analys.

**“Snabb brainstorm…”**  
→ samma metod, men komprimerad; mindre research och snabbare syntes.

Och du kan lägga på constraints naturligt:

> Brainstorma kring X. Ingen implementation ännu.

> Deep brainstorm kring X. Utmana även om själva grundidén är fel.

> Brainstorma kring X från first principles. Jämför med hur OpenAI, Anthropic och relevanta open-source-projekt gör.

### Ännu viktigare: jag bör inte alltid hålla med grundpremissen

Om du exempelvis säger:

> “Jag tror Nortropic behöver en research-agent som kör varje natt. Brainstorma.”

ska jag **inte** börja med att designa research-agenten.

Jag bör först fråga/undersöka:

**Är en research-agent ens rätt lösning på problemet?**

Kanske problemet egentligen är knowledge decay. Kanske retrieval. Kanske dåliga feedback-loopar. Kanske research inte är flaskhalsen alls.

Det är där first-principles-delen blir väldigt värdefull.

---

Jag skulle dessutom göra brainstormingen till en liten **state machine**:

**QUESTION → FRAME → RESEARCH → HYPOTHESES → RED TEAM → SYNTHESIS → EVAL → EXPERIMENT**

Och först därefter:

**SPECIFICATION → BUILD**

Det betyder att vi inte råkar gå från *“jag fick en idé”* till *“Claude Code, implementera detta”* innan vi faktiskt vet att idén håller.

Det här tror jag blir den stora förbättringen: **brainstorming blir inte längre en konversationstyp. Det blir första delen av samma systematiska loop som så småningom kan leda hela vägen till en verifierad implementation.**

---

## Meddelande 7 — Johnny (användare)

Det ska alltid vara deep tänker jag

---

## Meddelande 8 — ChatGPT (assistent)

Ja. Då sätter vi **Deep Brainstorm som standardläge varje gång**.

Det betyder att när du framöver skriver exempelvis:

> Brainstorma kring detta…

så går jag automatiskt på full process: bred research där det behövs, primärkällor, best practices + first principles, flera konkurrerande hypoteser, red-team/falsifiering, second-order effects, syntes, evals och minsta validerande experiment.

Du behöver alltså inte längre skriva `websearcha`, `best practices`, `think hard`, `iterate` eller ens `deep` varje gång. Det är default nu.

Enda gången jag gör det lättare är om du uttryckligen säger exempelvis **“snabbt”**, **“ingen research”** eller **“bara bolla idéer kort”**.

Och jag kommer inte automatiskt acceptera premissen i din idé — en del av Deep Brainstorm blir alltid att pröva om **själva problembilden eller föreslagna riktningen är fel** innan vi bygger vidare på den. memcite
