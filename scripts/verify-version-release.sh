#!/usr/bin/env bash
set -euo pipefail

version_file="${1:-VERSION}"
tag="${2:-${GITHUB_REF_NAME:-}}"

if [[ -z "$tag" ]]; then
  echo "Usage: $0 VERSION_FILE TAG" >&2
  exit 2
fi
if [[ ! -f "$version_file" ]]; then
  echo "Missing version file: $version_file" >&2
  exit 1
fi
version="$(tr -d '[:space:]' < "$version_file")"
if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid semantic version in $version_file: $version" >&2
  exit 1
fi
expected="v$version"
if [[ "$tag" != "$expected" ]]; then
  echo "Tag $tag does not match $version_file ($expected)" >&2
  exit 1
fi
echo "Version check passed: $tag"
