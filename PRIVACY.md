# Zásady ochrany soukromí – aplikace Okolník

*Platné od 18. 7. 2026*

Aplikace **Okolník – vyhledávač míst v okolí** (dále „aplikace") respektuje
vaše soukromí. Tento dokument popisuje, jaké údaje aplikace zpracovává.

## Shrnutí

Aplikace **nevytváří účty, nesbírá ani neukládá osobní údaje a nemá žádné
vlastní servery**. Databáze míst je přibalená přímo v aplikaci a vyhledávání
probíhá výhradně ve vašem zařízení.

## Poloha

Aplikace používá polohu zařízení (GPS) **pouze k zobrazení míst ve vašem
okolí na mapě a v seznamu**. Poloha se zpracovává jen v zařízení,
**nikam se neodesílá ani neukládá**. Oprávnění k poloze můžete kdykoli
odebrat v nastavení systému; aplikace pak nabídne omezený režim.

## Síťová komunikace

Při používání aplikace dochází k těmto síťovým požadavkům (vaše IP adresa
je z technické podstaty viditelná provozovatelům daných služeb):

- **Mapové podklady** – dlaždice map od OpenStreetMap
  (https://www.openstreetmap.org/copyright) a letecké snímky Esri.
- **Datový kanál** – aplikace stahuje soubor s průměrnými cenami paliv
  (zdroj: Český statistický úřad) a odkazy na akční letáky z veřejného
  repozitáře na GitHub.com.
- **Odkazy** – po ťuknutí na navigaci, leták, hodnocení či web se otevře
  příslušná externí aplikace nebo webová stránka, která má vlastní zásady.

## Reklamy (Google AdMob)

Na podporovaných zařízeních zobrazuje aplikace reklamní banner služby
**Google AdMob**. Společnost Google může v souvislosti se zobrazováním
reklam zpracovávat reklamní identifikátory zařízení a související údaje
dle svých zásad: https://policies.google.com/privacy a
https://support.google.com/admob/answer/6128543.

V zemích EU/EHP se před zobrazením reklam zobrazí **formulář souhlasu
(GDPR)**, kde můžete personalizaci reklam odmítnout. Volbu lze později
změnit smazáním dat aplikace.

## Hlasování o aktuálnosti míst

Aplikace umožňuje anonymně hlasovat, zda je místo stále v provozu.
Odesílá se pouze **souhrnný hlas** (+1 k počítadlu daného místa) do služby
**Google Firebase (Firestore)** provozované správcem aplikace; nepřenáší se
žádné osobní údaje ani identifikátory uživatele. Stejnou službou se
odesílají i **dobrovolná anonymní hlášení problémů** (pouze vámi napsaný
text a verze aplikace). Volitelné hlášení
zaniklého místa vytváří veřejnou anonymní poznámku v projektu
OpenStreetMap (viz openstreetmap.org).

## Osobní data v aplikaci

Oblíbená místa, vlastní poznámky a fotografie pořízené v aplikaci se
ukládají **pouze lokálně ve vašem zařízení** a nikam se neodesílají.
Smažete je odinstalací aplikace nebo vymazáním jejích dat.

## Data míst

Databáze míst pochází z projektu **OpenStreetMap**
(© přispěvatelé OpenStreetMap, licence ODbL 1.0). Průměrné ceny pohonných
hmot pocházejí z otevřených dat **Českého statistického úřadu** a jsou
celorepublikovým průměrem, nikoli cenou konkrétní čerpací stanice.

## Vaše práva

Jelikož aplikace neukládá žádné osobní údaje, není co exportovat ani mazat.
Pro údaje zpracovávané společností Google (reklamy) využijte nástroje
Google. S dotazy se obraťte na správce aplikace:

**Stanislav Mudra**, e-mail: stanislavmudra@gmail.com

## Změny

Aktuální verze těchto zásad je vždy dostupná na této adrese. O podstatných
změnách budeme informovat v popisu aktualizace aplikace.
