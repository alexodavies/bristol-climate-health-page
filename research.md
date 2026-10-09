---
permalink: /research/
title: Research
eyebrow: 01 / Research
lede: Heat, cold and morbidity; attribution and risk; and forecasting for resilience. Publications below update automatically from the group's ORCID records.
---
<div class="cards light">
{% for r in site.data.research %}
  <div class="card {{ r.cls }}" style="background-image:url('{{ r.image | relative_url }}')"><span>{{ r.kicker }}</span><h3>{{ r.title }}</h3><p>{{ r.text }}</p></div>
{% endfor %}
</div>

<h2 class="sub">Publications</h2>
{% include pub-filter.html %}
{% assign sorted = site.data.citations | sort: "year" | reverse %}
{% assign years = sorted | map: "year" | uniq %}
{% for y in years %}
<div class="year-block">
<h3 class="year">{{ y }}</h3>
<ul class="citations">
  {% for c in sorted %}{% if c.year == y %}{% include citation.html c=c avatars=true %}{% endif %}{% endfor %}
</ul>
</div>
{% endfor %}
