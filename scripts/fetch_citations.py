#!/usr/bin/env python3
"""Build _data/citations.yaml from ORCID iDs (prototype).

iDs come from `orcid:` in _members/*.md front matter and `group:` in
_data/sources.yaml. Works are pulled from the public ORCID API, enriched via
Crossref when a DOI is present, de-duplicated by DOI (fallback: normalised
title), and tagged with every ORCID iD that lists them.
"""
import html, json, re, sys, unicodedata, urllib.request
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"Accept": "application/json", "User-Agent": "bristol-climate-health-site/0.1"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def front_matter(path):
    m = re.match(r"---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def collect_orcids():
    ids = set()
    for p in (ROOT / "_members").glob("*.md"):
        if o := (front_matter(p).get("orcid") or "").strip():
            ids.add(o)
    sources = yaml.safe_load((ROOT / "_data" / "sources.yaml").read_text()) or {}
    ids.update(o.strip() for o in sources.get("group") or [] if o and o.strip())
    return sorted(ids)


def member_names():
    """orcid -> display name, from _members front matter."""
    names = {}
    for p in (ROOT / "_members").glob("*.md"):
        fm = front_matter(p)
        if (fm.get("orcid") or "").strip() and fm.get("name"):
            names[fm["orcid"].strip()] = fm["name"]
    return names


def norm(text):
    text = unicodedata.normalize("NFKD", text or "")
    return "".join(c for c in text if not unicodedata.combining(c)).lower().strip()


def author_position(raw_authors, orcid, name):
    """1-based position of a member in the author list, or None.

    Matches the Crossref author ORCID when present, otherwise surname (last word)
    plus first initial against the member's name.
    """
    for i, a in enumerate(raw_authors):
        if orcid in (a.get("ORCID") or ""):
            return i + 1
    parts = norm(name).split()
    if not parts:
        return None
    surname, initial = parts[-1], parts[0][:1]
    for i, a in enumerate(raw_authors):
        family = norm(a.get("family")).split()
        given = norm(a.get("given"))
        if family and family[-1] == surname and given[:1] == initial:
            return i + 1
    return None


def orcid_dois_and_titles(orcid, types):
    data = get(f"https://pub.orcid.org/v3.0/{orcid}/works")
    for group in data.get("group", []):
        summary = group["work-summary"][0]
        if types and summary.get("type", "").lower().replace("_", "-") not in types:
            continue
        doi = None
        for ext in (group.get("external-ids") or {}).get("external-id", []):
            if ext["external-id-type"] == "doi":
                doi = ext["external-id-value"].lower().removeprefix("https://doi.org/")
                break
        title = ((summary.get("title") or {}).get("title") or {}).get("value", "")
        year = ((summary.get("publication-date") or {}).get("year") or {}).get("value")
        yield doi, title, year, summary.get("journal-title", {}) and summary["journal-title"].get("value")


def clean(text):
    """Crossref titles can contain JATS markup (<scp>) and HTML entities."""
    if not isinstance(text, str):
        return text
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text))).strip()


def crossref(doi):
    try:
        msg = get(f"https://api.crossref.org/works/{doi}")["message"]
    except Exception:
        return {}
    authors = [" ".join(filter(None, [a.get("given"), a.get("family")])) for a in msg.get("author", [])]
    issued = (msg.get("issued", {}).get("date-parts") or [[None]])[0][0]
    return {
        "raw_authors": msg.get("author", []),
        "title": clean((msg.get("title") or [None])[0]),
        "authors": authors,
        "journal": clean((msg.get("container-title") or [None])[0]),
        "year": issued,
    }


def main():
    orcids = collect_orcids()
    sources = yaml.safe_load((ROOT / "_data" / "sources.yaml").read_text()) or {}
    types = [t.lower() for t in sources.get("types") or []]
    if not orcids:
        print("No ORCID iDs set; leaving citations.yaml unchanged.")
        return
    works = {}
    for orcid in orcids:
        try:
            found = list(orcid_dois_and_titles(orcid, types))
        except Exception as e:
            print(f"! {orcid}: {e}", file=sys.stderr)
            continue
        for doi, title, year, journal in found:
            key = doi or re.sub(r"\W+", "", title.lower())
            if not key:
                continue
            w = works.setdefault(key, {"title": title, "authors": [], "journal": journal,
                                       "year": int(year) if year else None, "doi": doi, "orcids": []})
            w["orcids"].append(orcid)
    names = member_names()
    for w in works.values():
        if w["doi"]:
            info = crossref(w["doi"])
            raw = info.pop("raw_authors", [])
            for k, v in info.items():
                if v:
                    w[k] = v
            w["link"] = f"https://doi.org/{w['doi']}"
            if raw:
                # author position of each listed member (1 = first author)
                w["n_authors"] = len(raw)
                pos = {o: author_position(raw, o, names[o]) for o in set(w["orcids"]) if o in names}
                w["positions"] = {o: n for o, n in sorted(pos.items()) if n}
    out = sorted(works.values(), key=lambda w: (w["year"] or 0), reverse=True)
    for w in out:
        w["orcids"] = sorted(set(w["orcids"]))
    header = "# GENERATED by scripts/fetch_citations.py -- do not edit by hand.\n"
    (ROOT / "_data" / "citations.yaml").write_text(
        header + yaml.safe_dump(out, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"Wrote {len(out)} works from {len(orcids)} ORCID iD(s).")


if __name__ == "__main__":
    main()
