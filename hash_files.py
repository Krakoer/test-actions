import argparse
import hashlib
import os
import sys
from pathlib import Path


def match_files(patterns: str) -> list[Path]:
    workspace = Path.cwd().resolve()
    include: list[str] = []
    exclude: list[str] = []

    for line in patterns.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("!"):
            exclude.append(line[1:])
        else:
            include.append(line)

    matched: set[Path] = set()
    for pattern in include:
        for hit in workspace.glob(pattern):
            resolved = hit.absolute()
            if not str(resolved).startswith(str(workspace) + os.sep):
                continue
            if resolved.is_dir():
                continue
            if hit.is_symlink():
                continue
            matched.add(resolved)

    for pattern in exclude:
        for hit in workspace.glob(pattern):
            resolved = hit.absolute()
            matched.discard(resolved)

    return sorted(matched)


def hash_files(patterns: str) -> str:
    files = match_files(patterns)
    if not files:
        return ""

    result = hashlib.sha256()
    for f in files:
        file_hash = hashlib.sha256()
        with open(f, "rb") as fh:
            for chunk in iter(lambda: fh.read(8192), b""):
                file_hash.update(chunk)
        result.update(file_hash.digest())

    print(f"Found {len(files)} file(s) to hash.", file=sys.stderr)
    return result.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute a deterministic hash of files matching glob patterns, "
        "compatible with GitHub Actions hashFiles().",
    )
    parser.add_argument(
        "patterns",
        help="Newline-separated glob patterns (prefix with ! to exclude). "
        "Use $'\\n' in shell for literal newlines.",
    )
    args = parser.parse_args()

    digest = hash_files(args.patterns)
    print(digest)


if __name__ == "__main__":
    main()
