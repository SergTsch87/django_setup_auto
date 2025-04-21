# ========= CONSTANTS ========= 
import os


PROJECT_NAME = "my_prj"     # Change it!
CREATE_APP = "tutors_app"   # Change it!
VENV_NAME = ".venv"
TARGET_FOLDER = "."         # Current dir

DIR_DJANGO = os.path.abspath('./root_prj/')
BASE_DIR = os.path.join(DIR_DJANGO, PROJECT_NAME)
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# TEMPLATE_PATH = os.path.join(BASE_DIR, PROJECT_NAME, CREATE_APP, 'templates', CREATE_APP)
TEMPLATE_PATH = os.path.join(BASE_DIR, CREATE_APP, 'templates', CREATE_APP)
BASE_TEMPLATE_FILE = os.path.join(TEMPLATE_PATH, 'base.html')   # parent template
EXTEND_TEMPLATE_FILE = os.path.join(TEMPLATE_PATH, 'extend.html')   # with extend template from base.html

content_for_base_templ_file = """
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

content_for_extend_templ_file = """
{% extends "base.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
"""

content_urls_app_with_cbv = """
# with templates
# # Class-Based View (CBV):
# from tutors_app.views import HomeView
from django.urls import path
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
"""

content_urls_prj_cbv = f"""
# For CBV
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include({CREATE_APP}.urls)),   # app.urls
    # path("extend/", TemplateView.as_view(template_name="extend.html")),
]
"""