from zcmds_win32._exec import os_exec

CMD = r"where"


def main() -> int:
    return os_exec(CMD)
