#!/usr/bin/env python3
"""Preview or install the optional NR hooks without changing other hook definitions."""
import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import sys
import tempfile
from datetime import datetime, timezone


def updated_config(config, command):
    if not isinstance(config, dict) or not isinstance(config.get("hooks", {}), dict):
        raise ValueError("hooks configuration must be an object")
    result = json.loads(json.dumps(config))
    hooks = result.setdefault("hooks", {})
    for event in ("UserPromptSubmit", "Stop"):
        groups = hooks.setdefault(event, [])
        if not isinstance(groups, list):
            raise ValueError(f"{event} must contain a list")
        if any(h.get("command") == command for g in groups for h in g.get("hooks", [])):
            continue
        groups.append({"hooks": [{"type": "command", "command": command, "timeout": 5,
                                  "statusMessage": "Checking NR summary"}]})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path.home() / ".codex" / "hooks.json")
    parser.add_argument("--apply", action="store_true", help="Write after making a backup; default is preview")
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text()) if args.config.exists() else {}
        command = shlex.join([sys.executable, str(Path(__file__).resolve().with_name("nr_hook.py"))])
        updated = updated_config(config, command)
        content = json.dumps(updated, ensure_ascii=False, indent=2) + "\n"
        if not args.apply:
            print(content, end="")
            return 0
        if updated == config:
            print("NR hook definitions already present; trust status is managed by Codex /hooks.")
            return 0
        args.config.parent.mkdir(parents=True, exist_ok=True)
        if args.config.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = args.config.with_name(args.config.name + "." + stamp + ".bak")
            shutil.copy2(args.config, backup)
            print(f"Backup: {backup}")
        fd, name = tempfile.mkstemp(dir=args.config.parent)
        try:
            with os.fdopen(fd, "w") as stream:
                stream.write(content)
            os.replace(name, args.config)
        finally:
            Path(name).unlink(missing_ok=True)
        print(f"Configured: {args.config}. Review and trust these definitions with /hooks in Codex.")
        return 0
    except (OSError, ValueError, AttributeError, TypeError) as error:
        print(f"NR hook installation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
