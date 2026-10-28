# ChatGPT custom plugins

Version-controlled source and recoverable release history for seven accessible custom plugins. Imported on 2026-10-28. This local repository is ready for a private GitHub remote; it has not yet been uploaded.

## Layout

- `plugins/`: authoritative current source from the plugin source reader.
- `history/<plugin>/`: stored release metadata, original archives, extracted snapshots, reconstructed changelogs, and exact text diffs.
- `plugins-lock.json`: plugin IDs, current versions and backend release IDs at import.
- `proposals/`: proposed changes that have not been published.

## Version policy

Keep each plugin's own existing version. Use MAJOR.MINOR.PATCH: PATCH for fixes, MINOR for new features, MAJOR for breaking behavior. Tags use `<plugin-name>/v<version>`, so one plugin can change without renumbering every plugin. Git commits record changes; backend release IDs identify installed packages. These are separate identifiers.

Every release should record the version, date, change description, validation performed, Git commit, backend release ID, package checksum, and publication status. Never label a candidate as deployed before a successful update and read-back. Shared plugins affect their existing audience.

Historical commits are imports made today. Original release dates remain in metadata and tag messages. Stored releases can include unpublished releases; current markers do not prove older releases were ever published. Original changelog text was not returned by the release API. Reconstructed changelogs describe observed file changes, not author intent.

## Release workflow

1. Fetch the current backend source and release ID; reconcile any drift.
2. Commit changes, update that plugin's changelog and version, and validate.
3. Package one plugin with files at its root; preserve configuration and identity.
4. Publish with the observed backend release ID as a conflict guard.
5. Read back affected files and record the new backend release ID.
6. Tag the verified commit and attach the package to a GitHub release when supported.

## Rollback

Select a previous tag or stored snapshot, restore its content on a new branch, and assign a version higher than the currently installed version. Plugin updates reject lower versions. Because updates overlay existing files, explicitly delete files introduced after the restored snapshot and preserve required generated compatibility files. Publish against the current backend release ID, verify the resulting file inventory, and record which historical release was restored. A Git revert alone does not change the installed plugin.

Do not commit credentials, learner records, lecture uploads, or signed download URLs. No automatic GitHub-to-plugin deployment is configured.
