"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from rest_framework import routers
from app.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name = 'index'),
    path('area/', area, name = 'areas'),
    path('fisico/', fisico, name = 'fisicos'),
    path('invencao/', invencao, name = 'invencoes'),
    path('questionario/', questionario, name = 'questionarios'),
    path('subarea/', subarea, name = 'subareas'),
    path('topico/', topico, name = 'topicos'),
    path('professor/', subarea, name = 'subareas'),
    path('aluno/', topico, name = 'topicos'),
    path('pessoa/', pessoa, name = 'pessoas'),
#   path('temporario/', Temporario, name = 'Enviar-Questionario'),
    path('temporario/', include("app.urls")),

]