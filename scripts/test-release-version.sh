#!/usr/bin/env bash
set -euo pipefail

script="$(cd "$(dirname "$0")" && pwd)/verify-version-release.sh"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
printf '1.2.3\n' > "$tmp/VERSION"
"$script" "$tmp/VERSION" v1.2.3
if "$script" "$tmp/VERSION" v1.2.4 2>/dev/null; then
  echo "mismatch was accepted" >&2
  exit 1
fi
echo "Release version tests passed"
