---
title: DELTA
tag: Funded project
themes: [attribution]
hero:  /assets/images/delta_matrix.jpg               # optional wide photo behind the project title, e.g. /assets/images/my-hero.jpg
image: /assets/images/delta_matrix.jpg
summary: Downscaled Ensemble for Local-scale Trend Attribution. An open data platform that provides bias-corrected, downscaled temperature and precipitation timeseries for every country, under both observed and counterfactual (no human influence) climates, so that health researchers can carry out climate change attribution studies without having to process climate model data themselves.
link:                  # optional external page; shown as a button on the project page
link_text: Project website →
status: current        # current or completed
funder:       # Funded by
pi: []                # PI(s): member file names, or plain names for people outside the group
team: [emily-vosper, ruby-lieber]          # member file names, e.g. [ruby-lieber, eunice-lo]
collaborators: []   # affiliates and other collaborators: member file names or plain names (affiliates listed in team also show here)
start:                # YYYY-MM (Duration)
end:                  # YYYY-MM (blank = ongoing)
partners: []          # e.g. [Met Office, {name: UKHSA, url: https://www.gov.uk/ukhsa}]
outputs: []           # e.g. [{title: Paper title, url: https://doi.org/..., note: Journal 2026}]
photos: []            # e.g. [{image: /assets/images/my-photo.jpg, caption: A caption}]
---
## Aims and outputs

- **DELTA data platform:** an open, user-friendly web platform providing daily temperature and monthly precipitation for every country, paired across factual (observed) and counterfactual (natural-only) climate scenarios, with area- and population-weighted timeseries down to subnational administrative levels.
- **Attributable warming estimates:** the first global, country-level estimates of attributable regional warming derived using optimal fingerprinting.
- **Dataset paper:** a peer-reviewed data description documenting the processing pipeline and methods, alongside technical documentation on the platform.
- **Enabling health attribution:** removing a key technical barrier for epidemiologists, policymakers and students, so that health impact attribution studies can be carried out consistently and with best-practice climate data.
- **Future development:** version 1 will act as a proof of concept for future funding, with version 2 planned to incorporate updated climate model data and AI downscaling methods being developed at Bristol.

## Methods

We are bias-correcting and downscaling the DAMIP historical and historical-natural experiments to 0.5° resolution, using ERA5 reanalysis for near-surface temperature and the MSWEP satellite-based product for precipitation. From these, we are producing gridded data and area- and population-weighted timeseries for every country and its administrative subdivisions using GADM boundaries. Optimal fingerprinting is being applied to robustly isolate the anthropogenic warming signal at global and regional scales.

In parallel, we are working with Research IT to build the web platform, including a graphical interface for exploring and downloading the data at national and subnational levels and tracking of usage to inform future products. The platform will be presented to the international climate and health attribution working group in Rio de Janeiro in 2027.

## Team

- **Ruby Lieber and Emily Vosper (School of Geographical Sciences):** climate attribution, bias correction, downscaling and data processing.
- **Mark McLaren (Research IT):** software development, back-end data pipeline and data visualisation.
- **Chin Yang Shapland (Bristol Medical School):** health modelling expertise, ensuring the data meets the needs of climate–health studies.

Funded by the Cabot Institute Seedcorn Fund.
