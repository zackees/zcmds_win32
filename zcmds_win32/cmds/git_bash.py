from zcmds_win32.unix_tool_path import unix_tool_exec
import os

CMDNAME = "bash.exe"

GIT_BIN = r"C:\Program Files\Git\usr\bin"

ENV = os.environ.copy()
ENV["PATH"] = f"{GIT_BIN};{ENV['PATH']}"
os.environ.update(ENV)


def main() -> int:
    return unix_tool_exec(
        CMDNAME,
    )
