"""Validate repository metadata and static-site navigation before publishing."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from ruamel.yaml import YAML


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://institut-du-numerique-responsable.github.io/green-codex/"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])


def check_readme_translation():
    # The French README is a translation; these checks catch a section, link or command
    # added to one README and forgotten in the other. They do not check the wording.
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    french = (ROOT / "README.fr.md").read_text(encoding="utf-8")
    assert "[Français](README.fr.md)" in english, "README.md lacks the French link"
    assert "[English](README.md)" in french, "README.fr.md lacks the English link"

    def outline(text):
        headings = re.findall(r"^#{1,3} ", text, re.M)
        local = {
            target for target in re.findall(r"\]\(([^)#]+)[^)]*\)", text)
            if not target.startswith("http") and not target.startswith("README")
        }
        code = re.findall(r"```[a-z]*\n(.*?)```", text, re.S)
        return headings, local, code

    en_headings, en_links, en_code = outline(english)
    fr_headings, fr_links, fr_code = outline(french)
    assert en_headings == fr_headings, "README.md and README.fr.md have different sections"
    assert en_links == fr_links, f"Local links differ: {sorted(en_links ^ fr_links)}"
    assert en_code == fr_code, "README.md and README.fr.md have different code blocks"


def main():
    check_readme_translation()
    yaml = YAML(typ="safe")
    for path in sorted((ROOT / ".github/workflows").glob("*.yml")):
        workflow = yaml.load(path.read_text())
        assert isinstance(workflow.get("jobs"), dict), f"Missing jobs: {path}"
    yaml.load((ROOT / ".github/dependabot.yml").read_text())

    manifest = json.loads((ROOT / "docs/manifest.json").read_text())
    assert manifest["scope"] == "/green-codex/"
    assert "share_target" not in manifest, "Static site has no sharing endpoint"
    assert "protocol_handlers" not in manifest, "Static site has no protocol handler"
    urls = [manifest["start_url"]]
    urls += [shortcut["url"] for shortcut in manifest.get("shortcuts", [])]
    urls += [icon["src"] for icon in manifest.get("icons", [])]
    for value in urls:
        url = urlsplit(urljoin(SITE + "manifest.json", value))
        assert url.netloc == urlsplit(SITE).netloc
        assert url.path.startswith("/green-codex/"), f"Outside site: {value}"
        relative = unquote(url.path.removeprefix("/green-codex/")) or "index.html"
        target = (ROOT / "docs" / relative).resolve()
        assert target.is_relative_to((ROOT / "docs").resolve())
        assert target.is_file(), f"Missing destination: {value}"
        if url.fragment:
            page = Page()
            page.feed(target.read_text())
            assert unquote(url.fragment) in page.ids, f"Missing anchor: {value}"
    print("Workflow YAML and static-site navigation verified")


if __name__ == "__main__":
    main()
