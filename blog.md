---
permalink: /blog/
title: Blog
eyebrow: 03 / Latest
lede: Ideas, evidence and updates.
---
{% assign by_author = site.posts | where_exp: "p", "p.author" | group_by: "author" %}
{% if by_author.size > 0 %}
<div class="pub-filter">
  <label for="post-filter">Show posts by</label>
  <select id="post-filter">
    <option value="">Everyone</option>
    {% for g in by_author %}{% for m in site.members %}{% if m.slug == g.name %}<option value="{{ g.name }}">{{ m.name }} ({{ g.size }})</option>{% endif %}{% endfor %}{% endfor %}
  </select>
</div>
{% endif %}
<div class="post-rows" id="post-grid">
{% for p in site.posts %}
{%- assign au = nil -%}
{%- for m in site.members -%}{%- if m.slug == p.author -%}{%- assign au = m -%}{%- endif -%}{%- endfor %}
<article class="post-row" data-author="{{ p.author }}">
  <div class="hexes big flat post-hex">
    {%- if au -%}
    <span class="person down">{% include avatar.html m=au title=au.name %}<small class="who"><b>{{ au.name }}</b><span>{{ au.title | truncate: 40 }}</span></small></span>
    {%- else -%}
    <span class="person down"><span class="avatar p1"><span>CH</span></span><small class="who"><b>Climate Health</b><span>Group post</span></small></span>
    {%- endif -%}
  </div>
  <div class="post-main">
    <small>{% if p.tag %}{{ p.tag }} · {% endif %}{{ p.date | date: "%-d %b %Y" }}</small>
    <h3><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p>{{ p.excerpt | strip_html }}</p>
    <a class="profile-link" href="{{ p.url | relative_url }}">Read more →</a>
  </div>
</article>
{% endfor %}
</div>
<p class="feed-link"><a href="{{ '/feed.xml' | relative_url }}">Subscribe to all posts (Atom feed) ↗</a></p>
