# apps/user/views.py

# django modules
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    login as user_login,
    logout as user_logout,
)

import logging
logger = logging.getLogger("django")

# my modules
from user.forms import SignupForm, LoginForm

# Create your views here.

# View: Sign up
def signup(request):
    
    """
    Creates a new user based on given email, password and other necessary informations
    """
    
    # 1. Handling POST request
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        
        # If data from the form is valid
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. Please login')
            return HttpResponseRedirect(reverse('main:home'))

        # If data from the form is NOT valid
        messages.error(request, 'Please enter valid data')
        return render(request, "user/signup.html", {"form": form})
    
    # 2. Handling GET request
    else:
        form = SignupForm()
    
    context = {"form": form}
    
    return render(request, "user/signup.html", context)


# View: Log in
def login(request):
    """
    Login the user if the given email and password are valid
    """

    # 1. Handling POST request
    if request.method == "POST":

        # 1.1 Get sent data from the form
        form = LoginForm(request, request.POST)
        
        # 1.2. Validate sent data

        # 1.2.1. If sent data is valid
        if form.is_valid():
            # 1.2.1.1. Clean data
            email = form.cleaned_data["username"] # refer to custome user
            password = form.cleaned_data["password"]
           
            # 1.2.1.2. Authenticate the email and password
            user = authenticate(email=email, password=password)
            
            # 1.2.1.3 if user exists in db
            if user is not None:
                user_login(request, user)
                logger.info("User Logged in")
                messages.success(request, "Logged in Successfully")
                return HttpResponseRedirect(reverse("main:home"))
            
            # 1.2.1.4. If user is not exists in db
            else:
                logger.error("User is None")
                messages.error(request, "Invalid Login! Please enter correct data")
                return HttpResponseRedirect(reverse("user:login"))
        
        # 1.2.2. If sent data is not valid
        else:
            logger.error("Invalid Username and Passsword")
            messages.error(request, "Please Enter Correct Username and Password")
            return render(request, "user/login.html", {"form": form})
    
    # 2. Handling GET request
    else:
        form = LoginForm()
    
    context = {"form": form}
    
    return render(request, "user/login.html", context)

# View: Log out
def logout(request):
    """
    Logout the user from the current session
    """
    user_logout(request)
    logger.info("Logged out successfully")
    messages.info(request, "Logged out successfully")
    return HttpResponseRedirect(reverse("user:login"))