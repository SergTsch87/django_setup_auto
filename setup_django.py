import os
import sys
import subprocess
import constants as cnst

# cnst.PROJECT_NAME
# cnst.CREATE_APP
# cnst.VENV_NAME
# cnst.TARGET_FOLDER
# cnst.DIR_DJANGO
# cnst.BASE_DIR
# cnst.BASE_TEMPLATE_FILE
# cnst.EXTEND_TEMPLATE_FILE
# cnst.content_for_base_templ_file
# cnst.content_for_extend_templ_file


# ================= DJANGO_and_VENV_CONF =====================
def ensure_django_admin_installed():
    run_command("pip install pipx")
    run_command("pipx install django || echo 'django already installed with pipx'")


def ensure_project_created():
    manage_py_path = os.path.join(cnst.BASE_DIR, "manage.py")
    if os.path.exists(manage_py_path):
        print("⚠️  manage.py вже існує. Пропускаємо створення Django-проєкту.")
        return
    run_command(f'django-admin startproject {cnst.PROJECT_NAME}', cwd=cnst.DIR_DJANGO)
    # run_command(f'django-admin startproject {cnst.PROJECT_NAME} {cnst.TARGET_FOLDER}')


def install_django_and_bootstrap_in_venv(pip_path):
    run_command(f'"{pip_path}" install django')
    run_command(f'"{pip_path}" install django-bootstrap-v5')


def ensure_venv_created():
    venv_path = os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME, cnst.VENV_NAME)
    if not os.path.exists(venv_path):
        run_command(f'py -m venv {cnst.VENV_NAME}', cwd=os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME))
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
    run_command(f'"{python_path}" "{manage_py}" startapp {cnst.CREATE_APP}', cwd=cnst.BASE_DIR)


def get_num_line_with_text():
    # run_command(f'echo INSTALLED_APPS += \'{cnst.CREATE_APP},\' >> {cnst.PROJECT_NAME}/settings.py')
    # run_command(f'echo INSTALLED_APPS += \'bootstrap5,\' >> {cnst.PROJECT_NAME}/settings.py')
    # write_content_to_file(f'{cnst.PROJECT_NAME}/settings.py', f'INSTALLED_APPS += [{cnst.CREATE_APP}, bootstrap5]')
    # num_temp = 0
    with open(f'{cnst.PROJECT_NAME}/settings.py', 'r') as file:
        lines = file.readlines()
        for num_line, line in enumerate(lines, 1):
            if 'INSTALLED_APPS' in line:
                # num_temp = num_line
                return num_line


def write_text_by_num_line():
    num_line_text = get_num_line_with_text()
    with open(f'{cnst.PROJECT_NAME}/settings.py', 'r') as file:
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


# ================= TEMPLATE =====================
def ensure_template_dir_created():
    template_path = os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME, cnst.CREATE_APP, 'templates', cnst.CREATE_APP)
    if os.path.exists(template_path):
        print(f"⚠️  Django-шаблон templates/'{cnst.CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    # manage_py = os.path.join(cnst.BASE_DIR, "manage.py")
    
    # run_command(f'mkdir {template_path}')
    os.makedirs(template_path, exist_ok=True)


def ensure_template_file_created(path_file, content):
    with open(path_file, 'w') as f:
        f.write(content)
    # with open(cnst.BASE_TEMPLATE_FILE, 'w'):   # Створює порожній файл
    #     pass
    
    # extend_template = '{% extends "base.html" %}'
    # with open(cnst.EXTEND_TEMPLATE_FILE, 'w') as f:
    #     f.write(extend_template)
    

# ================= VIEWS =====================
def append_to_cbv_py():
    views_path = os.path.join(cnst.BASE_DIR, cnst.CREATE_APP, 'views.py')
    content = f"""
    # with templates
    # Class-Based View (CBV):
    from django.views.generic import TemplateView


    class HomeView(TemplateView):
        template_name = '{cnst.EXTEND_TEMPLATE_FILE}'
    """

    with open(views_path, 'a') as f:
        f.write(content)
    print(f"✅ CBV додано до {views_path}")
    # run_command(f'echo {content_view} >> {cnst.CREATE_APP}/views.py')


# ================= URLS =====================
# Створює app/urls.py з відповідним вмістом
def create_urls_py_app_cbv():
    content_urls_with_cbv = """
    # with templates
    # # Class-Based View (CBV):
    # from tutors_app.views import HomeView
    from django.urls import path
    from .views import HomeView


    urlpatterns = [
        path('', HomeView.as_view(), name='home'),
    ]
    """
    
    write_content_to_file(f'{cnst.CREATE_APP}/urls.py', content_urls_with_cbv, mode='a')
    # run_command(f'echo {content_urls_with_cbv} > {cnst.PROJECT_NAME}/urls.py')


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    # run_command(f'type nul > {cnst.CREATE_APP}/urls.py')
    content_urls_prj_cbv = f"""
    # For CBV
    from django.contrib import admin
    from django.urls import path, include
    # from django.views.generic import TemplateView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include({cnst.CREATE_APP}.urls)),   # app.urls
        # path("extend/", TemplateView.as_view(template_name="extend.html")),
    ]
    """
    write_content_to_file(f'{cnst.PROJECT_NAME}/urls.py', content_urls_prj_cbv, mode='a')
    # run_command(f'echo {content_urls_app_cbv} > {cnst.CREATE_APP}/urls.py')


# ================= MAIN =====================
def main():
    os.makedirs(cnst.DIR_DJANGO, exist_ok=True)
    ensure_django_admin_installed()   # Встановлює pipx та django
    ensure_project_created()          # Створює Django-проєкт. Інакше - минає цей етап
    pip_path, python_path = ensure_venv_created()  # Створює venv
    install_django_and_bootstrap_in_venv(pip_path)
    ensure_app_created(python_path)   # Створює Django-застосунок. Інакше - минає цей етап
    write_text_by_num_line()
    print("\n✅ Готово! Django-проєкт і застосунок створено успішно.")

    # + додай можливість одразу створити шаблони, view, route або підключити Bootstrap
    ensure_template_dir_created()         # Створює Django-шаблон. Інакше - минає цей етап
    
    # Створює HTML-файли Django-шаблону зі шляхом path_file та вмістом content
    ensure_template_file_created(cnst.BASE_TEMPLATE_FILE, cnst.content_for_base_templ_file)
    ensure_template_file_created(cnst.EXTEND_TEMPLATE_FILE, cnst.content_for_extend_templ_file)
    
    append_to_cbv_py()                    # Дописує CBV-функцію до view
    append_to_urls_py_cbv()               # Дописує route до списку urlpatterns файлу prj/urls.py
    create_urls_py_app_cbv()              # Створює app/urls.py з відповідним вмістом

    # write_to_gitignore()                  # Розкоментуй, коли тре буде пушити Django-проєкт


if __name__ == '__main__':
    main()