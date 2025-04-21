# ================= VIEWS =====================
import constants as cnst
import os


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