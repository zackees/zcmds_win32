from zcmds_win32.unix_tool_path import unix_tool_exec

CMDNAME = "arch.exe"


def main() -> int:
    return unix_tool_exec(CMDNAME)
