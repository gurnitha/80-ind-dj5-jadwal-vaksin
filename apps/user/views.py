# apps/user/views.py

# django modules
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# my modules
from user.forms import SignupForm
# from user.email import send_email_verification

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