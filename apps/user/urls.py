# apps/user/urls.py

# django modules
from django.urls import path

# my modules
from user import views

app_name = "user"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("change-password/", views.change_password, name="change-password"),
]