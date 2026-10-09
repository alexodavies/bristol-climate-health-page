---
permalink: /team/
title: Team
eyebrow: 02 / People
description: The Climate Health team at the University of Bristol, from group leads Professor Dann Mitchell and Dr Eunice Lo to postdoctoral researchers and PhD students working on climate and human health.
lede: Led across climate science and human health.
---
{% include ring-key.html %}
{% assign all = site.members | sort: "order" %}
{% assign ids = site.data.team_groups | map: "id" %}
{% for g in site.data.team_groups %}
{% assign list = all | where: "group", g.id %}
{% if list.size > 0 %}
{% include sort-by-surname.html list=list %}
<h2 class="sub group-head">{{ g.label }}</h2>
{% include hex-cluster.html list=sorted_members cls="big" %}
{% endif %}
{% endfor %}
{% assign others = "" | split: "" %}
{% for m in all %}{% unless ids contains m.group %}{% assign others = others | push: m %}{% endunless %}{% endfor %}
{% if others.size > 0 %}
{% include sort-by-surname.html list=others %}
<h2 class="sub group-head">Members</h2>
{% include hex-cluster.html list=sorted_members cls="big" %}
{% endif %}
