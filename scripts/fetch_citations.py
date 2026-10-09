#!/usr/bin/env python3
"""Build _data/citations.yaml from ORCID iDs (prototype).

iDs come from `orcid:` in _members/*.md front matter and `group:` in
_data/sources.yaml. Works are pulled from the public ORCID API, enriched via
Crossref when a DOI is present, de-duplicated by DOI (fallback: normalised
title), and tagged with every ORCID iD that lists them.
"""
import difflib, html, json, re, sys, unicodedata, urllib.parse, urllib.request
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
    """orcid -> {"name", "aliases"}, from _members front matter.

    `aliases:` (optional) lists other ways the person's name appears on papers,
    e.g. ["Y. T. Eunice Lo"].
    """
    members = {}
    for p in (ROOT / "_members").glob("*.md"):
        fm = front_matter(p)
        if (fm.get("orcid") or "").strip() and fm.get("name"):
            members[fm["orcid"].strip()] = {"name": fm["name"], "aliases": fm.get("aliases") or []}
    return members


def norm(text):
    text = unicodedata.normalize("NFKD", text or "")
    return "".join(c for c in text if not unicodedata.combining(c)).lower().strip()


def name_tokens(text):
    return [t for t in re.split(r"[\s.\-]+", norm(text)) if t]


def author_position(raw_authors, orcid, member):
    """1-based position of a member in the author list, or None.

    Order of preference: Crossref author ORCID; an exact `aliases:` match; then
    same surname plus either the member's first name appearing among the given
    names ("Y. T. Eunice Lo" for Eunice Lo) or the same first initial
    ("Daniel M. Mitchell" for Dann Mitchell).
    """
    for i, a in enumerate(raw_authors):
        if orcid in (a.get("ORCID") or ""):
            return i + 1
    aliases = {tuple(name_tokens(x)) for x in member.get("aliases", [])}
    parts = norm(member["name"]).split()
    if not parts:
        return None
    surname, first = parts[-1], parts[0]
    for i, a in enumerate(raw_authors):
        # Crossref splits names inconsistently ("Y. T." + "Eunice Lo"), so use all tokens
        tokens = name_tokens(a.get("given")) + name_tokens(a.get("family"))
        if tuple(tokens) in aliases:
            return i + 1
        if len(tokens) > 1 and tokens[-1] == surname:
            given = tokens[:-1]
            if first in given or given[0][:1] == first[:1] or first[:1] in [t for t in given if len(t) == 1]:
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
        put_code = summary.get("put-code")
        title = ((summary.get("title") or {}).get("title") or {}).get("value", "")
        year = ((summary.get("publication-date") or {}).get("year") or {}).get("value")
        yield doi, title, year, summary.get("journal-title", {}) and summary["journal-title"].get("value"), put_code


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


def orcid_contributors(orcid, put_code):
    """Author names listed on the ORCID record itself (often empty)."""
    try:
        data = get(f"https://pub.orcid.org/v3.0/{orcid}/work/{put_code}")
    except Exception:
        return []
    out = []
    for c in (data.get("contributors") or {}).get("contributor") or []:
        name = (c.get("credit-name") or {}).get("value")
        if name:
            if "," in name:  # "Davies, Alex O." -> "Alex O. Davies"
                family, _, given = name.partition(",")
                name = f"{given.strip()} {family.strip()}"
            out.append(name)
    return out


def crossref_search(title):
    """Best Crossref match for a work that has no DOI on ORCID (title similarity >= 0.93)."""
    if not title:
        return None
    try:
        items = get("https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(title))["message"]["items"]
    except Exception:
        return None
    for it in items:
        t = clean((it.get("title") or [""])[0])
        if t and difflib.SequenceMatcher(None, norm(t), norm(title)).ratio() >= 0.93:
            return it
    return None


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
        for doi, title, year, journal, put_code in found:
            key = doi or re.sub(r"\W+", "", title.lower())
            if not key:
                continue
            w = works.setdefault(key, {"title": title, "authors": [], "journal": journal,
                                       "year": int(year) if year else None, "doi": doi, "orcids": [],
                                       "_src": (orcid, put_code)})
            w["orcids"].append(orcid)
    names = member_names()
    for w in works.values():
        raw = []
        if not w["doi"] and (hit := crossref_search(w["title"])):
            w["doi"] = hit["DOI"].lower()
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
        src = w.pop("_src", None)
        if not w["authors"] and src:
            # no Crossref record: fall back to contributors on the ORCID entry
            listed = orcid_contributors(*src)
            if listed:
                w["authors"] = listed
                raw = [{"given": " ".join(n.split()[:-1]), "family": n.split()[-1]} for n in listed]
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
