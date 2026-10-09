# Climate Health — University of Bristol

Jekyll site (Greene Lab template structure, custom styling).

- Add a person: create `_members/<name>.md` (copy an existing one); set `orcid:` to enable auto-publications.
- Publications: `python3 scripts/fetch_citations.py` (also runs weekly via GitHub Actions) writes `_data/citations.yaml`.
- Run locally: `bundle install && bundle exec jekyll serve`.

## Deploying (GitHub Pages)
1. Push to `main` on GitHub.
2. Settings → Pages → Source: **GitHub Actions**.
3. `.github/workflows/pages.yml` builds with Jekyll 4 and deploys; the base URL is set automatically.
4. Settings → Actions → General → Workflow permissions: **Read and write** (needed for the weekly citation update).
