# app/main/views.py

# Django modules
from django.shortcuts import render


def home_view(request):
    return render(request, 'main/index.html')