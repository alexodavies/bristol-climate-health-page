---
permalink: /projects/
title: Projects
eyebrow: Projects
description: Climate Health projects at the University of Bristol, including UNSEEN heatwave mortality, beyond heat mortality, and the National Climate Impacts and Risks meetings.
lede: Selected projects connecting climate evidence to health decisions.
---
<div class="news-grid">
{% for p in site.data.projects %}
  <a href="{{ p.link }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>{{ p.cta }}</b></a>
{% endfor %}
</div>
