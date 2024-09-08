from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'  # Set the app namespace

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:cur_slug>/', views.single_post, name='single_post'),
]