"""Structural regression checks for Tutor me's pedagogical support protocol."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "tutor-me"
PROTOCOL = PLUGIN / "skills" / "learn-combined" / "references" / "scaffolded-independence.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


manifest = json.loads(read(PLUGIN / "plugin.json"))
codex_manifest = json.loads(read(PLUGIN / ".codex-plugin" / "plugin.json"))
assert manifest["name"] == codex_manifest["name"] == "tutor-me"
assert manifest["version"] == codex_manifest["version"] == "0.10.0"

lock_entry = next(item for item in json.loads(read(ROOT / "plugins-lock.json")) if item["name"] == "tutor-me")
releases = json.loads(read(ROOT / "history" / "tutor-me" / "releases.json"))
expected_release = "pluginrel_6ae9809e1c788191bce6e8f3ae45509b"
assert lock_entry["version"] == manifest["version"]
assert lock_entry["description"] == manifest["description"]
assert releases["current_release_id"] == expected_release
assert sum(item["is_current"] for item in releases["releases"]) == 1
assert releases["releases"][0]["release_id"] == expected_release
assert releases["releases"][0]["version"] == "0.9.1"

protocol = read(PROTOCOL)
for required in (
    "## Source and mode guardrails",
    "## 1. Diagnose the stuck point or error",
    "## 2. Progressive Hint Ladder",
    "Level 0 — Diagnostic",
    "Level 5 — Near-complete scaffold",
    "## 3. Unassisted Evidence Checkpoint",
    "Providing a target-skill cue closes the independent window",
    "Use `unassisted` only for work completed inside the independent window",
    "Do not create persistent learner records",
):
    assert required in protocol, required

for skill in (
    PLUGIN / "skills" / "learn-combined" / "SKILL.md",
    PLUGIN / "skills" / "review-mode" / "SKILL.md",
    PLUGIN / "skills" / "project-assessment" / "SKILL.md",
):
    text = read(skill)
    assert "scaffolded-independence.md" in text, skill

# Every relative Markdown link in current Tutor me Markdown must resolve.
for markdown in (PLUGIN / "skills").rglob("*.md"):
    for target in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)", read(markdown)):
        if "://" not in target:
            assert (markdown.parent / target).resolve().exists(), f"{markdown}: {target}"

print("Tutor pedagogy validation passed: manifests, mode integration, protocol guardrails, and local links.")
