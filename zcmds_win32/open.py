import os
import sys
from zcmds_win32._exec import os_exec


def main() -> int:
    cmd = "explorer"
    if len(sys.argv) == 1:
        cmd += " ."
        return os.system(cmd)
    for i, _ in enumerate(sys.argv):
        if i < 1:
            continue
        arg = sys.argv[i].replace("/", "\\")
        sys.argv[i] = arg
    return os_exec(cmd)
