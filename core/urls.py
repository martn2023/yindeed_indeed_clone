from django.urls import path
from .views import home_view, RegisterUserView, LoginStartView  # Ensure your views are imported
from django.contrib.auth.views import LogoutView


app_name = 'core'  # take note that the app was called out specifically to avoid conflicts during url such as core:details vs jobs:details

urlpatterns = [
    path('', home_view, name='home'),  # Existing homepage URL
    path('register_user/', RegisterUserView.as_view(), name = 'register'),  # URL for the registration view
    path('login_start/', LoginStartView.as_view(), name = 'login_start'),
    path('logout/', LogoutView.as_view(), name = 'logout'), #there is no logout page, we send back to home, but this code might not work, we might have to override in settings.py
]