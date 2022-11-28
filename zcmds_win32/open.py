from zcmds_win32._exec import os_exec

CMD = r"explorer"


def main() -> int:
    return os_exec(CMD)
