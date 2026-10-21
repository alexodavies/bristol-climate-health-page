---
title: CHAI
tag: Funded project
themes: [geoai]
image: /assets/images/hero.jpg
summary: Using diffusion models to enhance coarse, health-relevant climate model data to 2.2–5 km, 3-hourly resolution over the UK climate, so that we can better understand how extreme weather affects health, particularly maternal health and hospitalisation.
link:                  # optional external page; shown as a button on the project page
link_text: Project website →
status: current        # current or completed
funder:       # Funded by
pi: []                # PI(s): member file names, or plain names for people outside the group
team: [emily-vosper, dann-mitchell]          # member file names, e.g. [ruby-lieber, eunice-lo]
collaborators: []   # affiliates and other collaborators: member file names or plain names (affiliates listed in team also show here)
start:                # YYYY-MM (Duration)
end:                  # YYYY-MM (blank = ongoing)
partners: []          # e.g. [Met Office, {name: UKHSA, url: https://www.gov.uk/ukhsa}]
outputs: []           # e.g. [{title: Paper title, url: https://doi.org/..., note: Journal 2026}]
photos: []            # e.g. [{image: /assets/images/my-photo.jpg, caption: A caption}]
---
## Aims and outputs

- **AI downscaling tool:** develop an open-source AI tool that turns coarse climate model output into high-resolution, health-relevant climate data. It will come with code, a pretrained UK model and tutorials.
- **Open dataset:** create a ready-to-use, high-resolution dataset of current and future UK climate for the health community.
- **Exposure and inequalities:** measure which communities are most exposed to extreme weather, with a focus on maternal health and hospitalisations.
- **Policy and practice:** provide evidence to guide public health interventions and adaptation planning, including future UK Climate Change Risk Assessments.

## Methods

We are extending our diffusion-based emulator, originally developed to downscale UK precipitation and now taken in-house by the Met Office, to jointly simulate multiple health-relevant variables at sub-daily resolution, including temperature, humidity, heat stress, wind speed, direction and gusts, and precipitation. Using a video diffusion approach, the emulator will generate spatially and temporally coherent fields that preserve the physical relationships between variables, including their joint behaviour during extremes.

The emulator is being trained on the Met Office UKCP Local convection-permitting simulations on around 1,600 years of training data, so the emulator can learn a physically based climate change signal and represent extreme events with return periods of 100 years or more. We are evaluating performance against observational datasets (CEH-GEAR 1hr and MIDAS Open), with particular attention to extremes and inter-variable dependence.

We are then applying the trained emulator to downscale a large ensemble from the HadCM3b-ESM climate model, being developed in Bristol in preparation for CMIP7. This samples climate variability far more comprehensively than is possible with the original high-resolution simulations. We will downscale to 2.2–5 km resolution and mapp onto Lower Layer Super Output Areas (LSOAs), the spatial units used for UK health data, and combine with high-resolution population data to quantify exposure to single and compound hazards under current and future climates.

## Partners

- **Met Office:** expertise and guidance on high-resolution climate modelling and datasets.
- **Office for National Statistics (ONS):** health-linked data, data governance, and routes into policy.
