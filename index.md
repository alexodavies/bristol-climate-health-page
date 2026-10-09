---
layout: default
title: Home
description: Climate Health is a University of Bristol research group studying how climate change and extreme weather affect human health, from heatwave mortality to long-term health burdens.
---
<section class="hero">
  <div class="hero-photo" role="img" aria-label="Landscape and weather"></div>
  <video class="hero-video" autoplay muted loop playsinline preload="auto" aria-hidden="true" tabindex="-1"><source src="{{ '/assets/video/hero-small.mp4' | relative_url }}" type="video/mp4"></video><div class="hero-shade"></div>
  <div class="hero-copy"><p class="eyebrow">University of Bristol</p><h1>Climate changes,<br>health changes,<br>and climate <em>changes health.</em></h1><p class="dek">We study how climate change and extreme weather affect human health, and turn climate evidence into useful information for health decisions.</p><a class="round-link" href="{{ '/research/' | relative_url }}">Explore our work <span>↘</span></a></div>
  <div class="scroll">Scroll to explore ↓</div>
</section>

<section id="research" class="section dark">
  {% include section-head.html eyebrow="01 / Research" title="Where climate<br>meets <em>health.</em>" %}
  <div class="cards">
  {% for r in site.data.research %}
    <a class="card {{ r.cls }}" style="background-image:url('{{ r.image | relative_url }}')" href="{{ '/research/' | relative_url }}"><span>{{ r.kicker }}</span><h3>{{ r.title }}</h3><p>{{ r.text | truncatewords: 14 }}</p><b>Explore research →</b></a>
  {% endfor %}
  </div>
</section>

<section id="people" class="people">
  {% include section-head.html eyebrow="02 / People" title="Led across climate science<br><em>&amp; human health.</em>" %}
  {% assign all = site.members | sort: "order" %}
  {% assign leads = all | where: "group", "leads" %}
  {% assign ids = site.data.team_groups | map: "id" %}
  {%- assign rest = "" | split: "" -%}
  {%- for g in site.data.team_groups -%}{%- unless g.id == "leads" -%}
    {%- assign grp = all | where: "group", g.id -%}
    {%- include sort-by-surname.html list=grp -%}
    {%- for m in sorted_members -%}{%- assign rest = rest | push: m -%}{%- endfor -%}
  {%- endunless -%}{%- endfor -%}
  {%- for m in all -%}{%- unless ids contains m.group -%}{%- assign rest = rest | push: m -%}{%- endunless -%}{%- endfor %}
  {% include ring-key.html %}
  <div class="people-split">
    <div class="people-col">
      <h3 class="people-sub">Team leads</h3>
      {% include hex-cluster.html list=leads cls="big flat leads" %}
    </div>
    <div class="people-col">
      <h3 class="people-sub">Researchers</h3>
      {% include honeycomb.html list=rest %}
    </div>
  </div>
  <a class="round-link inverse" href="{{ '/team/' | relative_url }}">Meet the team <span>↗</span></a>
</section>
