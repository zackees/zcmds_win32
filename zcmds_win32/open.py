import os
import sys
from zcmds_win32._exec import os_exec


def main() -> int:
    cmd = "explorer"
    if len(sys.argv) == 1:
        cmd += " ."
        return os.system(cmd)
    return os_exec(cmd)
