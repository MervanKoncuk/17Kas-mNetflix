from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('movies/<str:slug>/<str:profilId>', movies, name='movies')
]