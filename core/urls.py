from django.urls import path
from .views import RegisterUserView, home_view  # Ensure your views are imported

app_name = 'core'  # take note that the app was called out specifically to avoid conflicts during url such as core:details vs jobs:details

urlpatterns = [
    path('', home_view, name='home'),  # Existing homepage URL
    path('register_user/', RegisterUserView.as_view(), name='register'),  # URL for the registration view
    # Add other URLs as needed
]