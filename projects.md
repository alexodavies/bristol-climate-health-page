---
permalink: /projects/
title: Projects
eyebrow: Projects
description: Funded projects of the Climate Health group at the University of Bristol, including BREATHE, Futureproof, AI for Heat Mortality, CHAI and DELTA.
lede: Our funded projects, current and completed, each with its own page. For wider themes see Research.
---
{% assign current = site.projects | where_exp: "p", "p.status != 'completed'" %}
{% assign done = site.projects | where_exp: "p", "p.status == 'completed'" %}
{% if current.size > 0 %}
<h2 class="sub">Current projects</h2>
<div class="news-grid">
{% for p in current %}
  <div class="proj" id="{{ p.slug }}">
    <a href="{{ p.url | relative_url }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>View project →</b></a>
    {%- if p.team.size > 0 %}
    <p class="proj-team">{% for s in p.team %}{% include byline.html slug=s %}{% endfor %}</p>
    {%- endif %}
    {%- if p.themes.size > 0 %}
    <p class="proj-themes"><small>Research themes</small>
      {%- for t in p.themes %}{% for r in site.data.research %}{% if r.id == t %}<a href="{{ '/research/#' | append: r.id | relative_url }}">{{ r.title }}</a>{% endif %}{% endfor %}{% endfor %}
    </p>
    {%- endif %}
  </div>
{% endfor %}
</div>
{% endif %}
{% if done.size > 0 %}
<h2 class="sub">Completed projects</h2>
<div class="news-grid">
{% for p in done %}
  <div class="proj" id="{{ p.slug }}">
    <a href="{{ p.url | relative_url }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>View project →</b></a>
    {%- if p.team.size > 0 %}
    <p class="proj-team">{% for s in p.team %}{% include byline.html slug=s %}{% endfor %}</p>
    {%- endif %}
    {%- if p.themes.size > 0 %}
    <p class="proj-themes"><small>Research themes</small>
      {%- for t in p.themes %}{% for r in site.data.research %}{% if r.id == t %}<a href="{{ '/research/#' | append: r.id | relative_url }}">{{ r.title }}</a>{% endif %}{% endfor %}{% endfor %}
    </p>
    {%- endif %}
  </div>
{% endfor %}
</div>
{% endif %}
