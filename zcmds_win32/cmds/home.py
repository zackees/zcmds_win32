import os

from zcmds_win32._exec import os_exec

CMD = r"cmd"


def main() -> int:
    home_directory = os.path.expanduser("~")
    return os_exec(CMD, inherit_params=False, cwd=home_directory)
