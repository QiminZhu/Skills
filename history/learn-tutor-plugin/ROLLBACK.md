# Restore Tutor me behavior

The exact pre-update 0.10.0 backend source is preserved at
[pluginrel_6ae983fe57d88191badd7768db92ffb8/source](pluginrel_6ae983fe57d88191badd7768db92ffb8/source).
Its release.json records file hashes and the reconstructed archive checksum.
Existing historical releases remain untouched. Restoring Git files alone does not restore the installed workspace plugin.

1. Read current backend files and release ID. Reconcile plugins/learn-tutor-plugin and plugins-lock.json with that live state before preparing a rollback.
2. Select the historical snapshot. Use a NEW version higher than the current installed version. For an installed 0.11.0, 0.11.1 is suitable; it restores 0.10.0 behavior under a forward version.
3. Run from the repository root, using an output directory outside the repository:

   python3 scripts/prepare_tutor_rollback.py pluginrel_6ae983fe57d88191badd7768db92ffb8 --version 0.11.1 --output /tmp/tutor-me-rollback

4. The helper verifies snapshot hashes and identity, preserves all content except the two version fields, validates the ZIP, and writes rollback-request.json. It never publishes. Inspect its explicit delete_paths: overlays otherwise retain newly added files. For the 0.11.0-to-0.10.0 behavior restore, no files need deletion.
5. With user authorization to roll back, call Plugin Creator update_plugin using that request and the freshly observed expected_release_id. If the release changed, reconcile and rebuild; do not replace the guard blindly. Preserve identity, workspace and audience.
6. Read back every file and inventory; record the new version/release, restored-from release, checksums and validation. Commit the restoration without rewriting prior history.

The helper supports snapshots with file_sha256 metadata; older snapshots can use the repository's manual restore workflow after inspecting their archive. Never delete existing historical snapshots.
