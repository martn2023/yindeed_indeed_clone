from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from job_catalog.models import EmployerOrganization
from django.core.exceptions import ValidationError


def home_view(request):
    """job_poster code now redundant because we made context processor in core app
    context = {'is_job_poster': False}
    if request.user.is_authenticated:
        context['is_job_poster'] = request.user.groups.filter(name='JobPosters').exists()
    """
    return render(request, 'home.html')


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'core/user_registration.html'
    success_url = reverse_lazy('core:login_start')


class LoginStartView(LoginView):
    template_name = 'core/user_login.html'


class ClaimOrganizationView(View):
    template_name = 'core/representative_claims_company.html'

    def get(self, request, *args, **kwargs):
        organizations = EmployerOrganization.objects.all()
        return render(request, self.template_name, {'organizations': organizations})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            org_id = request.POST.get('organization')
            claim_token = request.POST.get('claim_token')
            try:
                new_organization = EmployerOrganization.objects.get(id=org_id)
                current_org = request.user.profile.organization

                # Check if the user is already tied to an organization
                if current_org:
                    # User is already representing an organization
                    messages.error(request,
                                   f"You are already tied to {current_org.employer_org_name} and need to leave that organization before representing {new_organization.employer_org_name}.")
                    return redirect('core:claim_organization')

                if new_organization.representative_claim_token == claim_token:
                    job_poster_group, _ = Group.objects.get_or_create(name='JobPosters')
                    request.user.groups.add(job_poster_group)

                    request.user.profile.organization = new_organization
                    request.user.profile.save()
                    return redirect('core:home')
                else:
                    messages.error(request, "CLAIM REJECTED: Incorrect password.")
                    return render(request, self.template_name, {'organizations': EmployerOrganization.objects.all()})

            except EmployerOrganization.DoesNotExist:
                messages.error(request, "CLAIM REJECTED: Organization not found.")
        else:
            messages.warning(request, "You must be logged in to claim an organization.")

        return render(request, self.template_name, {'organizations': EmployerOrganization.objects.all()})