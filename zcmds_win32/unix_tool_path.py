"""
Resolves the unix tool, either by finding it in PATH or by downloading it.
"""

import os
import shutil
from typing import Optional

from download import download  # type: ignore

from zcmds_win32._exec import os_exec

GIT_BIN = r"C:\Program Files\Git\usr\bin"
GIT_BIN_TOOL_URL = "https://github.com/zackees/zcmds_win32/raw/main/assets/git-bash-bin.zip"

HERE = os.path.abspath(os.path.dirname(__file__))
OUT_BIN = os.path.join(HERE, "git-bash-bin")


def get_or_fetch_unix_tool_path(name: str) -> Optional[str]:
    """Attempts to find the given Unix tool."""
    path = shutil.which(name)
    if path and os.path.basename(os.path.dirname(path)).lower() != "scripts":
        return path
    # add .exe to the name if it's not there
    if not name.lower().endswith(".exe"):
        name += ".exe"
    if os.path.exists(os.path.join(GIT_BIN, name)):
        return os.path.join(GIT_BIN, name)
    # else download
    download(GIT_BIN_TOOL_URL, OUT_BIN, replace=False, kind="zip")
    return os.path.join(OUT_BIN, name)


def unix_tool_exec(cmdname: str, inherit_params: bool = True, cwd: Optional[str] = None) -> int:
    """Executes the given Unix tool."""
    cmd = get_or_fetch_unix_tool_path(cmdname)
    if not cmd:
        raise FileNotFoundError(f"Could not find {cmdname} in PATH or in {GIT_BIN}")
    return os_exec(cmd, inherit_params, cwd)
