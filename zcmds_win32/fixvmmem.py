"""
Fixes the VMMem issue on Windows 10.
"""

from sudo_win32.elevated_exec import elevated_exec


def main() -> int:
    """Main entry point."""
    elevated_exec("taskkill /F /im wslservice.exe")


if __name__ == "__main__":
    exit(main())
