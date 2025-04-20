import subprocess
import sys
# import platform
# from  pathlib import Path


# # ------------------------------------
# # Old funcs:
# def get_os():
#     return platform.system()


# def is_file(path: Path) -> bool:
#     return path.is_file()
# # --------------------------------------


# # ================= CMD, OS, GIT =====================
def run_command(command, cwd=None):
    try:
        print(f'-> {command}')
        subprocess.run(command, shell=True, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Помилка при виконанні команди: {command}")
        print(f"   Код завершення: {e.returncode}")
        sys.exit(1)

    # --------------------- А чи не зробити декоратор з цих двох ф-цій?.. -------------------
def write_content_to_file(path_file, content, mode='a'):
    with open(path_file, mode) as f:  # mode == 'w' or 'a'
        f.write(content)


def write_to_gitignore():
    # Файл .gitignore — краще перевірити, чи рядки вже не існують, щоб уникнути дублювання.
    content = """
    *.txt
    my_prj/
    tutors_app/
    """
    with open('.gitignore', 'a') as f:
        f.write(content)