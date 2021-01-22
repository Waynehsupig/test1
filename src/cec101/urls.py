"""cec101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from cec101.views import index
from cec101.joesongyy_view import jTemplate, joeAction
from cec101.ray_view import rayTemplate, rayAction
from cec101.abc_view import abcTemplate, abcAction
from cec101.york_view import yorkTemplate, yorkAction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    path('chatRoom/', jTemplate, name="jTemplate"),
    path('ray/', rayTemplate, name="rayTemplate"),
    path('abc/', abcTemplate, name="abcTemplate"),
    path('york/', yorkTemplate, name="yorkTemplate"),
    path('joe/action', joeAction, name="joeAction"),
    path('ray/action', rayAction, name="rayAction"),
    path('abc/action', abcAction, name="abcAction"),
    path('york/action', yorkAction, name="yorkAction")
]

