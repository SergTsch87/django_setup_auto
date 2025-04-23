# ================= CONTENT =====================
import constants as cnst

CONTENT_TO_IGNORE = """
*.txt
my_prj/
tutors_app/
"""

CONTENT_TO_CBV_PY = f"""
# with templates
# Class-Based View (CBV):
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = '{cnst.EXTEND_TEMPLATE_FILE}'
"""

# YES
# 1 time in func ensure_template_file_created
CONTENT_FOR_BASE_TEMPL_FILE = """
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

# YES
# 1 time in func ensure_template_file_created
CONTENT_FOR_EXTEND_TEMPL_FILE = """
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

# YES
# 1 time in func create_urls_py_app_cbv
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

# YES
# 1 time in func append_to_urls_py_cbv
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