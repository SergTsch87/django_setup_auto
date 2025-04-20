# ================= URLS =====================
import constants as cnst
import utils as utls


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
