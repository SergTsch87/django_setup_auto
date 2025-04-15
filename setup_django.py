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


def ensure_django_admin_installed():
    run_command("pip install pipx")
    run_command("pipx install django || echo 'django already installed with pipx'")


def ensure_project_created():
    manage_py_path = os.path.join(BASE_DIR, "manage.py")
    if os.path.exists(manage_py_path):
        print("⚠️  manage.py вже існує. Пропускаємо створення Django-проєкту.")
        return
    run_command(f'django-admin startproject {PROJECT_NAME} {TARGET_FOLDER}')


def ensure_venv_created():
    venv_path = os.path.join(BASE_DIR, PROJECT_NAME, VENV_NAME)
    if not os.path.exists(venv_path):
        run_command(f'py -m venv {VENV_NAME}', cwd=os.path.join(BASE_DIR, PROJECT_NAME))
    else:
        print("⚠️  Віртуальне середовище вже існує. Пропускаємо створення.")
    return os.path.join(venv_path, "Scripts", "pip.exe"), os.path.join(venv_path, "Scripts", "python.exe")


def main():
    pass


if __name__ == '__main__':
    main()