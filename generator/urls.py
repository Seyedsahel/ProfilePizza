from .views import *
from django.urls import path

urlpatterns = [
    path('<str:username>/', svg_generator),
]
