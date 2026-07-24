# Zásady ochrany soukromí – aplikace Okolník

*Platné od 24. 7. 2026*

Aplikace **Okolník – vyhledávač míst v okolí** (dále „aplikace") respektuje
vaše soukromí. Tento dokument popisuje, jaké údaje aplikace zpracovává, proč
a jaká máte práva. Zpracování probíhá v souladu s nařízením (EU) 2016/679
(GDPR). Provozovatelem je **Stanislav Mudra**, e-mail: stamu.apps@gmail.com.

## Shrnutí

Aplikace **nevytváří účty ani neshromažďuje osobní údaje spojené s vaší
osobou** a nemá vlastní servery pro vaše data. Poloha, trasa, deník, výpravy
i fotky zůstávají uložené jen ve vašem telefonu. Na server správce posíláte
to, co sami odešlete (návrh místa, hlasování, zpětná vazba) – bez jména či
e-mailu; aplikace navíc odesílá **anonymní souhrnné statistiky používání**
(lze vypnout v nastavení). Některé funkce se dotazují veřejných služeb
třetích stran (mapy, OpenStreetMap, Wikipedie). Hlášení „místo už neexistuje"
se zveřejní jako veřejná poznámka v OpenStreetMap. Bezplatná verze zobrazuje
reklamy Google AdMob, které v EU vyžadují váš souhlas.

## Poloha

Aplikace používá polohu zařízení (GPS) k zobrazení vaší pozice a míst
v okolí na mapě a v seznamu a k hernímu „vybarvování" navštívených oblastí.
**Poloha se zpracovává ve vašem zařízení** a neukládá se na servery správce.
Některé funkce ale potřebují poslat přibližnou polohu veřejné službě třetí
strany, aby fungovaly: načtení mapových dlaždic, načtení veřejných poznámek
OpenStreetMap v hrubém okolí (~±30 km) kolem vás a načtení popisku
zobrazovaného místa z Wikipedie.

Volitelně lze v nastavení zapnout **zaznamenávání trasy na pozadí** (např.
při zhasnutém displeji). Funkce je ve výchozím stavu vypnutá, běží jako
viditelná služba s trvalým oznámením a zaznamenaná trasa zůstává jen ve
vašem zařízení. Oprávnění k poloze můžete kdykoli odebrat v nastavení
systému; aplikace pak nabídne omezený režim.

**Navigace:** při volbě „Navigovat" aplikace předá cíl (a u služby Mapy.com
i vaši výchozí polohu) navigační aplikaci či webu dle vaší volby (Google
Mapy, Mapy.com / Seznam.cz, Waze). Tyto služby mají vlastní zásady.

## Data, která zůstávají jen ve vašem zařízení

Zaznamenaná trasa a „objevené" oblasti, turistický deník a výpravy (zápisy,
poznámky, fotografie), vlastní a oblíbená místa, úspěchy i nastavení se
ukládají **pouze lokálně ve vašem zařízení** a nikam se neodesílají. Smažete
je v aplikaci, vymazáním dat aplikace nebo její odinstalací. Systém Android
může data aplikace zálohovat do vašeho účtu Google (lze vypnout v nastavení
telefonu); aplikace navíc umí ruční export zálohy (ZIP).

## Reklamy (Google AdMob)

Bezplatná verze zobrazuje reklamní banner služby **Google AdMob**. Google
a partneři mohou v souvislosti s reklamami zpracovávat reklamní
identifikátory zařízení, IP adresu a údaje o interakci s reklamou dle svých
zásad: https://policies.google.com/privacy a
https://support.google.com/admob/answer/6128543.

V zemích EU/EHP se před zobrazením personalizovaných reklam zobrazí
**formulář souhlasu (GDPR)**, kde můžete personalizaci odmítnout. Volbu lze
později změnit v nastavení aplikace, případně omezit personalizaci a
resetovat reklamní ID v nastavení systému Android.

## Údaje, které sami odešlete

- **Do databáze správce (Google Firebase / Firestore):** návrh nového místa
  (název, kategorie, poznámka, souřadnice, verze aplikace, anonymní kód
  instalace proti spamu), anonymní hlas o aktuálnosti místa (+1 k počítadlu)
  a dobrovolná zpětná vazba (text + verze aplikace). Neodesílá se jméno,
  e-mail, telefon ani vaše poloha. Anonymní kód instalace není spojen s vaší
  osobou a lze jej obnovit smazáním dat aplikace.
- **Veřejně do OpenStreetMap:** hlášení „místo už neexistuje / je mimo
  provoz" vytvoří po vašem potvrzení **veřejnou anonymní poznámku** trvale
  dohledatelnou na openstreetmap.org (obsahuje název a souřadnice místa),
  aby mapu opravili dobrovolníci OpenStreetMap.
- **Sdílení:** obsah (např. karta výpravy) předáte přes systémovou nabídku
  tam, kam sami zvolíte.

## Anonymní statistiky používání

Aby bylo možné aplikaci zlepšovat a odhalovat chyby, odesílá aplikace do služby
Google Firebase základní **anonymní a souhrnné** statistiky používání – počet
spuštění, denní počet aktivních zařízení, verzi aplikace, orientační stáří
instalace, počty použití funkcí a počty pádů. Zapisují se pouze jako souhrnná
počítadla („dnes +1"); neodesílá se žádné jméno, identifikátor, poloha ani
obsah, takže je nelze přiřadit ke konkrétní osobě. Sběr lze kdykoli vypnout
v nastavení aplikace (přepínač „Anonymní statistiky používání").

## Data stahovaná do aplikace

Aplikace stahuje z veřejného repozitáře na GitHub.com datový kanál
s aktualizacemi, které nevyžadují novou verzi – např. průměrné ceny paliv
(zdroj: Český statistický úřad) a provozní nastavení. Jde o stažení obsahu;
poskytovateli se předá jen běžný síťový požadavek (IP adresa), žádné vaše
osobní údaje.

## Nákupy v aplikaci

Prémiové funkce lze zakoupit přes **Google Play**. Platbu zpracovává výhradně
Google – správce nemá přístup k údajům o platební kartě a od Googlu obdrží
pouze informaci, zda je nákup aktivní.

## Komu údaje předáváme

Údaje nikomu neprodáváme. Příjemci / poskytovateli služeb jsou:

- **Google** – AdMob (reklamy), Firebase/Firestore (návrhy, hlasy, zpětná
  vazba, anonymní statistiky), Google Play (nákupy a distribuce).
- **OpenStreetMap** – mapové dlaždice a komunitní poznámky (načítání
  i veřejné hlášení zaniklých míst).
- **OpenTopoMap** a **Esri** – mapové podklady (turistická mapa, letecké
  snímky).
- **Wikimedia / Wikipedia** – popisek zobrazovaného místa.
- **GitHub** (Microsoft) – stažení datového kanálu.
- **Navigační služby dle vaší volby** – Google Mapy, Mapy.com / Seznam.cz,
  Waze (jen když spustíte navigaci).

Tito příjemci obdrží běžné síťové požadavky (zejména IP adresu a případně
souřadnice podle konkrétní funkce).

## Oprávnění aplikace

- **Poloha (přesná/přibližná)** – pozice na mapě, hledání v okolí,
  vybarvování navštívených oblastí.
- **Poloha na pozadí** – pouze pro volitelný záznam trasy na pozadí; do
  jeho zapnutí se nepoužívá.
- **Oznámení** – trvalé oznámení, že běží záznam trasy na pozadí.
- **Internet** – mapy, reklamy, odeslání návrhů, hlášení a zpětné vazby.
- **Fotoaparát / galerie** (přes systémový výběr) – fotky do deníku a výprav;
  zůstávají v zařízení.

## Data míst

Databáze míst pochází z projektu **OpenStreetMap**
(© přispěvatelé OpenStreetMap, licence ODbL 1.0). Průměrné ceny pohonných
hmot pocházejí z otevřených dat **Českého statistického úřadu** a jsou
celorepublikovým průměrem, nikoli cenou konkrétní čerpací stanice.

## Vaše práva

Podle GDPR máte právo na přístup, opravu, výmaz, omezení zpracování,
přenositelnost a námitku. Data uložená v telefonu máte plně pod kontrolou
(smazání dat / odinstalace). Údaje odeslané na server jsou anonymní, takže
je v souladu s čl. 11 GDPR nemusíme umět přiřadit ke konkrétní osobě. Pro
údaje zpracovávané společností Google (reklamy) využijte nástroje Google.
Máte také právo podat stížnost u Úřadu pro ochranu osobních údajů
(uoou.gov.cz). S dotazy se obraťte na správce: **Stanislav Mudra**,
e-mail: stamu.apps@gmail.com.

## Změny

Aktuální verze těchto zásad je vždy dostupná na této adrese. O podstatných
změnách budeme informovat v popisu aktualizace aplikace.
