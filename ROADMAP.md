# Learn Reference Guide Roadmap

## 1. UI, Layout & Architecture Enhancements
- [x] **Hierarchical Curriculum Data:** Create `_data/curriculum.yml` to structure the multi-disciplinary learning guide (Discipline > Subject > Category) for dynamic navigation.
- [x] **Automatic Collection Pages:** Generate missing landing pages from published articles, using curriculum labels and ordering without linking empty planned subjects.
- [x] **Multi-Source Attributions:** Update article front matter to accept an array of attribution sources and render respective attribution snippets dynamically.
- [ ] **Interactive Language Tabs:** Implement the `jekyll-tabs` plugin to cleanly display multi-language code implementations (Python, Java, C++, JS) in a tabbed interface instead of sequential code blocks.
- [ ] **Sequential Pagination:** Implement "Next" and "Previous" buttons using Liquid templating to dynamically link adjacent topics within the same category.
- [x] **Contextual Sidebar:** Use collapsible sibling and child-topic navigation, with breadcrumbs preserving the discipline and subject hierarchy.
- [x] **Sticky Sidebar:** Keep article navigation visible on desktop with bounded scrolling.
- [x] **Responsive Design:** Use responsive collection cards, readable articles, and compact mobile navigation.
- [ ] **Typewriter Animation :** to apply this to other headings on site, wrap the target text in `<span class="typewriter">` and adjust the `22ch` in the `@keyframes` to match the exact number of characters in that specific string.

## 2. Search Integration
- [x] **Client-Side Search:** Search article titles and collection paths on the homepage without an external dependency.

## 3. CI/CD & Maintenance
- [x] **Clean up legacy files:** Delete the obsolete `.travis.yml` file, as builds are successfully handled by GitHub Actions.
- [ ] **Translation Progress Tracker:** Write a Python script for GitHub Actions to count the remaining `# TODO: Implement in Python` stubs and automatically update a progress badge on `index.md`.