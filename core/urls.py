from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import home_view, RegisterUserView, LoginStartView, ClaimOrganizationView, before_leaving_organization, leave_organization_confirmed


app_name = 'core'  # take note that the app was called out specifically to avoid conflicts during url such as core:details vs jobs:details

urlpatterns = [
    path('', home_view, name='home'),  # Existing homepage URL
    path('register_user/', RegisterUserView.as_view(), name = 'register'),  # URL for the registration view
    path('login_start/', LoginStartView.as_view(), name = 'login_start'),
    path('logout/', LogoutView.as_view(), name = 'logout'), #there is no logout page, we send back to home, but this code might not work, we might have to override in settings.py

    path('claim_org/', ClaimOrganizationView.as_view(), name='claim_organization'),
    path('leave_org/', before_leaving_organization, name='leaving_organization'), # different treatment for function vs class based views, missing the asview tail
    path('leave_organization/confirm/', leave_organization_confirmed, name='left_organization_confirmation'),

]