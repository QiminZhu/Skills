"""Check rollback preparation without publishing or changing live source."""
import importlib.util
import json
from pathlib import Path
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("rollback", root / "scripts/prepare_tutor_rollback.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
release = "pluginrel_6ae983fe57d88191badd7768db92ffb8"
lock = next(x for x in json.loads((root / "plugins-lock.json").read_text()) if x["name"] == module.NAME)
parts = list(module.version(lock["version"])); parts[2] += 1
new_version = ".".join(map(str, parts))
with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp)
    request = module.prepare(root, release, new_version, out)
    assert request["expected_release_id"] == lock["current_release_id"]
    assert request["delete_paths"] == []
    source = root / "history" / module.NAME / release / "source"
    with zipfile.ZipFile(request["archive"]) as archive:
        for path in source.rglob("*"):
            if not path.is_file():
                continue
            name = path.relative_to(source).as_posix()
            if name in ("plugin.json", ".codex-plugin/plugin.json"):
                original = json.loads(path.read_text())
                restored = json.loads(archive.read(name))
                assert restored.pop("version") == new_version
                original.pop("version")
                assert restored == original
            else:
                assert archive.read(name) == path.read_bytes()
    for invalid in (lock["version"], "0.0.1", "bad"):
        try:
            module.prepare(root, release, invalid, out)
        except ValueError:
            pass
        else:
            raise AssertionError("Accepted invalid rollback version: " + invalid)
print("Rollback preparation passed: exact restored content except version, inventory, conflict guard and version rejection; nothing published.")
