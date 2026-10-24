import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class PageLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.navigation = []
        self.assets = []
        self.nav_depth = 0
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "nav":
            self.nav_depth += 1
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if self.nav_depth:
                self.navigation.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.assets.append(attrs["href"])
        if tag == "script" and "src" in attrs:
            self.assets.append(attrs["src"])

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav_depth -= 1


class CatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.source = Path(cls.temp.name) / "source"
        cls.source.mkdir()
        for name in ("_layouts", "_includes", "_plugins", "_data", "assets", "computer-science"):
            shutil.copytree(ROOT / name, cls.source / name)
        for name in ("_config.yml", "index.md"):
            shutil.copy(ROOT / name, cls.source / name)

        cls.article_paths = [
            path.relative_to(cls.source).with_suffix(".html")
            for path in cls.source.rglob("*.md")
            if re.search(r"^layout: algo\s*$", path.read_text(), re.MULTILINE)
        ]
        cls.fixture = "physics/quantum-mechanics/Wave & particle/Overview"
        article = cls.source / cls.fixture / "index.md"
        article.parent.mkdir(parents=True)
        article.write_text(
            "---\nlayout: algo\ntitle: Wave & particle overview\n"
            "category: Data Structures\n---\n\nFixture article.\n"
        )
        introduction = cls.source / "physics/index.md"
        introduction.write_text(
            "---\nlayout: topics-index\ntitle: Physics\n---\n\nA custom introduction.\n"
        )
        cls.outputs = {}
        for baseurl in ("/learn", ""):
            destination = Path(cls.temp.name) / ("project" if baseurl else "root")
            result = subprocess.run(
                [
                    "bundle", "exec", "jekyll", "build", "--quiet",
                    "--source", str(cls.source), "--destination", str(destination),
                    "--baseurl", baseurl,
                ],
                cwd=ROOT, env={**os.environ, "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8"},
                text=True, capture_output=True,
            )
            if result.returncode:
                raise AssertionError(result.stdout + result.stderr)
            cls.outputs[baseurl] = destination

    def assert_links_exist(self, links, destination, baseurl):
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            with self.subTest(link=link, baseurl=baseurl):
                self.assertTrue(parsed.path.startswith(baseurl + "/"), link)
                relative = unquote(parsed.path[len(baseurl):]).lstrip("/")
                target = destination / relative
                if parsed.path.endswith("/"):
                    target /= "index.html"
                self.assertTrue(target.is_file(), f"Broken link: {link}")

    def test_homepage_links_only_published_collections(self):
        for baseurl, destination in self.outputs.items():
            html = (destination / "index.html").read_text()
            self.assertNotIn("From Original Repo", html)
            self.assertNotIn('href="' + baseurl + '/Mathematics/', html)
            self.assertIn("Computer Science", html)
            self.assertIn("Physics", html)
            self.assertIn(f"{len(self.article_paths) + 1} articles", html)
            self.assert_links_exist(PageLinks(html).links, destination, baseurl)

    def test_navigation_and_assets_resolve_on_every_article(self):
        for baseurl, destination in self.outputs.items():
            for path in self.article_paths + [Path(self.fixture) / "index.html"]:
                html = (destination / path).read_text()
                links = PageLinks(html)
                self.assertTrue(links.navigation)
                self.assert_links_exist(links.navigation + links.assets, destination, baseurl)

    def test_shared_terminal_theme_loads_after_local_fallback_styles(self):
        for baseurl, destination in self.outputs.items():
            shared_theme = baseurl + "/assets/css/terminal.css"
            for path in destination.rglob("index.html"):
                assets = PageLinks(path.read_text()).assets
                with self.subTest(path=path, baseurl=baseurl):
                    self.assertEqual(assets.count(shared_theme), 1)
                    self.assertLess(assets.index(baseurl + "/assets/css/learn.css"),
                                    assets.index(shared_theme))
                    self.assertLess(assets.index(baseurl + "/assets/css/topics-index.css"),
                                    assets.index(shared_theme))

    def test_all_generated_collection_links_resolve(self):
        for baseurl, destination in self.outputs.items():
            for path in destination.rglob("index.html"):
                html = path.read_text()
                if '<main class="topics-index">' in html:
                    self.assert_links_exist(PageLinks(html).links, destination, baseurl)

    def test_new_discipline_and_nested_categories_are_discovered(self):
        for baseurl, destination in self.outputs.items():
            for path in (
                "physics", "physics/quantum-mechanics",
                "physics/quantum-mechanics/Wave & particle",
            ):
                self.assertTrue((destination / path / "index.html").is_file())
            custom = (destination / "physics/index.html").read_text()
            self.assertIn("A custom introduction.", custom)
            article = (destination / self.fixture / "index.html").read_text()
            self.assertIn("Wave &amp; particle overview", article)
            self.assertNotIn(">Bloom Filter</a>", article)
            self.assert_links_exist(PageLinks(article).navigation, destination, baseurl)

    def test_existing_article_with_children_keeps_its_content(self):
        for baseurl, destination in self.outputs.items():
            tree = (destination / "computer-science/data-structures/tree/index.html").read_text()
            self.assertIn('class="post-content"', tree)
            self.assertIn("Fenwick Tree", tree)
            self.assertIn("Explore Tree", tree)
            self.assert_links_exist(PageLinks(tree).navigation, destination, baseurl)

    def test_existing_collection_has_automatic_topic_links(self):
        for destination in self.outputs.values():
            html = (destination / "computer-science/algorithms/Dynamic Programming/index.html").read_text()
            self.assertIn('class="topic-card card"', html)
            self.assertIn("Knapsack Problem", html)


if __name__ == "__main__":
    unittest.main()
