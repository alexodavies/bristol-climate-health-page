---
permalink: /projects/
title: Projects
eyebrow: Projects
lede: Selected projects connecting climate evidence to health decisions.
---
<div class="news-grid">
{% for p in site.data.projects %}
  <a href="{{ p.link }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>{{ p.cta }}</b></a>
{% endfor %}
</div>
