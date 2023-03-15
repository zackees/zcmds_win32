"""
Executes an elevated command in windows. Very tricky.
1. Powershell is used to execute a batch file as admin.
2. The batch file executes the command as admin.
3. The batch file executes a second batch file as a normal user which writes a file
   signaling that the command has finished.
"""

import atexit
import os
import shutil
from tempfile import TemporaryDirectory
import time


def write_utf8(path: str, content: str) -> None:
    """Write a file with utf-8 encoding."""
    with open(path, encoding="utf-8", mode="w") as f:
        f.write(content)


def elevated_exec(cmd: str) -> None:
    """Execute a command as admin."""

    with TemporaryDirectory(ignore_cleanup_errors=True) as tmpdir:

        def get_path(file: str) -> str:
            os.makedirs(tmpdir, exist_ok=True)
            path = os.path.join(tmpdir, file)
            out = os.path.abspath(path)
            return out

        write_bat_file = get_path("write.bat")
        run_bat_file = get_path("myrun.bat")
        ps1_file = get_path("run.ps1")
        done_txt = get_path("done.txt")

        atexit.register(lambda: shutil.rmtree(".tmp", True))

        write_cmd = f"""
        @echo off
        echo done > "{done_txt}"
        """

        # First execute the service as admin.
        # Then execute write.bat as a normal user, "done.txt" will appear.
        admin_cmd = f"""
        @echo off
        {cmd}
        runas /trustlevel:0x20000 "{write_bat_file}"
        """

        entrypoint_ps1 = f"""
        Start-Process -Verb runAs "{run_bat_file}"
        """

        write_utf8(write_bat_file, write_cmd)
        write_utf8(run_bat_file, admin_cmd)
        write_utf8(ps1_file, entrypoint_ps1)

        cmd = f'powershell -c "{os.path.abspath(ps1_file)}"'
        # print(cmd)
        os.system(cmd)
        # time.sleep(20)
        while not os.path.exists(write_bat_file):
            time.sleep(0.1)
