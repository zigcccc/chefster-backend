"""
chefster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import get_docs_view

API_TITLE = "Chefster"
schema_view = get_schema_view(title=API_TITLE)
docs_view = get_docs_view(title=API_TITLE)

api_url_patterns = [
    path("", include("recipes.urls", namespace="recipes")),
    path("", include("users.urls", namespace="users")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", docs_view),
    path("schema/", schema_view),
    path("v1/", include(api_url_patterns)),
]
