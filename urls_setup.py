# ================= URLS =====================
import constants as cnst
import content as cont
import utils


# Створює app/urls.py з відповідним вмістом
def create_urls_py_app_cbv():
    utils.write_content_to_file(f'{cnst.URLS_PY_PATH_APP_CBV}', cont.content_urls_app_with_cbv, mode='a')     # YES


# Дописує route до списку urlpatterns файлу prj/urls.py
def append_to_urls_py_cbv():
    utils.write_content_to_file(f'{cnst.URLS_PY_PATH_PRJ_CBV}', cont.content_urls_prj_cbv, mode='a')  # YES