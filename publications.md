---
permalink: /publications/
title: Publications
eyebrow: Publications
description: Publications by the Climate Health group at the University of Bristol on heat, cold and health, climate change attribution, and forecasting for health resilience.
lede: Journal articles from group members, updated automatically from ORCID. Each person's papers are shown for the period they were in the group.
---
{% include ring-key.html %}
{% include pub-filter.html %}
{% assign sorted = site.data.citations | sort: "year" | reverse %}
{%- assign visible = "" | split: "" -%}
{%- for c in sorted -%}{%- include tenure-orcids.html c=c -%}{%- if in_tenure -%}{%- assign visible = visible | push: c -%}{%- endif -%}{%- endfor -%}
{% assign years = visible | map: "year" | uniq %}
{% for y in years %}
<div class="year-block">
<h3 class="year">{{ y }}</h3>
<ul class="citations">
  {% for c in visible %}{% if c.year == y %}{% include citation.html c=c avatars=true tenure=true %}{% endif %}{% endfor %}
</ul>
</div>
{% endfor %}
