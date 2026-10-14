---
permalink: /projects/
title: Projects
eyebrow: Projects
description: Funded projects of the Climate Health group at the University of Bristol, including BREATHE, UNSEEN heatwave mortality and the National Climate Impacts and Risks meetings.
lede: Our funded projects, each with its own award and team. For wider themes see Research.
---
<div class="news-grid">
{% for p in site.data.projects %}
  <a href="{{ p.link }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>{{ p.cta }}</b></a>
{% endfor %}
</div>
