#!/usr/bin/env python3
"""Kontrola změn menu na menicka.cz (běží v GitHub Actions, bez Clauda).

Stáhne stránky restaurací, vytáhne dnešní jídla a porovná je s minulou kontrolou
(soubor stav-menu.json). Když se něco změnilo, zapíše zprávu do souboru zprava.md,
ze které workflow udělá upozornění (push přes úlohu „Obědy upozornění“). Nic dalšího nespouští.
"""
import datetime, html, json, os, re, sys, urllib.request
from zoneinfo import ZoneInfo

RESTAURACE = [
    ("Prostě Restaurace", "https://www.menicka.cz/8250-proste-restaurace.html"),
    ("Pilsner Urquell Original Restaurant", "https://www.menicka.cz/2992-pilsner-urquell-original-restaurant.html"),
    ("Restaurace Flip (Bernard Pub)", "https://www.menicka.cz/24-restaurace-flip-bernard-pub.html"),
    ("Budvarka Zlín", "https://www.menicka.cz/5881-budvarka-zlin.html"),
    ("U Ševce", "https://www.menicka.cz/5492-u-sevce.html"),
    ("Radegastovna Rex", "https://www.menicka.cz/3538-radegastovna-rex.html"),
    ("U Barcuchů (jídelna)", "https://www.menicka.cz/3027-u-barcuchu.html"),
]
STAV = "stav-menu.json"
ZPRAVA = "zprava.md"


def cisty(s):
    s = re.sub(r"<em[^>]*>.*?</em>", " ", s, flags=re.S)  # alergeny
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def dnesni_jidla(stranka, dnes):
    """Seznam „jídlo – cena“ z bloku s dnešním datem, None když blok chybí."""
    hledany = f"{dnes.day}.{dnes.month}.{dnes.year}"
    for blok in re.split(r"<div class='menicka'>", stranka)[1:]:
        m = re.search(r"<div class='nadpis'>(.*?)</div>", blok, re.S)
        if not m or hledany not in cisty(m.group(1)).split():
            continue
        jidla = []
        for li in re.findall(r"<li class='(?:polevka|jidlo)'>(.*?)</li>", blok, re.S):
            p = re.search(r"<div class='polozka'>(.*?)</div>", li, re.S)
            c = re.search(r"<div class='cena'>(.*?)</div>", li, re.S)
            if p:
                nazev = cisty(p.group(1))
                jidla.append(nazev + (" – " + cisty(c.group(1)) if c else ""))
        return jidla
    return None


def prazdne_v_tabulce(dnes):
    """Restaurace, které v dnešní tabulce (index.html) nemají žádné jídlo."""
    try:
        t = open("index.html", encoding="utf-8").read()
    except OSError:
        return set()
    i = t.find(f'datum:"{dnes.isoformat()}"')
    if i < 0:
        return None  # tabulka pro dnešek ještě není
    j = t.find("{datum:", i + 10)
    den = t[i:j if j > 0 else len(t)]
    return {url for _, url in RESTAURACE
            if re.search(re.escape(url) + r'"\s*,\s*"(?:[^"\\]|\\.)*"\s*,\s*\[\s*\]', den)}


def main():
    dnes = datetime.datetime.now(ZoneInfo("Europe/Prague")).date()
    try:
        stav = json.load(open(STAV, encoding="utf-8"))
    except (OSError, ValueError):
        stav = {}
    puvodni = stav.get("menu", {}) if stav.get("datum") == dnes.isoformat() else None

    nove, chyby = {}, []
    for nazev, url in RESTAURACE:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (kontrola obedu)"})
            stranka = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
            nove[url] = dnesni_jidla(stranka, dnes)
        except Exception as e:  # stránku teď nejde načíst, příště to zkusíme znovu
            chyby.append(f"{nazev}: {e}")
            if puvodni and url in puvodni:
                nove[url] = puvodni[url]

    zmeny = []
    if puvodni is None:
        # první kontrola dne: upozorni jen na restaurace, které v tabulce nemají menu, ale teď ho mají
        prazdne = prazdne_v_tabulce(dnes) or set()
        for nazev, url in RESTAURACE:
            if url in prazdne and nove.get(url):
                zmeny.append(f"**{nazev}** – v tabulce menu nemá, ale na menicka.cz už je.")
    else:
        for nazev, url in RESTAURACE:
            if url not in nove:
                continue
            a, b = puvodni.get(url) or [], nove[url] or []
            if a == b:
                continue
            pribylo = [x for x in b if x not in a]
            ubylo = [x for x in a if x not in b]
            radky = [f"**{nazev}**" + (" – menu se objevilo" if not a else " – menu zmizelo" if not b else "")]
            radky += [f"- ➕ {x}" for x in pribylo] if a else []
            radky += [f"- ➖ {x}" for x in ubylo] if b else []
            if a and b and not pribylo and not ubylo:
                radky.append("- změnilo se pořadí jídel")
            zmeny.append("\n".join(radky))

    json.dump({"datum": dnes.isoformat(), "menu": nove}, open(STAV, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for c in chyby:
        print("Nepodařilo se načíst:", c, file=sys.stderr)
    if zmeny:
        open(ZPRAVA, "w", encoding="utf-8").write("\n\n".join(zmeny) + "\n")
        print("\n\n".join(zmeny))
    else:
        print("Beze změny." if puvodni is not None else "První kontrola dne uložena.")


if __name__ == "__main__":
    main()
