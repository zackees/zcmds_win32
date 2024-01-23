import argparse

from zcmds_win32.unix_tool_path import install


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install the Unix tools",
    )
    args = parser.parse_args()
    if args.install:
        install()
    return 0
