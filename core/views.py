from django.shortcuts import render

# Create your views here.
# core/views.py

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm  #premade view coming out of auth app?
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group

from django.urls import reverse_lazy  #url isn't formed until a trigger event (such as a successful registration), which means harder to test
from django.urls import reverse

from django.views import View
from django.views.generic.edit import CreateView  #need to pull in 2 django pre-built forms

from django.shortcuts import render
from django.shortcuts import redirect

from job_catalog.models import EmployerOrganization


def home_view(request):
    return render(request, 'home.html')

class RegisterUserView(CreateView):   #view for account registration
    form_class = UserCreationForm
    template_name = 'core/user_registration.html'  # remember that we have a master templates folder at root level
    success_url = reverse_lazy('core:login_start')  # attempting to redirect users to login page after successful registration, added /core directory above

class LoginStartView(LoginView):   #view for attempting to authenticate
    template_name = 'core/user_login.html'  # remember that we have a master templates folder at root level

class ClaimOrganizationView(View):
    template_name = 'core/representative_claims_company.html'

    def get(self, request, *args, **kwargs):
        organizations = EmployerOrganization.objects.all()
        return render(request, self.template_name, {'organizations': organizations})

    def post(self, request, *args, **kwargs):
        org_id = request.POST.get('organization')
        claim_token = request.POST.get('claim_token')
        try:
            organization = EmployerOrganization.objects.get(id=org_id, representative_claim_token=claim_token)
            job_poster_group, _ = Group.objects.get_or_create(name='JobPosters')
            request.user.groups.add(job_poster_group)
            # Redirect to the home page:
            return redirect(reverse('core:home_view'))  # Use the name of your home page URL
        except EmployerOrganization.DoesNotExist:
            messages.error(request, "Invalid organization or claim token.")
            return render(request, self.template_name)