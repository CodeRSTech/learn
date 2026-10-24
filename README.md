# Learn Reference Guide

A growing, multi-disciplinary library of learning notes, explanations, and code
examples. Browse the [learning library](https://coderstech.github.io/learn/), or
search by article title, subject, and category.

## Run locally

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000/learn/`. The site is built by the existing GitHub
Actions workflow, which supports the custom catalog generator in `_plugins/`.
GitHub Pages' built-in safe-mode Jekyll build does not run custom generators.

## Add learning material

Place an article under its discipline, subject, and optional category:

```text
computer-science/
  algorithms/
    Backtracking/
      N-Queens Problem/
        index.md
```

Use this front matter:

```yaml
---
layout: algo
title: My topic
category: My category
attribution_sources:
  - Trekhleb
---
```

Keep the original source attribution, license notices, and relevant links when
adapting material. Existing articles also use `Algorithm Visualizer Project` and
`GeeksforGeeks` as attribution sources.

The catalog discovers articles with `layout: algo` and generates missing
discipline, subject, and category landing pages at build time. You do **not** need
to maintain link lists or add empty `index.md` files. Existing articles that also
contain subtopics (such as Tree) keep their content and show their child topics
in the sidebar.

`_data/curriculum.yml` supplies optional display names and ordering. Add entries
there to customize a new subject; folders not listed are still discovered.
Planned subjects without articles are omitted rather than linked to empty pages.
The folder hierarchy, not the legacy `category` field, determines navigation, so
similarly named categories in different subjects remain separate.

For a custom collection introduction, add an `index.md` in its folder with
`layout: topics-index`, a `title`, and an optional `description`. Its child-topic
cards are populated automatically.

## Navigation and layout

Landing pages use responsive collection cards with article counts. Articles
provide breadcrumbs, a sticky contextual sidebar, and child-topic links.
The primary theme is the main site's shared
[`terminal.css`](https://coderstech.github.io/assets/css/terminal.css), bundled at
`assets/css/terminal.css` and loaded after the local layout styles. Learning-page
colors use its terminal palette, and
collection cards use its interactive card styling. If the shared stylesheet
cannot load, the existing local theme in `assets/css/learn.css` and
`assets/css/topics-index.css` remains the fallback, without requiring JavaScript.
Navigation uses local assets; math rendering still uses MathJax.
The homepage search runs locally in the browser and matches article titles and
their full collection paths. Browsing remains available without JavaScript.
Local navigation and assets respect Jekyll's `baseurl`, including spaces and
Unicode in existing article paths.

## Check the catalog

```sh
python -m unittest discover -s tests
```

These checks build the site with both `/learn` and an empty base URL, verify
catalog links and local assets, and exercise automatic discovery of a new subject.
