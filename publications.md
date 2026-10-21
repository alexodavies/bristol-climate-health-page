---
permalink: /publications/
title: Publications
eyebrow: Publications
description: 
---
{% include ring-key.html %}
{% include pub-filter.html %}
{% assign sorted = site.data.citations | sort: "date" | reverse %}
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
