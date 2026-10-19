#!/usr/bin/env python3
"""Reject OS metadata in the Git index and the Pages source directory."""

import json
from pathlib import Path, PurePosixPath
import subprocess
import sys


def is_metadata(path):
    mac_names = {
        ".DS_Store", ".AppleDouble", ".LSOverride", ".Spotlight-V100",
        ".Trashes", "__MACOSX",
    }
    windows_names = {
        "thumbs.db", "thumbs.db:encryptable", "ehthumbs.db",
        "ehthumbs_vista.db", "desktop.ini",
    }
    return any(
        part in mac_names or part.startswith("._") or part.lower() in windows_names
        for part in PurePosixPath(path).parts
    )


def main():
    root = Path(__file__).resolve().parents[1]
    # NUL delimiters preserve spaces, Unicode, and newlines in filenames.
    tracked = subprocess.check_output(
        ["git", "ls-files", "--cached", "-z"], cwd=root
    ).decode("utf-8", errors="surrogateescape").split("\0")
    blocked = {path for path in tracked if path and is_metadata(path)}
    # Also catch ignored local metadata before a directory is packaged manually.
    blocked.update(
        path.relative_to(root).as_posix()
        for path in (root / "docs").rglob("*")
        if is_metadata(path.relative_to(root).as_posix())
    )
    if blocked:
        print("OS metadata must be removed before publishing:", file=sys.stderr)
        for path in sorted(blocked):
            print("  " + json.dumps(path, ensure_ascii=False), file=sys.stderr)
        return 1
    print("OK: no OS metadata in tracked files or the docs directory.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
