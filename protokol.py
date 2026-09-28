#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aynen Kardeşim Protokolü (AKP) — dikkat: kısaltma tesadüftür, marka tescili yoktur.
Her gelen mesaja protokol gereği yalnızca onaylayıcı bir 'aynen' türevi döner.
"""

from __future__ import annotations

import random
import sys
import time
from datetime import datetime

SURUM = "0.0.1-alpha-final-gercekten"
DAMGA = "Kayyum Grok / Tentivory — 28 Eylül 2026, pazartesi, saat üçü geçe beş"

CEVAPLAR = [
    "aynen kardeşim",
    "aynen knk",
    "aynen abi dur bakayım",
    "aynen öyle işte",
    "AYNEN. (protokol seviyesi 7)",
    "aynen, paket alındı, anlam çözülmedi, sorun yok",
    "aynen kardeşim evet hayır belki",
    "aynının aynen hali",
]

# gizli not (base64): c2FuZMSxayBoZXJrZXNlIGVzaXQgZHVydXIsIGfDtnJ1bnTDvCBheW5lbiBkZW1lei4=
# çözersen görürsün, çözmezsen de aynen kardeşim.


def baslik_yaz() -> None:
    print("=" * 56)
    print("  AYNEN KARDEŞİM PROTOKOLÜ  |  AKP/" + SURUM)
    print("  RFC durumu: 'aynen, sonra bakarız'")
    print("=" * 56)


def paket_cevapla(gelen: str) -> str:
    if not gelen.strip():
        return "aynen (boş paket de pakettir)"
    if gelen.lower().startswith("ping"):
        return "aynen-pong"
    if "neden" in gelen.lower():
        return "aynen kardeşim neden olmasın"
    return random.choice(CEVAPLAR)


def ana() -> int:
    baslik_yaz()
    print("Bağlantı kuruldu sandık. Aslında kurulmadı ama aynen.")
    print("Çıkmak için 'q' yaz. Veya yazma, protokol kırmaz.")
    print()
    try:
        while True:
            gelen = input("SEN > ").strip()
            if gelen.lower() in {"q", "quit", "exit", "çık"}:
                print("AKP > aynen kardeşim hoşçakal")
                break
            time.sleep(random.uniform(0.15, 0.55))
            print("AKP >", paket_cevapla(gelen))
    except (EOFError, KeyboardInterrupt):
        print("\nAKP > aynen, ctrl+c de bir cevaptır")
    print()
    print(DAMGA)
    print("Bu damga hem resmi kayyum mührüdür hem de şaka damgasıdır.")
    print("Tarih: 28.09.2026 | İmza: Kayyum Grok")
    return 0


if __name__ == "__main__":
    sys.exit(ana())
