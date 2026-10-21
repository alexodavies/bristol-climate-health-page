---
permalink: /projects/
title: Projects
eyebrow: 03/ Projects
description: Our current funded projects.
---
{% assign current = site.projects | where_exp: "p", "p.status != 'completed'" %}
{% assign done = site.projects | where_exp: "p", "p.status == 'completed'" %}
{% if current.size > 0 %}
<h2 class="sub">Current projects</h2>
<div class="news-grid">
{% for p in current %}
  <div class="proj" id="{{ p.slug }}">
    <a href="{{ p.url | relative_url }}"><div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div><small>{{ p.tag }}</small><h3>{{ p.title }}</h3><p>{{ p.summary }}</p><b>View project →</b></a>
    {%- if p.team.size > 0 or p.pi.size > 0 %}
    <p class="proj-team">{% for s in p.pi %}{% include byline.html slug=s %}{% endfor %}{% for s in p.team %}{% unless p.pi contains s %}{% include byline.html slug=s %}{% endunless %}{% endfor %}</p>
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
    {%- if p.team.size > 0 or p.pi.size > 0 %}
    <p class="proj-team">{% for s in p.pi %}{% include byline.html slug=s %}{% endfor %}{% for s in p.team %}{% unless p.pi contains s %}{% include byline.html slug=s %}{% endunless %}{% endfor %}</p>
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
