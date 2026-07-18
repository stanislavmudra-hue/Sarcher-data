#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Automatická aktualizace průměrných cen paliv v live.json.

Spouští ji GitHub Actions (viz .github/workflows/update-fuel.yml) každou
středu. Zdroj: otevřená data ČSÚ, sada CENPHMT (týdenní průměrné
spotřebitelské ceny pohonných hmot v ČR).
"""
import csv
import io
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

LIVE = Path(__file__).resolve().parent / "live.json"
CSV_URL = "https://data.csu.gov.cz/opendata/sady/CENPHMT/distribuce/csv"

FUELS = {
    "Natural 95": "natural95",
    "nafta": "diesel",
    "LPG": "lpg",
}


def main() -> int:
    live = json.loads(LIVE.read_text(encoding="utf-8"))

    req = urllib.request.Request(
        CSV_URL, headers={"User-Agent": "OkolnikDataBot/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read().decode("utf-8")

    rows = list(csv.DictReader(io.StringIO(data)))
    prices = [r for r in rows if r.get("IndicatorType") == "6621T"]
    if not prices:
        print("CSV nemá očekávanou strukturu – končím bez změny.")
        return 1

    latest = max(r["CASTPHM"] for r in prices)  # např. "2026-W29"
    fuel = {}
    for r in prices:
        if r["CASTPHM"] != latest:
            continue
        for pattern, key in FUELS.items():
            if pattern.lower() in r["Druh PHM"].lower():
                try:
                    fuel[key] = float(r["Hodnota"])
                except ValueError:
                    pass

    week_num = latest.split("-W")[-1].lstrip("0")
    year = latest.split("-W")[0]
    live["fuel"] = {
        "week": f"{week_num}. týden {year}",
        "natural95": fuel.get("natural95"),
        "diesel": fuel.get("diesel"),
        "lpg": fuel.get("lpg"),
        "source": "ČSÚ",
    }
    live["updated"] = date.today().isoformat()

    LIVE.write_text(
        json.dumps(live, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    print(f"Aktualizováno: {live['fuel']['week']} – "
          f"N95 {fuel.get('natural95')} / nafta {fuel.get('diesel')} / "
          f"LPG {fuel.get('lpg')} Kč/l")
    return 0


if __name__ == "__main__":
    sys.exit(main())
