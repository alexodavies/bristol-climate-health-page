---
permalink: /research/
title: Research
eyebrow: 01 / Research
description: Research themes and directions of the Climate Health group at the University of Bristol, covering heat, cold and health, climate change attribution, and forecasting for health resilience.
lede: Heat, cold and morbidity; attribution and risk; and forecasting for resilience. See Projects for our funded work and Publications for our papers.
---
<div class="themes">
{% for r in site.data.research %}
  <section class="theme" style="background-image:url('{{ r.image | relative_url }}');--tint:{{ r.tint | default: '#294739' }}">
    <div class="theme-inner">
      <span class="theme-num">{{ forloop.index | prepend: '0' }} / {{ r.kicker }}</span>
      <h2>{{ r.title }}</h2>
      <p>{{ r.text }}</p>
      {%- if r.projects.size > 0 %}
      <p class="theme-projects"><small>Related projects</small>
        {%- for t in r.projects %}{% for p in site.data.projects %}{% if p.title == t %}<a href="{{ p.link }}">{{ p.title }} ↗</a>{% endif %}{% endfor %}{% endfor %}
      </p>
      {%- endif %}
    </div>
  </section>
{% endfor %}
</div>
<p><a class="round-link inverse-pill" href="{{ '/publications/' | relative_url }}">Read our publications <span>↗</span></a></p>
