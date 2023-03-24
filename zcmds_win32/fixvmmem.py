"""
Fixes the VMMem issue on Windows 10.
"""
import sys

from sudo_win32.elevated_exec import elevated_exec  # type: ignore


def main() -> int:
    """Main entry point."""
    return elevated_exec("taskkill /F /im wslservice.exe")


if __name__ == "__main__":
    sys.exit(main())
