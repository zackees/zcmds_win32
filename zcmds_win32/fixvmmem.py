import os
import atexit
import time
import shutil

def get_path(file: str) -> str:
    os.makedirs(".tmp", exist_ok=True)
    path = os.path.join(".tmp", file)
    out = os.path.abspath(path)
    return out

WRITE_BAT_FILE = get_path("write.bat")
RUN_BAT_FILE = get_path("myrun.bat")
PS1_FILE = get_path("run.ps1")
DONE_TXT = get_path("done.txt")

atexit.register(lambda: shutil.rmtree(".tmp", True))

WRITE_CMD = f"""
@echo off
echo done > "{DONE_TXT}"
"""

# First execute the service as admin.
# Then execute write.bat as a normal user, "done.txt" will appear.
CMD = f"""
@echo off
taskkill /F /im wslservice.exe
runas /trustlevel:0x20000 "{WRITE_BAT_FILE}"
"""

ENTRYPOINT_PS1 = f"""
Start-Process -Verb runAs "{RUN_BAT_FILE}"
"""

def write_files() -> None:
    with open(WRITE_BAT_FILE, encoding="utf-8", mode="w") as f:
        f.write(WRITE_CMD)
    with open(RUN_BAT_FILE, encoding="utf-8", mode="w") as f:
        f.write(CMD)
    with open(PS1_FILE, encoding="utf-8", mode="w") as f:
        f.write(ENTRYPOINT_PS1)

def main() -> int:
    write_files()
    cmd = f'powershell -c "{os.path.abspath(PS1_FILE)}"'
    # print(cmd)
    os.system(cmd)
    # time.sleep(20)
    while not os.path.exists(WRITE_BAT_FILE):
        time.sleep(.1)


if __name__ == "__main__":
    exit(main())
