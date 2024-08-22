from .views import *
from django.urls import path

urlpatterns = [
    path('generate/<str:username>/', svg_generator),
]
