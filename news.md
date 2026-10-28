---
permalink: /news/
title: News & Media
eyebrow: 05 / News & Media
description: 
lede: News, media interviews and blog posts from the group.
---
{% assign blog_posts = site.posts %}
{% assign by_author = "" | split: "" %}
{% for m in site.members %}{% assign n = blog_posts | where_exp: "p", "p.author contains m.slug" %}{% if n.size > 0 %}{% assign by_author = by_author | push: m %}{% endif %}{% endfor %}
<div class="pub-filter">
  <label for="cat-filter">Show</label>
  <select id="cat-filter">
    <option value="">Everything</option>
    <option value="news">News</option>
    <option value="media">Media</option>
    <option value="blog">Blog</option>
  </select>
  {% if by_author.size > 0 %}
  <label for="post-filter">by</label>
  <select id="post-filter">
    <option value="">Everyone</option>
    {% for m in by_author %}{% assign n = blog_posts | where_exp: "p", "p.author contains m.slug" %}<option value="{{ m.slug }}">{{ m.name }} ({{ n.size }})</option>{% endfor %}
  </select>
  {% endif %}
</div>
{% if blog_posts.size == 0 %}<p class="prose">Nothing here yet. News and media items will appear as they are added.</p>{% endif %}
<div class="post-rows" id="post-grid">
{% for p in blog_posts %}
{%- assign slugs = p.author | join: "," | split: "," -%}
{%- assign nau = 0 -%}
{%- capture people -%}{%- for s in slugs -%}{%- for m in site.members -%}{%- if m.slug == s -%}{%- assign nau = nau | plus: 1 -%}
    <span class="person down">{% include avatar.html m=m title=m.name %}<small class="who"><b>{{ m.name }}</b>{% if slugs.size == 1 %}<span>{{ m.title | truncate: 40 }}</span>{% endif %}</small></span>
{%- endif -%}{%- endfor -%}{%- endfor -%}{%- endcapture %}
<article class="post-row" data-author="{{ slugs | join: ' ' }}" data-category="{{ p.category | default: 'blog' }}">
  <div class="hexes big flat post-hex{% if nau == 2 %} multi-2{% elsif nau > 2 %} multi-3{% endif %}">
    {%- if nau > 0 -%}
    {{ people }}
    {%- else -%}
    <span class="person down"><span class="avatar p1"><span>CH</span></span><small class="who"><b>Climate Health</b><span>Group post</span></small></span>
    {%- endif -%}
  </div>
  <div class="post-main">
    <small>{{ p.category | default: 'blog' | capitalize }} · {% if p.tag %}{{ p.tag }} · {% endif %}{{ p.date | date: "%-d %b %Y" }}</small>
    <h3><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p>{{ p.excerpt | strip_html }}</p>
    <a class="profile-link" href="{{ p.url | relative_url }}">Read more →</a>
  </div>
</article>
{% endfor %}
</div>
<p class="feed-link"><a href="{{ '/feed.xml' | relative_url }}">Subscribe to everything (Atom feed) ↗</a></p>
