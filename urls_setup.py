# ================= URLS =====================
import constants as cnst
import utils
import os


# Створює app/urls.py з відповідним вмістом
def create_urls_py_app_cbv():
    utils.write_content_to_file(f'{os.path.join(cnst.BASE_DIR, cnst.CREATE_APP)}/urls.py', cnst.content_urls_app_with_cbv, mode='a')
    # utils.run_command(f'echo {cnst.content_urls_app_with_cbv} > {cnst.PROJECT_NAME}/urls.py')


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    # utils.run_command(f'type nul > {cnst.CREATE_APP}/urls.py')
    utils.write_content_to_file(f'{os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME)}/urls.py', cnst.content_urls_prj_cbv, mode='a')
    # utils.run_command(f'echo {content_urls_app_cbv} > {cnst.CREATE_APP}/urls.py')