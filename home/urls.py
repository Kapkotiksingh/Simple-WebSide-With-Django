from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
    path('base/', views.base,name="base"),
    path('list/', views.list,name="list"),
]
