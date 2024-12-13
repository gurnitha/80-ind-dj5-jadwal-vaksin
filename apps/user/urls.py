# apps/user/urls.py

# django modules
from django.urls import path

# my modules
from user import views

app_name = "user"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]