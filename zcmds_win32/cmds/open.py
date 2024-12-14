import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from typing import Optional

from zcmds_win32._exec import os_exec


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="*", help="Path to open.", default=".")
    parser.add_argument("--text", action="store_true", help="Open in text editor.")
    return parser.parse_args()


@dataclass
class Program:
    path: str
    args: list[str]


def get_sublime() -> Optional[Program]:
    """Attempts to find the Sublime Text executable."""
    path = shutil.which("subl") or shutil.which("sublime_text")
    args = ["-n"]
    if path:
        return Program(path, args)
    for i in ["", "2", "3", "4"]:
        path = f"C:\\Program Files\\Sublime Text{i}\\sublime_text.exe"
        if os.path.exists(path):
            return Program(path, args)
    return None


def get_textpad() -> Optional[Program]:
    path = shutil.which("textpad")
    if path:
        return Program(path, [])
    for i in ["", "2", "3", "4", "5", "6", "7", "8"]:
        path = f"C:\\Program Files\\TextPad {i}\\TextPad.exe"
        if os.path.exists(path):
            return Program(path, [])
    return None


def get_notepad() -> Optional[Program]:
    path = shutil.which("notepad")
    if path:
        return Program(path, [])
    path = "C:\\Windows\\System32\\notepad.exe"
    if os.path.exists(path):
        return Program(path, [])
    return None


TEXT_EDITOR = get_sublime() or get_textpad() or get_notepad()

TEXT_EXTENSIONS = [
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
    ".pub",
    ".pem",
    ".key",
    ".crt",
    ".cer",
    ".pfx",
    ".toml",
]

IMAGE_EXTENSIONS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".ico",
    ".webp",
    ".svg",
]


def _has_text_encoding(file: str) -> bool:
    encodings = ["utf-8", "utf-16", "utf-32", "ascii", "latin-1", "cp1252"]
    for encoding in encodings:
        try:
            with open(file, "rb") as f:
                f.read().decode(encoding)
            return True
        except UnicodeDecodeError:
            pass
    return False


def handle_file(file: str, force_text=False) -> tuple[bool, int]:
    """Attempts to handle the file with a specific program."""
    ext = os.path.splitext(file)[1]
    file_uses_text_encoding = _has_text_encoding(file)
    if (
        force_text
        or ext.lower() in TEXT_EXTENSIONS
        or ext.lower() == ""
        and file_uses_text_encoding
    ):
        if TEXT_EDITOR:
            # empty quotes is for title.
            args_statement = " ".join(TEXT_EDITOR.args)
            cmd = f'start "" "{TEXT_EDITOR.path}" {args_statement} "{file}"'
            rtn = os.system(cmd)
            return (True, rtn)
    if ext.lower() in IMAGE_EXTENSIONS:
        cmd = f'explorer "{file}"'
        rtn = os.system(cmd)
        return (True, rtn)
    return (False, 0)


def git_bash_path_to_windows(path: str) -> str:
    if path.startswith("/"):
        drive = path[1].upper()
        return drive + ":" + path[2:].replace("/", "\\")
    else:
        return path


def main() -> int:
    cmd = "explorer"
    args = parse_args()
    path = args.path
    force_text = args.text
    if len(sys.argv) == 1:
        cmd += " " + path
        return os.system(cmd)
    for i, _ in enumerate(sys.argv):
        if i < 1:
            continue
        arg = git_bash_path_to_windows(sys.argv[i])
        arg = arg.replace("\\\\", "\\")
        sys.argv[i] = arg
        if os.path.isfile(arg):
            handled, ret = handle_file(arg, force_text=force_text)
            if handled:
                return ret
    arg = sys.argv[1]
    if arg == ".":
        return os.system("explorer .")
    return os_exec(cmd)


def unit_test() -> None:
    """Unit test for this module."""
    # target = r"C:\Users\niteris\dev\StatsDashPublic\www\src\assets\preview_image.webp"
    main()


if __name__ == "__main__":
    unit_test()
