# Nortropic innovation-intake — idékorpusen

Detta repo är korpusen/idébanken som skillen `nortropic-intake`
(`~/.claude/skills/nortropic-intake/`) levererar till. Varje idé är en låda med två
papper: byggritningen (briefen) och dagboken (transkriptet). Briefen styr, dagboken
förklarar — **vid konflikt vinner alltid briefen**.

## Struktur

- `<slug>/idea-<slug>.md` — briefen: beslut (inkl. förkastade vägar) med proveniens
  `(← msg N)`, EARS-acceptanskriterier, öppna frågor. Det agenten planerar och bygger från.
- `<slug>/<slug>-full-chat.md` — det ordagranna transkriptet, fail-closed-verifierat.
  Läses på begäran via subagent när rationale behövs; aldrig förladdat.
- `INDEX.md` — en rad per idé: `slug | title | status | created | links`. Upsertas vid
  varje leverans och statusbyte. Börja där för att se vad som finns.
- Idémappen ligger **direkt i repo-roten** (`<slug>/`, inte `ideas/<slug>/`).

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
  plan mode → bygg i färsk session → adversariell granskning.

## Trust-lagret (invarianter)

Det ingen brief får bryta ägs av konstitutionen och regelverket:
`~/nortropic/nortropic-system/docs/07-konstitution.md` och
`~/nortropic/nortropic-system/docs/03-regelverk.md` — trust-kontrakt, frusna grindar,
§-regler. Briefer **pekar** dit (en rad i §2 och §6); de kopierar aldrig innehållet.

## Vad som INTE händer här

Skillen skriver filer och indexrader — den committar inte, pushar inte och laddar inte
upp till Drive. Git-historik är Johnnys explicita beslut.
