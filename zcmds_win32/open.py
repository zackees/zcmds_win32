import os
import shutil
import sys

from zcmds_win32._exec import os_exec


def get_sublime() -> str | None:
    """Attempts to find the Sublime Text executable."""
    path = shutil.which("subl") or shutil.which("sublime_text")
    if path:
        return path
    for i in ["", "2", "3", "4"]:
        path = f"C:\\Program Files\\Sublime Text{i}\\sublime_text.exe"
        if os.path.exists(path):
            return path
    return None


def get_textpad() -> str | None:
    path = shutil.which("textpad")
    if path:
        return path
    for i in ["", "2", "3", "4", "5", "6", "7", "8"]:
        path = f"C:\\Program Files\\TextPad {i}\\TextPad.exe"
        if os.path.exists(path):
            return path
    return None


TEXT_EDITOR = get_textpad() or get_sublime()

SOURCE_EXTENSIONS = [
    ".c",
    ".cpp",
    ".cxx",
    ".cc",
    ".c++",
    ".h",
    ".hpp",
    ".hxx",
    ".hh",
    ".h++",
    ".py",
    ".kt",
    ".java",
    ".js",
    ".ts",
    ".html",
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".json",
    ".xml",
    ".yml",
    ".yaml",
    ".md",
    ".txt",
    ".bat",
    ".cmd",
    ".sh",
    ".ps1",
]


def handle_file(file: str) -> tuple[bool, int]:
    """Attempts to handle the file with a specific program."""
    ext = os.path.splitext(file)[1]
    if ext in SOURCE_EXTENSIONS:
        if TEXT_EDITOR:
            # empty quotes is for title.
            cmd = f'start "" "{TEXT_EDITOR}" "{file}"'
            rtn = os.system(cmd)
            return (True, rtn)
    return (False, 0)


def main() -> int:
    cmd = "explorer"
    if len(sys.argv) == 1:
        cmd += " ."
        return os.system(cmd)
    for i, _ in enumerate(sys.argv):
        if i < 1:
            continue
        arg = sys.argv[i].replace("/", "\\")
        sys.argv[i] = arg
        if os.path.isfile(arg):
            handled, ret = handle_file(arg)
            if handled:
                return ret
    return os_exec(cmd)
