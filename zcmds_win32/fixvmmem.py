import os
import atexit
import time

CMD = 'taskkill /F /im wslservice.exe'
BAT_FILE = os.path.abspath("fixmme.bat")

def main() -> int:
    with open(BAT_FILE, encoding="utf-8", mode="w") as f:
        f.write(CMD)
    atexit.register(os.remove, BAT_FILE)
    cmd = f"""powershell -c "Start-Process Powershell -Verb runAs '{BAT_FILE}'" """
    print(cmd)
    os.system(cmd)
    time.sleep(20)


if __name__ == "__main__":
    exit(main())
