# ================= DJANGO_and_VENV_CONF =====================
import utils
import constants as cnst
import os


def ensure_django_admin_installed():
    utils.run_command("pip install pipx")
    utils.run_command("pipx install django || echo 'django already installed with pipx'")


def ensure_project_created():
    if os.path.exists(cnst.MANAGE_PY_PATH):
        print("⚠️  manage.py вже існує. Пропускаємо створення Django-проєкту.")
        return
    utils.run_command(f'django-admin startproject {cnst.PROJECT_NAME} .', cwd=cnst.BASE_DIR)  # YES
    # utils.run_command(f'django-admin startproject {cnst.PROJECT_NAME} {cnst.TARGET_FOLDER}')  # Перевір!


def install_django_and_bootstrap_in_venv(pip_path):
    utils.run_command(f'"{pip_path}" install django')
    utils.run_command(f'"{pip_path}" install django-bootstrap-v5')


def ensure_venv_created():
    venv_name = ".venv"     # YES
    venv_path = os.path.join(cnst.BASE_DIR, venv_name)  # venv_name повинно бути Поряд з PROJECT_NAME!  # YES
    if not os.path.exists(venv_path):
        utils.run_command(f'py -m venv {venv_name}', cwd=cnst.BASE_DIR)    # YES
    else:
        print("⚠️  Віртуальне середовище вже існує. Пропускаємо створення.")
    
    return os.path.join(venv_path, "Scripts", "pip.exe"), os.path.join(venv_path, "Scripts", "python.exe")


# ================= APP =====================
def ensure_app_created(python_path):
    app_path = os.path.join(cnst.BASE_DIR, cnst.CREATE_APP) # YES
    if os.path.exists(app_path):
        print(f"⚠️  Django-застосунок '{cnst.CREATE_APP}' вже існує. Пропускаємо створення.")   # YES
        return
    
    utils.run_command(f'"{python_path}" "{cnst.MANAGE_PY_PATH}" startapp {cnst.CREATE_APP}', cwd=cnst.BASE_DIR)   # YES


def get_num_line_with_text():    
    with open(f'{cnst.SETTINGS_PY_PATH}', 'r') as file:   # YES
        lines = file.readlines()
        for num_line, line in enumerate(lines, 1):
            if 'INSTALLED_APPS' in line:
                # num_temp = num_line
                return num_line


def write_text_by_num_line():
    num_line_text = get_num_line_with_text()
    with open(f'{cnst.SETTINGS_PY_PATH}', 'r') as file:   # YES
        lines = file.readlines()

    if num_line_text is not None:
        lines.insert(num_line_text, f"    '{cnst.CREATE_APP}',\n    'bootstrap5',\n")  # YES

    with open(f'{cnst.SETTINGS_PY_PATH}', 'w') as file:  # YES
        file.writelines(lines)

    # Хіба це ефективно, - перезаписувати увесь файл?..


        # for num_line, line in enumerate(lines, 1):
        #     line += f"\n'{cnst.CREATE_APP}',\n'bootstrap5',\n"
        # f'INSTALLED_APPS += [{cnst.CREATE_APP}, bootstrap5]')
        # f.write(content)