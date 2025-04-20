import os
import sys
import subprocess
import constants as cnst
import utils as utls

# utils:
# utls.run_command
# utls.write_content_to_file
# utls.write_to_gitignore

# constants:
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
    # utls.run_command(f'echo {content_view} >> {cnst.CREATE_APP}/views.py')


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
    
    utls.write_content_to_file(f'{cnst.CREATE_APP}/urls.py', content_urls_with_cbv, mode='a')
    # utls.run_command(f'echo {content_urls_with_cbv} > {cnst.PROJECT_NAME}/urls.py')


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    # utls.run_command(f'type nul > {cnst.CREATE_APP}/urls.py')
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
    utls.write_content_to_file(f'{cnst.PROJECT_NAME}/urls.py', content_urls_prj_cbv, mode='a')
    # utls.run_command(f'echo {content_urls_app_cbv} > {cnst.CREATE_APP}/urls.py')


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

    # utls.write_to_gitignore()                  # Розкоментуй, коли тре буде пушити Django-проєкт


if __name__ == '__main__':
    main()