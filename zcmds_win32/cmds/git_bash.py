import os

from zcmds_win32.unix_tool_path import unix_tool_exec

CMDNAME = "bash.exe"

GIT_BIN = r"C:\Program Files\Git\usr\bin"

ENV = os.environ.copy()
OS_PATH_SEP = os.pathsep
ENV["PATH"] = f"{GIT_BIN}{OS_PATH_SEP}{ENV['PATH']}"
os.environ.update(ENV)


def main() -> int:
    return unix_tool_exec(
        CMDNAME,
    )
