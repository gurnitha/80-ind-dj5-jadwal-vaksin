# config/urls.py

# Django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # user
    path("accounts/", include("user.urls", namespace="user")),
    # main
    path('', include('main.urls', namespace='main')),
    # admin
    path('admin/', admin.site.urls),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)