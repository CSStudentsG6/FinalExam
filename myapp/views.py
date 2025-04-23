import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
  

# Home view
def home(request):
    return render(request, 'myapp/home.html')

from django.shortcuts import redirect

# Start Over View - Clear the session and redirect to home
def start_over(request):
    # Clear the session data
    request.session.flush()  # This will clear all session data
    
    # Redirect to the home page to restart the process
    return redirect('home')


