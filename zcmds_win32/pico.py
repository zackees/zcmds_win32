from zcmds_win32._exec import os_exec

CMD = r"C:\Program Files\Git\usr\bin\nano.exe"


def main() -> int:
    return os_exec(CMD)
