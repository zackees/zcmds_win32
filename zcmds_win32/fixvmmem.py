import os
from subprocess import check_output


def main() -> int:
    current_user = check_output("whoami", shell=True).decode("utf-8").strip()
    cmd = f'runas /user:"{current_user}" "taskkill /F /im wslservice.exe"'
    return os.system(cmd)


if __name__ == "__main__":
    exit(main())
