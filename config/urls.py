# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# my modules
from app.main import views

urlpatterns = [
    # main
    path('', views.halodunia),
    # admin
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)