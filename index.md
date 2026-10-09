---
layout: default
title: Home
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
  <div class="people-grid">
  {% assign members = site.members | where: "group", "leads" | sort: "order" %}
  {% for m in members %}{% include member-card.html m=m %}{% endfor %}
  </div>
  <a class="round-link inverse" href="{{ '/team/' | relative_url }}">Meet the team <span>↗</span></a>
</section>
