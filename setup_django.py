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
# ========= CONSTANTS ========= 
# !!! Мо, константи краще винести до иншого файлу?.. Як саме це краще зробити?

PROJECT_NAME = "my_prj"     # Change it!
CREATE_APP = "tutors_app"   # Change it!
VENV_NAME = ".venv"
TARGET_FOLDER = "."         # Current dir

DIR_DJANGO = os.path.abspath('./root_prj/')
BASE_DIR = os.path.join(DIR_DJANGO, PROJECT_NAME)
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

BASE_TEMPLATE_FILE = 'base.html'   # parent template
EXTEND_TEMPLATE_FILE = 'extend.html'   # with extend template from base.html

content_for_base_templ_file = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

content_for_extend_templ_file = """
{% extends "base.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
"""

# ================= CMD, OS, GIT =====================
def run_command(command, cwd=None):
    try:
        print(f'-> {command}')
        subprocess.run(command, shell=True, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Помилка при виконанні команди: {command}")
        print(f"   Код завершення: {e.returncode}")
        sys.exit(1)

    # --------------------- А чи не зробити декоратор з цих двох ф-цій?.. -------------------
def write_content_to_file(path_file, content, mode='a'):
    with open(path_file, mode) as f:  # mode == 'w' or 'a'
        f.write(content)


def write_to_gitignore():
    content = """
    *.txt
    my_prj/
    tutors_app/
    """
    with open('.gitignore', 'a') as f:
        f.write(content)


# ================= DJANGO_and_VENV_CONF =====================
def ensure_django_admin_installed():
    run_command("pip install pipx")
    run_command("pipx install django || echo 'django already installed with pipx'")


def ensure_project_created():
    manage_py_path = os.path.join(BASE_DIR, "manage.py")
    if os.path.exists(manage_py_path):
        print("⚠️  manage.py вже існує. Пропускаємо створення Django-проєкту.")
        return
    run_command(f'django-admin startproject {PROJECT_NAME}', cwd=DIR_DJANGO)
    # run_command(f'django-admin startproject {PROJECT_NAME} {TARGET_FOLDER}')


def install_django_and_bootstrap_in_venv(pip_path):
    run_command(f'"{pip_path}" install django')
    run_command(f'"{pip_path}" install django-bootstrap-v5')


def ensure_venv_created():
    venv_path = os.path.join(BASE_DIR, PROJECT_NAME, VENV_NAME)
    if not os.path.exists(venv_path):
        run_command(f'py -m venv {VENV_NAME}', cwd=os.path.join(BASE_DIR, PROJECT_NAME))
    else:
        print("⚠️  Віртуальне середовище вже існує. Пропускаємо створення.")
    return os.path.join(venv_path, "Scripts", "pip.exe")
    
    # А тут, мабуть, помилка:
    # return os.path.join(venv_path, "Scripts", "pip.exe"), os.path.join(venv_path, "Scripts", "python.exe")


# ================= APP =====================
def ensure_app_created(python_path):
    app_path = os.path.join(BASE_DIR, PROJECT_NAME, CREATE_APP)
    if os.path.exists(app_path):
        print(f"⚠️  Django-застосунок '{CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    manage_py = os.path.join(BASE_DIR, "manage.py")
    run_command(f'"{python_path}" "{manage_py}" startapp {CREATE_APP}', cwd=BASE_DIR)


def get_num_line_with_text():
    # run_command(f'echo INSTALLED_APPS += \'{CREATE_APP},\' >> {PROJECT_NAME}/settings.py')
    # run_command(f'echo INSTALLED_APPS += \'bootstrap5,\' >> {PROJECT_NAME}/settings.py')
    # write_content_to_file(f'{PROJECT_NAME}/settings.py', f'INSTALLED_APPS += [{CREATE_APP}, bootstrap5]')
    # num_temp = 0
    with open(f'{PROJECT_NAME}/settings.py', 'r') as file:
        lines = file.readlines()
        for num_line, line in enumerate(lines, 1):
            if 'INSTALLED_APPS' in line:
                # num_temp = num_line
                return num_line


def write_text_by_num_line():
    num_line_text = get_num_line_with_text()
    with open(f'{PROJECT_NAME}/settings.py', 'a') as file:
        lines = file.writelines()
        for num_line, line in enumerate(lines, 1):
            if num_line == num_line_text:
                line += f"\n'{CREATE_APP}',\n'bootstrap5',\n"
        # f'INSTALLED_APPS += [{CREATE_APP}, bootstrap5]')
        # f.write(content)


# ================= TEMPLATE =====================
def ensure_template_dir_created():
    template_path = os.path.join(BASE_DIR, PROJECT_NAME, CREATE_APP, 'templates', CREATE_APP)
    if os.path.exists(template_path):
        print(f"⚠️  Django-шаблон templates/'{CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    # manage_py = os.path.join(BASE_DIR, "manage.py")
    
    # run_command(f'mkdir {template_path}')
    os.makedirs(template_path, exist_ok=True)


def ensure_template_file_created(path_file, content):
    with open(path_file, 'w') as f:
        f.write(content)
    # with open(BASE_TEMPLATE_FILE, 'w'):   # Створює порожній файл
    #     pass
    
    # extend_template = '{% extends "base.html" %}'
    # with open(EXTEND_TEMPLATE_FILE, 'w') as f:
    #     f.write(extend_template)
    

# ================= VIEWS =====================
def append_to_cbv_py():
    views_path = os.path.join(BASE_DIR, CREATE_APP, 'views.py')
    content = f"""
    # with templates
    # Class-Based View (CBV):
    from django.views.generic import TemplateView


    class HomeView(TemplateView):
        template_name = '{EXTEND_TEMPLATE_FILE}'
    """

    with open(views_path, 'a') as f:
        f.write(content)
    print(f"✅ CBV додано до {views_path}")
    # run_command(f'echo {content_view} >> {CREATE_APP}/views.py')


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
    
    write_content_to_file(f'{CREATE_APP}/urls.py', content_urls_with_cbv, mode='a')
    # run_command(f'echo {content_urls_with_cbv} > {PROJECT_NAME}/urls.py')


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    # run_command(f'type nul > {CREATE_APP}/urls.py')
    content_urls_prj_cbv = f"""
    # For CBV
    from django.contrib import admin
    from django.urls import path, include
    # from django.views.generic import TemplateView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include({CREATE_APP}.urls)),   # app.urls
        # path("extend/", TemplateView.as_view(template_name="extend.html")),
    ]
    """
    write_content_to_file(f'{PROJECT_NAME}/urls.py', content_urls_prj_cbv, mode='a')
    # run_command(f'echo {content_urls_app_cbv} > {CREATE_APP}/urls.py')


# ================= MAIN =====================
def main():
    os.makedirs(DIR_DJANGO, exist_ok=True)
    ensure_django_admin_installed()   # Встановлює pipx та django
    ensure_project_created()          # Створює Django-проєкт. Інакше - минає цей етап
    pip_path, python_path = ensure_venv_created()  # Створює venv
    install_django_and_bootstrap_in_venv(pip_path)
    ensure_app_created(python_path)   # Створює Django-застосунок. Інакше - минає цей етап
    write_text_by_num_line()
    print("\n✅ Готово! Django-проєкт і застосунок створено успішно.")

    # + додай можливість одразу створити шаблони, view, route або підключити Bootstrap
    ensure_template_dir_created()         # Створює Django-шаблон. Інакше - минає цей етап
    
    # Створює HTML-файл Django-шаблону зі шляхом path_file та вмістом content
    ensure_template_file_created(BASE_TEMPLATE_FILE, content_for_base_templ_file)
    ensure_template_file_created(EXTEND_TEMPLATE_FILE, content_for_extend_templ_file)
    
    append_to_cbv_py()                    # Дописує CBV-функцію до view
    append_to_urls_py_cbv()               # Дописує route до списку urlpatterns файлу prj/urls.py
    create_urls_py_app_cbv()              # Створює app/urls.py з відповідним вмістом

    # write_to_gitignore()                  # Розкоментуй, коли тре буде пушити Django-проєкт


if __name__ == '__main__':
    main()