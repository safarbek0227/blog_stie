from django.urls import path
from .import views

app_name = "main"
urlpatterns = [
    path('', views.homeView, name="index"),
    path("post/<slug>", views.postDetail, name='post'),
    path('tag/<slug>', views.categoryView, name="index"),
    path("search/", views.inline_search, name="search"), 
    path("contact/", views.contact, name='contact'),  
]