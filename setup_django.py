import os
import sys
import subprocess
import platform
from  pathlib import Path


# # ------------------------------------
# # Old funcs:
# def get_os():
#     return platform.system()


# def is_file(path: Path) -> bool:
#     return path.is_file()
# # --------------------------------------

PROJECT_NAME = "my_prj"     # Change it!
CREATE_APP = "tutors_app"   # Change it!
VENV_NAME = ".venv"
TARGET_FOLDER = "."         # Current dir
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def run_command(command, cwd=None):
    try:
        print(f'-> {command}')
        subprocess.run(command, shell=True, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Помилка при виконанні команди: {command}")
        print(f"   Код завершення: {e.returncode}")
        sys.exit(1)


def main():
    pass


if __name__ == '__main__':
    main()