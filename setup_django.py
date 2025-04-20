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