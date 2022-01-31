from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import *

app_name = "main"
urlpatterns = [
    path('', HomeView.as_view(), name='Blog'),
    path('post/<slug>/', PostView, name= 'post'),
    path('tag/<slug>/', TagView, name='tag')
]
