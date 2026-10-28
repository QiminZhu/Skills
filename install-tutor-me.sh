#!/bin/sh
# Install Tutor me through Codex's native marketplace manager.
set -eu
if ! command -v codex >/dev/null 2>&1; then
  printf '%s\n' 'Codex CLI is required. Install it first, then run this installer again.' >&2
  exit 127
fi
if ! command -v git >/dev/null 2>&1; then
  printf '%s\n' 'Git is required. Install it first, then run this installer again.' >&2
  exit 127
fi
codex plugin marketplace add QiminZhu/Skills
codex plugin add learn-tutor-plugin@anker-skills
printf '%s\n' 'Tutor me installed. Start a new Codex session to load its skills.'
