# ================= TEMPLATE =====================
import os
import constants as cnst


def ensure_template_dir_created():
    if os.path.exists(cnst.TEMPLATE_PATH):    # YES
        print(f"⚠️  Django-шаблон templates/'{cnst.CREATE_APP}' вже існує. Пропускаємо створення.")    # YES
        return

    os.makedirs(cnst.TEMPLATE_PATH, exist_ok=True)    # YES


def ensure_template_file_created(path_file, content):
    with open(path_file, 'w') as f:
        f.write(content)