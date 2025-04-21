# ================= DJANGO_and_VENV_CONF =====================
import utils as utls
import constants as cnst
import os


def ensure_django_admin_installed():
    utls.run_command("pip install pipx")
    utls.run_command("pipx install django || echo 'django already installed with pipx'")


def ensure_project_created():
    manage_py_path = os.path.join(cnst.BASE_DIR, "manage.py")
    if os.path.exists(manage_py_path):
        print("⚠️  manage.py вже існує. Пропускаємо створення Django-проєкту.")
        return
    utls.run_command(f'django-admin startproject {cnst.PROJECT_NAME}', cwd=cnst.DIR_DJANGO)
    # utls.run_command(f'django-admin startproject {cnst.PROJECT_NAME} {cnst.TARGET_FOLDER}')


def install_django_and_bootstrap_in_venv(pip_path):
    utls.run_command(f'"{pip_path}" install django')
    utls.run_command(f'"{pip_path}" install django-bootstrap-v5')


def ensure_venv_created():
    venv_path = os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME, cnst.VENV_NAME)
    if not os.path.exists(venv_path):
        utls.run_command(f'py -m venv {cnst.VENV_NAME}', cwd=os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME))
    else:
        print("⚠️  Віртуальне середовище вже існує. Пропускаємо створення.")
    
    return os.path.join(venv_path, "Scripts", "pip.exe"), os.path.join(venv_path, "Scripts", "python.exe")


# ================= APP =====================
def ensure_app_created(python_path):
    app_path = os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME, cnst.CREATE_APP)
    if os.path.exists(app_path):
        print(f"⚠️  Django-застосунок '{cnst.CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    manage_py = os.path.join(cnst.BASE_DIR, "manage.py")
    utls.run_command(f'"{python_path}" "{manage_py}" startapp {cnst.CREATE_APP}', cwd=cnst.BASE_DIR)


def get_num_line_with_text():
    # utls.run_command(f'echo INSTALLED_APPS += \'{cnst.CREATE_APP},\' >> {cnst.PROJECT_NAME}/settings.py')
    # utls.run_command(f'echo INSTALLED_APPS += \'bootstrap5,\' >> {cnst.PROJECT_NAME}/settings.py')
    # utls.write_content_to_file(f'{cnst.PROJECT_NAME}/settings.py', f'INSTALLED_APPS += [{cnst.CREATE_APP}, bootstrap5]')
    # num_temp = 0
    
    # with open(f'{cnst.PROJECT_NAME}/settings.py', 'r') as file:
    with open(f'{cnst.BASE_DIR}/settings.py', 'r') as file:
        lines = file.readlines()
        for num_line, line in enumerate(lines, 1):
            if 'INSTALLED_APPS' in line:
                # num_temp = num_line
                return num_line


def write_text_by_num_line():
    num_line_text = get_num_line_with_text()
    # with open(f'{cnst.PROJECT_NAME}/settings.py', 'r') as file:
    with open(f'{cnst.BASE_DIR}/settings.py', 'r') as file:
        lines = file.readlines()

    if num_line_text is not None:
        lines.insert(num_line_text, f"    '{cnst.CREATE_APP}',\n    'bootstrap5',\n")

    with open(f'{cnst.PROJECT_NAME}/settings.py', 'w') as file:
        file.writelines(lines)

    # Хіба це ефективно, - перезаписувати увесь файл?..


        # for num_line, line in enumerate(lines, 1):
        #     line += f"\n'{cnst.CREATE_APP}',\n'bootstrap5',\n"
        # f'INSTALLED_APPS += [{cnst.CREATE_APP}, bootstrap5]')
        # f.write(content)