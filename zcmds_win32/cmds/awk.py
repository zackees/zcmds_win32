from zcmds_win32.unix_tool_path import unix_tool_exec

CMDNAME = "awk.exe"


def main() -> int:
    return unix_tool_exec(CMDNAME)
