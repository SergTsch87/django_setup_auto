# ================= TEMPLATE =====================
import os
import constants as cnst


def ensure_template_dir_created():
    # cnst.TEMPLATE_PATH = os.path.join(cnst.BASE_DIR, cnst.PROJECT_NAME, cnst.CREATE_APP, 'templates', cnst.CREATE_APP)
    if os.path.exists(cnst.TEMPLATE_PATH):
        print(f"⚠️  Django-шаблон templates/'{cnst.CREATE_APP}' вже існує. Пропускаємо створення.")
        return
    # manage_py = os.path.join(cnst.BASE_DIR, "manage.py")
    
    # utls.run_command(f'mkdir {cnst.TEMPLATE_PATH}')
    os.makedirs(cnst.TEMPLATE_PATH, exist_ok=True)


def ensure_template_file_created(path_file, content):
    with open(path_file, 'w') as f:
        f.write(content)
    # with open(cnst.BASE_TEMPLATE_FILE, 'w'):   # Створює порожній файл
    #     pass
    
    # extend_template = '{% extends "base.html" %}'
    # with open(cnst.EXTEND_TEMPLATE_FILE, 'w') as f:
    #     f.write(extend_template)
