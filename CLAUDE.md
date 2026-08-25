# Nortropic innovation-intake — idékorpusen

Detta repo är korpusen/idébanken som skillen `nortropic-intake`
(`~/.claude/skills/nortropic-intake/`) levererar till. Varje idé är en låda med tre
papper: byggritningen (briefen = VAD), designrationalen (= VARFÖR) och dagboken
(transkriptet = RÅ BEVISNING). Briefen styr; rationalen förklarar designlogiken vid
behov; transkriptet slås upp i riktade meddelandeintervall.

Paketmodellen i sin helhet:

    RÅ              vad som faktiskt sades och bifogades      <slug>-full-chat.md
    VARFÖR          varför designen ser ut som den gör        <slug>-design-rationale.md
    VAD             vad som är avsett                         idea-<slug>.md
    ÄGARDELTAN      vad ägaren klargjort efteråt              <slug>-owner-clarifications.md
    VAR             var varje källa finns och dess identitet  <slug>-context-manifest.json
    HUR (förslag)   det Claude föreslår — det ägaren läser    <slug>-plan-candidate.md
    HUR (godkänt)   exakt ägargodkänd exekveringsplan         <slug>-approved-plan.md
    VERKLIGHETEN    vad målrepona faktiskt innehåller         läses färskt, varje gång

**Fullständig kontext betyder fullständigt BEVARANDE, inte fullständig förladdning.**
Varje källa bevaras varaktigt, adresserbart och hashbundet; varje fas får sedan den
minsta högsignalmängd som ger full täckning för just sitt jobb. Transkriptet hämtas i
riktade intervall — det dumpas aldrig.

## Struktur

- `<slug>/idea-<slug>.md` — briefen: beslut (inkl. förkastade vägar) med proveniens
  `(← msg N)`, EARS-acceptanskriterier, öppna frågor. Det agenten planerar och bygger
  från — den enda intake-fil en byggsession laddar som standard.
- `<slug>/<slug>-design-rationale.md` — designrationalen: resonemangskedjor, förkastanden
  med vilket haveri de skulle skapa, avvägningar, hämtkarta (ämne → meddelandeintervall).
  Läses på begäran när designlogik behövs; aldrig förladdad. (Idéer fångade före
  trekontraktet saknar den — det flaggar backfill, inte fel.)
- `<slug>/<slug>-full-chat.md` — det ordagranna transkriptet, fail-closed-verifierat och
  orörligt efter verifierad capture. Riktade meddelandeintervall hämtas via subagent när
  rationalen inte räcker eller exakt formulering spelar roll; aldrig förladdat.
- `<slug>/<slug>-approved-plan.md` — den godkända planen: exakt den plan ägaren godkände
  i Plan Mode, i sin helhet (exekveringsordning, avgränsningar, beslut, uppskjutet,
  förkastat, ägaröverlämningar, stoppvillkor, acceptanskriterier, nuvarande/nästa
  skiva, precedensplåster). Skapas **aldrig** före godkännandet och aldrig ur briefen.
  Version N≥2 heter `<slug>-approved-plan-v<N>.md`. Läses tillsammans med briefen i en
  exekveringssession.
- `<slug>/<slug>-context-manifest.json` — källkartan: varje källa som tänkandet vilar på
  får ett stabilt `SRC-*`-id, en sha256 och en `capture_status`
  (`captured` / `not_load_bearing` / `unavailable_owner_acknowledged` / `pending`).
  Här står också `execution_targets` med roller. Innehåll dupliceras aldrig — kartan gör
  källmängden **hittbar och kontrollerbar**, inte förladdad. Aldrig hemligheter.
- `<slug>/<slug>-owner-clarifications.md` — ägardeltan: exakt fråga, exakt ägarsvar,
  datum, vilket `Q` det löser och vilka `D`/`R`/`AC` det påverkar, med `CLAR-*`-id.
  **Append-only** — ett registrerat svar redigeras aldrig, och transkriptet skrivs aldrig
  om för att matcha det. Finns bara när ägaren faktiskt svarat.
- `<slug>/<slug>-plan-candidate.md` — planförslaget: det Plan Mode producerade och det
  ägaren faktiskt läser. Behålls orört efter godkännandet som kvitto.
- `INDEX.md` — en rad per idé (aldrig per fil): `slug | title | status | created | links`.
  Upsertas vid varje leverans och statusbyte. Börja där för att se vad som finns.
  Planfilen får **ingen egen rad** — indexet är inte en filförteckning.
- Idémappen ligger **direkt i repo-roten** (`<slug>/`, inte `ideas/<slug>/`).

## Progressiv exponering & auktoritet

Läsordning efter roll: implementerare → briefen (+ den godkända planen när en sådan
finns); arkitekt/planerare/granskare → briefen, + rationalen när den gör materiell nytta;
exakt proveniens → riktade transkriptintervall, inget mer. Auktoritetsordning (högst
vinner): gällande kanonisk repo-auktoritet (konstitution, regelverk, godkänd arkitektur) →
senare ägargodkänd spec/arkitektur/plan → godkänd intake-plan → ägarklargöranden → brief →
rationale → transkript. Inom ett intake-paket tolkas godkänd plan > ägarklargöranden >
brief > rationale > transkript: ett senare ägarsvar väger tyngre än den brief det rättar.
Intake bevarar intention och proveniens — det är aldrig exekveringsauktoritet.

Den godkända planen är den starkaste intake-artefakten och ändå inte auktoritet: den kör
aldrig över konstitutionen, regelverket, frusna grindar, gällande publicerad
produktionssanning eller en senare ägargodkänd övergång. Den är inte en andra runtime,
inte en andra sanningskälla och inget exekveringstillståndsregister. Går plan och
gällande repo-sanning isär vinner repot och avvikelsen rapporteras till ägaren — den
löses aldrig tyst till planens fördel.

## Konventioner

- Statuslivscykel i briefens frontmatter: `idea → clarified → planned → building →
  verified`; terminal: `superseded`. (`ready-for-clarification` i äldre briefer är det
  gamla namnet på `idea`.) `idea` = ligger i banken med öppna frågor intakta; `clarified`
  = ägarintervjun är gjord och idén är redo att planeras.
- Korslänkar i frontmatter, satta av korpus-kollen (Phase 2.8 i skillen):
  `supersedes: [slug]`, `superseded_by: <slug>` (på den gamla briefen, tillsammans med
  `status: superseded`), `related: [slug, …]`. Aldrig tysta dubbletter — vid trolig
  dubblett/evolution frågas ägaren.
- En idé dras till bygge via skillens implementera-nu-flöde, startat från den lagrade
  briefen: korpus-omkoll → Phase 2.5-intervju (öppna frågor) → `status: clarified` →
  plan mode → **ägaren godkänner planen** → planen sparas, valideras och binds →
  `status: planned` → bygg i färsk session → adversariell granskning.

## `planned` är ett mekaniskt tillstånd

`status: planned | building | verified` är giltigt **endast** när briefen är bunden till
en giltig godkänd plan: filen finns, dess sha256 matchar `approved_plan_sha256`, den bär
rätt slug och ägargodkännandemetadata, och den är den aktuella (ej ersatta) versionen.
Saknas det får statusen inte gå förbi `clarified`. Det är inte en regel på papperet —
den valideras:

```bash
python3 ~/.claude/skills/nortropic-intake/scripts/plan_contract.py validate
```

Samma kontroll finns som commit-grind i `hooks/pre-commit`, så att ett obevisbart
tillstånd inte når git-historiken. Git spårar inte `.git/hooks`, så installationen är ett
steg per klon (och `--no-verify` är ägarens uttryckliga val, aldrig ett default):

```bash
chmod +x hooks/pre-commit
ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
```

Grinden är en grind, inte en mur: `--no-verify` går förbi den, och den släpper igenom om
skillen inte är installerad på maskinen — båda är ägarens uttryckliga val. Den upptäcker
tillståndet men kan inte tvinga fram att Phase 4 körs alls, och kan inte bevisa att
planens text är trogen det ägaren godkände. Det första är skillens instruktion, det andra
är disciplin.

Bindningen står i briefens frontmatter (`approved_plan`, `approved_plan_sha256`,
`plan_version`, `plan_approved_at`). Briefen **pekar** på planen — den kopierar den
aldrig. En kort exekveringsprompt är inte planen; den får peka på planen, aldrig ersätta
den.

Planen skrivs aldrig om tyst efter godkännande. Vid medvetet omtag: den gamla filen
behålls med `status: superseded` + `superseded_by_plan`, den nya får
`supersedes_plan` + nästa `plan_version`, och briefens pekare flyttas medvetet.

**Saknad plan på `planned`/`building`** rapporteras som `LEGACY_PLAN_ARTIFACT_MISSING`
och är ett fel, inte en varning. Enda tillåtna vägen tillbaka är avgränsad och manuell:
ägaren pekar ut den kända källan, planen sparas med
`plan_source: recovered-from-known-source` och `fidelity: partial`, ägaren verifierar,
sedan binds den. Transkriptet skrapas aldrig automatiskt, och en modellrekonstruktion
godtas aldrig som plan. Finns ingen känd källa är det ärliga utfallet `status: clarified`
och en ny planering.

## Innan Plan Mode: täckningsgrinden

En brainstorm kan vara månader gammal. Innan planering får börja körs:

```bash
python3 ~/.claude/skills/nortropic-intake/scripts/context_contract.py \
    coverage --slug <slug> --target-repo <path> [--target-repo <path> …]
```

Den skriver `PLANNING_CONTEXT_COMPLETE=YES|NO` med **räknade tal, aldrig ett betyg**, och
kräver: källtaggar på varje beslut, förkastande och acceptanskriterium; en disposition för
varje öppen fråga (besvarad / uppskjuten / medvetet öppen — annars BLOCKING); giltiga
klargöranden; varje bärande källa `captured` eller uttryckligen ägarkvitterad som
otillgänglig; paketet inte ersatt; och att varje deklarerat målrepo faktiskt har
inspekterats.

Planering är `INTENTION + NULÄGE → PLAN`, aldrig `GAMMAL BRAINSTORM → PLAN`. Krockar
gällande auktoritet med intake-intentionen lyfts konflikten till ägaren — den gamla idén
vinner aldrig tyst. Vid `NO` börjar inte Plan Mode: fyll luckan, eller registrera ett
uttryckligt ägarbeslut. Gissa aldrig vad den saknade källan sannolikt sa.

## Ägaren godkänner exakta bytes

Planen finns i två filer med flit: kandidaten som ägaren läser, och den godkända planen
vars **kropp är kopierad byte för byte** ur kandidaten. Identiteten är sha256 över
kroppen (allt efter frontmatter), så metadata får skilja sig men innehållet inte:

```bash
python3 …/plan_contract.py coherence --slug <slug>     # deltat ägaren läser
python3 …/plan_contract.py approve   --slug <slug> --candidate-sha <sha> …
```

`approve` vägrar om den godkända sha:n inte är kandidaten på disk. Kandidaten muteras
aldrig efteråt — den är kvittot på vad som stod på skärmen. Coherence-rapporten visar
deltat (nya planbeslut, scope-utvidgningar, tappade krav, återupplivade förkastanden)
**före** godkännandet; materiella ändringar begravs aldrig i planens brödtext.

## Flera arbetsströmmar mot samma repo

Pekarblock är nycklade på `workstream=<NAMN> slug=<slug>`, så Webbförvaltningen,
Bootstrap och en orelaterad förbättring kan peka mot samma repo utan att skriva över
varandra. En session måste lösa ut **sin** arbetsström innan den använder någon pekare;
går det inte rapporteras `POINTER_AMBIGUOUS` och ingen används. Det finns ingen
repo-global "nästa uppgift" — bara en nästa skiva inom en namngiven arbetsström.

## `building` och `verified` är observationer

De kräver evidens i briefen: `execution_repo`, `execution_commit`, `execution_slice`, och
för `verified` dessutom `verification_evidence`. Korpuskontrollen granskar formen (skivan
måste finnas i den godkända planen); `resume` bevisar commiten mot det verkliga repot.
**En `verified`-etikett blir inte sann av att det finns en giltig plan.** Säger repot emot
etiketten skrivs `EXECUTION_STATE_CONTRADICTED=YES` — repot vinner, och briefen rättas.

## Efter komprimering och i en färsk session

Den varaktiga planen ligger på disk; minnet behöver bara hitta tillbaka till den.
En återupptagande session — efter `/compact`, automatisk komprimering, eller helt ny —
kör:

```bash
python3 ~/.claude/skills/nortropic-intake/scripts/plan_contract.py resume \
    --slug <slug> --workstream <NAMN> --target-repo <repo> [--pointer <repo>/CLAUDE.md]
```

och får hela paketets identitet — brief, rationale, manifest, klargöranden, plan,
godkännandekvitto — plus repo-evidens för varje mål och en ordnad laddningsplan
(minst först; rationale och transkript förblir on-demand). För en lång plan ger
`map --slug <slug>` skiv-id och radintervall, så en liten skiva inte kräver hundra sidor. **Läs sedan om den godkända planen från disk innan du härleder framtida
arbete**, och stäm av den mot repots faktiska tillstånd. Rekonstruera aldrig en saknad
plan ur samtalsminne, ur ett utkast eller ur transkriptet; kan planen eller dess
registrerade identitet inte bevisas: STOPPA med `PLAN_IDENTITY_UNAVAILABLE`.

En eventuell pekare i målrepots `CLAUDE.md` (`ACTIVE_INTAKE_SLUG`,
`ACTIVE_APPROVED_PLAN_PATH`, `ACTIVE_APPROVED_PLAN_SHA256`, `TARGET_REPO`,
`CURRENT_EXECUTION_POINTER`) är en **cache, inte tillstånd**. Nuvarande position räknas
om genom att jämföra planen med repots tillstånd. Krockar pekaren med repo-evidens vinner
repot och avvikelsen rapporteras.

## Trust-lagret (invarianter)

Det ingen brief får bryta ägs av konstitutionen och regelverket:
`~/nortropic/nortropic-system/docs/07-konstitution.md` och
`~/nortropic/nortropic-system/docs/03-regelverk.md` — trust-kontrakt, frusna grindar,
§-regler. Briefer **pekar** dit (en rad i §2 och §6); de kopierar aldrig innehållet.

## Vad som INTE händer här

Skillen skriver filer och indexrader — den committar inte, pushar inte och laddar inte
upp till Drive. Git-historik är Johnnys explicita beslut.
