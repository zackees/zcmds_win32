
from zcmds_win32._exec import os_exec

CMDNAME = "python.exe"

def main() -> int:
    return os_exec(CMDNAME)


if __name__ == "__main__":
    main()
