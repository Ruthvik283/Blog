
from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    
    path('home/', views.home,name="home"),
    path('blogs/', views.blogs,name="home"),
    path('blogs/<int:pk>', views.blog,name="home"),
    path('addblog', views.addblog,name="home"),
]
