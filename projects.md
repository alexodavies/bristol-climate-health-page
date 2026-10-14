---
permalink: /projects/
title: Projects
eyebrow: Projects
description: Funded projects of the Climate Health group at the University of Bristol, including BREATHE, UNSEEN heatwave mortality and the National Climate Impacts and Risks meetings.
lede: Our funded projects, each with its own award and team. For wider themes see Research.
---
<div class="news-grid">
{% for p in site.projects %}
  <div class="proj" id="{{ p.slug }}">
    <a href="{{ p.url | relative_url }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>View project →</b></a>
    {%- if p.themes.size > 0 %}
    <p class="proj-themes"><small>Research themes</small>
      {%- for t in p.themes %}{% for r in site.data.research %}{% if r.id == t %}<a href="{{ '/research/#' | append: r.id | relative_url }}">{{ r.title }}</a>{% endif %}{% endfor %}{% endfor %}
    </p>
    {%- endif %}
  </div>
{% endfor %}
</div>
