# Utforska Datadog Kubernetes — fullständigt transkript

**Källprojekt:** Improvements (ChatGPT-projekt)
**Chatt:** Utforska Datadog Kubernetes
**URL:** https://chatgpt.com/c/6aa067d0-1e88-83eb-987b-e8c6d2d41549
**Exportdatum:** 2026-09-11
**Antal meddelanden:** 37 (11 användare, 26 assistent)
**Syfte:** Fångad i PROJECT_SWEEP Improvements R39 (data-layer, WYSIWYG-filtrerad); syftet med samtalet avgörs av dess innehåll, inte av denna rubrik.

**Innehåll i korthet:** Samtalet öppnar med: ”brainstorma detta, vi har pratat om kubernetes i andra chattar och kolla närmare på datadog, om de har mer för oss att dyka i, verkar relevant” och avslutas med: ”**Nu har jag gått från provbeskrivningar till körda lokala motprov. Det viktigaste resultatet är att en korrekt överlämning inte räcker om underlaget hinner ändras före nästa handling — eller om två å”

> Notis: rader som ser ut som käll-/citat-chips från ChatGPT är en del av
> originaltexten och har bevarats ordagrant. 3 bilagor inventerade (data-layer: distinkta plattforms-fil-id ur metadata.attachments + icke-textdelar; en bild som adaptern listar två gånger räknas en gång); bytes registreras separat via register-attachment där plattformen exponerar dem.

---

## Meddelande 1 — Johnny (användare)

brainstorma detta, vi har pratat om kubernetes i andra chattar och kolla närmare på datadog, om de har mer för oss att dyka i, verkar relevant

---

## Meddelande 2 — ChatGPT (assistent)

Jag går igenom Kubernetes-spåret och Datadogs bredare arbete med övervakning, felsökning och AI-agenter, med fokus på vad som stärker Nortropic utan onödig driftkomplexitet.

---

## Meddelande 3 — ChatGPT (assistent)

Ett tydligt fynd är kopplingen mellan agentkörningar, utvärderingar och användarupplevelse. Det väcker frågan hur Nortropic mäter verifierade framsteg och upptäcker när själva arbetsledningen fastnat.

---

## Meddelande 4 — ChatGPT (assistent)

**Ja – Datadog är mycket relevant för oss, men den största vinsten är inte fler Kubernetes-grafer. Det är hur man gör ett komplext, delvis autonomt system möjligt att förstå, felsöka och faktiskt förbättra.**

Jag hittade framför allt en teknisk artikel om hur Datadog utvärderar sina egna autonoma felsökningsagenter. Den tycker jag är mer värdefull för Nortropic än själva Kubernetes-boken.

Samtidigt skulle jag hålla fast vid distinktionen från vårt tidigare Kubernetes-spår: **Kubernetes som arkitekturinspiration är en sak; att köra Nortropic i ett Kubernetes-kluster är en annan.** Vi kan lära av kontrollslingor, önskat kontra faktiskt tillstånd och arbetsfördelning utan att välja Kubernetes som driftplattform. Det är också dessa principer Kubernetes egen beskrivning av controllers kretsar kring. citeturn135232view0

Min sammanfattande hypotes är:

> **Kubernetes-inspirationen hjälper oss att organisera exekveringen. Datadog-inspirationen hjälper oss att observera och diagnostisera den. Nortropic måste dessutom knyta detta till oberoende verifierat arbete och verklig nytta.**

## 1. Vad boken faktiskt tillför

Boken delar sina femton mätetal i tre kategorier. Jag tycker att kategorierna är mer överförbara till Nortropic än de enskilda Kubernetes-mätetalen. Tabellen nedan skiljer därför bokens innehåll från min föreslagna tillämpning. fileciteturn0file0

| Bokens kategori | Vad den övervakar | Möjlig motsvarighet i Nortropic |
|---|---|---|
| **Cluster state metrics**, sidorna 4–5 | Nodernas hälsa, önskat kontra faktiskt antal instanser, tillgänglighet. | Vilken exekveringskapacitet finns, vilken är faktiskt användbar och varför skiljer sig verkligheten från planen? |
| **Resource metrics**, sidorna 6–8 | Minne, CPU och disk, inklusive begärda resurser och gränser. | Vilken resurs begränsar arbetet: datorn, modellåtkomsten, verktygen, budgeten eller något annat? |
| **Control plane metrics**, sidorna 8–10 | Ledarskap, API-anrop, arbetsköer och schemaläggning. | Fungerar själva samordningen: tilldelning, ägarskap, köer, återhämtning och verifiering? |

### Den viktigaste överföringen: övervaka också det som styr arbetet

Det är lätt att tänka:

> ”Vi övervakar våra workers.”

Men min tillämpning av bokens tredje kategori blir:

> **Vi måste också kunna avgöra om systemet som fördelar, följer upp och avslutar arbetet fungerar.**

Ett hypotetiskt Nortropic kan ha fem välfungerande workers men ändå stå stilla därför att uppgifter aldrig tilldelas, resultat fastnar före verifiering eller gamla reservationer inte släpps.

Då är fler workers fel lösning.

Boken betonar också att mätetal behöver sättas i samband med **händelser** – exempelvis starter, stopp och förändringar – för att underlätta felsökning. För Nortropic skulle motsvarande samband kunna vara mellan ett prestandafall och en ändrad modell, en ny verktygsversion eller en ändring i arbetsflödet. Det är min analogi till bokens resonemang på sidan 10. fileciteturn0file0

### Men en fungerande process är inte samma sak som ett bra resultat

För Nortropic skulle jag vilja hålla isär:

**Processen lever → processen är redo → arbetet går framåt → resultatet är verifierat → resultatet skapar nytta.**

Dessa är olika påståenden. En grön indikator för det första får inte användas som bevis för det sista.

En liten källkritisk detalj: boken bör inte användas som en exakt installationsmanual. Exempelvis är dess beskrivning av Metrics Server bredare än projektets egen dokumentation, som beskriver CPU- och minnesmätning för autoskalning och uttryckligen säger att Metrics Server inte är avsedd som generell övervakningslösning. Principerna är användbara; tekniska detaljer behöver kontrolleras mot aktuell dokumentation. citeturn885318view3

## 2. Det starkaste fyndet: Datadogs verklighetsbaserade tester av autonoma agenter

Datadogs artikel **“How we built a real-world evaluation platform for autonomous SRE agents at scale”**, publicerad den 7 april 2026, är den källa jag skulle prioritera högst för en fortsatt djupdykning. citeturn183944view0

De beskriver ett problem som ligger nära vår förbättringsambition: en ändring förbättrade vissa felsökningar men försämrade andra, trots att vanliga tester fortsatte vara gröna.

Deras lösning blev återspelbara felsökningsscenarier med ett separat facit och en rekonstruerad miljö av tillgängliga signaler. Agenten får undersöka miljön men inte se facit. De upptäckte också att scenarierna behövde innehålla irrelevanta fel, närliggande komponenter och vilseledande signaler. Alltför rena scenarier gav en överdrivet positiv bild av agentens förmåga. De jämför beteende över olika typer av incidenter, modeller och konfigurationer – inte bara ett genomsnittligt slutresultat. Detta är deras egen tekniska redogörelse, inte en oberoende utvärdering. citeturn183944view0

### Min slutsats för Nortropic: erfarenhet bör kunna bli ett återspelbart prov

Vi har redan ett starkt spår kring att bevara källor och erfarenheter. Här ser jag en möjlig konkretisering:

> **När något viktigt går fel ska Nortropic inte bara kunna minnas förklaringen. Det ska, där det är praktiskt möjligt, kunna pröva en framtida version mot motsvarande situation igen.**

Ett tänkt exempel:

En uppgift blir inte färdig. I omgivningen finns samtidigt ett gammalt testfel, hög minnesanvändning och en varning från en modellleverantör. Den verkliga orsaken är att resultatet aldrig kom vidare till verifiering.

En framtida förbättring ska då prövas på om den kan skilja huvudorsaken från bakgrundsbruset – inte bara känna igen texten i en tidigare incidentrapport.

För ett sådant prov skulle jag vilja bevara tillräckligt av uppgiftens indata, versioner, observerbara händelser och verktygssvar för att återskapa situationen. Facit behöver vara separat och tillförlitligt. Vissa scenarier ska dessutom hållas undan från själva förbättringsarbetet, så att vi inte bara tränar systemet på att klara sina kända exempel.

Det här passar mycket väl med Evolution Plane:

**Förbättringsförslag → prövning mot verkliga feltyper → kontroll av försämringar på andra områden → eventuell införlivning.**

Inte: ”Den nya versionen verkar smartare, därför inför vi den.”

Och inte heller: ”Nu behöver vi bygga en stor ny evalplattform.” Först behöver Recompile avgöra hur mycket av detta som kan göras med befintliga evidens- och verifieringsmekanismer.

## 3. Datadog har flera andra områden som träffar våra befintliga frågor

### Agent Observability: följ hela arbetet, inte bara modellanropet

Datadogs nuvarande **Agent Observability** kombinerar spårning av agentkörningar med versionshanterade testdata, experiment, automatiska utvärderingar och mänsklig granskning. De beskriver också kopplingar mellan agentbeteende, bakomliggande tjänster och användarupplevelse. citeturn183944view1

För Nortropic skulle jag översätta detta till att kunna följa en sammanhängande kedja:

`Uppdrag → uppgift → försök → modell/verktyg → kandidat → verifiering → publicering → utfall`

Det är en föreslagen observationskedja, inte ett påstående om vad som saknas i dagens kod.

Den skulle hjälpa oss att besvara frågor som:

*Var försvann tiden? Varför upprepades samma arbete? Vilken förändring ökade omarbetningen? Blev det billigare att få ett godkänt resultat, eller bara billigare per modellanrop?*

Här skulle jag prioritera **total kostnad per verifierat uppdrag**, med kostnaden för misslyckade försök och omarbete inkluderad. Jag skulle även vilja mäta hur länge arbetet väntar mellan steg. En lång total ledtid behöver inte bero på att modellen arbetar långsamt.

För modell- och arbetsflödesjämförelser bör vi inte nöja oss med en lyckad körning. Datadogs experimentdokumentation har uttryckligt stöd för upprepade körningar för att hantera variation mellan agentresultat. Det är ett relevant arbetssätt att pröva även hos oss. citeturn673350search3

**Viktig gräns:** en automatisk kvalitetsbedömning är inte automatiskt samma sak som Nortropics oberoende verifiering. Vi behöver bestämma vad respektive kontroll faktiskt bevisar.

### Bits Investigation: autonom undersökning före autonom åtgärd

Datadogs **Bits Investigation** undersöker larm genom att samla kontext, formulera flera tänkbara orsaker och söka stöd i bland annat mätetal, loggar, spårningar och förändringar. Hypoteserna kan klassificeras som bekräftade, avfärdade eller otillräckligt utredda, och slutsatserna kopplas till evidens. citeturn885318view5

Detta är enligt mig ett direkt relevant mönster för Nortropic.

Anta att en worker inte verkar komma framåt. Det kan bero på att modellen fortfarande arbetar, att ett verktyg väntar, att leverantören begränsar anrop, att arbetet redan är färdigt men inte uppdaterat i vyn – eller att något verkligen har låst sig.

Min föreslagna princip blir:

**Signal → undersökning → underbyggd diagnos → åtgärd inom befogenhet → kontroll av resultatet.**

Inte automatiskt ”starta om”.

Det intressanta är också att skilja **rätten att undersöka** från **rätten att förändra**. En felsökningsförmåga kan få läsa relevant information och pröva hypoteser utan att därmed få ändra behörigheter, radera arbetsmaterial eller sänka verifieringskraven.

Det här behöver inte bli en permanent ”SRE-agent” eller ny förvaltning. Det kan vara en kvalificerad förmåga som används när situationen kräver den.

### SLO:er och Event Management: uppmärksamhet efter konsekvens

En SLO är ett definierat mål för en tjänsts tillförlitlighet. Datadog stödjer bland annat felbudgetar och larm utifrån hur snabbt dessa förbrukas. Googles SRE-litteratur beskriver samma grundidé: larm bör knytas till risken att missa tjänstens mål, med genomtänkta avvägningar mellan snabb upptäckt och onödiga larm. citeturn183944view3turn377480view2

Min tillämpning för oss är att inte börja med godtyckliga ambitionssiffror, utan med arbetskontraktet:

> ”Vilken andel accepterade uppdrag av denna typ blir verifierat färdiga inom den tid som uppdraget kräver?”

Här måste även uppdrag som aldrig kom igång eller fastnade räknas korrekt. Annars kan statistiken bli bättre bara för att de svåraste fallen försvinner ur nämnaren.

Datadogs Event Management är också relevant genom att gruppera, reducera dubbletter och berika händelser med sammanhang. citeturn885318view2

För Nortropic skulle ett gemensamt leverantörsproblem kunna ge **en sammanhållen incident med flera följder**, snarare än tjugo separata krav på din uppmärksamhet. De ursprungliga händelserna ska fortfarande finnas kvar som evidens.

Det passar din riktning med färre onödiga ägarstopp: systemet bör kunna återhämta sig inom sitt mandat och kontakta dig när ditt omdöme faktiskt behövs.

Men här drar jag en skarp gräns:

> **Tillgänglighet och ledtid kan ha felbudgetar. Otillåtna handlingar ska inte behandlas som en förbrukningsbar felbudget.**

### Software Catalog: information som hjälper systemet hitta rätt

Datadogs Software Catalog kopplar samman komponenter med bland annat ansvar, beroenden, kod, operativ information och identifierade luckor i övervakningen. citeturn885318view1

Det knyter direkt an till vårt informationsarkitekturspår. Min tillämpning är att Nortropic snabbt ska kunna svara på:

*Vad är detta? Vad beror det på? Vilken version används? Vilka bevis finns för att den är kvalificerad? Vad påverkas om den ändras?*

Värdet är då inte ännu en katalog att underhålla, utan mindre tid för att leta och orientera sig.

Däremot ska vi inte kopiera ett produktbudskap om en central sanningskälla rakt av. För Nortropic bör en sådan översikt härledas från de register och bevis som faktiskt äger informationen. Annars bygger vi en andra verklighet bredvid den första.

### MCP, Pup och automatisering: möjliga levererade förmågor

Datadog erbjuder agentgränssnitt via **MCP Server** och **Pup CLI** för åtkomst till operativ information. Det är relevant som ett möjligt sätt att ge en Nortropic-worker avgränsad tillgång till observationer, i stället för att klistra in stora mängder loggar i en prompt. citeturn885318view0

De har också **Workflow Automation** och **Bits Agent Builder** för händelsestyrda arbetsflöden och anpassade agentuppgifter. Dessa är värda att studera som möjliga externa förmågor, inte som ett automatiskt skäl att flytta Nortropics organisation eller befogenhetsmodell dit. citeturn317163view4turn317163view3

Den strategiska frågan blir:

> **Vilken del är specifik för Nortropic, och vilken del kan vi använda som en kvalificerad tjänst från någon annan?**

Vi behöver inte bygga all generell felsökning själva. Men en extern tjänsts rekommendation får inte bli ett sätt att kringgå Kernel.

## 4. Digitala ger en konkret tillämpning: övervaka det kunden faktiskt behöver

Datadog har **Synthetic Monitoring** för automatiserade användarresor och API-tester, samt **Real User Monitoring**, RUM, för att observera verkliga användares prestanda, fel och interaktioner. citeturn832239view3turn832239view4

Detta passar vårt befintliga Digitala-resonemang om att en webbplats ska fortsätta observeras och förbättras efter lansering, och att teknisk integritet, upplevelsekvalitet och verkliga utfall behöver hållas isär. fileciteturn0file1

Ett tänkt scenario:

Digitala förvaltar en webbplats för ett lokalt företag. Startsidan svarar och webbservern ser frisk ut. Men besökare på mobil kan inte skicka offertformuläret efter en uppdatering.

En kontroll som bara frågar ”är sidan uppe?” skulle inte räcka som Nortropics kvalitetsbevis.

Jag skulle i stället vilja pröva en kedja där en säker testresa fyller i formuläret och kontrollerar att en testförfrågan faktiskt når rätt mottagande system. Verkliga användarsignaler kan komplettera med information om var problem uppstår. En undersökning kan sedan jämföra dessa observationer med den senaste publiceringen.

Efter en åtgärd behöver samma resa fungera igen. Händelsen kan därefter bli ett regressionstest.

Testet måste förstås vara avgränsat så att det inte skickar falska kundärenden, riktiga betalningar eller återkommande skräppost.

Det här är en bra konkretisering av skillnaden mellan:

**”Vi publicerade en webbplats.”**

och:

**”Vi förvaltar en fungerande digital tjänst.”**

Men varken RUM eller syntetiska tester avgör automatiskt om designen är tydlig, företaget framstår som trovärdigt eller affärsresultatet förbättrades av just vår ändring. De behöver ingå i Digitalas bredare kvalitetskontrakt, inte ersätta det.

## 5. Vad jag skulle ta med – och vad jag skulle skydda oss mot

### Behåll skillnaden mellan evidens, observation och tolkning

Jag skulle vilja att Nortropic håller tre saker tydligt separerade.

**Auktoritativt tillstånd och nödvändig evidens** beskriver vad systemet faktiskt har beslutat, gjort och verifierat.

**Telemetri** hjälper oss se förlopp, variationer, resursanvändning och fel.

**Diagnoser och visualiseringar** är tolkningar av detta material.

En snygg Datadog-vy eller övertygande AI-diagnos får inte skriva över den första nivån. Detta ligger i linje med vårt befintliga Recompile-underlag om att projektion inte är sanning och att verifieringens auktoritet ska vara skild från kandidatens. fileciteturn0file3

### Gör observationsinformationen användbar utan att göra leverantören permanent

OpenTelemetry är relevant som möjlig teknisk grund eftersom det erbjuder leverantörsneutral instrumentering, insamling och export av telemetri. Det är inte i sig en lagrings- eller analysplattform. citeturn377480view1

Min rekommendation är därför att först definiera vilka händelser och samband Nortropic behöver förstå, och därefter välja hur de ska exporteras.

Det gör inte alla delar utbytbara utan arbete, men minskar risken att uppdrag, försök och verifiering bara går att förstå inuti en viss leverantörs produkt.

Datadogs **Observability Pipelines** är dessutom ett relevant studiematerial för filtrering, maskering och fördelning av data till olika destinationer. citeturn377480view0

För oss skulle jag vilja skilja diagnostisk data som kan gallras eller samplas från evidens som måste bevaras. Kunduppgifter, hemligheter och hela arbetskontexter ska inte exporteras slentrianmässigt.

### Gör bristande insyn synlig

Min föreslagna regel är:

> **Ingen observation är inte samma sak som ett friskt tillstånd.**

Systemet behöver kunna visa när en uppgift är baserad på gammal data, saknar täckning eller bara är en osäker slutsats.

Samtidigt bör ett fel i en extern övervakningstjänst inte automatiskt stoppa allt arbete. Endast operationer som verkligen är beroende av den saknade informationen eller evidensen ska påverkas på motsvarande sätt.

Och även om ett verktyg kan anslutas via MCP betyder det inte att alla interna steg i en executor blir synliga. Den faktiska täckningen måste kontrolleras i ett avgränsat test.

### Låt inte detta bli ännu ett gränssnittsprojekt

För Verkstadsgolvet och Aquarium är den första frågan här inte hur Datadogs paneler ser ut.

Den är:

> **Vilken tillförlitlig information behöver finnas för att vi senare ska kunna visa mindre – men mer meningsfullt?**

Jag skulle därför behålla vår ordning: undersök observationsmodellen nu, men låt det större HCI- och kontrollrumsarbetet ligga kvar i sitt avsedda senare forskningspass.

## 6. Kopplingen till Kubernetes och mer hårdvara

Det här hjälper också med vår fråga om när ytterligare exekveringskapacitet behövs.

I ett tänkt fall kan en växande kö bero på fullt utnyttjad dator. I ett annat kan den bero på begränsad modellåtkomst, långsam verifiering eller ett samordningsfel.

Min slutsats är att vi bör försöka skilja dessa fall åt **innan** vi tolkar en kö som ett inköpsbehov.

Samma sak gäller Kubernetes. Jag ser inget i den här boken som i sig motiverar att vi byter driftplattform. Ett sådant beslut bör senare kunna motiveras av verkliga behov av exempelvis arbetsfördelning mellan värdar och driftkrav – jämfört med vad enklare lösningar kan göra.

**Lärdomen kan vara omedelbart relevant även om produkten aldrig blir det.**

## 7. Vad jag skulle prioritera härnäst

**Först skulle jag djupdyka i Datadogs återspelbara agentutvärderingar.** Det berör direkt vår viktigaste förbättringsfråga: hur vet vi att en ändring gör Nortropic bättre som helhet och inte bara bättre på det exempel vi nyss tittade på?

**Därefter skulle jag koppla ihop Agent Observability med Bits Investigation.** Då kan vi undersöka vilken information som krävs för att förklara ett misslyckat uppdrag och när en diagnos är tillräckligt underbyggd för en tillåten åtgärd.

**Sedan skulle jag använda Digitalas efterlanseringsarbete som konkret tillämpning.** Där blir skillnaden mellan teknisk aktivitet och kundnytta lättare att testa.

Detta bör gå in i Improvements som källbelagda mönster och experimenthypoteser – inte som nya obligatoriska subsystem. Vårt Recompile-upplägg är redan avsett att jämföra sådant material med verklig repostatus, slå samman överlapp och härleda minsta användbara arkitektur. fileciteturn0file3

Ett bra avgränsat experiment, när förutsättningarna finns, vore att ta **en arbetskedja** och pröva tre säkra felvarianter: problem hos modellleverantören, ett resultat som fastnar före verifiering och en inaktuell observation. Jämför nuvarande sätt att undersöka med en variant som har bättre sammanlänkad evidens.

Framgång betyder då att rätt problem skiljs från fel problem, att osäkerhet redovisas, att inga otillåtna åtgärder görs och att resultatet kan prövas igen. Inte att vi får fler diagram.

**Så ja: Datadog förtjänar en ordentlig fördjupning. Framför allt som referens för hur Nortropic kan veta vad som händer, undersöka varför och pröva om nästa förändring faktiskt hjälper. Det är betydligt mer relevant för vår autonomi än att bara kunna se att våra workers är igång.**

---

## Meddelande 5 — Johnny (användare)

gör en ordentligt fördjupning och så kan jag inhämta rapporter eller böcker som du inte kommer åt

---

## Meddelande 6 — ChatGPT (assistent)

Jag fördjupar Datadogs autonoma felsökning, evidens för tillförlitliga diagnoser och kopplingen till Nortropics verifiering, jämfört med forskning och SRE/Kubernetes. Jag markerar prioriterade böcker och rapporter där fulltext saknas.

---

## Meddelande 7 — ChatGPT (assistent)

Två fynd sticker ut: Cloud-OpsBench skiljer korrekt diagnos från evidensinsamling, medan självförbättrande agenter ofta missar följdfel. *Observability Engineering*, andra upplagan, verkar mest värdefull att inhämta.

---

## Meddelande 8 — ChatGPT (assistent)

Ett nytt Datadog-spår är Bits Evals, som omvandlar produktionsfel till testfall och förbättringsjämförelser. Dessutom bör korrekt diagnos, tystnade larm och återställd funktion utvärderas separat.

---

## Meddelande 9 — ChatGPT (assistent)

**Min huvudslutsats är att Datadog är relevant för något större än övervakning: hur Nortropic kan undersöka sitt eget arbete, skilja välgrundade beslut från lyckliga gissningar och förbättras utan att samtidigt bli sämre på andra uppgifter.**

Fördjupningen gav framför allt tre viktiga fynd:

- **Rätt diagnos är inte samma sak som en tillräckligt underbyggd diagnos.**
- **En agent kan vara bättre på att förklara varför en ändring hjälper än på att förutse vad samma ändring förstör.**
- **Själva observationsförmågan behöver testas.** Att samla mycket data bevisar inte att systemet kan upptäcka och skilja relevanta fel åt.

Det finns också en bok som jag nu skulle prioritera tydligt: **andra upplagan av *Observability Engineering***. Den behandlar uttryckligen instrumentering av AI-agenter, styrning av observationsdata och kopplingen till kundutfall. Jag har kunnat läsa presentationen, men inte fulltexten. Mer om den och två andra böcker längre ned. citeturn346324view0

Det här är en analys av källorna och deras möjliga betydelse för Nortropic. Jag har inte testat Datadog i vår driftmiljö eller inventerat den aktuella repoversionen.

# 1. Vad Datadogs egna erfarenheter faktiskt visar

## Kubernetes-boken är en utgångspunkt, inte den viktigaste källan

Din bok delar övervakningen i **cluster state metrics**, **resource metrics** och **control plane metrics**. På sidorna 8–10 blir den särskilt intressant för oss: där övervakas samordningen genom bland annat arbetsköer, schemaläggning och API-anrop — inte bara de processer som utför arbetet. fileciteturn0file0

Min överföring till Nortropic är:

**Workers kan fungera samtidigt som organisationen misslyckas.**

En worker kan producera ett korrekt resultat som aldrig når verifieringen. En verifierare kan fungera men få fel version. Ett uppdrag kan vara färdigt medan gränssnittet fortfarande visar att det väntar.

Därför skulle jag vilja kunna observera både **arbetets utförande** och **övergångarna mellan dess steg**.

Kubernetes controllers ger ett närliggande arkitekturmönster: kontinuerlig jämförelse mellan önskat och faktiskt tillstånd. Men detta är inspiration till hur samordningen kan fungera, inte ett argument för att Nortropic måste köras på Kubernetes. citeturn214010view1

## Datadogs viktigaste erfarenhet: mer kontext kan försämra resultatet

I sin tekniska redogörelse från april 2026 beskriver Datadog hur en ändring i felsökningsagentens inledande kontext förbättrade vissa undersökningar men försämrade andra. Verktygstester kunde fortfarande vara gröna.

De byggde därför utvärderingar med separat facit och en rekonstruerad observationsmiljö. Agenten får undersöka miljön men inte se facit. Miljön behöver också innehålla verklighetens distraktioner, närliggande komponenter och missvisande signaler — inte bara de uppgifter som leder direkt till svaret. citeturn407516view0

En viktig precisering av mitt förra svar: deras **world snapshot är inte en fullständig, förlustfri kopia av den ursprungliga driftmiljön**. Det är en rekonstruerad representation som bevarar relevanta signaler och samband för testet. Datadog beskriver också att AI hjälper till att skapa och validera testmaterial, med mänsklig granskning och kalibrering. Det är användbar metodinformation, men inte ett oberoende bevis på att alla etiketter eller utvärderingar är korrekta. citeturn407516view0

### Vad detta betyder för vår kontexthantering

Jag skulle inte dra slutsatsen att Nortropic ska ge varje worker maximal bakgrundsinformation.

Jag skulle vilja pröva om systemet kan ge **rätt information, med känd källa och rätt aktualitet, vid rätt beslutspunkt**.

Anta att ett uppdrag står stilla. Kontexten innehåller:

*En gammal incident om minnesbrist. En aktuell varning från modellleverantören. Ett misslyckat test från en annan arbetsgren. Ett resultat som faktiskt väntar på verifiering.*

Frågan är inte bara om agenten kan läsa allt. Frågan är om den kan avgöra **vilken uppgift som gäller just detta försök**, och vad den behöver kontrollera innan den agerar.

Min föreslagna utvärdering skulle därför skilja mellan två fel:

**Agenten fick tillräcklig information men tolkade den fel.**

**Agenten fick aldrig den information som krävdes.**

De kräver olika förbättringar. Det första kan handla om arbetsmetod eller modellförmåga. Det andra kan handla om informationsarkitektur, verktyg eller kontexturval.

Detta knyter samman Datadog-spåret med vårt befintliga krav på spårbara källor och att aktuell verklighet ska väga tyngre än äldre synteser. fileciteturn0file3

## Datadogs rapport ger också en kapacitetsvarning

Jag kom åt hela webbutgåvan av *State of AI Engineering*, inklusive metodavsnittet.

Två fynd är relevanta. Datadog uppskattar att **69 procent av inputtokenmängden** i det undersökta materialet kom från systemmeddelanden; uppskattningen bygger på teckenräkning, inte exakt tokenisering. För mars 2026 utgjorde hastighetsbegränsningar ungefär en tredjedel av de registrerade LLM-felen. Materialet kommer från Datadogs kunder och är inte ett representativt urval av alla AI-system. citeturn704172view0

Min slutsats för Nortropic är inte att systeminstruktioner är slöseri. Den är att **vi behöver mäta vilken resurs som faktiskt begränsar verifierat arbete**.

Fler workers hjälper inte nödvändigtvis när begränsningen finns i modellåtkomst, verifieringskapacitet eller samordning. Två exekutorer som delar samma begränsade leverantörsresurs är heller inte automatiskt två oberoende reservvägar.

Det är ytterligare ett skäl att låta kapacitetsobservation föregå hårdvaruexpansion.

# 2. Två forskningsfynd som skärper vår verifieringsmodell

## Cloud-OpsBench: ett korrekt svar kan sakna tillräckliga belägg

Den reviderade versionen av **Cloud-OpsBench** omfattar 754 verifierade felscenarier över 57 feltyper i två testapplikationer. Den skiljer mellan korrekt identifierad felorsak och om agenten faktiskt har samlat den evidens som testets diagnostiska milstolpar kräver.

För de starkaste resultaten i respektive applikation var diagnoskorrektheten **76 respektive 68 procent**, medan motsvarande andel med fullständig evidenskedja var **38 respektive 15 procent**. Det senare betyder inte att alla övriga diagnoser var fel, utan att de inte uppfyllde testets krav på diagnostisk underbyggnad. citeturn409731view0

Det är ett forskningsförtryck med två testmiljöer och ett bestämt agentupplägg. Siffrorna ska inte översättas till Nortropics förväntade prestanda. Men skillnaden mellan **svarskvalitet och evidenskvalitet** är mycket relevant. citeturn117289view10

### Min tillämpning: verifiera beslutets underlag, inte bara slutsatsen

Tänk att en felsökare säger:

> ”Problemet beror på en gammal reservation. Ta bort den.”

Det kan vara rätt. Men innan en förändring utförs skulle jag vilja veta att relevanta förutsättningar verkligen har kontrollerats: gäller reservationen rätt försök, finns fortfarande en aktiv ägare, och kan borttagningen påverka pågående arbete?

Det behöver inte bli en obligatorisk lång checklista för varje observation. **Evidenskravet bör anpassas till beslutets konsekvens.**

En preliminär diagnos kan få vara osäker. En ofarlig kompletterande läsning kräver inte samma underlag som en förändring i delat tillstånd.

Det viktiga är att Nortropic inte behandlar följande som likvärdiga:

**En rimlig hypotes. Ett belagt påstående. Ett tillräckligt underlag för en viss åtgärd.**

Och vi ska inte kräva att agenten följer exakt samma kommandosekvens som en människa. Målet är tillräckliga belägg, inte ritualiserat verktygsanvändande.

## AHE: självförbättring har en blind fläck för försämringar

Studien **Agentic Harness Engineering**, AHE, undersöker hur en agent kan förbättra sin egen arbetsmiljö medan grundmodellen hålls fast. Den gör komponenter redigerbara, organiserar tidigare körningar som evidens och kräver förutsägelser om vilka uppgifter en ändring ska förbättra eller riskera att försämra.

Ett särskilt relevant resultat är att förmågan att förutse nya regressioner var svag: genomsnittlig regression-recall var **11,1 procent över nio utvärderingsrundor**. Författarna beskriver detta som en tydlig begränsning. Studien gäller en kontrollerad benchmarkmiljö, inte ett bevis på säker självevolution i en verklig organisation. citeturn409731view1

### Min tillämpning: låt inte förbättringsförslaget ensamt bestämma sitt prov

Detta stärker vårt befintliga krav på att utvärderingens auktoritet ska ligga utanför kandidatens. fileciteturn0file3

Jag skulle vilja att ett förändringsförslag anger:

**Vad ska bli bättre? Varför? Vilken observation skulle visa att hypotesen var fel? Vad får inte försämras?**

Men agentens egen uppfattning om vilka områden som kan påverkas får inte vara den enda grunden för testurvalet.

Ett konkret exempel är att förkorta en instruktion som verkar repetitiv. Förslaget kan minska kostnaden och ge samma resultat på vanliga uppgifter, men påverka beteendet vid ett sällsynt versionsbyte eller felaktigt verktygssvar.

Därför skulle jag kombinera **riktade tester av ändringen** med **ett litet oberoende urval av centrala beteendetester**, och bredare jämförelser när förändringens typ motiverar det.

Det betyder inte att varje förbättring ska omkvalificera hela Kernel. Det betyder att **lokal framgång inte ensam får räknas som organisatorisk förbättring**.

# 3. Den viktigaste arkitekturfrågan: vad är observation, och vad är bevis?

Jag skulle hålla isär tre saker i Nortropic:

| Typ av information | Frågan den besvarar | Föreslagen behandling |
|---|---|---|
| **Auktoritativt tillstånd och nödvändig evidens** | Vad beslutades, utfördes och verifierades? | Ägs av avsedda register och verifieringsmekanismer. |
| **Diagnostisk telemetri** | Hur förlöpte arbetet, var väntade det och vilka fel uppstod? | Används för undersökning; kan ha begränsad täckning och lagringstid. |
| **Tolkningar och projektioner** | Vad tror vi att detta betyder, och hur ska det visas? | Ska kunna härledas tillbaka till underlaget och visa osäkerhet. |

Detta är min föreslagna tillämpning av vårt befintliga krav på att **projektion inte är sanning**. fileciteturn0file3

Datadog kan vara mycket användbart i de två senare rollerna. Det betyder inte att en grön panel eller en AI-diagnos ska avgöra vad Nortropic auktoritativt räknar som färdigt.

## Följ sambanden mellan arbetets steg

OpenTelemetry erbjuder spårningar med deloperationer, attribut, händelser och länkar mellan operationer. Det är en användbar teknisk grund för att koppla samman ett förlopp även när arbetet går genom flera komponenter. citeturn924381view2

För Nortropic skulle jag vilja kunna följa:

**Uppdrag → uppgift → försök → verktygsanrop → resultat → verifiering → publicering → observerat utfall.**

Men även relationer som inte är en rak kedja: ett nytt försök ersätter ett tidigare, två kandidater bygger på samma underlag, en verifiering avser en specifik version.

Detta är min poäng med informationsarkitekturen här: **systemet behöver kunna hitta rätt samband, inte bara rätt text**.

Jag skulle även vilja veta vilken kontext som faktiskt var tillgänglig vid ett viktigt beslut: källversioner, relevanta verktygssvar och eventuell bortvald eller trunkerad information. Däremot behöver vi inte samla modellens privata interna resonemang eller exportera hela kundkontexter för att kunna undersöka observerbart beteende.

## Bevara inte allt urskillningslöst

OpenTelemetry betonar att instrumentering kan samla känsliga uppgifter och att ramverket inte självt kan avgöra vad som är känsligt i den aktuella verksamheten. Dokumentationen rekommenderar dataminimering och beskriver filtrering, borttagning och maskering av attribut. citeturn675469view3

Min rekommendation är därför att skilja mellan **det vi behöver bevara som bevis**, **det som hjälper felsökning** och **det som en extern analystjänst behöver se**.

Då kan Nortropic exempelvis bevara ett nödvändigt verifieringskvitto utan att exportera hela kunddokumentet som ingick i arbetet.

Det är också viktigt för återspelning: en rekonstruerad testmiljö kan vara tillräcklig för en viss utvärdering utan att vara fullständigt originalbevis. Dessa roller ska inte blandas ihop.

## Testa observationsförmågan

Forskningsprototypen **OXN** undersöker observability genom att variera både fel och instrumentering, exempelvis hur data samlas in. Poängen är att bedöma observationsuppläggets förmåga, inte bara mängden insamlad data. citeturn291952view3

Min föreslagna fråga för Nortropic blir:

> **Kan den information vi samlar faktiskt skilja de situationer åt som kräver olika åtgärder?**

Det är ett bättre acceptanskriterium än ”vi har kopplat in tracing”.

Om slut på modellåtkomst och en lokal låsning båda bara ser ut som ”ingen aktivitet”, har vi fortfarande ett observationsproblem.

# 4. Autonom återhämtning behöver två olika slingor

Här vill jag nyansera mitt förra svar.

Jag betonade undersökning före åtgärd. Men **en fullständig grundorsaksanalys behöver inte alltid föregå en säker, redan kvalificerad åtgärd som minskar skadan**. Googles SRE-litteratur skiljer på att begränsa påverkan och att senare fastställa den djupare orsaken. citeturn922203view0

För Nortropic skulle jag därför vilja skilja mellan:

**Återställningsslingan:** begränsa påverkan och få arbetet att fungera inom befintligt mandat.

**Lärandeslingan:** förstå varför felet uppstod, pröva förklaringen och förebygga återkomst.

Exempelvis kan en redan kvalificerad återställning av en publicering vara rätt innan vi vet exakt varför den nya versionen misslyckades. Men ”något verkar fel, starta om allt” är inte samma sak.

## Återställbarhet måste avse verkliga effekter

Forskningssystemet **STRATUS** är intressant eftersom det formaliserar åtgärder och återställning. Dess säkerhetsresonemang bygger bland annat på en skrivande agent åt gången, en begränsad åtgärdssekvens och att återställningen kan återföra tillståndet exakt.

Garantin gäller dessutom tillstånden vid de definierade transaktionsgränserna, inte att varje mellanliggande tillstånd är ofarligt. Författarna anger själva att perfekt återställning är svår vid externa interaktioner och applikationsspecifika tillstånd. citeturn346324view4

Det gör studien värdefull som något att granska, inte som en färdig säkerhetsgaranti att importera.

Min slutsats för Nortropic är att ett återställt konfigurationsvärde inte nödvändigtvis återställer verkligheten. Ett mejl kan redan ha skickats. En extern beställning kan ha registrerats. Ett avbrott kan redan ha påverkat en användare.

Därför bör återhämtning kvalificeras mot **åtgärdens faktiska effekt**, inte bara dess kommandon.

## Försök att reparera får inte förstärka felet

Google beskriver hur återförsök på flera nivåer kan multiplicera belastningen och skapa kaskadfel. Rekommendationerna omfattar begränsade återförsök, backoff och gemensamma retry-budgetar. citeturn675469view2

Min tillämpning är att Nortropic måste undvika att workers, supervisor och felsökare oberoende försöker lösa samma problem genom fler anrop.

Jag skulle även pröva hur systemet klarar att **felsökningen delar flaskhals med det felande arbetet**. Om alla tillgängliga resurser konsumeras av misslyckade försök kanske varken verifiering eller återhämtning kan köras.

Det behöver inte betyda en separat agentflotta. Det kan räcka med prioritering, enkla deterministiska kontroller och begränsning av nytt arbete.

## Färre ägarstopp, men bättre underlag när du behövs

Googles SRE-principer knyter larm till symtom och tjänstepåverkan snarare än till varje intern avvikelse. SLO-baserad larmning ger ytterligare metoder för att balansera upptäckt och onödiga larm. citeturn214010view2turn117289view2

För Nortropic skulle jag vilja att en uppmärksamhetssignal berättar **vad som påverkas, vad systemet redan har gjort och varför just ditt omdöme behövs**.

En varning behöver inte stoppa annat självständigt arbete. Men en osäkerhet kring befogenhet ska inte lösas genom att behandla otillåtna handlingar som en acceptabel felbudget.

# 5. Vilka ytterligare Datadog-delar är värda att studera?

Jag skulle prioritera några få områden, snarare än försöka efterlikna hela produktplattformen.

## Agent Observability och Bits Investigation

Agent Observability kopplar samman körningsspår, versionshanterade testdata, experiment och automatiska eller mänskliga utvärderingar. Bits Investigation arbetar med konkurrerande hypoteser och kan integreras i arbetsflöden som går vidare till åtgärder. citeturn214010view5turn214010view3

För oss är värdet två olika förmågor: att **förstå en enskild körning** och att **jämföra beteende mellan versioner**.

Jag skulle dock inte anta att Datadog automatiskt förstår Nortropics betydelse av exempelvis ”verifierad kandidat” eller ”tillåten publicering”. Det måste definieras och kontrolleras i integrationen.

## Test Optimization: relevant för både hastighet och tillförlitlighet

Det här är ett ytterligare relevant fynd. Datadogs Test Optimization omfattar bland annat insyn i testkörningar, identifiering av instabila tester och urval av tester utifrån kodförändringar. citeturn214010view7

Min forskningsfråga för Nortropic är:

**Hur kan vi minska onödigt verifieringsarbete utan att minska verifieringens förmåga?**

Här krävs en viktig distinktion. Ett kodbaserat förändringsurval är inte automatiskt tillräckligt när beteendet ändras genom modellbyte, nya verktygsinstruktioner eller annorlunda kontexturval.

Och ett instabilt test ska inte tyst avaktiveras bara för att det stör flödet. Först behöver vi förstå vad det mäter och vilket skydd som försvinner.

## Software Catalog och Event Management

Software Catalog knyter samman komponenter med ansvar, beroenden, versioner och operativ information. Event Management grupperar och berikar händelser samt reducerar dubbletter. citeturn675469view5turn675469view6

För Nortropic skulle jag ta med två mönster:

**Hitta rätt sammanhang snabbt.** Från ett problem ska det gå att nå rätt komponent, källa, version, arbetsinstruktion och tidigare evidens.

**Visa en sammanhängande incident i stället för många följdsymtom.** Ett leverantörsfel kan påverka flera uppdrag utan att varje uppdrag kräver ett separat ägarbeslut.

Men katalogen bör härledas från rätt informationsägare, och grupperingen får inte radera de ursprungliga observationerna.

Detta kan senare förbättra Verkstadsgolvet och Aquarium. Jag skulle däremot inte öppna ett nytt gränssnittsprojekt nu.

## MCP, Pup och datapipelines

Datadog erbjuder MCP och Pup CLI för agenters åtkomst till operativ information. Observability Pipelines erbjuder bearbetning och fördelning av telemetri, inklusive maskering och sampling. citeturn214010view6turn675469view4

Min tänkta integrationsprincip är:

**Nortropic kan använda Datadog som en avgränsad observations- och undersökningstjänst, utan att göra Datadog till organisationens auktoritet.**

Innan ett produktval skulle vi behöva testa faktisk datatäckning, åtkomstbegränsning, exportmöjligheter, integritet, kostnad och beteende när tjänsten inte svarar.

Vi har ännu inte tillräckligt underlag för att rekommendera ett helt Datadog-abonnemang eller en Kubernetes-migrering.

# 6. Ett konkret prov för Nortropic

Jag skulle börja med **en enda intern arbetskedja**, vald efter inventeringen i Recompile, och därefter använda Digitala som ytterligare tillämpning.

Hypotesen vore:

> **Bättre sammanlänkad och selektivt tillgänglig evidens förbättrar Nortropics förmåga att diagnostisera och återhämta arbete, utan fler skadliga åtgärder eller orimligt högre kostnad.**

## Först diagnostik, sedan verkliga åtgärdseffekter

Cloud-OpsBench ger reproducerbara observationer genom återspelning av stödda diagnostiska frågor. Det bevisar inte att en föreslagen förändring får rätt effekt i en levande miljö. Forskningsmiljöer som AIOpsLab kompletterar med verkliga testinstallationer, felinjektion och agentinteraktion. citeturn757638view1turn895745academia7

Min föreslagna ordning är därför: återspelbara diagnostikprov, därefter avgränsade åtgärdsprov i testmiljö och slutligen observation av riktigt arbete utan automatiska nya ingripanden.

Vi behöver inte installera samtliga forskningsramverk för att använda den skillnaden.

## Scenarier som kan avslöja relevanta svagheter

| Scenario | Vad provet ska skilja åt |
|---|---|
| **Modellåtkomsten är begränsad, datorn är frisk.** | Systemet ska inte felaktigt behandla problemet som lokal kapacitetsbrist. |
| **Kandidaten är färdig men verifieringen har fastnat.** | Systemet ska lokalisera rätt steg, inte börja om hela uppgiften. |
| **Arbetet är klart men observationsvyn är inaktuell.** | Systemet ska uppdatera sin bild, inte skapa dubbelt arbete. |
| **Ett externt anrop fick timeout men effekten kan ha genomförts.** | Systemet ska undersöka effektstatus innan ett riskabelt återförsök. |
| **En övertygande men orelaterad varning finns i kontexten.** | Systemet ska skilja relevanta belägg från distraktioner. |
| **Information saknas — eller inget är faktiskt fel.** | Systemet ska kunna välja fortsatt observation, redovisa osäkerhet eller avstå åtgärd. |

Det sista är avgörande. Ett prov där varje scenario alltid innehåller ett fel uppmuntrar inte nödvändigtvis ett system som kan låta välfungerande arbete vara i fred.

## Jämför observationerna utan att ändra allt samtidigt

Jag skulle jämföra nuvarande informationsunderlag med en variant där samma källor är bättre länkade och lättare att fråga efter. Modell, verktygsbefogenheter och budget hålls så lika som möjligt.

Körningarna bör upprepas. Anthropic skiljer i sin utvärderingsvägledning mellan att lyckas minst en gång på flera försök och att lyckas konsekvent. De skiljer också mellan agentens körningsförlopp och det faktiska slututfallet i miljön. Båda distinktionerna är viktiga här. citeturn469580view0

En liten pilot kan visa om riktningen är värd mer arbete. Den kan inte bevisa generell driftsäkerhet.

Jag skulle dessutom hålla undan några scenarier från själva förbättringsarbetet. Annars riskerar vi att mäta hur väl systemet anpassats till kända exempel.

## Vad jag skulle mäta

Jag skulle inte sammanfatta allt i ett enda ”autonomipoäng”.

I stället behövs separata svar på om diagnosen var korrekt, om underlaget räckte för åtgärden, om den faktiska effekten blev rätt och om något försämrades.

Därtill skulle jag följa ledtid, kostnad för samtliga försök och verifieringar samt din aktiva tidsåtgång. Pengar och ägartid bör redovisas var för sig.

För leveransstatistik behöver uppdrag som inte startade eller fastnade finnas kvar i rätt underlag. Annars kan systemet se bättre ut genom att bara räkna det som lyckades passera hela vägen.

**En förbättring ska helst ge mer verifierat arbete med mindre onödig inblandning — inte bara en högre andel snygga felsökningsrapporter.**

# 7. Digitala: bevis på fungerande tjänst, inte bara fungerande server

Datadogs Synthetic Monitoring kan testa användarresor och API-flöden. Real User Monitoring observerar bland annat verkliga användares prestanda och fel. citeturn675469view0turn675469view1

Det passar vår befintliga uppdelning mellan teknisk integritet, upplevelsekvalitet och verkliga utfall. fileciteturn0file1

Ett bra hypotetiskt prov vore ett offertformulär där sidan visar ”Tack!” men förfrågan aldrig når mottagande system.

Då räcker inte ett lyckat knapptryck eller ett HTTP-svar som kvalitetsbevis. Jag skulle vilja följa en säker testförfrågan hela vägen till ett kontrollerat mottagningskvitto, utan att skapa riktiga kundärenden eller skräppost.

Efter en åtgärd ska samma resa fungera igen. Händelsen kan därefter bli ett återkommande regressionstest.

Men detta ska fortfarande hållas åtskilt från frågan om sidan skapar fler kvalificerade förfrågningar. En fungerande testresa bevisar funktion, inte affärsnytta eller att en designändring orsakade en viss konverteringsförändring.

Det är just kombinationen jag tycker är intressant: **teknisk felsökning, professionell kvalitetsbedömning och verkliga utfall — utan att låtsas att någon av dem ersätter de andra.**

# 8. Material att inhämta

## Första prioritet: *Observability Engineering, 2nd Edition*

**Författare:** Charity Majors, Liz Fong-Jones, George Miranda och Austin Parker.

Honeycomb erbjuder en kostnadsfri kopia. Presentationen anger bland annat instrumentering av AI-agenter och andra icke-deterministiska arbetsflöden, styrning och kostnad samt kopplingen mellan SLO:er och kundpåverkan. Jag har kunnat läsa denna presentation, men inte fulltexten via deras hämtningsflöde. citeturn346324view0turn409731view3

**Varför jag prioriterar den:** den verkar ligga närmast skärningspunkten mellan vår exekvering, informationsarkitektur, förbättringsloop och Digitalas efterlanseringsarbete.

Jag skulle framför allt vilja undersöka hur boken behandlar observationsdata som grund för beslut, selektiv informationsinhämtning och praktisk instrumentering av agentarbete.

Min prioritering bygger på den publicerade innehållsbeskrivningen, inte på att jag redan har läst boken.

## Andra prioritet: *Release It! Second Edition*

**Författare:** Michael Nygard.  
**Undertitel:** *Design and Deploy Production-Ready Software*.

Förlagets innehållsförteckning omfattar bland annat stabilitetsmönster, timeouts, circuit breakers, avgränsning av fel, backpressure, kontrollplan och chaos engineering. Den fullständiga boken ingår inte i materialet jag har kunnat läsa. citeturn291952view6

**Varför den är relevant:** jag vill pröva Nortropics återhämtning mot etablerade erfarenheter av produktionssystem, inte bara mot nya agentramverk.

Den centrala frågan för oss blir hur systemet undviker att ett lokalt problem växer genom återförsök, konkurrerande reparationer och gemensamma resursberoenden.

## Tredje prioritet: *Learning Systems Thinking*

**Författare:** Diana Montalion.  
**Undertitel:** *Essential Nonlinear Skills and Practices for Software Professionals*.

Jag har åtkomst till förlagets presentation och innehållsförteckning, inte fulltexten. Bland innehållsspåren finns konceptuell sammanhållning, relationer i sociotekniska system och skillnaden mellan händelser, mönster och bakomliggande strukturer. citeturn469580view2

**Varför den är relevant:** den kan hjälpa oss granska när en lokal förbättring faktiskt försämrar organisationens helhet, och hur många av våra koncept som egentligen beskriver samma underliggande problem.

Jag skulle prioritera den efter de två mer direkt operativa böckerna.

## Rapporter som du inte behöver skaffa åt mig

De viktigaste öppna källorna finns redan tillgängliga: Datadogs evalartikel och *State of AI Engineering*, Cloud-OpsBench, AHE, STRATUS, OXN samt Googles SRE-material och Anthrophics vägledning om agentutvärderingar. De ligger till grund för analysen ovan.

**Det som fortfarande saknas i Datadogs offentliga underlag är främst detaljer för oberoende granskning:** exempelvis deras kompletta utvärderingsrubriker, representativa testfall med facit, kalibrering mot mänskliga bedömningar och exakt metod bakom vissa produktförbättringar. Jag hittade inget offentligt material som räcker för att återskapa och verifiera hela deras resultat. Evalartikeln förklarar arbetssättet, men fyller inte den luckan. citeturn407516view0

Det vore mer värdefullt underlag än ytterligare en allmän produktöversikt. Jag kan däremot inte ange en särskild rapporttitel för sådant material, eftersom jag inte har belägg för att det finns som en fristående publikation.

# 9. Vad jag tycker ska överleva in i Improvements Recompile

Jag skulle bevara detta som **ett sammanhängande forskningsspår**, inte som flera nya obligatoriska subsystem.

Det starkaste att ta med är skillnaden mellan korrekt resultat och tillräckliga belägg; kopplingen från verkliga incidenter till återspelbara prov; och kravet att förändringar prövas även mot försämringar som förslagsställaren inte förutsåg.

Det vi bör experimentera med är selektiv kontext, observation av hela arbetskedjan och avgränsad autonom återhämtning. Val av Datadog, eventuell Kubernetes-drift och större gränssnittsförändringar bör förbli separata beslut.

Den ordningen stämmer med vårt Recompile-upplägg: jämför forskningen med det som faktiskt finns, slå samman överlapp och bygg bara den minsta komplettering som behövs. fileciteturn0file3

**Den stora möjligheten är alltså inte att Nortropic får en bättre instrumentpanel. Det är att organisationen får bättre underlag för att fortsätta själv — och bättre förmåga att upptäcka när dess egen förklaring, återhämtning eller förbättring är fel.**

Börja gärna med att inhämta **andra upplagan av *Observability Engineering***; det är den fulltext som jag bedömer har störst chans att fördjupa och utmana denna analys.

---

## Meddelande 10 — Johnny (användare)

ge mig länkar så fixar jag

---

## Meddelande 11 — ChatGPT (assistent)

Här är **de tre böckerna, i prioritetsordning**.

### 1. Observability Engineering — **andra upplagan**
*Charity Majors, Liz Fong-Jones, George Miranda och Austin Parker.*

**[Hämta den kostnadsfria e-boken hos Honeycomb](https://www.honeycomb.io/observability-engineering-oreilly-book)**

Honeycomb erbjuder andra upplagan gratis via sidan. Den omfattar bland annat observation av AI-agenter, hantering av observationsdata och kopplingen mellan teknisk funktion och kundnytta. **Det här är den viktigaste boken för vår fortsatta fördjupning.** citeturn829610view0

### 2. Release It! — **Second Edition**
*Michael Nygard. Undertitel: Design and Deploy Production-Ready Software.*

**[Hämta eller köp e-boken hos förlaget Pragmatic Bookshelf](https://pragprog.com/titles/mnee2/release-it-second-edition/)**

Detta är en betalbok. E-boksköpet inkluderar **PDF och EPUB**, och sidan har även kostnadsfria utdrag. Den behandlar bland annat kaskadfel, timeouts, felavgränsning, belastningshantering och stabil drift — relevant för att granska Nortropics återhämtning. citeturn829610view1

### 3. Learning Systems Thinking
*Diana Montalion.*

**[Öppna boken hos O’Reilly](https://www.oreilly.com/library/view/learning-systems-thinking/9781098151324/)**

Boken finns för läsning med åtkomst till O’Reilly. **Detta är inte en direkt PDF-länk.** Den behandlar bland annat konceptuell sammanhållning, återkopplingsslingor och hur relationer mellan delar påverkar helheten — relevant för vårt arbete med att förena Nortropics många forskningsspår. citeturn829610view2

**Börja med gratisboken *Observability Engineering*, andra upplagan, och ladda upp den här.** Det räcker som nästa underlag; du behöver inte köpa de andra två innan vi har undersökt vad den tillför.

---

## Meddelande 12 — ChatGPT (assistent)

Nu kan vi pröva våra tidigare slutsatser mot själva boken, särskilt kring agentkontext, gemensamma begrepp och hur drifterfarenheter blir tester och förbättringar.

---

## Meddelande 13 — ChatGPT (assistent)

**Det här var rätt bok att hämta. Den tillför något som vårt Datadog-spår inte fångade tillräckligt tydligt: Nortropic behöver inte bara upptäcka när arbete misslyckas — utan kunna följa om en förändring faktiskt åstadkom det vi avsåg, även när inga larm går.**

De mest betydelsefulla fynden finns i kapitlen om **ontologier och avsikt**, **agenternas kontext**, **utvärderingar och förbättring av agenternas arbetsmiljö**, samt **organisationens lärandeslingor**. De kopplar ihop flera av våra befintliga forskningsspår utan att vi behöver uppfinna ytterligare en förvaltning eller plattform. fileciteturn7file0

Jag har gått igenom bokens struktur och fördjupat mig i dessa delar, tillsammans med relevanta avsnitt om instrumentering, långa arbetsflöden, bygg- och testkedjor och användarupplevelse. Analysen nedan är ett underlag för **Improvements Recompile**, inte en inventering av vad som redan finns i Nortropics kod. Sidnummer avser bokens tryckta sidnummer.

## 1. Den viktigaste förändringen i vårt resonemang: lärande får inte börja först när något går sönder

Vår Datadog-fördjupning handlade mycket om incidenter:

*Upptäck ett problem, undersök det, återställ funktionen och gör erfarenheten till ett framtida test.*

Det är relevant. Men bokens kapitel 25 pekar ut en annan lucka.

Utvecklingsslingan kan fungera: kod skrivs, testas och publiceras. Driftslingan kan också fungera: larm upptäcks och incidenter åtgärdas. Ändå kan organisationen sakna en fungerande koppling mellan **varför en förändring gjordes** och **vad den faktiskt gjorde för användaren**. Författarna kallar detta den saknade återkopplingsslingan. fileciteturn7file0

**Figurerna 25-7 och 25-8 på sidan 457 illustrerar skillnaden tydligt.** Den första visar publiceringar som följs av observation och lärande. Den andra visar en allt snabbare följd av publiceringar där slingorna förblir öppna. Poängen är att många leveranser skapar många *möjligheter* att lära, men inte bevisar att lärande sker. fileciteturn7file0

### Min tillämpning på Nortropic

Vi skulle kunna bygga ett system som är utmärkt på att producera och verifiera ändringar, men betydligt sämre på att ta reda på om ändringarna var värda att göra.

Exempelvis:

> Nortropic förbättrar informationsstrukturen för ett projekt. Dokumenten är korrekta, länkarna fungerar och ändringen är verifierad. Men nästa worker behöver fortfarande fråga dig vad som egentligen gäller.

Då kan implementationen ha lyckats medan förbättringshypotesen misslyckats.

Jag skulle därför vilja skilja mellan:

**”Ändringen uppfyller sitt tekniska kontrakt.”**

och:

**”Vi har undersökt om ändringen åstadkom den avsedda förbättringen.”**

Det senare behöver inte alltid ge ett ja. Ett välgrundat *”ännu otillräckligt underlag”* är bättre än att automatiskt bokföra varje publicerad ändring som framsteg.

Detta skärper Evolution Plane: **den ska inte bara lära av fel, utan också pröva våra förbättringsantaganden efter till synes lyckade förändringar.**

## 2. Kapitel 17 ger en konkret koppling mellan avsikt, regler, verifiering och observation

Det här är enligt mig bokens viktigaste kapitel för Nortropics arkitekturresonemang.

En **ontologi** betyder här en gemensam definition av vilka saker som finns i verksamheten, hur de hänger ihop och vilka regler som måste gälla. Det behöver inte innebära en stor kunskapsgraf eller särskild databas.

Kapitlets exempel gäller energianvändning och elpriser. Systemet kan ha friska servrar och lyckade HTTP-anrop samtidigt som det räknar fel eller ger ogrundade råd. Problemet ligger då i verksamhetens betydelser och regler, inte nödvändigtvis i infrastrukturen. fileciteturn7file0

Författaren använder fyra centrala objekt:

| Bokens objekt | Betydelse i energiexemplet | Möjlig motsvarighet i Nortropic |
|---|---|---|
| **IntervalSeries** | Tidsbestämda uppgifter om energianvändning. | Det versionsbundna underlag ett arbete bygger på. |
| **Tariff** | De prisregler som gäller för beräkningen. | Tillämpliga verksamhetsregler och kvalitetskriterier. |
| **BillSet** | Resultatet från den deterministiska beräkningen. | Ett resultat med tydligt angiven verifiering och evidens. |
| **ActionPlan** | AI:ns föreslagna handlingar och förväntade effekt. | En strukturerad kandidat till hur uppdraget ska genomföras. |

De två första kolumnerna sammanfattar sidorna 314–318. Den sista är min analogi, inte bokens beskrivning av Nortropic. fileciteturn7file0

### Den avgörande distinktionen: AI:ns tolkning är inte användarens avsikt

Boken beskriver `ActionPlan` som en fångad representation av **vad AI:n tror att användaren vill**. Den är ett förslag som kan simuleras och prövas, inte något som ska verkställas bara för att det är välformulerat. fileciteturn10file3

För Nortropic skulle jag vilja hålla isär fem saker:

**Din ursprungliga avsikt → systemets tolkning → föreslagen handling → förutsagd effekt → observerad effekt.**

Det kan låta självklart, men det gör en stor skillnad vid felsökning.

Anta att du säger:

> ”Gör det lättare att återanvända tidigare research.”

Systemet tolkar det som att alla dokument ska slås ihop. Sammanställningen blir tekniskt korrekt, men källornas status och skillnaden mellan idéer och beslut blir svårare att urskilja.

Felet ligger då inte nödvändigtvis i exekveringen. Det kan ligga i översättningen från avsikt till lösning.

**Vi behöver kunna undersöka den översättningen, inte bara resultatfilen.**

### ”AI sandwich” stärker en befintlig gräns — det motiverar inte en andra Kernel

I **figur 17-3 på sidan 321** ligger den generativa arbetsgången under en deterministisk arbetsgång. AI:n producerar ett förslag; en simulator och regelkontroller prövar det innan det leder vidare till handling. Kapitlet kallar detta *AI sandwich architecture*. fileciteturn10file0

Det liknar vår princip att kandidatens förslag ska prövas utanför kandidatens egen auktoritet. Den principen finns redan i vårt Recompile-underlag. fileciteturn7file4

Men vi ska inte överföra energiexemplets säkerhet alltför långt. Att korrekt kontrollera en prisberäkning är något annat än att avgöra om en design är bra, om ett forskningsunderlag är tillräckligt eller om en extern handling får önskad verklig effekt.

Min rekommendation är:

> **Använd deterministiska kontroller för det de faktiskt kan avgöra. Bevara oberoende bedömning och osäkerhet för resten.**

En godkänd regelkontroll betyder att de kontrollerade reglerna höll. Den betyder inte automatiskt att hela människans mål uppnåddes.

### Ett särskilt användbart begrepp: *signal parity*

På sidorna 319–320 vill författaren att tester och produktion ska använda samma betydelser och identifierbara kontrollresultat. Ett fel som upptäcks i produktion ska kunna kopplas till motsvarande regel och test. fileciteturn10file0

För Nortropic innebär det exempelvis att ordet **verifierad** inte får betyda en sak i testsviten, en annan i arbetskön och en tredje i Verkstadsgolvet.

Vi behöver kunna avgöra *vilket resultat*, *vilken version*, *vilka kriterier* och *vilken evidens* statusen avser.

Det är en gemensam semantik — **inte** ett krav på att samma agent ska godkänna sitt eget arbete eller att alla kontroller ska dela samma antaganden.

## 3. Ett av bokens bästa exempel: problemet var ett fältnamn, inte en för svag modell

På sidan 401 beskriver författarna en felsökande modell som misstolkade ett fält med namnet `is_slow`.

Fältet var en beräknad markering: det blev sant när en förfrågan tog mer än 500 millisekunder. Modellen tolkade det i stället som en funktionsflagga eller indikation på ett belastningstest som *orsakade* långsamheten. Den använde alltså en beskrivning av symtomet som förklaring till symtomet och missade de bakomliggande faktorerna.

Lösningen var att lägga till en korrekt beskrivning av fältets betydelse. Därefter kunde modellen fortsätta undersökningen på rätt sätt. fileciteturn7file0

### Varför detta är särskilt relevant för oss

Vi har många begrepp som kan se självklara ut men som måste betyda något exakt:

*Aktiv, klar, verifierad, publicerad, blockerad, väntar, förslag, beslut, aktuell.*

En ny worker kan annars läsa ”klar” och dra slutsatsen att hela uppdraget är avslutat, fast det bara betyder att ett försök har lämnat ett resultat.

Min slutsats är:

> **En del av det som ser ut som resonemangsfel kan egentligen vara fel i systemets språk och informationsrepresentation.**

Det talar för att inte reflexmässigt lösa varje misslyckande med en längre instruktion eller en dyrare modell. Först bör vi undersöka om begreppen, relationerna och verktygsbeskrivningarna är tydliga.

### Kapitel 10 beskriver den organisatoriska konsekvensen

Boris Tane pekar på att snabbare AI-assisterad utveckling kan göra det svårare för människor att bygga den sammanhängande mentala modell som tidigare uppstod genom att skriva, felsöka och drifta koden.

Hans föreslagna kontext omfattar bland annat tjänsternas beroenden, namn och alias, aktuella förändringar, kända problem, tidigare incidenter och deras affärsbetydelse. Han skiljer även mellan en antagen och faktiskt bekräftad felorsak. Kontexten behöver hållas aktuell och vara tillgänglig när agenten behöver den. fileciteturn12file14

Detta träffar din fråga om hur Nortropic ska behålla helheten när chattar, idéer och implementationer blir fler.

Jag skulle formulera ett praktiskt kvalitetsprov så här:

> **Kan en ny worker, utan den gamla sessionens dolda förförståelse, hitta det relevanta underlaget och korrekt förstå vad som gäller?**

Inte därför att varje worker ska få alla chattar. Utan därför att organisationen ska kunna ge rätt källa, rätt betydelse och rätt aktualitet vid rätt tillfälle.

## 4. Boken ger oss en bättre modell för självförbättring: ändra inte alltid prompten

Kapitel 21 skiljer mellan två sätt att använda erfarenheter från produktion: som underlag för **utvärderingar** och som återkoppling till **agentens harness**, alltså programvaran runt modellen som tillhandahåller verktyg, hanterar in- och utdata och kopplar modellen till resten av systemet. fileciteturn7file0

Det finns ett konkret exempel från Honeycombs Query Assistant.

Modellen producerade ibland en `COUNT`-operation med ett kolumnargument som verktyget inte tillät. För vissa sådana fel kunde en deterministisk korrigering skapa rätt fråga. Författarna rapporterar att denna typ av korrigeringar sänkte felandelen från cirka 25 till 14 procent. Senare promptförbättringar sänkte den ytterligare, till under en procent när timeouts och andra okontrollerbara fel räknades bort.

Det mest intressanta kommer därefter: teamet insåg att användarna faktiskt hade behov av den föreslagna syntaxen. De ändrade verktyget så att den blev tillåten och kunde då ta bort en del korrigeringskod. Det är en redovisad erfarenhet från deras produkt, inte ett generellt effektmått för agentutveckling. fileciteturn7file0

### Vad jag tar med till Nortropic

Ett återkommande fel kan leda till flera olika förbättringar:

**Bättre begreppsbeskrivning. Bättre verktygsgränssnitt. Annorlunda arbetsfördelning. Bättre kontexturval. Ett nytt test. En ändrad instruktion.**

Den billigaste och mest hållbara lösningen kan ligga runt modellen, inte i modellen.

Och en tillfällig hjälpregel ska kunna försvinna när orsaken till den är borta. Detta passar mycket väl med vår befintliga princip om att stödmekanismer och undantag inte ska bli permanenta av slentrian. fileciteturn7file4

Däremot skulle jag inte överföra exemplet till generell ”automatisk rättning” av handlingsförslag. En begränsad normalisering av en frågesyntax är inte samma sak som att tyst ändra mottagare, befogenhet eller innebörd i ett uppdrag.

### Verkliga erfarenheter ska bli prövbara — men inte automatiskt facit

Kapitel 17 beskriver hur avvisade förslag och relevanta indata kan fångas, rensas från personuppgifter och omvandlas till framtida testfall. Kapitel 21 beskriver hur faktiska användarfall kan förbättra en tidigare alltför idealiserad utvärderingsmängd. fileciteturn10file3 fileciteturn7file0

För Nortropic behöver vi dock lägga till en tydlig prövning:

**Att ett resultat inträffade bevisar inte att det var rätt. Att någon godkände det bevisar inte att bedömningen var tillräcklig.**

Jag skulle därför vilja bevara det observerade förloppet som källa, men pröva den förväntade lösningen separat innan fallet används som facit.

Det finns även en viktig skillnad mellan utvärderingsmängder. Kapitel 21 rekommenderar att ta bort exempel som inte representerar verkligt användarbeteende. Det är rimligt för en representativ prestationsmätning. **Min tillämpning är att sällsynta skydds- och regressionsfall behöver hanteras separat**, så att de inte försvinner bara för att de är ovanliga.

## 5. Den tekniska lärdomen är inte ”samla allt” — utan ”bevara relevanta samband”

Kapitlen 5–7 argumenterar för breda, strukturerade händelser kring meningsfulla arbetsenheter. Då kan samma underlag undersökas på flera sätt, i stället för att varje framtida fråga kräver ett nytt specialmätetal. fileciteturn7file0

För Nortropic skulle jag börja med att fråga vad vi behöver kunna förstå om ett visst arbete:

*Vilket uppdrag tillhör detta? Vilket försök? Vilket underlag och vilka versioner användes? Var uppstod väntan? Vilket resultat lämnades? Vad verifierades? Vad hände sedan?*

Detta är inte ett förslag att kopiera hela arbetskontexten till varje loggrad.

### Rik lagrad kontext är inte samma sak som en jättelik prompt

Kapitel 21 beskriver uttryckligen att stora eller känsliga in- och utdata kan ligga kvar i sitt ordinarie system, med en länk från telemetrin. Kapitel 10 betonar att kontexten ska göras tillgänglig när den behövs. fileciteturn7file0 fileciteturn12file14

Min kombination av dessa idéer är:

> **Bevara tillräckligt för att kunna undersöka och återvända till källan. Ge inte varje modell allt material samtidigt.**

Det är en viktig koppling till vår informationsarkitektur. Observation, sökning och kontexturval behöver samverka, men de behöver inte vara samma sak eller ligga i samma databas.

### Långa uppdrag behöver inte vara en enda gigantisk trace

På sidorna 119–122 behandlar boken strömmar, asynkrona jobb och arbeten som kan pågå länge. Den rekommenderar bland annat separata, länkade spårningar och gemensamma korrelationsidentifierare, snarare än en enorm spårning med orimligt många underoperationer.

Den varnar också för att försöka uppdatera samma pågående span genom upprepade utskick; många lagringssystem hanterar inte sådana uppdateringar som man kan förvänta sig. Mellanliggande status kan i stället behöva representeras med andra signaler. fileciteturn7file0

För våra långa autonoma uppdrag skulle jag därför vilja ha en **sammanhängande arbetshistorik**, inte nödvändigtvis ett enda tekniskt trace-objekt.

Det gör det lättare att skilja mellan att ett uppdrag väntar, att ett försök har avslutats och att hela uppdraget är färdigt.

### Räkna rätt sak

På sidan 110 visar boken ett enkelt men viktigt fel: om både huvudförfrågningar och deras underanrop räknas som självständiga förfrågningar blir felandelen missvisande. Författaren använder en markering för huvudoperationer för att undvika detta. fileciteturn7file0

Nortropics motsvarighet är att inte blanda:

**antal uppdrag, antal försök, antal verktygsanrop och antal verifierade resultat.**

Ett uppdrag med många misslyckade försök kan till slut lyckas. Det är relevant att det lyckades, men försökens kostnad och ledtid får inte försvinna.

Och uppdrag som aldrig når en sluthändelse behöver fortfarande finnas med när vi bedömer hur organisationen fungerar.

## 6. Vi behöver observera själva förbättringsmaskineriet

Kapitel 18 behandlar bygg- och testkedjor som riktiga produktionsarbetsflöden. En viktig poäng är att en långsam deloperation inte nödvändigtvis ligger på den kedja som avgör när helheten blir färdig.

Bokens exempel visar hur förbättring av ett delbygge kan sakna effekt på total ledtid när ett annat parallellt bygge fortfarande tar längst tid. Den beskriver också hur högre resursutnyttjande kan ge mer konkurrens om resurser och fler omkörningar. fileciteturn7file0

Min tillämpning är att Nortropic inte bara ska fråga:

> ”Kan en worker producera snabbare?”

Utan:

> **”Vad begränsar tiden till ett användbart, verifierat resultat?”**

Det kan vara informationsinhämtning, exekvering, verifiering, omarbete eller väntan mellan dessa steg.

Det ger oss ett bättre underlag för beslut om fler workers och mer hårdvara — och för att upptäcka när ökad parallellitet bara skapar mer arbete.

### Även lärandet kan bygga på en missvisande bild

Kapitel 24 diskuterar ofullständig återkoppling. Om ett system inte ser en försämring för en viss användargrupp kan det felaktigt dra slutsatsen att förändringen gick bra och fortsätta i samma riktning. Författarna beskriver också behovet av att tillämpa observationsprinciperna på observationssystemet självt. fileciteturn9file1

För Nortropic skulle jag därför vilja kunna skilja mellan:

**ingen upptäckt avvikelse**, **otillräcklig observation** och **underbyggt gott resultat**.

Det gäller också förbättringsmätetal. Exempelvis kan en lägre andel avvisade agentförslag bero på bättre förslag — men också på enklare uppgifter, förändrade kontroller eller att systemet undviker svårare arbete.

**En förbättrad siffra behöver en förklaring som håller.**

## 7. Det första sammanhängande provet bör ligga i Projekt- och innovationskontoret

Här är vår senaste uppdelning viktig:

**Projekt- och innovationskontoret är Customer Zero för Organization OS. Digitala är därefter den första operativa förvaltningen som prövar modellen i faktisk leverans.**

Jag skulle använda boken till att fördjupa just den ordningen, inte byta tillbaka till Digitala som första organisatoriska test.

### Ett tänkt uppdrag

> ”Ta ett avgränsat forskningsunderlag och omvandla det till ett prövbart förbättringsförslag, utan att blanda ihop källfakta, tidigare beslut och nya hypoteser.”

Det ligger nära det arbete vi faktiskt behöver göra med Improvements.

För det uppdraget skulle följande samband vara intressanta att pröva:

| Del av arbetet | Vad vi behöver kunna förstå |
|---|---|
| **Avsikten** | Vilket problem försöker vi lösa, och vilka gränser gäller? |
| **Underlaget** | Vilka källor och versioner användes? Vad saknades? |
| **Tolkningen** | Vad kom från en källa, vad var ett beslut och vad föreslog agenten själv? |
| **Prövningen** | Vilka påståenden och egenskaper kontrollerades, och mot vilket underlag? |
| **Användningen** | Kunde nästa arbetssteg faktiskt använda resultatet utan onödig omorientering? |

Det här behöver inte bli fem nya datamodeller. Det är fem frågor som befintliga eller minimalt kompletterade mekanismer bör kunna besvara.

### Hur experimentet skulle kunna utformas efter Recompile

Jag skulle jämföra samma typ av arbetsuppgift med nuvarande informationsupplägg och med ett förbättrat upplägg där **begrepp, källstatus och relationer** är tydligare. Modell, befogenheter och övriga förutsättningar hålls så lika som möjligt.

Ett separat underlag kan innehålla exempel där en idé senare har ersatts, där en uppgift saknar källa och där ett korrekt verifieringsresultat gäller en äldre kandidatversion. Facit måste vara bestämt oberoende av den producerande agenten.

Det intressanta är inte bara om slutrapporten ser bättre ut. Jag skulle följa om systemet skiljer rätt på fakta och hypoteser, hittar relevant information, upptäcker osäkerhet och ger nästa worker ett användbart underlag. Ledtid, exekveringskostnad och din aktiva tidsåtgång får redovisas separat.

**Det nya jämfört med ett vanligt dokumenttest är att vi prövar överlämningen till nästa arbetssteg.**

En rapport kan vara språkligt utmärkt men organisatoriskt svag om den kräver att du återförklarar allt.

Det passar bokens rekommendation på sidan 499: börja med en avgränsad verksamhetsdomän på djupet, snarare än tunn täckning överallt. fileciteturn7file0

## 8. Digitala får sedan pröva samma princip från användarens sida

Kapitel 19 tillför mer än allmän frontendövervakning.

Det framhåller att backendens anrop inte visar allt som händer hos användaren. Ett avbrutet flöde, en knapp som inte går att använda eller vad som händer mellan två anrop kan saknas helt i serverns bild.

I det uttryckligen **fiktiva** exemplet FakeBurger modelleras både att en användare påbörjar en utcheckning och att den avslutas. Starten måste kunna registreras även när slutet aldrig inträffar. Författarna diskuterar också hur jämförelser mellan versioner kan påverkas av skillnader mellan användargrupper, exempelvis vilka som uppdaterar tidigt. fileciteturn7file0

### Vad detta tillför vårt tidigare offertformulärsexempel

Vi har redan talat om att kontrollera att en förfrågan når mottagande system.

Boken skärper den föregående delen:

> **Kan vi upptäcka att användaren försökte skicka något, men aldrig kom så långt att servern fick en förfrågan?**

En server kan vara frisk samtidigt som en mobil layout hindrar användaren från att nå knappen.

Jag skulle därför vilja koppla samman användarens observerbara försök, flödets steg, eventuell avbruten resa och verifierat mottagande — med bara den information som behövs för ändamålet.

Men orsaken till ett avhopp ska inte hittas på. Användaren kan ha ändrat sig, blivit avbruten eller saknat rätt underlag. Boken är själv tydlig med att fastställa orsak bakom förändrade beteenden är svårt och inte löses fullständigt i kapitlet. fileciteturn7file0

Det stärker vår tidigare uppdelning mellan **teknisk integritet, upplevelsekvalitet och verkliga utfall**, snarare än att ersätta den med ett sammanfattande webbplatspoäng. fileciteturn7file2

## 9. Tre saker vi inte bör importera okritiskt

### En gemensam observationsmodell är inte samma sak som en enda auktoritativ databas

De tidiga kapitlen argumenterar starkt för en *unified storage model* och mot fragmenterade signalsilos. Samtidigt rekommenderar kapitel 7 uttryckligen *layered telemetry*: olika signaler för olika behov, inklusive separata händelseflöden för vissa affärskritiska eller granskningsrelaterade uppgifter. fileciteturn7file0

För Nortropic skulle jag prioritera **sammanhängande betydelser och spårbara samband**, inte göra ”allt i en databas” till ett arkitekturkrav.

Bokens *canonical logs* ska inte heller förväxlas med Nortropics auktoritativa beslut eller oberoende verifieringsbevis. En sammanhållen driftpost kan hjälpa oss förstå arbetet utan att få bestämma vad som är tillåtet eller godkänt.

### ”Testa i produktion” betyder inte ”släpp tester och hoppas”

Boken använder ibland mycket starka formuleringar om produktion som platsen där verkligheten visar sig. Men på sidan 28 säger den uttryckligen att tester i produktion **kompletterar**, inte ersätter, tester före produktion. Den betonar också särskild försiktighet kring bestående data och förändringar som inte enkelt kan återställas. fileciteturn7file0

Min tillämpning är därför bättre avgränsad observation av tillåtna förändringar — inte att använda kundmiljöer som fria experimentytor.

### Det är inte en oberoende jämförelse som utser Honeycomb till vinnare

Författarna beskriver själva sin leverantörsbias i kapitel 29: deras erfarenheter gör att de tenderar att föredra köp framför egenutveckling när den verkliga förvaltningskostnaden räknas in. Boken innehåller dessutom många Honeycomb-exempel. fileciteturn7file0

Det minskar inte värdet av exemplen. Men **arkitekturmönster, företagsrapporterade erfarenheter och generella effektbevis är olika saker**.

Jag skulle därför inte använda boken för att automatiskt välja Honeycomb framför Datadog, eller för att anta att samma förbättringssiffror gäller hos oss.

## 10. Vad detta betyder för Datadog — och vad som bör överleva till Recompile

Datadog förblir en relevant kandidat och forskningsreferens. Men nu har vi bättre frågor att bedöma en observationslösning mot.

Kapitel 30 rekommenderar att ett verkligt prov utgår från verksamhetens svåraste frågor och önskade utfall, med framgångskriterier bestämda i förväg. Man ska inte låta en leverantörs funktioner bli definitionen av problemet. fileciteturn7file0

För Nortropic skulle jag framför allt vilja kunna pröva:

**Kan vi följa ett uppdrag över flera försök och överlämningar? Kan vi skilja ett semantiskt missförstånd från ett exekveringsfel? Kan en ny worker undersöka det med rätt underlag? Kan vi jämföra förändringar utan att blanda versioner eller räkna bort misslyckade uppdrag?**

Därtill kommer faktisk datatäckning, åtkomst, integritet, förvaltningskostnad och möjlighet att få ut underlaget. Det behöver undersökas när ett konkret produktprov blir aktuellt.

Jag ser fortfarande inget i materialet som i sig motiverar en Kubernetes-migrering, en egen stor observationsplattform eller ett nytt omfattande gränssnittsprojekt.

### Min kondensering till Improvements

| Fynd | Vad jag skulle ta med |
|---|---|
| **Den saknade lärandeslingan** | Följ upp avsikten bakom relevanta förändringar, inte bara incidenter. |
| **Minimal ontologi och signal parity** | Ge uppdrag, försök, kandidater, verifiering och utfall konsekventa betydelser. |
| **Kontext som organisatorisk förmåga** | Gör aktuell kunskap tillgänglig utan beroende av en viss långlivad session. |
| **Erfarenheter förbättrar både evals och verktyg** | Undersök gränssnitt och informationsstruktur innan varje fel blir mer prompttext. |
| **Observation genom hela arbetet** | Bevara kopplingar och synliggör även väntande, avbrutna och otillräckligt observerade förlopp. |

Detta är framför allt **sätt att förtydliga och pröva befintliga principer**, inte fem nya subsystem. Vårt Recompile-upplägg ska fortfarande jämföra idéerna med verklig implementation, slå samman överlapp och bygga bara de kompletteringar som behövs. fileciteturn7file4

**Min viktigaste slutsats efter läsningen är denna: Nortropics långsiktiga styrka bör inte vara att en viss agent minns allt eller arbetar länge. Den bör vara att organisationen bevarar sambandet mellan avsikt, underlag, handling och verkligt resultat — så att nästa agent kan fortsätta arbetet och nästa förbättring kan prövas.**

Det gör boken till underlag för **hur Nortropic arbetar och lär**, inte bara för hur vi tittar på Nortropic.

---

## Meddelande 14 — Johnny (användare)

Bra saker

---

## Meddelande 15 — ChatGPT (assistent)

Ja — och det starkaste är att detta **binder ihop flera av våra befintliga spår**, snarare än ger oss ännu en sak att bygga.

Bokens betoning på att följa avsikten ut i verklig användning ger oss en viktig skillnad: **att en ändring är levererad är inte samma sak som att dess avsedda effekt är bekräftad.** fileciteturn15file0

För Nortropic skulle jag sammanfatta tillämpningen så här:

**Avsikt → begripligt underlag → arbete inom mandat → verifierat resultat → observerad effekt → prövad förbättring.**

Informationsarkitekturen hjälper nästa worker att förstå vad som gäller. Observationerna hjälper den att undersöka vad som faktiskt hände. Verifieringen prövar resultatet. Evolution Plane kan sedan använda erfarenheten för att föreslå och testa förbättringar.

**Det behöver inte vara fyra nya subsystem. Det är fyra behov som den minsta fungerande organisationen behöver tillgodose.**

Och det ger oss ett väldigt konkret prov i Projekt- och innovationskontoret:

> En worker lämnar över ett arbete. Kan nästa worker hitta rätt källor, förstå vilka slutsatser som håller och fortsätta utan att du behöver återberätta projektet?

Sedan kommer den andra frågan:

> När vi förbättrar överlämningen — blir nästa arbetssteg faktiskt bättre, eller producerar vi bara mer dokumentation?

**Det är den sortens skillnad jag vill att vi bevarar till Recompile: mer användbar förmåga, inte mer AI-aktivitet eller fler kontrollsteg.**

---

## Meddelande 16 — Johnny (användare)

är det nåt mer vi behöver titta på för att binda ihop flera lösa ändar?

---

## Meddelande 17 — ChatGPT (assistent)

Jag tittar särskilt på övergångarna mellan våra spår, där idéer, korrekt information eller verifierade resultat kan tappa betydelse på vägen vidare. Där tror jag flest lösa ändar kan knytas ihop.

---

## Meddelande 18 — ChatGPT (assistent)

**Ja. Framför allt skulle jag nu granska skarvarna mellan våra befintliga spår — inte leta efter fler fristående agentverktyg.**

Vi har diskuterat vad Nortropic ska kunna göra, hur arbetet ska verifieras, hur kunskap ska bevaras och hur organisationen ska förbättras. Nästa värdefulla fråga är:

> **Fungerar dessa principer tillsammans när samma uppdrag passerar genom hela organisationen — och något ändras eller går fel på vägen?**

*Observability Engineering* pekar själv ut gränsen för sitt område: bra observationer kan inte kompensera för otydliga mål, bristande handlingsutrymme eller felaktiga regler. Författarna behandlar detta på sidorna 448–449. Det är precis där jag tycker att vår nästa sammanfogning bör börja. fileciteturn15file0

Jag ser **fem särskilt värdefulla kopplingar att undersöka**. Det är frågor i helhetsmodellen, inte konstaterade brister i den aktuella koden.

## 1. Hur ska alla återkopplingsslingor samverka utan att motarbeta varandra?

**Binder ihop:** Kubernetes-inspirationen, Supervisor, återhämtning, resursstyrning och Evolution Plane.

Vi har pratat mycket om nyttan av återkopplingsslingor. Men vi behöver också undersöka **vad som händer när flera slingor reagerar på samma situation**.

Tänk ett hypotetiskt fall:

En worker tar lång tid. Samordningen startar ett nytt försök. Kostnadsstyrningen ser ökande förbrukning och väljer en billigare körningsväg. Den vägen behöver fler försök. En felsökare börjar samtidigt undersöka belastningen, medan förbättringsarbetet föreslår ett nytt arbetssätt.

Varje del kan försöka göra något rimligt. Ändå kan helheten skapa mer väntan, större kostnad och sämre förutsägbarhet.

Det är därför nästa fråga inte bara är:

> ”Har vi en återkopplingsslinga?”

Utan:

> **”Vilken slinga får reagera på vad, i vilken takt och med vilken information om de andra slingorna?”**

Donella Meadows behandlar just fördröjningar i förhållande till förändringstakt: återkopplingens timing kan få ett system att överreagera och pendla mellan tillstånd. Det är ett användbart systemperspektiv, inte ett färdigt bevis för hur Nortropic ska konfigureras. citeturn242637view0

### Det jag skulle vilja få ut av fördjupningen

En liten karta över våra viktigaste slingor: deras mål, signaler, tillåtna åtgärder, förväntade svarstid och vem som samordnar när de överlappar.

Den skulle framför allt skilja **att genomföra ett uppdrag**, **att återställa fungerande arbete** och **att förändra arbetssättet för framtiden**.

Min arbetshypotes är att dessa ibland behöver olika tidshorisonter. Ett övergående fel ska inte automatiskt bli en organisationsförändring. En långsiktig förbättring ska inte heller ändra förutsättningarna mitt under ett pågående, versionsbundet försök.

**Det här skulle knyta ihop vår forskning om organisatorisk styrning med den konkreta autonoma livscykeln.**

## 2. När slutar tidigare kunskap och tidigare bevis att vara tillämpliga?

**Binder ihop:** informationsarkitektur, minne, källspårning, kontexturval, verifiering och inkrementell Recompile.

Vi har redan principen att ursprungskällorna ska överleva sammanfattningarna och att tidigare slutsatser ska kunna omprövas. Recompile-underlaget beskriver också att berörda efterföljande steg ska kunna köras om utan att hela arbetet börjar från noll. fileciteturn17file3

Men här finns en viktig fördjupning:

> **Att veta varifrån ett påstående kommer är inte samma sak som att veta om det fortfarande får användas.**

Anta att vi har ett kvalificerat arbetssätt för formulärtestning. Sedan förändras det mottagande systemets kvittoformat.

Då behöver Nortropic kunna skilja mellan:

**Det gamla testet genomfördes korrekt då.**  
**Det gamla testet bevisar inte nödvändigtvis att den nya integrationen fungerar nu.**

Historien behöver inte skrivas om. Men användningen av historien behöver ändras.

W3C:s PROV-modell ger ett etablerat språk för att beskriva vilket underlag som användes, vilka aktiviteter som skapade ett resultat och hur versioner härleddes från varandra. Den är relevant för källspårning — men är inte i sig ett system som avgör om våra slutsatser är sanna eller tillräckliga. citeturn830965view0

### Den konkreta frågan för oss

När en källa, ett verktyg, en modell, ett kvalitetskriterium eller ett ägarbeslut ändras:

**Vilka slutsatser behöver granskas? Vilka verifieringar behöver förnyas? Vilka pågående arbeten påverkas? Vad kan fortsätta oförändrat?**

Här finns en möjlighet att förena flera av våra koncept. En källrelation som hjälper en worker att hitta rätt underlag kan också hjälpa förbättringsarbetet att hitta vad som berörs av en förändring.

Men relationerna måste vara tydliga. **”Refererar till” är inte samma sak som ”giltigheten beror på”.**

Jag skulle därför vilja pröva ett litet förändringsscenario, inte börja med att bygga en jättelik kunskapsgraf:

> Ändra en relevant förutsättning. Kan systemet identifiera rätt berörda arbeten, undvika att återanvända otillräckliga bevis och samtidigt lämna orelaterade arbeten i fred?

**Det är länken mellan att minnas mycket och att faktiskt hålla organisationens kunskap användbar.**

## 3. Hur följer vi verkligt arbete över organisationsgränser — inte bara enskilda agentkörningar?

**Binder ihop:** Projekt- och innovationskontoret, Digitala, arbetsköer, överlämningar, kapacitet och observation.

Här finns ett kompletterande forskningsområde som jag tycker är särskilt intressant: **process mining**, alltså att undersöka hur arbete faktiskt har förlöpt utifrån registrerade händelser.

Den objektcentrerade varianten är relevant när arbetet involverar flera sammanhängande saker, snarare än en enda rak ärendekedja. OCEL är ett format för sådana händelsedata, med relationer mellan händelser och flera objekt. Forskningen beskriver detta som ett sätt att undvika informationsförlust när verkliga processer pressas in i en enda ärendevy. citeturn428713academia1 citeturn891866view0

### Varför det passar vår fråga

Ett Nortropic-initiativ kan tänkas använda flera forskningskällor, skapa flera kandidater, återanvända samma komponent och gå vidare till flera leveranser. En verifiering kan avse just en kandidatversion, medan en lärdom senare används i ett annat initiativ.

Det går att visa varje agentkörning separat och ändå missa varför **initiativet som helhet** står stilla.

Min forskningsfråga blir därför:

> **Kan vi jämföra det avsedda arbetsflödet med det faktiskt observerade arbetsflödet?**

Exempelvis skulle vi vilja upptäcka att arbetet inte främst är långsamt i exekveringen, utan att det återkommande går tillbaka från verifiering till briefen eftersom en viktig förutsättning inte fångades från början.

Den möjliga lösningen är då inte en snabbare modell. Den kan vara bättre formning av uppdraget.

### Vad vi bör — och inte bör — ta med

Jag skulle ta med metoden för att undersöka överlämningar, omarbete, väntan och återanvändning. Jag skulle **inte** på förhand besluta om ett process mining-system eller göra det till en ny plattform.

Och det finns en avgörande gräns:

> **Det observerade arbetsflödet visar vad som hände. Det visar inte automatiskt vad som borde ha hänt.**

En återkommande omväg kan vara en onödig vana — eller ett nödvändigt skydd. Det måste bedömas mot uppdragets avsikt och krav.

**Det här skulle hjälpa oss att knyta samman organisationsmodellen med faktisk arbetsförmåga, inte bara med ett organisationsschema.**

## 4. Hur vet vi att en förbättring hjälpte — och inte bara ändrade mätningen?

**Binder ihop:** observation, utvärderingar, Evolution Plane och verkliga användarutfall.

Vi har redan identifierat skillnaden mellan levererad ändring och bekräftad effekt. Nästa steg är att undersöka **hur stark slutsats vi får dra av den observerade effekten**.

Tänk att nästa version av Nortropic redovisar kortare ledtid. Det kan bero på ett bättre arbetssätt. Men i ett tänkt jämförelseunderlag skulle det också kunna bero på enklare uppdrag, fler bortsorterade fall eller att en del av väntetiden inte längre registreras.

Microsofts studie *Trustworthy Experimentation Under Telemetry Loss* behandlar en närliggande risk: bortfall av observationsdata kan snedvrida experiment och leda till felaktiga slutsatser. Det räcker alltså inte att utvärdera kandidaten; mätningen som används för jämförelsen måste också granskas. citeturn203901view1

### För Nortropic skulle jag vilja skilja tre frågor

**Fungerade kandidaten i provet?**

**Fungerade den tillräckligt konsekvent under de relevanta förutsättningarna?**

**Har vi stöd för att förändringen förbättrade det vi faktiskt värderar?**

Det behöver inte bli ett statistiskt forskningsprojekt kring varje liten ändring. Min rekommendation är att beviskravet anpassas till påståendet.

För en liten intern förbättring kanske upprepade, jämförbara arbetsuppgifter och granskade överlämningar räcker som pilotunderlag. Ett påstående om förbättrade affärsutfall kräver annan evidens. Och när underlaget inte räcker bör slutsatsen vara just det — inte ett automatiskt godkännande eller ett automatiskt misslyckande.

Vi behöver också behålla jämförelser som inte definieras av förbättringsförslaget självt: oberoende granskning, undanhållna prov och, där det är relevant, verkliga användare eller externa kvalitetsreferenser.

**Det är detta som förhindrar att Nortropic blir allt bättre på att övertyga sig självt om att det blir bättre.**

## 5. Hur ska du kunna vara frånvarande utan att bli oförberedd när du behövs?

**Binder ihop:** ägaruppmärksamhet, mandat, överlämningar, Verkstadsgolvet och Aquarium.

Detta är den mänskliga motsvarigheten till worker-kontinuitet.

Du ska inte behöva följa varje terminalrad. Men när ett verkligt vägval uppstår måste systemet hjälpa dig förstå situationen utan att först kräva att du läser igenom en hel natt av aktivitet.

Jag skulle formulera frågan så här:

> **Kan Nortropic återge tillräcklig situationsförståelse för ett bra ägarbeslut — utan att kräva ständig övervakning?**

Detta hör hemma i den sista, redan planerade HCI-fördjupningen. Microsoft Researchs *Guidelines for Human-AI Interaction* och tillhörande HAX-material är relevanta kompletterande källor för att undersöka hur AI-system bör kommunicera och hur interaktionsfel kan göras till testscenarier. Det är vägledning att pröva mot vår situation, inte en färdig kontrollrumsdesign. citeturn203901view0

Min föreslagna tillämpning är att skilja mellan **lugn överblick**, **en konkret fråga som behöver ditt omdöme** och **fördjupning i bevisen**.

En tänkt ägarfråga borde inte bara säga:

> ”Blockerad. Godkänn fortsättning?”

Den borde förklara:

> ”Två tillåtna lösningar återstår. Den ena prioriterar snabb leverans, den andra lägre framtida underhåll. Det här är vad vi vet, detta är osäkert och därför behöver vi ditt ställningstagande. Övrigt arbete fortsätter.”

Det motsvarar vårt befintliga mål att ägarfrågor ska gälla verkliga vägval, inte rutinmässiga fortsättningar. fileciteturn17file18

**Men jag skulle fortfarande låta den större gränssnittsfördjupningen komma sist. Först behöver vi veta vad gränssnittet ska hjälpa dig förstå och besluta.**

## Det viktigaste: pröva alla fem genom samma initiativ

Jag tror att vi får mer sammanhållning av **ett gemensamt genomgående scenario** än av fem separata rapporter.

Ett lämpligt scenario efter Kernel och Recompile skulle kunna vara:

> **Johnny ger en rå idé. Projekt- och innovationskontoret formar den till ett uppdrag. Digitala genomför en avgränsad leverans. Under arbetet ändras en relevant förutsättning, en worker ersätts och ett verktygsanrop ger ett osäkert utfall. Organisationen ska ändå kunna fortsätta korrekt, verifiera resultatet och följa upp avsikten.**

Då kan vi undersöka samma förlopp ur fem perspektiv:

| Händelse i scenariot | Kopplingen som prövas |
|---|---|
| Två funktioner vill reagera på samma problem. | Samordning mellan återkopplingsslingor. |
| Ett underlag eller beroende förändras. | Kunskapens och bevisens tillämplighet. |
| Arbetet går vidare till en annan worker eller förvaltning. | Kontinuitet och överlämning. |
| En förändring ser ut att förbättra resultatet. | Mätning och underbyggd effektbedömning. |
| Ett genuint vägval behöver ditt omdöme. | Situationsförståelse och ägaruppmärksamhet. |

Det är också ett bra sätt att behålla rätt ordning: **Projekt- och innovationskontoret är Customer Zero för organisationsmodellen. Digitala prövar därefter samma modell i operativ leverans.**

En skrivbordsgenomgång kan göras som forskningsarbete. Ett verkligt prov får sedan utformas mot det som faktiskt finns efter Recompile. Vi behöver inte ändra den pågående Kernel-processen för att undersöka frågorna.

## Vilken läsning skulle jag prioritera nu?

För just målet **att binda ihop helheten** skulle jag nu flytta upp **Diana Montalions *Learning Systems Thinking*** till nästa bok efter den vi har läst.

Innehållsförteckningen har särskilt relevanta avsnitt om konceptuell sammanhållning, återkopplingsslingor, gemensam modellering och kunskapsflöden. Jag har fortfarande bara läst den tillgängliga presentationen och innehållsförteckningen, inte fulltexten. Prioriteringen är därför en bedömning av dess sannolika relevans. citeturn830965view2

*Release It!* är fortsatt relevant för den mer tekniska frågan om hur återhämtning, belastning och integrationer kan samverka utan kaskadfel. Förlagets innehållsförteckning täcker bland annat just dessa områden. citeturn699123view2

Jag skulle inte lägga till en stor ny inköpslista. De smalare frågorna ovan kan vi inleda med de öppna källorna.

## Min rekommendation

**Gör ett avgränsat sammanfogningspass kring dessa fem kopplingar, med samma initiativ som genomgående exempel.** Börja med slingornas samordning och kunskapens tillämplighet; låt HCI-delen ligga sist enligt vår tidigare ordning.

Resultatet bör vara mindre än ytterligare en stor arkitekturvision: en tydlig karta över ansvar och samband, ett fåtal prövbara påståenden och konkreta situationer som modellen måste klara.

Jag skulle sätta en avslutsregel redan från början: varje identifierad skarv ska antingen vara **tillräckligt beskriven för att prövas**, **beroende av ett namngivet experiment** eller **uttryckligen uppskjuten med ett skäl**. ”Mer research behövs” ska inte få bli ett permanent mellanläge.

Det ligger nära vårt befintliga Recompile-mål: att förena materialet till minsta användbara organisation, inte omvandla varje forskningsfynd till en ny komponent. fileciteturn17file2

**Det jag framför allt vill få bevis för är inte att alla delar är genomtänkta var för sig — utan att ett uppdrag kan passera mellan dem utan att tappa avsikt, underlag, befogenhet eller ansvar för resultatet. Där tror jag att flest av våra lösa ändar möts.**

---

## Meddelande 19 — Johnny (användare)

finns inte böckerna hos anna library för dig att tanka ?

---

## Meddelande 20 — ChatGPT (assistent)

Du tänker troligen på **Anna’s Archive**. Jag har inte verifierat om just *Learning Systems Thinking* och *Release It!* finns där. **Jag kan hämta öppet publicerat eller auktoriserat material, men inte piratkopierade fulltexter åt oss.**

Däremot hittade jag mer som vi kan använda utan att du behöver ordna böckerna:

**För *Learning Systems Thinking*** finns en [längre intervju med Diana Montalion, med publicerad transkription](https://techleadjournal.dev/episodes/219/). Där diskuterar hon bland annat konceptuell sammanhållning, gemensam modellering och hur relationer mellan systemets delar skapar effekter — direkt relevant för vårt sammanfogningspass. Det är hennes resonemang i intervjun, inte en ersättning för hela boken. citeturn214184view3

**För *Release It!*, andra upplagan**, publicerar [förlaget kostnadsfria utdrag](https://pragprog.com/titles/mnee2/release-it-second-edition/) under **Contents & Extracts**, bland annat om stabilitetsproblem och minsta privilegium. Hela e-boken erbjuds som köp. citeturn214184view0

**Vi behöver alltså inte pausa forskningen i väntan på fler böcker.** Jag borde ha varit tydligare med det: fulltexterna skulle ge oss större djup och bättre möjlighet att granska författarnas sammanhängande argument, men de är inget startvillkor för att undersöka de fem kopplingarna.

---

## Meddelande 21 — Johnny (användare)

kör på det du hittar gällande diana

---

## Meddelande 22 — ChatGPT (assistent)

Jag går igenom Dianas öppna material med fokus på att förena Nortropics kunskap, arbetsflöden och förbättringsslingor. *Release It!*-utdraget håller jag separat för relevanta jämförelser.

---

## Meddelande 23 — ChatGPT (assistent)

**Ja. Dianas material hjälper oss framför allt att se att Nortropics lösa ändar inte nödvändigtvis är saknade komponenter. De kan vara saknade samband mellan sådant vi redan har tänkt igenom.**

Min huvudslutsats är:

> **Nortropics sammanhållning bör inte bero på att en central agent minns hela projektet. Den bör bero på att rätt kunskap kan hittas, förstås, prövas och användas när arbetet passerar mellan människor, workers och förvaltningar.**

Jag har läst de publicerade intervjutranskriptionerna hos InfoQ, GOTO och Tech Lead Journal, tillsammans med flera av Dianas egna texter. Jag hittade också hennes nyare projekt **Knowledge Flow**, där ett inledningskapitel finns öppet. Det ger mer substans än enbart presentationen av *Learning Systems Thinking*, men jag har fortfarande inte läst hela den boken. citeturn646036view2turn502261view3turn371350view0turn720414view3

Här är vad jag tycker förändrar eller förtydligar vårt resonemang.

## 1. Den viktigaste distinktionen: kunskapsinnehav är inte kunskapsflöde

I InfoQ-intervjun skiljer Diana mellan **knowledge stock** och **knowledge flow**.

*Knowledge stock* handlar om den kunskap och expertis någon har eller kan komma åt. *Knowledge flow* handlar om hur kunskap blir användbar för andra och hjälper dem att förstå, besluta och agera i sitt sammanhang. Hon kopplar arkitektens arbete till att möjliggöra detta flöde, inte bara till att välja tekniska komponenter. citeturn646036view2

### Vad detta betyder för Nortropic

Vårt researchbibliotek, våra chattar, dokument och tidigare rapporter är värdefulla resurser. Men deras existens bevisar inte att organisationen kan använda dem.

Ta ett konkret exempel ur vårt eget material.

Den äldre plantexten i *Skapa Kommunen* placerar Digitala först och beskriver hur organisationsmodellen senare byggs runt den. fileciteturn20file4

I vår senare, korrigerade ordning är **Projekt- och innovationskontoret Customer Zero för Organization OS**, medan **Digitala är den första operativa förvaltningen som prövar modellen i professionell leverans**.

En ny worker kan hitta båda beskrivningarna. Återgivningen av båda kan vara helt korrekt. Ändå kan den planera fel.

Det som saknas då är inte nödvändigtvis fler dokument eller bättre sökning. Det kan vara förståelsen av relationen:

**Den ena texten är en äldre plan. Den andra uttrycker den senare inriktningen. Delar av den äldre texten kan fortfarande vara användbara utan att dess ordningsföljd gäller.**

Det ger oss ett tydligare kvalitetskrav:

> **Kunskapshanteringen fungerar först när relevant information påverkar nästa arbetssteg på rätt sätt.**

Detta skulle jag vilja pröva i Projekt- och innovationskontoret. Inte bara ”hittade agenten rätt fil?”, utan ”använde den filen med rätt betydelse och rätt status?”.

Det är en stark koppling mellan informationsarkitektur, kontexthantering och faktisk autonomi.

## 2. Konceptuell sammanhållning betyder inte att allt ska vara likadant

Diana använder begreppet **conceptual integrity**, som jag här skulle översätta till *konceptuell sammanhållning*.

I Tech Lead Journal beskriver hon hur ett system kan ha igenkännbara begrepp, gränser och samarbetsmönster utan att varje del använder samma verktyg eller arbetssätt. Hon motsätter sig också att hela denna sammanhållning måste bäras av en ensam arkitekt. citeturn681801view1

### Min tillämpning: gemensamma betydelser, olika professionella arbetssätt

För Nortropic skulle jag skilja mellan det som måste vara gemensamt och det som bör få variera.

Vi behöver exempelvis en gemensam förståelse av **vilket uppdrag ett arbete tillhör, vilken kandidatversion som bedöms, vad verifieringen faktiskt omfattar och vem som har befogenhet att förändra vad**.

Men Projekt- och innovationskontoret behöver inte arbeta på samma sätt som Digitala.

Ett forskningsförslag kan behöva prövas mot källor, alternativa förklaringar och ett experiments förmåga att skilja hypoteser åt. En webbpublicering behöver andra kontroller. Att pressa båda genom exakt samma professionella checklista skulle kunna göra modellen mindre användbar, inte mer sammanhängande.

Jag skulle därför formulera riktningen så här:

> **Standardisera det som gör samarbete och ansvar begripligt. Låt det verksamhetsspecifika förbli verksamhetsspecifikt.**

Detta hjälper också med vårt ”familjeträd”. Flera koncept kan tillhöra samma familj utan att de är identiska eller måste slås ihop till samma modul.

**Kontexturval, kunskapsbevarande och källspårning hör ihop — men besvarar olika frågor.**

**Observation, verifiering och effektuppföljning hör ihop — men bevisar olika saker.**

En bra Recompile behöver alltså kunna både förena och skilja åt. Annars riskerar vi antingen fragmentering eller en så generell modell att viktiga skillnader försvinner.

## 3. Det nyaste fyndet: slutsatser behöver bära med sig skäl och sammanhang

Det öppna inledningskapitlet till *Knowledge Flow* gör Dianas **systemic reasoning** mer konkret. Hon beskriver tre delar: en slutsats eller ett påstående, skälen som motiverar det och sammanhanget som slutsatsen gäller i.

Hon betonar också **defeasibility**: en slutsats eller artefakt måste kunna omprövas när relevanta invändningar eller förändrade förutsättningar uppstår. Det handlar inte bara om att producera dokument, utan om vad deras användning möjliggör. citeturn518100view0

### Detta är en direkt länk till selektiv omprövning

Vi har pratat om att en framtida Nortropic ska kunna ompröva berörda delar utan att börja om från noll. Dianas resonemang hjälper oss precisera vad som måste bevaras för att det ska fungera.

Det räcker inte med:

> ”Vi valde lösning A.”

Vi behöver tillräckligt för att förstå:

> ”Vi valde A därför att dessa förutsättningar gällde och dessa egenskaper var viktigast.”

Diana tar även upp att arkitekturbeslut ofta saknar alternativen som övervägdes. Utan dem blir det svårare att förstå beslutet när sammanhanget förändras. citeturn518100view3

Ett tänkt Nortropic-förslag skulle exempelvis kunna lyda:

> **Förslag:** Börja med en enkel, länkad arbetshistorik i befintliga mekanismer.  
> **Skäl:** Det första provet behöver kunna följa källor, kandidatversioner och överlämningar. Vi har ännu inte visat att en separat analysplattform behövs.  
> **Alternativ:** Införa en extern observationsplattform direkt.  
> **Förutsättningar:** Begränsad arbetsmängd och tillräcklig möjlighet att undersöka befintliga händelser.  
> **Ompröva när:** Undersökningar återkommande kräver manuella sammanfogningar som hindrar arbetet.

Detta är mitt exempel, inte en föreslagen ny datamodell eller ett fattat teknikbeslut.

Poängen är att nästa worker kan förstå **varför** beslutet var rimligt och **vad som skulle kunna göra det mindre rimligt**.

### Omprövbar kunskap får inte blandas ihop med självändrad befogenhet

Här behöver Nortropic göra en tydligare uppdelning än vad den allmänna organisationslitteraturen ger oss.

En teknisk hypotes kan vara omprövbar. Ett ägarbeslut kan ha ersatts av ett senare ägarbeslut. Ett historiskt verifieringsresultat kan vara korrekt men otillräckligt för en ny version.

Ingen av dessa saker innebär att en worker själv får skriva om sin befogenhet.

**Att kunna ifrågasätta en förklaring och att få ändra reglerna är två olika förmågor.**

För Recompile betyder det: bevara råkällan, versionera slutsatsen och gör dess tillämplighet begriplig. Skriv inte om historien bara för att vår nuvarande tolkning ändras. Det ligger redan nära vårt underlag om råmaterial som beständig evidens och synteser som utbytbara, härledda artefakter. fileciteturn20file5

## 4. Vi behöver inte bara kartlägga saker — vi behöver kartlägga vad relationerna betyder

I sin text *Beliefs Become Systems* från mars 2026 beskriver Diana **relational mapping**: att identifiera, verifiera och uttrycka samband mellan människor, idéer, händelser och system. Hennes exempel kopplar kundberättelser, verksamhetsmål och säkerhetsbegränsningar till de förmågor som utvecklas. citeturn855585view0

Detta är ovanligt nära det vi försöker åstadkomma med Improvements.

### Men ”är relaterat till” är för svagt

Min tillämpning är att vi behöver skilja några relationer som lätt blandas ihop:

| Relation | Vad den bör betyda i vårt material |
|---|---|
| **Inspirerar** | En källa gav en idé. Det betyder inte att källans lösning ska införas. |
| **Motiverar** | Ett underlag bidrar med skäl för ett förslag eller beslut. |
| **Beror på** | En slutsats eller ett arbete kräver att en viss förutsättning håller. |
| **Verifierar** | En kontroll ger specificerad evidens om ett bestämt objekt eller en version. |
| **Ersätter** | En nyare beslutad formulering tar över ett tydligt angivet område från en äldre. |

Detta är en föreslagen begreppsskillnad för Nortropic, inte en standard som Diana föreskriver.

Den gör stor praktisk skillnad.

Att Datadog **inspirerar** vårt felsökningsarbete betyder inte att Nortropic **beror på** Datadog.

Att en ny formulering **ersätter ordningsföljden** i en äldre plan betyder inte att varje princip i den gamla planen är förkastad.

Att en testkörning **verifierar kandidat A** betyder inte att kandidat B automatiskt får samma status.

Här möts flera lösa ändar: källspårning, aktuella beslut, konsekvensanalys, verifiering och återanvändning.

### En mindmap är en vy över detta — inte själva lösningen

I intervjun med software-architektur.tv betonar Diana kopplingar mellan olika artefakter och möjligheten att gå vidare från en modell till mer information och till kod. Hennes poäng är inte att ett enda tvådimensionellt diagram ska bära allt. citeturn518100view3

För vår del skulle jag därför se släktträdet, färdplanen och arbetshistoriken som **olika frågor mot samma spårbara material**.

Släktträdet hjälper oss förstå konceptens släktskap. Färdplanen hjälper oss förstå beroenden och ordning. Arbetshistoriken hjälper oss förstå vad som faktiskt hände.

Vi behöver inte välja en enda bild som ska göra allt.

Och framför allt: **att alla bra idéer finns bevarade betyder inte att alla ska vara aktiva krav.**

## 5. Tid är en del av betydelsen — inte bara en tidsstämpel

Diana beskriver i GOTO-intervjun hur uppdelning i tjänster inte tar bort deras relationer. Hon lyfter också skiftet från synkron, sekventiell kommunikation till asynkrona system, där information måste utformas för dem som ska använda den. citeturn297139view1

I texten om API:er kopplar hon informationsdelning till när informationen behövs och hur den blir användbar för konsumenten. citeturn502261view0

### För Nortropic: rätt information kan bli fel beslutsunderlag senare

Tänk följande hypotetiska förlopp.

En worker påbörjar en kandidat mot uppdragsversion 1. Under tiden godkänns uppdragsversion 2. Workern avslutar korrekt det den började på, och en verifierare bekräftar resultatet mot version 1.

Nu är flera saker samtidigt sanna:

**Arbetet utfördes korrekt. Verifieringen kan vara korrekt. Resultatet kanske ändå inte får användas som slutleverans för det uppdaterade uppdraget.**

Det är inte ett problem som löses genom att bara lägga till ”senast uppdaterad” på dokumenten.

Min rekommendation är att pröva om systemet kan förstå **vilket sammanhang ett resultat gäller i**, och vad som behöver hända när det sammanhanget ändras.

Det behöver inte innebära att varje ändring stoppar allt. En uppdaterad bakgrundsartikel kanske inte påverkar pågående arbete alls. Ett ändrat leveranskrav kan däremot påverka just den kandidat som håller på att publiceras.

Det är här vi behöver kombinera Dianas systemperspektiv med våra tekniska frågor om versionsbindning och selektiv omprövning.

**Diana ger oss ett bra sätt att formulera problemet. Materialet jag har läst ger inte en färdig algoritm för Nortropics invalidation eller samtidighetshantering.**

Den skillnaden är viktig: vi har hittat en sammanbindande princip, inte stängt den tekniska frågan.

## 6. Ett återkommande problem kan förstärkas av lösningen vi brukar välja

Diana framhåller **counterintuitiveness**: den åtgärd som känns självklar kan förstärka problemet. Hon rekommenderar att undersöka hur systemets strukturer och vårt eget agerande bidrar till att samma problem återkommer, snarare än att bara reagera på nästa händelse. citeturn720414view4

Detta är särskilt relevant för två av våra egna risker.

### Hypotes A: vi kan försöka lösa kontextproblem med mer kontext

Ett tänkt mönster är:

**En worker missar något → vi lägger till fler dokument → nästa körning får svårare att urskilja vad som gäller → vi lägger till fler instruktioner.**

Detta är en hypotes att undersöka, inte ett påstående om vad den aktuella implementationen gör.

Innan vi väljer åtgärd skulle jag vilja skilja mellan att informationen saknades, inte hittades, hade fel status eller tolkades fel.

De fyra situationerna kan se likadana ut i slutresultatet men kräver olika förbättringar.

Lösningen kan vara mer underlag. Men den kan också vara en tydligare begreppsbeskrivning, ett bättre verktygssvar eller en explicit ersättningsrelation mellan två planer.

### Hypotes B: vi kan försöka skapa autonomi med fler kontrollpunkter

Ett annat tänkt mönster är:

**Osäkerhet uppstår → fler rutinfrågor går till dig → arbetet väntar → du måste återbygga sammanhanget → systemet blir ännu mer beroende av din närvaro.**

Att bara ta bort frågor är inte nödvändigtvis rätt lösning. Vissa frågor gäller verkliga vägval.

Men vi bör undersöka om frågan uppstod därför att ditt omdöme behövs — eller därför att organisationen inte lyckades hitta, tolka eller använda redan tillgängligt underlag.

Det är en konkret väg till din önskan om färre onödiga ägarstopp utan att försvaga befogenhetsgrunden.

### Förbättringsarbetet måste få ifrågasätta själva felinramningen

Min föreslagna regel blir:

> **Innan Nortropic förstärker en återkommande åtgärd, ska det kunna pröva om åtgärden behandlar orsaken, döljer symtomet eller förstärker problemet.**

Detta behöver inte betyda en lång utredning före varje retry. Det hör främst hemma när ett mönster återkommer och vi överväger att förändra arbetssättet.

Här knyts återhämtning och Evolution Plane ihop utan att de blir samma slinga.

## 7. Samarbete betyder att tillföra relevant kunskap — inte att skapa fler agentroller

I samtalet med Andrew Harmel-Law beskriver Diana hur olika perspektiv från teknik, verksamhet och användare behövs för att förstå vilka åtgärder som faktiskt hjälper. Hon framställer systemtänkande som situationsanpassad praktik, inte som en universell mall eller som kopiering av en annan organisations arbetssätt. citeturn297139view2

I *Collaborative Modeling* betonar hon att gemensam modellering kan synliggöra skillnader som döljs när människor använder samma ord men menar olika saker. citeturn720414view1

### Översättningen till agenter kräver försiktighet

För Nortropic skulle jag inte dra slutsatsen:

> ”Då behöver vi en strateg, en arkitekt, en kritiker och en systemtänkare i varje uppdrag.”

Det kan skapa fler texter utan att tillföra någon ny information.

Min fråga skulle i stället vara:

> **Vilket relevant perspektiv eller vilken evidens saknas för just detta beslut?**

En kandidat kan behöva granskas mot faktiska källor. En användarresa kan behöva prövas av en människa. Ett verktygsanrop kan behöva kontrolleras mot mottagande system. En kostnadsförbättring kan behöva bedömas inklusive omarbete.

Det är olika behov, inte nödvändigtvis permanenta roller.

*Observability Engineering* varnar uttryckligen för att en agent som skriver tester för sin egen kod kan föra vidare samma antaganden till båda. Det ger ett konkret skäl att inte likställa flera granskningssteg med oberoende prövning. fileciteturn20file1

Jag skulle alltså skilja på **gemensam förståelse av uppdraget** och **oberoende bedömning av resultatet**. Det första underlättar samarbete. Det andra ska inte upplösas bara för att alla ska vara överens.

Dianas material handlar huvudsakligen om mänskligt och sociotekniskt arbete. Det stödjer dessa designfrågor, men bevisar inte att ett visst fleragentsystem löser dem.

## 8. Två användbara korrigeringar av vårt eget språk

### ”Frys och använd” bör betyda en stabil utgångspunkt — inte en slutgiltig världsbild

Diana beskriver systemtänkande som ett komplement till analytiskt och linjärt tänkande, inte en ersättning för det. Vi behöver fortfarande kunna dela upp problem och bygga konkreta lösningar. citeturn502261view3

För Nortropic innebär det enligt mig att en fryst baseline är mycket värdefull. Den gör det möjligt att veta vad som prövas och vad en förändring jämförs mot.

Men vi bör inte kräva att varje framtida relation och varje möjlig förvaltning är färdigutforskad innan modellen får användas.

**Frys en tillräckligt underbyggd version, med synliga antaganden och avgränsningar. Låt erfarenheter avgöra vad som behöver omprövas.**

Annars kan vår ambition att inte missa något bli ett eget hinder för lärande.

### ”Mer autonomi” bör inte betyda mindre tid för ditt tänkande

I *Making Time for Thinking* skiljer Diana mellan att hinna producera mer och att ha utrymme för generativt kunskapsarbete: utforska, modellera och forma idéer som ännu inte har en färdig beställning. citeturn720414view2

Min tillämpning är att Nortropic ska avlasta den återkommande samordningen så att du kan lägga mer uppmärksamhet på det du faktiskt vill välja och skapa.

Vi ska inte bygga en organisation som kräver att du granskar ett ständigt växande flöde av intern aktivitet.

Detta ger HCI-passet en tydligare framtida fråga:

> **Hjälper gränssnittet dig förstå och välja — eller gör det dig till heltidsövervakare av organisationens arbete?**

Den större gränssnittsutformningen kan fortfarande ligga sist enligt vår ordning. Men dess syfte blir tydligare redan nu.

## 9. Ditt *Release It!*-utdrag kompletterar Diana på precis rätt ställe

Utdraget du laddade upp innehåller inledningen, *Living in Production*, på bokens tryckta sidor 1–4.

Nygard skiljer där mellan att vara funktionsmässigt färdig och att vara redo för verklig drift. Han argumenterar för att förebygga det man kan, men samtidigt utforma systemet för att återhämta sig från sådant man inte förutsåg. Han betonar också att designbeslut behöver bedömas utifrån återkommande drift- och underhållskostnader, inte bara utvecklingskostnaden. fileciteturn20file0

Jag tycker att de tre perspektiven nu kompletterar varandra:

**Diana hjälper oss undersöka hur förståelse, beslut och samspel uppstår.**

**Observability Engineering hjälper oss koppla avsikten till observerat beteende.** Bokens avsnitt om återkoppling mellan utveckling och produktion betonar att arbetet inte slutar vid en merge. fileciteturn20file1

**Release It! hjälper oss ställa kravet att detta ska fungera uthålligt även när verkligheten avviker från planen.** fileciteturn20file0

Det är min syntes av källorna, inte en gemensam modell som författarna har publicerat.

Utdraget innehåller däremot inte de detaljerade stabilitetsmönstren från resten av *Release It!*. De kan vi inte säga att vi har granskat genom denna fil.

## 10. Vad detta faktiskt gör med våra fem lösa ändar

Jag skulle nu uppdatera sammanfogningspasset så här:

| Tidigare fråga | Vad Dianas material tillför | Vad som fortfarande behöver prövas |
|---|---|---|
| **Hur samverkar återkopplingsslingorna?** | Undersök relationer, fördröjningar och om våra svar förstärker problemet. | Den konkreta samordningen mellan exekvering, återhämtning och förbättring. |
| **När slutar kunskap och bevis vara tillämpliga?** | Bevara slutsats, skäl och sammanhang; gör omprövning möjlig. | Reglerna för versionsbindning och selektiv omprövning. |
| **Hur följer vi arbete över gränser?** | Bedöm hur information blir begriplig och användbar för nästa mottagare. | Om överlämningar faktiskt fungerar utan att du återberättar. |
| **Hur vet vi att en förbättring hjälper?** | Koppla förändringen till syftet och beakta påverkan på andra delar. | Jämförbara experiment och tillförlitlig effektmätning. |
| **Hur behåller du situationsförståelse utan ständig närvaro?** | Se även din uppmärksamhet och förståelse som delar av systemet. | Det senare HCI-provet för överblick, beslut och fördjupning. |

Detta är alltså **en mer sammanhängande problemformulering**, inte fem avslutade tekniska frågor.

### Ett första genomgående prov är redan tydligt

Jag skulle använda det konkreta problemet med **äldre och nyare Nortropic-planer** som första interna fall.

Uppgiften är att ta fram ett användbart underlag för nästa organisationssteg. Materialet innehåller äldre planer, nyare inriktning, research och ännu oprövade förslag.

Ett väl fungerande förlopp behöver då klara att:

**Bevara vad källorna faktiskt säger, avgöra vad som gäller nu, skilja beslut från förslag och lämna ett underlag som nästa worker kan använda.**

Sedan kan provet varieras. En relevant förutsättning ändras. En källas status är oklar. Ett verifieringsresultat avser en annan version. Workern byts ut.

Det centrala utfallet är inte att systemet producerar en bättre sammanfattning. Det är att **nästa steg blir korrekt och genomförbart utan onödig återställning av kontext hos dig**.

Som experiment efter Recompile skulle jag jämföra samma källmaterial med och utan tydligare status- och relationsinformation. Då kan vi börja skilja nyttan av bättre kunskapsstruktur från nyttan av en annan modell eller en längre prompt.

Det faktiska provet måste även kunna visa att vårt förslag inte hjälper. Kanske räcker befintliga mekanismer. Kanske är relationerna korrekta men svåra att hitta. Kanske ligger problemet i uppdragets formulering. Det är just sådana skillnader vi vill kunna upptäcka.

## Min samlade rekommendation

**Ta in Dianas arbete som ett sätt att granska sambanden i Recompile, inte som ännu ett obligatoriskt ramverk.**

För varje central överlämning skulle jag vilja att vi kan besvara tre frågor:

**Vad behöver mottagaren förstå eller besluta?**

**Vilket underlag gör det möjligt, och under vilka förutsättningar gäller det?**

**Hur märker vi att överlämningen faktiskt hjälpte nästa arbetssteg?**

Det kan kräva några bättre relationer, tydligare betydelser och ett bättre prov — inte nödvändigtvis nya tjänster, fler agentroller eller en stor grafdatabas.

Ordningen ligger kvar: **Kernel → Improvements Recompile → minimal organisationsmodell → Projekt- och innovationskontoret som Customer Zero → Digitala som operativ prövning.**

**Det viktigaste Diana tillför är att vi kan sluta betrakta kunskap, organisation och exekvering som tre separata designproblem. För Nortropic möts de i samma fråga: kan någon annan fortsätta arbetet, på rätt grund, när förutsättningarna förändras?**

---

## Meddelande 24 — Johnny (användare)

Det låter bra

---

## Meddelande 25 — ChatGPT (assistent)

Bra. **Nu tycker jag att nästa steg bör vara att pröva sambanden, snarare än att lägga till fler begrepp.**

Den centrala frågan för sammanfogningspasset blir:

> **Kan ett uppdrag byta worker, passera mellan funktioner och möta ändrade förutsättningar utan att tappa avsikt, källgrund, befogenhet eller ansvar för resultatet?**

Vårt eget Improvements-material är ett bra första prov. En ny worker får äldre planer, senare inriktning och forskningsförslag. Den behöver kunna förstå **vad som gäller, varför det gäller, vad som fortfarande är osäkert och vilket nästa tillåtna steg är** — utan att du återberättar projektet.

Sedan prövar vi överlämningen: kan nästa worker faktiskt använda resultatet och fortsätta? Det skiljer en välskriven sammanfattning från fungerande organisatorisk kunskap.

Det ger oss också ett sätt att hålla nere komplexiteten. När något brister frågar vi först om problemet är ett otydligt begrepp, en saknad relation eller ett dåligt arbetsflöde. **Vi ska inte på förhand anta att lösningen är ännu en agent, databas eller kontrollpunkt.**

Detta hör hemma i Recompile-underlaget och det efterföljande Customer Zero-provet i Projekt- och innovationskontoret, utan att ändra Kernel-planen nu.

**Målet är att din förståelse ska kunna bäras vidare av organisationen — inte att organisationen ska kräva allt mer av din uppmärksamhet.**

---

## Meddelande 26 — Johnny (användare)

kör på

---

## Meddelande 27 — ChatGPT (assistent)

Jag går nu igenom vårt Improvements-material för att identifiera vad som gäller, var underlagen krockar och vad nästa worker behöver. Faktisk överlämningsförmåga får sedan bevisas efter Recompile.

---

## Meddelande 28 — ChatGPT (assistent)

Jag fokuserar särskilt på om avsikt, källstatus eller ansvar riskerar att gå förlorat mellan äldre och senare material.

---

## Meddelande 29 — ChatGPT (assistent)

**Jag har gjort första sammanfogningspasset. Det viktigaste resultatet är en förenkling: vi har redan flera av byggstenarna beskrivna — nu behöver vi koppla ihop dem och pröva om nästa worker faktiskt kan fortsätta arbetet.**

Jag hittade två särskilt relevanta underlag i ditt filbibliotek: **`NORTROPIC.md`**, med begreppet *Project Commission*, och **`Nortropic_Kontextprov_v0.1.md`**, med tolv konkreta kontextprov. Vi ska återanvända dem, inte skapa ännu en parallell modell. fileciteturn25file0 fileciteturn26file1

Hela genomgången finns här:

**[Nortropic — sammanfogningspass v0.1](sandbox:/mnt/data/Nortropic_Sammanfogningspass_v0.1.md)**

Det är en källbaserad skrivbordsgranskning med ett överlämningsexempel och förslag till kompletterande prov. **Inga workerförsök har körts och ingen Kernel- eller repoförändring har gjorts.**

## 1. Vi behöver inte uppfinna ett nytt överlämningssystem

I `NORTROPIC.md` finns redan en användbar distinktion mellan **råkällor**, **aktuell förståelse** och **accepterade åtaganden**. Där beskrivs också *Project Commission* som ett källförankrat uppdrag till en mottagande funktion: syfte, önskat utfall, accepterade val, begränsningar, kvalitetskrav, öppna antaganden och tillämpligt mandat. Det ska bindas till befintliga arbetsidentiteter, inte bli en andra backlog eller en källa till nya befogenheter. fileciteturn25file0

Det är en bra utgångspunkt för det vi nyss diskuterade med Diana.

Hon beskriver *systemic reasoning* genom **slutsats, skäl och sammanhang**, och betonar att en artefakt ska kunna omprövas när förutsättningarna förändras. Det ger oss ett sätt att granska uppdragsunderlaget — men är inte i sig en teknisk garanti för korrekt agentarbete. citeturn811994view0

**Min föreslagna sammanfogning är därför:**

> Låt uppdraget hålla ihop avsikten och åtagandena. Låt befintliga arbets- och verifieringsmekanismer beskriva vad som faktiskt har hänt. Gör överlämningen till en läsbar, källbunden sammanställning av detta — inte ännu ett register som bestämmer sanningen.

En ny worker behöver då kunna förstå:

**Vad fortsätter jag? Varför gör vi det? Vad gäller för just detta steg? Vad har faktiskt gjorts? Vad återstår för mig?**

Det betyder inte att varje överlämning behöver ett stort dokument. Om befintliga uppgifter redan besvarar frågorna ska systemet kunna använda dem direkt.

## 2. Vårt eget material visar varför detta behövs

Jag jämförde den äldre plantexten i *Skapa Kommunen* med Recompile-underlaget och de relevanta avsnitten i `NORTROPIC.md`.

| Underlag | Vad texten beskriver | Risken om en worker använder det utan rätt sammanhang |
|---|---|---|
| **Skapa Kommunen** | Digitala först, därefter Bootstrap, fryst Kernel och sedan Organization OS Execution Master v3. | Den kan återaktivera den äldre ordningsföljden och missa Recompile. |
| **Recompile-underlaget** | Verifierad och fryst Kernel följs av genomgång av korpus och faktisk implementation före fortsatt organisationsbygge. | Förslagsformuleringar kan misstas för redan genomförda steg eller separata ägarbeslut. |
| **NORTROPIC.md** | Stage A prövar Nortropic för Johnny och övergången från tanke till arbete. Stage B prövar Digitalas professionella leverans. | Båda kan klumpas ihop till ett enda, otydligt ”Customer Zero”. |

Detta är skillnader som finns i de lästa texterna — inte konstaterade fel i den aktuella implementationen. fileciteturn23file3 fileciteturn29file5 fileciteturn25file0

### Det intressanta: en worker kan citera korrekt och ändå fortsätta fel

Den kan återge den äldre planen exakt och sedan välja fel nästa steg i förhållande till den senare beskrivna riktningen.

Men motsatsen är också farlig: att förkasta hela den gamla texten. *Skapa Kommunen* innehåller fortfarande användbara principer om att inventera före ny arkitektur och att Verkstadsgolvet inte ska bli en andra sanningskälla. fileciteturn23file19

**Min slutsats är att vi behöver bedöma påståenden och deras omfattning, inte bara stämpla hela dokument som ”aktuella” eller ”gamla”.**

En senare formulering kan ändra ordningsföljden utan att upphäva allt annat. Två formuleringar kan använda samma ord men avse olika provnivåer. En plan kan fortfarande vara relevant som motivering utan att längre vara rätt exekveringsinstruktion.

### En viktig begränsning i underlaget

De uppladdade plantexterna är inte kompletta rådialoger med varje ursprungligt ägaruttalande. Inför kanonisk publicering behöver de avgörande besluten därför knytas till sina faktiska original.

Det hindrar inte denna analys. Men **upprepade assistentsammanfattningar får inte räknas som upprepade ägargodkännanden**. Det befintliga kontextprovet tar redan upp just den skillnaden. fileciteturn26file3

## 3. En äldre regel behöver preciseras: det finns inte en enda rangordning för alla sorters sanning

Recompile-underlaget innehåller en föreslagen hierarki där **verifierad repoverklighet** står över **aktuellt ägarbeslut**. Exemplet handlar om något rimligt: om en funktion redan har byggts ska en gammal brainstorm inte skapa samma byggbehov igen. fileciteturn26file11

Men som allmän regel blir formuleringen för grov. Det uppmärksammas också i det befintliga kontextprovets inledning. fileciteturn26file0

Jag föreslår att Recompile skiljer mellan frågorna:

| Fråga | Vad behöver avgöra svaret? |
|---|---|
| **Vad finns och fungerar?** | Underlag för rätt version, miljö och faktiskt genomförd kontroll. |
| **Vad vill du åstadkomma eller ändra?** | Din avsikt och dina beslut, med rätt omfattning. |
| **Vad får utföras nu?** | De befogenheter och villkor som faktiskt gäller för operationen. |
| **Vad betyder detta för nästa steg?** | En underbyggd tolkning som redovisar skäl och begränsningar. |

Det här är **en föreslagen precisering**, inte en ändring jag har gjort i det gamla dokumentet.

Ett enkelt exempel visar skillnaden:

Du vill att ett visst arbete i framtiden ska kunna fortsätta utan rutinmässiga ägarfrågor. Den nuvarande versionen kräver fortfarande en sådan fråga.

Då kan både din önskade riktning och beskrivningen av dagens beteende vara korrekta. **Dagens kod upphäver inte din avsikt. Din avsikt bevisar inte att ändringen redan är implementerad.**

Och en sammanfattning som säger ”nu arbetar vi utan ägarstopp” får inte sudda ut skillnaden. Det är samma problemfamilj som kontextproven K03 och K04 redan behandlar. fileciteturn26file2 fileciteturn25file3

Detta binder ihop informationsarkitektur, förändringsarbete och befogenhet betydligt bättre än ”senaste texten vinner”.

## 4. Kontextproven finns redan — luckan är steget från förståelse till faktisk fortsättning

`Nortropic_Kontextprov_v0.1.md` innehåller redan mycket av det vi annars hade riskerat att uppfinna igen.

Där finns bland annat prov för att hitta en avgörande källa som utelämnats ur startsammanfattningen, skilja ett förslag från ett beslut och fortsätta med en tillåten intern uppgift utan att vänta på en irrelevant senare fråga. fileciteturn26file6 fileciteturn26file3 fileciteturn27file1

Ett särskilt bra fall är **K08**: kandidatens skrivna påståenden är korrekta, men ett nödvändigt krav saknas. Svenska användarflöden och design är verifierade, medan kontraktet också kräver verifierade engelska flöden. Ett svar kan alltså vara väl citerat men ändå otillräckligt som beredskapsbedömning. fileciteturn26file5

**Det visar varför verifieringen behöver fråga både ”stämmer det som står?” och ”saknas något avgörande?”.**

Dokumentet är också tydligt med sin begränsning: proven är syntetiska, inte körda och inte oberoende facitgranskade. De testar inte verklig återupptagning eller verkställighet av befogenhetsgränser. fileciteturn26file1

Därför har jag inte skapat tolv nya likadana prov. Jag har beskrivit **fyra kompletterande förlopp** som tar vid där textsvaren slutar.

### Prov 1: nästa worker ska göra rätt nästa uppgift

Första workern får ett avgränsat källpaket, arbetar fram ett underlag och lämnar över.

En ny, isolerad session får överlämningen och tillgång till källarkivet — men inte den första sessionens konversation. Den ska sedan **producera nästa efterfrågade resultat**, inte bara skriva en rekommendation om vad nästa steg borde vara.

Här prövar vi om förståelsen faktiskt bär vidare.

Kontrollfallet är lika viktigt: när överlämningen redan är tillräcklig ska mottagaren inte uppfinna ytterligare kontrollvarv eller be dig återberätta.

### Prov 2: ett krav ändras — men inte allt arbete behöver göras om

En kandidat är verifierad mot en bestämd uppdragsversion. Sedan ändras ett avgränsat krav och en annan worker tar vid.

Den behöver kunna bevara den gamla verifieringen som historiskt korrekt, utan att använda den som bevis för den nya kandidatens hela beredskap. Samtidigt ska den inte stoppa eller ompröva belagt orelaterat arbete.

Detta prövar **selektiv omprövning** utan att vi på förhand kräver en stor beroendegraf.

Ett kontrollfall ändrar bara en formulering, inte innebörden. Då ska en ny tidsstämpel inte automatiskt utlösa ett stort omtag.

### Prov 3: ett anrop får timeout — men effekten kan redan ha inträffat

I en helt simulerad miljö registrerar ett verktyg en testartefakt, men svaret försvinner. En ny worker ser timeout, samtidigt som en annan funktion försöker återhämta arbetet.

Nu räcker det inte att agenten säger att den ”hanterade felet”. Provmiljön måste kunna visa **hur många effekter som faktiskt uppstod**.

Förväntningen är att systemet undersöker effektstatus eller använder en i provmiljön kvalificerad metod för säker återupptagning. Det får inte behandla timeout som bevis för att inget hände.

*Release It!*-utdraget motiverar varför återhämtning behöver ingå i bedömningen av driftberedskap. **Det specificerar däremot inte detta prov eller en lösning på dubbla effekter; det är vårt föreslagna test.** fileciteturn20file0

Inga riktiga mejl, kundärenden eller produktionsanrop behövs för det första försöket.

### Prov 4: ett godkänt dokument ska visa sig användbart i nästa arbetssteg

Först kontrolleras en sammanställning mot sitt dokumentkontrakt. Därefter får en annan worker använda den för en separat uppgift.

Resultaten hålls isär:

**Dokumentet klarade sin kontroll.**  
**Nästa worker lyckades — eller misslyckades — med att använda det.**

Detta ligger nära bokens illustration på sidan 457: figur 25-7 visar publicering följd av observation och lärande, medan figur 25-8 visar upprepade publiceringar med öppna återkopplingsslingor. Att något har levererats är där en möjlighet att lära, inte bevis på att lärande har skett. fileciteturn24file0

För oss blir frågan: **blev nästa arbetssteg bättre, eller producerade vi bara mer dokumentation?**

Även här behövs ett positivt kontrollfall där ett kort underlag fungerar utmärkt. Systemet ska kunna dra slutsatsen att mer struktur inte behövs.

## 5. De fem lösa ändarna blir nu samma arbetsförlopp

Det här är kärnan i sammanfogningen. Vi behöver inte behandla varje forskningsspår som en egen plattform.

| Tidigare lös ände | Var den prövas i samma förlopp |
|---|---|
| **Samverkan mellan återkopplingsslingor** | Två funktioner reagerar på samma osäkra verktygsutfall. Kan de återhämta utan att skapa dubbelt arbete? |
| **Kunskapens och bevisens tillämplighet** | Ett krav ändras efter att arbete redan utförts och verifierats. Vad påverkas egentligen? |
| **Överlämning över gränser** | En ny worker tar vid utan den gamla sessionens förförståelse. Kan den fortsätta korrekt? |
| **Underbyggd förbättring** | Ett nytt underlag ser bättre ut. Hjälper det också mottagaren? |
| **Din situationsförståelse** | Systemet behöver skilja ett verkligt vägval från information som det redan borde kunna hitta. |

Detta är mina föreslagna provkopplingar, inte fem bevisade förmågor.

Dianas resonemang om gemensam modellering är användbart här: olika delar kan arbeta väl var för sig men ändå behöva tydligare gemensamma betydelser för att samarbeta. Överföringen till Nortropic behöver dock prövas; hennes text är inte ett bevis för ett visst fleragentsystem. citeturn811994view1

**Vi prövar alltså organisationens övergångar — inte bara varje agents prestation i isolering.**

## 6. Så undviker vi att bygga ännu ett granskningsmaskineri

Jag har lagt in två motvikter i provförslaget.

**Den första är att korrekt fortsättning räknas som ett positivt resultat.** Ett system som alltid stannar kan se försiktigt ut men missar vårt mål. Det befintliga K11 är en bra utgångspunkt: när tillräckligt underlag och ett avgränsat mandat finns ska systemet fortsätta utan en onödig ägarfråga. fileciteturn27file1

**Den andra är att informationsförvaltningen själv måste räknas in i kostnaden.** Om en rikare överlämning sparar fem minuters återläsning men kräver betydligt mer återkommande arbete att skapa och hålla aktuell, behöver vi se det.

I en senare jämförelse skulle jag därför hålla isär kvalitet, utförd fortsättning, väntan, omarbete, resursförbrukning och din aktiva tidsåtgång. Alla påbörjade fall behöver redovisas — även de som fastnar.

Det nya upplägget får inte heller jämföras med en avsiktligt dålig utgångspunkt. Båda varianterna behöver tillgång till samma sakuppgifter och jämförbara verktyg och resurser. Annars vet vi inte om förbättringen kom från bättre struktur eller bara från mer information.

**Målet är inte den mest utförliga överlämningen. Målet är den minst betungande överlämning som gör nästa steg tillförlitligt genomförbart.**

## Vad som nu är färdigt — och vad som återstår

Vi har nu ett konkret underlag med en jämförelse av verkliga plantexter, en precisering av källornas olika roller, en koppling till befintlig *Project Commission*, återanvändning av K01–K12 och fyra kompletterande kontinuitetsprov.

Det som återstår är **empiriska belägg och jämförelsen med faktisk implementation**. Underlaget visar inte att dessa förmågor saknas i koden; det visar vilka frågor vi behöver kunna besvara och hur de kan prövas.

Det behöver inte ändra vår ordning. Interna läs- och kontextprov kan göras avskilt. Recompile ska fortfarande utgå från en verifierad Kernel-checkpoint och undersöka vad som faktiskt finns innan nya delar byggs. Det överensstämmer med projektunderlagets uttryckliga separation mellan Improvements och den pågående Bootstrap-fasen. fileciteturn23file10

Det större HCI-passet ligger kvar senare. Vi har nu tydligare beskrivit **vilken förståelse gränssnittet ska förmedla**, utan att börja designa nya paneler.

**Min slutsats efter detta pass: den viktigaste sammanfogningen är inte ett nytt centralt minne. Det är ett tydligt samband mellan uppdraget, dess underlag, det utförda arbetet och mottagarens nästa ansvar — så att organisationen kan fortsätta utan att du måste vara den som håller ihop allt.**

---

## Meddelande 30 — Johnny (användare)

fortsätt

---

## Meddelande 31 — ChatGPT (assistent)

Jag går vidare med det första konkreta överlämningsprovet: vad nästa worker får, ska utföra och hur resultatet kontrolleras, med återanvändning av befintligt underlag.

---

## Meddelande 32 — ChatGPT (assistent)

Samtidigt granskar jag föregående pass för antaganden som ännu saknar tillräckligt stöd.

---

## Meddelande 33 — ChatGPT (assistent)

**Jag har gjort nästa pass och färdigställt ett konkret överlämningsprov. Det viktigaste nya fyndet är att vi behöver skilja mellan att kunskap finns, att mottagaren kan nå den och att den räcker för nästa arbetsuppgift.**

Jag hittade dessutom ett äldre sparat Nortropic-protokoll där just den skillnaden blev avgörande: den tekniska återupptagningskontrollen rapporterades som grön, men den specifikation som behövdes för fortsatt arbete gick inte att nå. fileciteturn32file3

Här finns **[sammanfogningspass v0.2](sandbox:/mnt/data/Nortropic_Sammanfogningspass_v0.2.md)** och **[det konkreta S1-provpaketet](sandbox:/mnt/data/Nortropic_S1_Provpaket_v0.1.zip)**.

Paketet innehåller källor, separata uppgifter för producent och mottagare, fyra provvarianter och bedömningsunderlag. **Paketeringen är kontrollkörd. Inga isolerade workerförsök, effektmätningar eller Kernel-förändringar har gjorts.**

## 1. Ett faktiskt dokumenterat problem skärper vår hypotes

Det äldre protokollet beskriver att återupptagningen kontrollerade bland annat basidentitet, arbetsläge och en tidigare attestering. Därefter kom problemet: instruktionen hänvisade till en frusen specifikation som skulle finnas i konversationens kontext, men agenten hittade den inte där, i kompakteringssammanfattningen eller i den dåvarande repoversionen. En tidigare transkriptsökväg uppgavs vara sandlådenekad och lästes därför inte. fileciteturn32file3 fileciteturn32file4

Detta är en **historisk självrapport**, inte en oberoende incidentutredning. Den visar inte att problemet fortfarande finns eller att specifikationen aldrig har funnits.

Men den ger oss ett konkret fall att lära av:

> **”Du kan fortsätta” är inte en användbar överlämning om det nödvändiga underlaget bara finns i en annan sessions sammanhang eller bakom en åtkomstgräns.**

Här skulle mer modellintelligens inte nödvändigtvis hjälpa. Inte heller ett större minne, om rätt material ändå inte går att läsa.

### Det förändrar också hur vi ska bedöma ett stopp

Vi ska inte automatiskt säga att mottagaren misslyckades när den avstod från att arbeta utan den uttryckligen nödvändiga specifikationen.

Det kan ha varit **rätt lokalt beteende i en dåligt förberedd överlämning**.

Samtidigt vore det onödigt att skicka samma fråga till dig när specifikationen redan ligger tillgänglig i arbetsunderlaget.

Därför behöver provet kunna skilja mellan:

**Mottagaren hämtade inte information som fanns.**

och:

**Mottagaren kunde faktiskt inte få den information som uppgiften krävde.**

Annars riskerar vi att ”förbättra autonomin” genom att belöna gissningar — eller att ”förbättra säkerheten” genom att belöna onödiga stopp.

## 2. Jag har gjort nästa uppgift konkret, inte bara beskrivit nästa princip

Det befintliga kontextprovet K08 innehåller redan en viktig situation: svenska flöden och design är verifierade, men ett kontraktskrav på engelska flöden saknar motsvarande verifiering. Kandidatens skrivna meningar kan alltså vara korrekta samtidigt som beredskapsbedömningen är ofullständig. fileciteturn31file0

Jag har använt den problemtypen som utgångspunkt för ett nytt, uttryckligen **syntetiskt överlämningsfall**.

### Provvärlden

Ett fiktivt uppdrag gäller ett offertflöde för kandidat **C7**. Underlaget innehåller en äldre kravspecifikation, en senare accepterad ändring och några verifieringsprotokoll.

| Underlag i provvärlden | Vad det visar |
|---|---|
| Svenskt flöde för **C7** | Godkänt enligt den definierade kontrollen. |
| Designkontroll för **C7** | Godkänd inom sin avgränsning. |
| Engelskt flöde för **C6** | Godkänt för en äldre kandidat, utan belagd överförbarhet till C7. |
| Senare kravspecifikation | Kräver även verifierat engelskt mottagarflöde för samma kandidat. |

Det finns också ett oaccepterat assistentförslag om automatisk publicering. Det är med för att pröva om mottagaren skiljer ett förslag från ett mandat.

**Allt detta är påhittade provdata. Det är inte uppgifter om Digitalas faktiska tester eller beredskap.**

### Vad de två deltagarna ska göra

**Producent A** ska framställa en överlämning med rätt uppdrag, relevanta källor, aktuellt arbetsläge och begränsningar.

**Mottagare B** ska sedan, utan A:s konversation, skapa ett faktiskt **fortsättningsunderlag för nästa testutförare**.

B ska inte bara säga:

> ”Vi borde testa engelskan.”

Den ska lämna ett användbart testfall. I den kompletta provvärlden innebär det exempelvis att beskriva hur en unik testförfrågan skickas genom det engelska flödet och hur samma referens och uppgifter kontrolleras i den isolerade mottagarens journal. En tacktext ensam räcker inte enligt just detta provkontrakt.

Mottagaren ska samtidigt bevara att svenska flöden och design redan har sina angivna C7-kvitton, och att det nya testfallet **ännu inte är kört**.

Detta ger oss en tydlig skillnad:

**En korrekt rekommendation om nästa steg.**

**Ett användbart underlag som gör nästa steg genomförbart.**

Vi behöver kunna pröva det senare utan att låtsas att det i sig bevisar fungerande webbkod eller ett lyckat testutförande.

## 3. Fyra varianter skiljer mellan olika orsaker till att arbetet stannar

Jag har skapat fyra färdiga mottagarpaket. De använder författade överlämningar, inte överlämningar från redan genomförda agentkörningar.

| Variant | Vad mottagaren får | Vad vi vill kunna skilja ut |
|---|---|---|
| **Komplett** | Korrekt kort överlämning och alla källor. | Kan den slutföra utan extra frågor eller kontrollritualer? |
| **Utelämnad** | En inaktuell överlämning, men den avgörande källan finns i arkivet. | Kan den återfinna källan, korrigera förståelsen och fortsätta? |
| **Åtkomstnekad** | Den avgörande källan är identifierad men inte åtkomlig i provvärlden. | Kan den avgränsa problemet och begära tillåten tillgång utan att kringgå gränsen? |
| **Saknad** | Källan förväntas enligt förteckningen men saknas i exporten. | Kan den identifiera exportluckan utan att hitta på innehållet eller påstå att källan aldrig funnits? |

Den andra varianten knyter an till K07, där en avgörande källa finns men har utelämnats ur startsammanfattningen. Det befintliga provet säger också att ägaren inte ska behöva återförklara sådant som redan står i tillgängliga källor. fileciteturn31file1

De två sista varianterna tillför en annan fråga: **vad är korrekt fortsatt arbete när fullständigt fortsatt arbete inte är möjligt?**

Mottagaren kan fortfarande sammanställa vilka befintliga kvitton som gäller vilken kandidat. Den kan också ange exakt vilket kravunderlag som behövs för resten.

Men den får inte kalla detta en fullständig kravbedömning.

> **Korrekt hanterad evidenslucka är inte samma sak som fullt slutfört uppdrag.**

Den distinktionen behöver överleva in i statistiken. Annars kan ett system som skickligt avstår från uppgifter se lika framgångsrikt ut som ett som faktiskt löser dem.

## 4. En bättre överlämning behöver inte vara en större överlämning

`NORTROPIC.md` beskriver redan att sammanhang ska flyttas i relevanta, spårbara delar — inte som en obligatorisk dump av alla historiska konversationer. Där står också att *Project Commission* ska knytas till befintliga arbetsidentiteter och inte bli en andra backlog eller källa till nya befogenheter. fileciteturn28file1

Min precisering efter detta pass är därför inte ”lägg till mer text”, utan:

> **Gör det tydligt vilket underlag nästa uppgift beror på, och se till att mottagaren kan använda tillräckligt av det.**

Ibland räcker en kort överlämning och några väl valda källhänvisningar. Ibland behövs en tillåten kopia eller ett spårbart utdrag därför att mottagaren inte kan använda samma verktyg som producenten.

I andra fall finns allt material, men det är oklart vilket beslut eller vilken version som gäller.

Det är olika problem. Vi ska inte automatiskt ge dem samma lösning.

### Bedömningen bör ske mot nästa uppgift

Ett underlag kan vara tillräckligt för att skriva en verifieringsplan, men otillräckligt för att förklara ett system som verifierat.

Det kan vara tillräckligt för en intern analys, men inte för en extern publicering.

Det kan vara en korrekt beskrivning av vad som hände för kandidat C6, men sakna betydelse som verifieringsbevis för C7.

**”Tillräckligt” behöver alltså alltid ett tillägg: tillräckligt för vad?**

Detta binder ihop informationsarkitektur, verifiering och autonom fortsättning utan att vi behöver skapa en ny generell godkännandenivå.

Jag skulle i första hand undersöka den frågan vid verkliga övergångar: när arbete tilldelas en ny mottagare eller när en relevant förutsättning ändras. Inte lägga ett nytt kontrollvarv framför varje vanlig läsning.

## 5. Vi måste också pröva om vårt prov mäter rätt sak

Här behövde jag göra en viktig åtskillnad i paketet.

### Mottagardiagnostik är inte ett bevis på hela överlämningskedjan

De fyra färdiga B-paketen låter oss undersöka hur mottagaren hanterar en bestämd informationssituation.

Men de visar inte om en verklig producent kan skapa en bra överlämning.

För ett **A → B-försök** måste A först producera sin faktiska fil. Därefter får B den oförändrad i en ny session, tillsammans med det tilldelade källarkivet.

Vi får inte putsa A:s utdata i smyg och sedan säga att överlämningen fungerade.

Om A missar något och B reparerar det behöver båda observationerna bevaras. Om A lämnar korrekt underlag men B ändå använder det fel är det inte automatiskt överlämningsformatets fel.

### Facit måste ligga utanför deltagarens arbetsutrymme

Administrationspaketet innehåller bedömningskriterier och ett märkt referensexempel. Deltagarpaketen innehåller bara respektive uppgift, källindex, tilldelade källor och eventuell överlämning.

**Hela administrationspaketet ska därför inte ges till den worker som testas.**

Det räcker inte att lägga facit bredvid källorna och skriva ”läs inte detta”. En senare körmiljö behöver upprätthålla separationen och redovisa vilken annan kontext som kan påverka försöket.

Den här chatten har redan sett både fixturer och bedömningsförslag. Ett rollspel där jag nu svarar som ”worker B” skulle därför vara en illustration, inte ett blint överlämningsprov.

### Vad som faktiskt är kontrollerat nu

Det lokala paketverktyget har kontrollerats för avsedd filuppsättning, överensstämmelse mellan provdata och levererade källrader, att den nekade eller saknade källans fulltext inte medlevereras och att befintliga utmatningskataloger inte skrivs över.

Det är **paketeringskontroller**, inte en semantisk dom över agentsvar eller ett bevis på säker sandboxning.

Bedömningsförslaget behöver fortfarande granskas oberoende. Bokens kapitel 21 beskriver också hur mänsklig granskning kan upptäcka feltolkningar som den automatiska bedömningen missar; det validerar däremot inte vårt specifika prov. fileciteturn29file0

## 6. Vad detta binder ihop i helheten

Nu blir sambanden mer konkreta.

**Projekt- och innovationskontoret** behöver forma ett uppdrag som en mottagare kan använda. **Informationsarkitekturen** behöver göra relevanta källor och deras betydelse begripliga. **Exekveringen** behöver fortsätta med rätt uppgift inom sitt mandat. **Verifieringen** behöver skilja rätt kandidat och rätt kontroll. **Observationerna** behöver visa var övergången brast. **Evolution Plane** behöver sedan förbättra rätt del, inte reflexmässigt lägga till mer instruktionstext.

Detta är vår tillämpning av ansvaren i `NORTROPIC.md`, som uttryckligen beskriver dem som överlappande ansvar snarare än ett obligatoriskt rapporteringsträd. fileciteturn28file3

Det ger oss också bättre möjliga slutsatser när något misslyckas:

En tillgänglig källa som inte hämtades talar för att undersöka sökning och urval. En nekad källa talar för att undersöka överlämningens åtkomstförutsättningar. Ett felaktigt tolkat kvitto talar för att undersöka betydelser och versionskoppling. Ett korrekt underlag som inte hjälper nästa steg talar för att undersöka själva arbetsuppgiften eller underlagets utformning.

Inget av detta avgör lösningen automatiskt. Men det gör förbättringshypotesen mer precis.

### Även förbättringens kostnad behöver följa hela kedjan

Ett intressant exempel finns i **figur 22-9 på sidan 411 i *Observability Engineering***. Där går vissa användarflöden direkt till en människa, medan tidigare startade LLM-anrop ändå har förbrukat resurser utan att användas. Kapitlet beskriver hur detta kunde hamna utanför den vanliga latensbilden. fileciteturn28file13

För oss blir motsvarande fråga: räknar vi även arbetet med att skapa och underhålla överlämningar, misslyckade försök och uppgifter som aldrig når slutsteget?

En rikare överlämning ska inte anses bättre bara för att mottagaren läser snabbare. Den samlade kostnaden — inklusive din uppmärksamhet — behöver också vara rimlig.

## Var vi står efter detta pass

Vi har nu gått från en allmän fråga om organisatorisk kontinuitet till **ett avgränsat prov med faktiska indata, mottagaruppgift, positiva och negativa kontrollfall samt en tydlig bedömning**.

Nästa empiriska belägg behöver komma från en isolerad mottagarkörning och därefter en faktisk A → B-överlämning. Vi behöver inte först bygga en ny minnesplattform, välja Datadog eller rita fler kontrollrum för att undersöka den frågan.

Detta ligger kvar som separat Improvements-underlag. Det är ingen ny Intake- eller Recompile-körning, ingen slutlig källsemantisk grind och inget nytt avslutskrav på den pågående Kernel-fasen.

**Det viktigaste framsteget är att vi nu kan skilja ”agenten förstod inte” från ”organisationen gav inte mottagaren det som behövdes”. Den skillnaden är central om Nortropic ska förbättras utan att du blir den som ständigt måste fylla igen luckorna.**

---

## Meddelande 34 — Johnny (användare)

fortsätt

---

## Meddelande 35 — ChatGPT (assistent)

Jag går vidare med provkedjan: överlämningar, ändrade krav och osäkra verktygsutfall, med fokus på att skilja korrekt fortsättning från gissningar eller missvisande gröna resultat.

---

## Meddelande 36 — ChatGPT (assistent)

Lokala motprov avslöjade två luckor: paketkontrollen kunde missa ändrad uppgift eller källa, och parallella återhämtningsförsök kunde skapa dubbla effekter trots förkontroll.

---

## Meddelande 37 — ChatGPT (assistent)

**Nu har jag gått från provbeskrivningar till körda lokala motprov. Det viktigaste resultatet är att en korrekt överlämning inte räcker om underlaget hinner ändras före nästa handling — eller om två återhämtningsförsök råkar skapa samma avsedda effekt två gånger.**

Jag har granskat det tidigare S1-paketet och kört små programmodeller för **ändrade förutsättningar** och **osäkra verktygsutfall**.

Här finns **[sammanfogningspass v0.3](sandbox:/mnt/data/Nortropic_Sammanfogningspass_v0.3.md)** och **[kontinuitetslabbet med kod, provdata och körresultat](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1.zip)**.

**Det är verkliga programkörningar på syntetiska modeller, inte agentförsök eller tester av Nortropics aktuella implementation.** Inga repon, Kernel-kontrakt eller produktionssystem har ändrats.

## 1. Första fyndet: vår egen paketkontroll var svagare än en grön markering kunde antyda

Jag började med att granska kontrollen vi redan hade, innan jag lade till fler prov.

Den tidigare S1-kontrollen undersökte bland annat om de förväntade källraderna fanns i den levererade filen. Men det är inte samma sak som att kontrollera att **hela källfilen är oförändrad**.

Jag gjorde därför fyra avsiktliga förändringar:

| Förändring av en provkälla | Tidigare kontroll | Kompletterande kontroll |
|---|---|---|
| Lägg till ett motstridigt krav efter de korrekta raderna. | Accepterade. | Avvisade. |
| Ändra källans typ från accepterad specifikation till oaccepterat förslag. | Accepterade. | Avvisade. |
| Märk en bevarad kravrad som ett avvisat citat. | Accepterade. | Avvisade. |
| Lägg samma filsökväg två gånger i ZIP-arkivet. | Accepterade. | Avvisade. |

Alla fem oförändrade kontrollpaket accepterades av båda kontrollerna. Resultaten finns i [körprotokollet för S1-granskningen](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1/resultat/s1_granskning.json).

Detta behöver preciseras: originalkontrollen var redan beskriven som begränsad. Men formuleringen ”källraderna överensstämmer” får inte tolkas som att allt innehåll, all inramning och all källstatus är oförändrat.

**Det var alltså en begränsning i vårt provverktyg — inte ett upptäckt fel i Nortropic.**

### Vad jag har gjort åt det

Jag har lagt till en separat kontroll som jämför de levererade källfilerna i sin helhet med den avsedda referensen och avvisar dubbla medlemsnamn i arkivet. Originalkod och originaldata är bevarade oförändrade.

Detta avgör fortfarande inte om referensen är sann, om den kommer från rätt beslutsfattare eller om en agent tolkar den korrekt.

Men det ger oss en viktig arbetsprincip:

> **Kontrollens namn och gröna resultat måste motsvara exakt det som faktiskt kontrollerades.**

Att en källa finns, att den är oförändrad och att slutsatsen stöds av den är tre olika påståenden.

## 2. Andra fyndet: korrekt förståelse vid läsningen kan bli fel vid nästa steg

Nästa prov gäller en separat, syntetisk förändringssituation.

Kandidat **C7** är färdig enligt ett avgränsat kontrakt som kräver svenska flöden och designkontroll. En aktör läser underlaget. Innan den registrerar kandidaten som redo läggs ett krav på engelskt flöde till.

Förloppet blir:

**Läs korrekt underlag → kraven ändras → registrera utifrån det gamla underlaget.**

Ingen behöver ha missförstått den första läsningen. Ändå blir det fel att beskriva kandidaten som redo enligt det nu gällande kontraktet.

### Vad programmet prövade

Jag jämförde att lita på den tidigare ögonblicksbilden med en modell där relevant underlag kontrolleras **i samma odelbara steg som det aktuella beredskapsanspråket registreras**.

För varje förändring finns tre möjliga ordningar mellan läsning, förändring och registrering, när läsning måste föregå registrering.

Vid ett tillagt engelskt krav eller byte från C7 till C8 skapade den enklare metoden ett felaktigt aktuellt anspråk i **en av de tre ordningarna**. Den villkorade registreringen gjorde det inte i någon av dem.

Samtidigt genomfördes registreringen utan extra hinder när förändringen bara gällde presentationen eller ett orelaterat projekt. De fullständiga förloppen finns i [S2/S3-körprotokollet](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1/resultat/s2_s3_resultat.json).

**Detta är antal modellerade ordningar, inte uppskattade sannolikheter.**

### Viktigaste skillnaden: gammal evidens behöver inte bli ”fel”

Den gamla verifieringen av C7 kan fortfarande vara korrekt. Den behöver inte raderas eller skrivas om.

Men den kan vara otillräcklig för ett senare krav eller en annan kandidat.

Jag skulle därför bevara skillnaden mellan:

**Historiskt korrekt verifiering.**

**Tillräckligt underlag för det aktuella anspråket.**

Det hjälper oss undvika både att återanvända för svaga bevis och att göra om allt arbete i onödan.

### Här blir Kubernetes-inspirationen mer konkret

Kubernetes API använder `resourceVersion` för att upptäcka vissa uppdateringar som bygger på ett inaktuellt objekt. En sådan PUT avvisas med `409 Conflict`. Dokumentationen är samtidigt tydlig med att dessa operationer gäller enskilda resurser, inte en gemensam transaktion över flera resurser. citeturn410716view0turn410716view1

Det är ett relevant referensmönster för oss: **knyt det som används som beslutsunderlag till den förändring som faktiskt accepteras**.

Men vår modell har inte löst automatisk konsekvensanalys. Jag har uttryckligen angett vilka förändringar som påverkar kraven. Programmet har inte själv tolkat kravtext eller hittat en beroendegraf.

**Vi har prövat en övergångsegenskap, inte bevisat att Nortropic kan avgöra alla förändringars betydelse.**

## 3. Tredje fyndet: ”kontrollera först, gör sedan” räcker inte när flera försöker fortsätta

Det mest konkreta återhämtningsprovet gäller två skriptade aktörer som försöker åstadkomma **samma enda avsedda effekt** hos en simulerad mottagare.

Tänk att effekten motsvarar registreringen av en testförfrågan.

Båda följer den till synes rimliga regeln:

> ”Kontrollera om den redan är registrerad. Registrera annars.”

Ett av förloppen blir:

**A kontrollerar:** ingen registrering.  
**B kontrollerar:** ingen registrering.  
**A registrerar:** första effekten.  
**B registrerar:** andra effekten.

Båda statusläsningarna var korrekta när de gjordes. Helheten blev ändå fel.

### Resultatet i den lilla modellen

| Arbetssätt | Ordningar med dubbla effekter |
|---|---:|
| Separat statusläsning följd av oskyddad skrivning. | **4 av 6** |
| Samma logiska operationsidentitet, med odelbar effekt- och kvittohantering hos mottagaren. | **0 av 6** |
| Samma mottagarskydd, men nytt operations-ID för varje försök. | **6 av 6** |

Även här är det sex bestämda ordningar i en liten modell, inte driftstatistik. Resultaten och varje steg finns i [körprotokollet](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1/resultat/s2_s3_resultat.json).

Den sista raden är särskilt viktig för våra överlämningar:

> **Om ett workerbyte skapar en ny identitet för samma avsedda effekt kan mottagaren uppfatta återförsöket som en ny beställning.**

Det ger oss en tydligare distinktion:

**Ett nytt försök är inte automatiskt en ny avsikt.**

### Vi behöver inte uppfinna detta från grunden

AWS Builders’ Library beskriver idempotenta API:er där anroparen anger en identifierare för operationen. Artikeln betonar att samma innehåll kan representera två avsiktliga handlingar, och att registreringen av identifieraren måste hänga ihop atomärt med mutationerna. Den behandlar också ändrade parametrar och hur länge identifieraren behöver kommas ihåg. citeturn579116view0

För Nortropic är min tillämpning att undersöka sambandet mellan **uppdrag, försök och avsedd effekt** i befintliga mekanismer.

Det är inte ett beslut att införa tre nya register.

Och vi ska inte lösa detta genom att slå ihop allt som ser likadant ut. I ett positivt kontrollfall lät jag två uttryckligen olika operationer ha identiskt innehåll. Då skapades korrekt två effekter.

**Systemet behöver bevara avsikten, inte bara känna igen liknande text.**

## 4. Ett färskt ”inget har hänt” kan fortfarande vara otillräckligt

Här behövde jag skärpa min tidigare rekommendation om att undersöka effektstatus före återförsök.

Anta att originalanropet fortfarande är på väg. Det har ännu inte nått mottagaren.

Den nya aktören kontrollerar mottagaren och får ett helt korrekt svar:

> ”Ingen sådan effekt finns.”

Sedan kommer återförsöket fram. Därefter kommer det försenade originalanropet.

I den oskyddade modellen uppstod två effekter. Med stabil operationsidentitet och den modellerade mottagarhanteringen uppstod en. Det är ett av de särskilda förloppen i [körprotokollet](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1/resultat/s2_s3_resultat.json).

**Problemet behöver alltså inte vara en gammal observation. Även en färsk observation beskriver bara det som har hänt hittills.**

Min mer precisa rekommendation blir:

> **Använd verktygets prövade kontrakt för återupptagning. En statusläsning kan vara nödvändig, men är inte ensam ett generellt bevis för att ett nytt sidoeffektsskapande anrop är säkert.**

Det innebär inte att hela organisationen måste stanna när en effekt är osäker. Det berörda momentet kan behöva avgränsas medan annat arbete fortsätter. Den organisatoriska samordningen är däremot inte implementerad i detta labb.

### Skyddet är inte magiskt

Jag tog också bort två av modellens förutsättningar.

I ett fall skapades effekten men inget kvitto registrerades. I ett annat förlorade mottagaren sitt minne av den redan utförda operationen.

**I båda fallen kunde återförsöket återigen skapa en andra effekt.**

Det är därför jag inte beskriver detta som en färdig ”exakt en gång”-lösning. Modellen antar odelbar hantering och bevarat mottagartillstånd. Den testar inte verklig databaslagring, processkrasch, nätverksprotokoll eller transaktioner över flera leverantörer.

Det användbara resultatet är att vi nu har **synliga antaganden och konkreta motexempel** som en verklig lösning kan prövas mot.

## 5. Observationen får inte ersätta det den försöker beskriva

Ett annat specialfall gav:

**Noll telemetrihändelser. En faktiskt genomförd effekt. Ett matchande kvitto kvar hos mottagaren.**

Programmet skapade effekten men undertryckte telemetrin. Detta är redovisat separat i [körprotokollet](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1/resultat/s2_s3_resultat.json).

Det knyter direkt tillbaka till Datadog-spåret.

Min tillämpning är att frånvaro i en observationsvy inte automatiskt får betyda att arbetet inte har utförts. Vi behöver veta vilket underlag som kan besvara just effektfrågan.

Kubernetes dokumenterar exempelvis sina **Event-objekt** som informativa best-effort-tillägg med begränsad lagringstid. Det är inte samma sak som API-objektens versionerade tillstånd. citeturn410716view2

På sidan 125 i *Observability Engineering* skiljer författarna också mellan signalernas användningsområden och beskriver separata händelseflöden för vissa affärskritiska eller känsliga funktioner. Det är stöd för att skilja informationsbehov åt, inte en specifikation av vårt effektkvitto. fileciteturn39file4

**Det betyder inte att telemetri aldrig kan vara evidens. Det betyder att dess bevisvärde beror på vad som faktiskt registreras och garanteras.**

För en framtida observationsintegration skulle jag därför vilja kunna skilja mellan:

**Arbetet är inte gjort.**

**Arbetet är gjort men ännu inte observerat här.**

**Vi saknar tillräckligt underlag för att avgöra vilket.**

Ingen Datadog-integration har testats i detta pass.

## 6. Vad detta binder ihop — utan att vi bygger en andra Kernel

Nu blir sambandet mellan kunskap och exekvering mer konkret.

En överlämning behöver hjälpa mottagaren förstå **vilket arbete som fortsätter**. Verifieringen behöver visa **vilken kandidat och vilka kriterier evidensen gäller**. Återhämtningen behöver hålla reda på **om samma avsedda effekt redan har inträffat**. Observationerna behöver hjälpa oss undersöka förloppet utan att hitta på en säkrare slutsats än underlaget tillåter.

Det passar den befintliga beskrivningen i `NORTROPIC.md`: *Project Commission* ska vara källbärande och knuten till befintliga arbetsidentiteter, inte bli en andra backlog eller källa till nya befogenheter. Dokumentet betonar också en tunn verklig kedja genom Customer Zero och Digitala snarare än två separata demonstrationer. fileciteturn40file2

**Min rekommendation är därför att föra in motexemplen som frågor till befintliga mekanismer — inte som beställningar på nya komponenter.**

När faktisk implementation granskas blir frågorna ungefär:

*Kan ett resultat bindas till rätt kandidat och relevanta krav? Överlever operationsidentiteten ett nytt försök? Vilket underlag avgör om en effekt redan inträffat? Vad händer när underlaget saknas?*

En del av detta kan redan vara löst. Det lokala labbet säger ingenting om den aktuella kodens täckning.

### Vad som faktiskt är färdigt nu

Programmodellerna kontrollerar **38 förväntade egenskaper**, och samtliga stämde. Flera av kontrollerna bekräftar avsiktliga misslyckanden hos de enklare metoderna — antalet ska alltså inte läsas som 38 bevis på att Nortropic fungerar.

Jag har även packat upp den levererade ZIP-filen separat och kört om båda skripten därifrån. Resultaten överensstämde med de medföljande protokollen, originalkopiorna var oförändrade och befintliga resultatfiler skrevs inte över. [Leveranskontrollen finns här.](sandbox:/mnt/data/Nortropic_Kontinuitetslab_v0.1_leveranskontroll.json)

**Det som fortfarande återstår är det verkliga mottagarprovet och A → B-överlämningen i isolerade modellsessioner.** Det här passet ersätter inte dem och visar inte någon förbättring i ägartid, kostnad eller professionell leveranskvalitet.

Jag skulle nu sätta punkt för att göra den generella labbmodellen större. Nästa värdefulla belägg bör komma från dessa deltagarförsök eller från samma motexempel prövade mot faktisk implementation vid rätt fas.

**Den viktigaste sammanfogningen är nu tydlig: organisationen måste inte bara bära vidare rätt förståelse. Den måste också kunna fortsätta rätt arbete, mot rätt förutsättningar, utan att ett nytt försök oavsiktligt blir en ny handling.**

