import os

from typing import Optional

from zcmds_win32.unix_tool_path import unix_tool_exec

from zcmds_win32.install_tool import get_or_fetch_tool, DOWNLOAD_DIR
from zcmds_win32._exec import os_exec



TOOL = "dig.exe"
# DIR = os.path.join(HERE, "downloads", "dig_dl.9.0.5")
DEST_DIR = os.path.join(DOWNLOAD_DIR, "dig_dl.9.0.5")
URL = "https://github.com/zackees/zcmds_win32/raw/main/assets/dig-for-windows-9.9.5-W1.zip"


def main() -> int:
    path = get_or_fetch_tool(toolname=TOOL, tooldir=DEST_DIR, url=URL)
    # os.system(f"{path} +short myip.opendns.com @resolver1.opendns.com")
    return os_exec(cmd=path, inherit_params=True, cwd=None)

if __name__ == "__main__":
    main()
