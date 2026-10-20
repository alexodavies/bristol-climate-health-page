---
permalink: /research/
title: Research
eyebrow: 01 / Research
description: Our research foci.
---
<div class="themes">
{% for r in site.data.research %}
  <section class="theme" id="{{ r.id }}" style="background-image:url('{{ r.image | relative_url }}');--tint:{{ r.tint | default: '#294739' }}">
    <div class="theme-inner">
      <span class="theme-num">{{ forloop.index | prepend: '0' }} / {{ r.kicker }}</span>
      <h2>{{ r.title }}</h2>
      <p>{{ r.text }}</p>
      {%- assign related = site.projects | where_exp: "p", "p.themes contains r.id" %}
      {%- if related.size > 0 %}
      <p class="theme-projects"><small>Related projects</small>
        {%- for p in related %}<a href="{{ p.url | relative_url }}">{{ p.title }}</a>{% endfor %}
      </p>
      {%- endif %}
    </div>
  </section>
{% endfor %}
</div>
<p><a class="round-link inverse-pill" href="{{ '/publications/' | relative_url }}">Read our publications <span>↗</span></a></p>
