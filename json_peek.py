#!/usr/bin/env python3
"""Read and query JSON from the command line without jq."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def walk(value, parts: list[str]):
    for part in parts:
        if isinstance(value, list):
            value = value[int(part)]
        elif isinstance(value, dict):
            value = value[part]
        else:
            raise KeyError(part)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Read and query JSON from the command line without jq.")
    parser.add_argument("path", type=Path, nargs="?", help="JSON file (stdin if omitted)")
    parser.add_argument("--path", dest="json_path", default="", help="dotted path")
    parser.add_argument("--keys", action="store_true", help="print object keys")
    parser.add_argument("--compact", action="store_true", help="compact output")
    args = parser.parse_args()
    raw = args.path.read_text(encoding="utf-8") if args.path else sys.stdin.read()
    data = json.loads(raw)
    if args.json_path:
        try:
            data = walk(data, args.json_path.split("."))
        except (KeyError, IndexError, ValueError) as exc:
            print(f"path error: {exc}", file=sys.stderr)
            return 2
    if args.keys:
        if not isinstance(data, dict):
            print("selected value is not an object", file=sys.stderr)
            return 2
        for key in sorted(data):
            print(key)
        return 0
    indent = None if args.compact else 4
    print(json.dumps(data, ensure_ascii=False, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
