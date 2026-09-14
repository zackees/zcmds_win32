"""
Prints the environment variables, sorted, with PATH listed one entry per line.
"""

import os


def main() -> int:
    """Prints the environment variables."""
    paths = None
    for key, val in sorted(os.environ.items(), key=lambda item: item[0].lower()):
        if key.lower() == "path":
            paths = val
            continue
        print(f"{key}={val}")
    if paths is not None:
        print("PATH:")
        for path in paths.split(os.pathsep):
            print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
