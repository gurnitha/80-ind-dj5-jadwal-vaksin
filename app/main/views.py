# app/main/views.py

# Django modules
from django.shortcuts import render


def home_view(request):
    page_title = "Home"
    context_dict = {'title':page_title}
    return render(request, 'main/index.html', context_dict)


def about_view(request):
    page_title = "About"
    context_dict = {'title':page_title}
    return render(request, 'main/about.html', context_dict)