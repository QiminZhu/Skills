#!/usr/bin/env python3
"""Prepare, but never publish, a version-bumped Tutor me rollback."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAME = "learn-tutor-plugin"


def version(value):
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", value):
        raise ValueError("Use a release version such as 0.11.1")
    return tuple(map(int, value.split(".")))


def prepare(root, release_id, new_version, output):
    if not re.fullmatch(r"pluginrel_[A-Za-z0-9]+", release_id):
        raise ValueError("Use an exact stored backend release ID")
    history = root / "history" / NAME / release_id
    metadata = json.loads((history / "release.json").read_text())
    source = history / "source"
    files = {p.relative_to(source).as_posix(): p.read_bytes() for p in source.rglob("*") if p.is_file()}
    expected_hashes = metadata["file_sha256"]
    if set(files) != set(expected_hashes):
        raise ValueError("Snapshot file inventory does not match its recorded hashes")
    for name, data in files.items():
        if hashlib.sha256(data).hexdigest() != expected_hashes[name]:
            raise ValueError("Snapshot checksum mismatch: " + name)
    current = next(x for x in json.loads((root / "plugins-lock.json").read_text()) if x["name"] == NAME)
    if metadata["release_id"] != release_id or metadata["plugin_id"] != current["plugin_id"]:
        raise ValueError("Snapshot plugin/release identity mismatch")
    if version(new_version) <= version(current["version"]):
        raise ValueError("Rollback must use a version higher than the installed version")
    for name in ("plugin.json", ".codex-plugin/plugin.json"):
        manifest = json.loads(files[name])
        if manifest["name"] != NAME:
            raise ValueError("Manifest identity mismatch")
        manifest["version"] = new_version
        files[name] = (json.dumps(manifest, indent=2) + "\n").encode()
    live_source = root / "plugins" / NAME
    current_paths = {p.relative_to(live_source).as_posix() for p in live_source.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    deletions = sorted(current_paths - files.keys())
    if ".codex-plugin/plugin.json" in deletions:
        raise ValueError("Do not delete a generated compatibility manifest")
    output = output.resolve()
    if output == root.resolve() or root.resolve() in output.parents:
        raise ValueError("Write rollback artifacts outside the repository")
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"tutor-me-rollback-{new_version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 26, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    request = {"plugin_id": current["plugin_id"], "expected_release_id": current["current_release_id"], "archive": str(archive), "delete_paths": deletions}
    (output / "rollback-request.json").write_text(json.dumps(request, indent=2) + "\n")
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(files)
        assert all(z.read(name) == data for name, data in files.items())
    return request


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("release_id")
    parser.add_argument("--version", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        request = prepare(ROOT, args.release_id, args.version, args.output)
    except (ValueError, KeyError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(request, indent=2))
    print("Prepared only. Refresh current backend source/release before publishing; do not reuse a stale conflict guard.")
