from django.urls import path
from .views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('profiles/', profiles, name='profiles'),
    path('create/', create, name='create'),
    path('logout/', userLogout, name='logout'),
    path('hesap/', hesap, name='hesap'),
    path('reset-password/', reset, name='reset'),
    path('update/', update, name='update'),
    path('delete/', userDelete, name='delete')
]