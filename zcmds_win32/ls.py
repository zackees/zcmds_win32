from zcmds_win32.unix_tool_path import unix_tool_exec

CMDNAME = "ls.exe"


def main() -> int:
    return unix_tool_exec(CMDNAME)


if __name__ == "__main__":
    main()
