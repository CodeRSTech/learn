# frozen_string_literal: true

module Learn
  class Catalog < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      labels = curriculum_labels(site.data.fetch("curriculum", []))
      nodes = {}
      root = { "title" => "All subjects", "url" => "/", "children" => [] }
      articles = site.pages.select { |page| page.data["layout"] == "algo" }

      ensure_node = lambda do |path|
        return root if path == "."
        return nodes[path] if nodes.key?(path)

        parent = ensure_node.call(File.dirname(path))
        label = labels[path] || {}
        node = {
          "title" => label["title"] || File.basename(path).tr("-", " ").split.map(&:capitalize).join(" "),
          "url" => "/#{path}/",
          "path" => path,
          "order" => label.fetch("order", labels.size),
          "children" => [],
          "article" => false
        }
        nodes[path] = node
        parent["children"] << node
        node
      end

      articles.each do |page|
        path = File.dirname(page.path)
        path = File.join(path, File.basename(page.path, ".*")) unless File.basename(page.path, ".*") == "index"
        node = ensure_node.call(path)
        node["title"] = page.data.fetch("title")
        node["url"] = page.url
        node["article"] = true
        page.data["catalog_path"] = path
      end

      summarize(root)
      site.data["catalog"] = root
      site.data["learn_articles"] = articles.sort_by { |page| page.data["title"].downcase }.map do |page|
        node = nodes.fetch(page.data["catalog_path"])
        {
          "title" => node["title"],
          "url" => node["url"],
          "context" => ancestors(node["path"], nodes).map { |ancestor| ancestor["title"] }.join(" / ")
        }
      end

      nodes.each_value do |node|
        page = site.pages.find { |candidate| candidate.url == node["url"] }
        unless page
          page = Jekyll::PageWithoutAFile.new(site, site.source, node["path"], "index.html")
          page.content = ""
          page.data["layout"] = "topics-index"
          page.data["title"] = node["title"]
          site.pages << page
        end
        page.data["catalog_node"] = node
        page.data["catalog_breadcrumbs"] = ancestors(node["path"], nodes)
        parent = nodes[File.dirname(node["path"])] || root
        page.data["catalog_siblings"] = parent["children"]
      end
    end

    private

    def curriculum_labels(curriculum)
      labels = {}
      curriculum.each do |discipline|
        path = discipline.fetch("folder")
        labels[path] = { "title" => discipline.fetch("discipline"), "order" => labels.size }
        discipline.fetch("subjects", []).each do |subject|
          subject_path = "#{path}/#{subject.fetch('folder')}"
          labels[subject_path] = { "title" => subject.fetch("name"), "order" => labels.size }
          subject.fetch("categories", []).each do |category|
            labels["#{subject_path}/#{category.fetch('folder')}"] = {
              "title" => category.fetch("name"), "order" => labels.size
            }
          end
        end
      end
      labels
    end

    def summarize(node)
      node["children"].sort_by! { |child| [child["order"], child["title"].downcase] }
      node["count"] = (node["article"] ? 1 : 0) + node["children"].sum { |child| summarize(child) }
    end

    def ancestors(path, nodes)
      parts = path.split("/")
      (1...parts.length).map do |length|
        node = nodes.fetch(parts.first(length).join("/"))
        { "title" => node["title"], "url" => node["url"] }
      end
    end
  end
end
