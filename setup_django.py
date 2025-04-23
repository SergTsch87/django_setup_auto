import os
import constants as cnst
import content as cont
import dj_conf as dj
import template_setup as tmpl
import views_setup as vw
import urls_setup as urlstp

# ================= MAIN =====================
def main():
    os.makedirs(cnst.BASE_DIR, exist_ok=True)   # YES   # exist_ok=True  означає:  if not os.path.exists(path): os.makedirs(path)
    dj.ensure_django_admin_installed()   # Встановлює pipx та django
    dj.ensure_project_created()          # Створює Django-проєкт. Инакше - минає цей етап
    pip_path, python_path = dj.ensure_venv_created()  # Створює venv
    dj.install_django_and_bootstrap_in_venv(pip_path)
    dj.ensure_app_created(python_path)   # Створює Django-застосунок. Инакше - минає цей етап
    dj.write_text_by_num_line()
    print("\n✅ Готово! Django-проєкт і застосунок створено успішно.")

    # + додай можливість одразу створити шаблони, view, route або підключити Bootstrap
    tmpl.ensure_template_dir_created()         # Створює Django-шаблон. Инакше - минає цей етап
    
    # Створює HTML-файли Django-шаблону зі шляхом path_file та вмістом content
    tmpl.ensure_template_file_created(cnst.BASE_TEMPLATE_FILE, cont.CONTENT_FOR_BASE_TEMPL_FILE)   # YES
    tmpl.ensure_template_file_created(cnst.EXTEND_TEMPLATE_FILE, cont.CONTENT_FOR_EXTEND_TEMPL_FILE)   # YES
    
    vw.append_to_cbv_py()                    # Дописує CBV-функцію до view
    urlstp.append_to_urls_py_cbv()               # Дописує route до списку urlpatterns файлу prj/urls.py
    urlstp.create_urls_py_app_cbv()              # Створює app/urls.py з відповідним вмістом

    # utils.write_to_gitignore()                  # Розкоментуй, коли тре буде пушити Django-проєкт


if __name__ == '__main__':
    main()