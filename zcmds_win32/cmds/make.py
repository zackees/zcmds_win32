"""
Installs and runs the `make` command on Windows.
This one is a little difficult because the binary is located in bin/make.exe
"""

import os
import shutil
from tempfile import TemporaryDirectory
from typing import Optional

from download import download  # type: ignore

from zcmds_win32._exec import os_exec
from zcmds_win32.install_tool import DOWNLOAD_DIR

CMDNAME = "make.exe"
URL = "https://github.com/zackees/zcmds_win32/raw/main/assets/make-3.81-bin.zip"
DEST_DIR = os.path.join(DOWNLOAD_DIR, "make")


HERE = os.path.abspath(os.path.dirname(__file__))

DOWNLOAD_DIR = os.path.join(HERE, "downloads")


def _install(tool_url: str, dst_dir: str) -> None:
    """Installs the Unix tools."""
    with TemporaryDirectory() as tmpdir:
        download(tool_url, tmpdir, replace=True, kind="zip")
        os.makedirs(dst_dir, exist_ok=True)
        shutil.rmtree(dst_dir, ignore_errors=True)
        shutil.copytree(tmpdir, dst_dir)


def _get_or_fetch_tool(tooldir: str, url: str) -> Optional[str]:
    """Attempts to find the given Unix tool."""
    path = shutil.which(CMDNAME)
    if path and os.path.basename(os.path.dirname(path)).lower() != "scripts":
        return path
    # add .exe to the name if it's not there
    expected_path = os.path.join(tooldir, "bin", CMDNAME)
    if os.path.exists(expected_path):
        return expected_path
    if not os.path.exists(expected_path):
        _install(url, tooldir)
    return os.path.join(tooldir, "bin", CMDNAME)


def main() -> int:
    path = _get_or_fetch_tool(tooldir=DEST_DIR, url=URL)
    assert path
    return os_exec(cmd=path, inherit_params=True, cwd=None)


if __name__ == "__main__":
    main()
