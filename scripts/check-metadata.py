"""Validate repository metadata and static-site navigation before publishing."""

import json
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


def main():
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
