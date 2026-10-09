---
permalink: /blog/
title: Blog
eyebrow: 03 / Latest
lede: Ideas, evidence and updates.
---
<div class="news-grid">
{% for p in site.posts %}
  <a href="{{ p.url | relative_url }}">{% if p.image %}<div class="news-art" style="background-image:url('{{ p.image | relative_url }}')"></div>{% endif %}<small>{{ p.tag }} · {{ p.date | date: "%-d %b %Y" }}</small><h3>{{ p.title }}</h3><p>{{ p.excerpt | strip_html }}</p><b>Read more →</b></a>
{% endfor %}
</div>
