import os
import sys
import subprocess
# import platform
# from  pathlib import Path


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
BASE_TEMPLATE_FILE = 'base.html'   # parent template
EXTEND_TEMPLATE_FILE = 'extend.html'   # with extend template from base.html


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


def install_django_in_venv(pip_path):
    run_command(f'"{pip_path}" install django')


def ensure_app_created(python_path):
    app_path = os.path.join(BASE_DIR, PROJECT_NAME, CREATE_APP)
    # !!! Але ж, папка Застосунку знаходиться Поряд з папкою Проєкту, - то ж, чи не буде правильним таке?:
    # app_path = os.path.join(BASE_DIR, CREATE_APP)
    if os.path.exists(app_path):
        print(f"⚠️  Django-застосунок '{CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    manage_py = os.path.join(BASE_DIR, "manage.py")
    run_command(f'"{python_path}" "{manage_py}" startapp {CREATE_APP}', cwd=BASE_DIR)


def ensure_template_dir_created():
    template_path = os.path.join(BASE_DIR, PROJECT_NAME, CREATE_APP, 'templates', CREATE_APP)
    if os.path.exists(template_path):
        print(f"⚠️  Django-шаблон templates/'{CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    # manage_py = os.path.join(BASE_DIR, "manage.py")
    extend_template = '{% extends "base.html" %}'
    run_command(f'mkdir {template_path}; type nul > {BASE_TEMPLATE_FILE}; type nul > {EXTEND_TEMPLATE_FILE}; echo "{extend_template}" > {EXTEND_TEMPLATE_FILE}')


def append_to_cbv_py():
    content_view = f"""
    # with templates
    # # Class-Based View (CBV):
    from django.views.generic import TemplateView


    class HomeView(TemplateView):
        template_name = '{CREATE_APP}/{EXTEND_TEMPLATE_FILE}'
    """
    run_command(f'echo {content_view} >> {CREATE_APP}/views.py')


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    content_urls_with_cbv = """
    # with templates
    # # Class-Based View (CBV):
    from tutors_app.views import HomeView


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', HomeView.as_view(), name='home'),
    ]
    """
    run_command(f'echo {content_urls_with_cbv} > {PROJECT_NAME}/urls.py')


# Створює app/urls.py з відповідним вмістом
def create_urls_py_app_cbv():
    run_command(f'type nul > {CREATE_APP}/urls.py')
    content_urls_app_cbv = """
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]
    """
    run_command(f'echo {content_urls_app_cbv} > {CREATE_APP}/urls.py')


def main():
    ensure_django_admin_installed()   # Встановлює pipx та django
    ensure_project_created()          # Створює Django-проєкт. Інакше - минає цей етап
    pip_path, python_path = ensure_venv_created()  # Створює venv
    install_django_in_venv(pip_path)
    ensure_app_created(python_path)   # Створює Django-застосунок. Інакше - минає цей етап
    print("\n✅ Готово! Django-проєкт і застосунок створено успішно.")

    # додай можливість одразу створити шаблони, view, route або підключити Bootstrap
    ensure_template_dir_created()         # Створює Django-шаблон з кількома HTML-файлами. Інакше - минає цей етап
    append_to_cbv_py()                    # Дописує CBV-функцію до view
    append_to_urls_py_cbv()               # Дописує route до списку urlpatterns файлу prj/urls.py
    create_urls_py_app_cbv()              # Створює app/urls.py з відповідним вмістом


if __name__ == '__main__':
    main()