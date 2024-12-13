# apps/user/views.py

# django modules
from django.shortcuts import render

# Create your views here.

# View: Sign up
def signup(request):
	return render(request, "user/signup.html")