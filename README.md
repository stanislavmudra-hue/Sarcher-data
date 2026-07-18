# Sarcher â€“ datovĂ˝ kanĂˇl

Tento repozitĂˇĹ™ slouĹľĂ­ jako **datovĂ˝ kanĂˇl aplikace Okolník** (vyhledĂˇvaÄŤ mĂ­st v okolĂ­).

Aplikace si pĹ™i kaĹľdĂ©m spuĹˇtÄ›nĂ­ stĂˇhne soubor [`live.json`](live.json) a pouĹľije z nÄ›j:

- **`fuel`** â€“ prĹŻmÄ›rnĂ© ceny pohonnĂ˝ch hmot v ÄŚR (tĂ˝dennĂ­ data ÄŚSĂš, otevĹ™enĂˇ datovĂˇ sada CENPHMT)
- **`leaflets`** â€“ adresy akÄŤnĂ­ch letĂˇkĹŻ obchodnĂ­ch Ĺ™etÄ›zcĹŻ (tlaÄŤĂ­tko â€žAkÄŤnĂ­ letĂˇk" v detailu obchodu)

DĂ­ky tomu lze ceny a odkazy **aktualizovat bez vydĂˇvĂˇnĂ­ novĂ© verze aplikace** â€“
staÄŤĂ­ zmÄ›nit `live.json` v tomto repozitĂˇĹ™i. KdyĹľ soubor nenĂ­ dostupnĂ˝
(offline, vĂ˝padek), aplikace pouĹľije data pĹ™ibalenĂˇ v instalaci.

## Jak aktualizovat

Na poÄŤĂ­taÄŤi s projektem Sarcher spusĹĄte:

```powershell
powershell -ExecutionPolicy Bypass -File C:\AI\Sarcher\tools\update_prices.ps1
```

Skript stĂˇhne ÄŤerstvĂ© ceny z ÄŚSĂš a zmÄ›nu sem automaticky nahraje (commit + push).
PĹ™Ă­padnÄ› lze `live.json` upravit ruÄŤnÄ› pĹ™Ă­mo na GitHubu (tuĹľka â€žEdit" â†’ Commit changes).

