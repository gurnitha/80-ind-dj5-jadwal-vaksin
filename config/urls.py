# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authView

urlpatterns = [
    # user
    path("accounts/", include("user.urls", namespace="user")),

    # main
    path('', include('main.urls', namespace='main')),

    # admin
    path('admin/', admin.site.urls),
    
    # auth: password reset
    path(
        "password_reset/", 
        authView.PasswordResetView.as_view(), 
        name="password_reset"),
    path(
        "password_reset/done/",
        authView.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        authView.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        authView.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)