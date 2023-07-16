import os
import shutil
from tempfile import TemporaryDirectory
from typing import Optional

from download import download  # type: ignore

HERE = os.path.abspath(os.path.dirname(__file__))

DOWNLOAD_DIR = os.path.join(HERE, "downloads")


def install(tool_url: str, dst_dir: str) -> None:
    """Installs the Unix tools."""
    with TemporaryDirectory() as tmpdir:
        download(tool_url, tmpdir, replace=True, kind="zip")
        os.makedirs(dst_dir, exist_ok=True)
        shutil.rmtree(dst_dir, ignore_errors=True)
        shutil.copytree(tmpdir, dst_dir)


def get_or_fetch_tool(toolname: str, tooldir, url: str) -> Optional[str]:
    """Attempts to find the given Unix tool."""
    path = shutil.which(toolname)
    if path and os.path.basename(os.path.dirname(path)).lower() != "scripts":
        return path
    # add .exe to the name if it's not there
    if not toolname.lower().endswith(".exe"):
        toolname += ".exe"
    expected_path = os.path.join(tooldir, toolname)
    if os.path.exists(expected_path):
        return os.path.join(tooldir, toolname)
    if not os.path.exists(expected_path):
        install(url, tooldir)
    return os.path.join(tooldir, toolname)


def main() -> int:
    toolname = "dig.exe"
    tooldir = os.path.join(HERE, "downloads", "dig_dl.9.0.5")
    url = "https://github.com/zackees/zcmds_win32/raw/main/assets/dig-for-windows-9.9.5-W1.zip"
    path = get_or_fetch_tool(toolname, tooldir, url)
    print(path)
    assert path == os.path.join(tooldir, toolname)
    print("OK")
    return 0


if __name__ == "__main__":
    main()
