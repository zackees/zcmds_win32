from zcmds_win32.unix_tool_path import unix_tool_exec

CMDNAME = "uniq.exe"


def main() -> int:
    return unix_tool_exec(CMDNAME)
