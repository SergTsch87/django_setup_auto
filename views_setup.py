# ================= VIEWS =====================
import constants as cnst
import content as cont
import os


def append_to_cbv_py():
    with open(cnst.VIEWS_PY_PATH, 'a') as f:
        f.write(cont.CONTENT_TO_CBV_PY)
    print(f"✅ CBV додано до {cnst.VIEWS_PY_PATH}")