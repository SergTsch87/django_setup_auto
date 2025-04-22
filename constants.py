# ========= CONSTANTS ========= 
import os


PROJECT_NAME = "my_prj"     # Change it!     # YES
CREATE_APP = "tutors_app"   # Change it!     # YES
# TARGET_FOLDER = "."         # Current dir     # YES  !!! Ніде не використ-ся, але потрібна для можливого вибору иншої папки

BASE_DIR = os.path.abspath('./root_prj/')     # YES
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, CREATE_APP, 'templates', CREATE_APP)         # YES
BASE_TEMPLATE_FILE = os.path.join(TEMPLATE_PATH, 'base.html')   # parent template   # YES
EXTEND_TEMPLATE_FILE = os.path.join(TEMPLATE_PATH, 'extend.html')   # with extend template from base.html   # YES

MANAGE_PY_PATH = os.path.join(BASE_DIR, "manage.py")  # YES
SETTINGS_PY_PATH = os.path.join(BASE_DIR, PROJECT_NAME, "settings.py")
VIEWS_PY_PATH = os.path.join(BASE_DIR, CREATE_APP, 'views.py')     # YES
URLS_PY_PATH_APP_CBV = os.path.join(BASE_DIR, CREATE_APP, 'urls.py')
URLS_PY_PATH_PRJ_CBV = os.path.join(BASE_DIR, PROJECT_NAME, 'urls.py')