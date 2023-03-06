import os
import sys


def main() -> int:
    cmd = "explorer"
    if len(sys.argv) == 1:
        cmd += " ."
    print(cmd)
    return os.system(cmd)
