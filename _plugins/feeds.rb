# Generates Atom feeds: /feed.xml (all posts) and /members/<name>/feed.xml (one per member).
# A post belongs to a member when its front matter has `author: <member file name>`.
# Custom plugins need the Actions build (see .github/workflows/pages.yml); the classic
# GitHub Pages branch builder would ignore this file.
require "cgi"

module ClimateHealth
  class FeedGenerator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      posts = site.posts.docs.sort_by(&:date).reverse
      site.pages << build(site, "", "feed.xml", "#{site.config['title']} — all posts", posts, "/")
      site.collections["members"].docs.each do |m|
        slug = m.basename_without_ext
        mine = posts.select { |p| p.data["author"] == slug }
        site.pages << build(site, "members/#{slug}", "feed.xml", "#{m.data['name']} — #{site.config['title']}", mine, "/members/#{slug}.html")
      end
    end

    private

    def abs(site, path)
      "#{site.config['url']}#{site.config['baseurl']}#{path}"
    end

    def build(site, dir, name, title, posts, home)
      page = Jekyll::PageWithoutAFile.new(site, site.source, dir, name)
      updated = (posts.first&.date || Time.now).utc.iso8601
      entries = posts.first(20).map do |p|
        summary = p.data["excerpt"].is_a?(String) ? p.data["excerpt"] : p.content.to_s.gsub(/\s+/, " ")[0, 300]
        <<~XML
          <entry>
            <title>#{CGI.escapeHTML(p.data['title'].to_s)}</title>
            <link href="#{CGI.escapeHTML(abs(site, p.url))}"/>
            <id>#{CGI.escapeHTML(abs(site, p.url))}</id>
            <updated>#{p.date.utc.iso8601}</updated>
            <summary>#{CGI.escapeHTML(summary.to_s)}</summary>
          </entry>
        XML
      end.join
      page.content = <<~XML
        <?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <title>#{CGI.escapeHTML(title)}</title>
          <link href="#{CGI.escapeHTML(abs(site, home))}"/>
          <link rel="self" href="#{CGI.escapeHTML(abs(site, "/#{dir.empty? ? '' : dir + '/'}#{name}"))}"/>
          <id>#{CGI.escapeHTML(abs(site, home))}</id>
          <updated>#{updated}</updated>
        #{entries}</feed>
      XML
      page.data["layout"] = nil
      page.data["sitemap"] = false
      page
    end
  end
end
