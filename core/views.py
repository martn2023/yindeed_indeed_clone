from django.shortcuts import render

# Create your views here.
# core/views.py
from django.contrib.auth.forms import UserCreationForm  #premade view coming out of auth app?
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy  #url isn't formed until a trigger event (such as a successful registration), which means harder to test
from django.views.generic.edit import CreateView  #need to pull in 2 django pre-built forms
from django.shortcuts import render



def home_view(request):
    return render(request, 'home.html')

class RegisterUserView(CreateView):   #view for account registration
    form_class = UserCreationForm
    template_name = 'core/user_registration.html'  # remember that we have a master templates folder at root level
    success_url = reverse_lazy('core:login')  # attempting to redirect users to login page after successful registration, added /core directory above

class LoginStartView(LoginView):   #view for attempting to authenticate
    template_name = 'core/user_login.html'  # remember that we have a master templates folder at root level

