from django.urls import path, include
from rest_framework import routers
from app.views import *

router = routers.DefaultRouter()

router.register(r"q", QuestaoViewsSet)

urlpatterns = [

    path('', Temporario, name = 'Enviar-Questionario'),
    path('', include(router.urls)),

]