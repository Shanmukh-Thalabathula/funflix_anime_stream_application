from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', userLogin, name='user-login'),
    path('register/', userRegister, name='user-register'),
    path('logout/', userLogout, name='user-logout'),
    path('', home, name='home'),
    path('episodes/<str:pk>/',episodes, name='episodes'),
    path('display/<int:pk>/',video, name='display-video'),
    path('favorite/<int:pk>/',favorite, name='favorite'),
    path('favorite_list/',fav_list, name='fav-list'),
    path('category/',category, name='category'),
    path('details/',details, name='details'),
]
