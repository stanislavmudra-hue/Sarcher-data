# Okolník – datový kanál

Tento repozitář slouží jako **datový kanál aplikace Okolník**
(vyhledávač míst v okolí, dříve pracovní název Sarcher).

Aplikace si při každém spuštění stáhne soubor [`live.json`](live.json)
a použije z něj:

- **`fuel`** – průměrné ceny pohonných hmot v ČR (týdenní data ČSÚ,
  otevřená datová sada CENPHMT)
- **`leaflets`** – adresy akčních letáků obchodních řetězců
  (tlačítko „Akční leták" v detailu obchodu)

Díky tomu lze ceny a odkazy **aktualizovat bez vydávání nové verze
aplikace** – stačí změnit `live.json` v tomto repozitáři. Když soubor
není dostupný (offline, výpadek), aplikace použije data přibalená
v instalaci.

## Jak aktualizovat

Na počítači s projektem spusťte:

```powershell
powershell -ExecutionPolicy Bypass -File C:\AI\Sarcher\tools\update_prices.ps1
```

Skript stáhne čerstvé ceny z ČSÚ a změnu sem automaticky nahraje
(commit + push). Případně lze `live.json` upravit ručně přímo na GitHubu
(tužka „Edit" → Commit changes).
