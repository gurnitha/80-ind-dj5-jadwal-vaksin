# app/main/urls.py

# Django modules
from django.urls import path

# my modules
from main import views

# app name
app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
]