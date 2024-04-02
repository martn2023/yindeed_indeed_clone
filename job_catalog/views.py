from django.shortcuts import render
from django.shortcuts import get_object_or_404  #test this to see error message
from django.shortcuts import redirect #i think this is leveraged in the create_org function

from django.contrib import messages

from .forms import EmployerOrganizationForm

from django.http import HttpResponse

from .models import EmployerOrganization, JobPosting #have to pull from the models to list them all
from core.models import UserProfile
from job_applications.models import JobApplication  # Adjust the import path according to your project structure


def index(request):
    return HttpResponse("Job Catalog app section")

def display_all_companies(request):  #not sure where "request" comes from
    all_organizations = EmployerOrganization.objects.all()
    context = {'organizations_list': all_organizations}  # we are declaring, not pulling variables here
    return render(request, 'job_catalog/all_companies.html' ,context)  #the 2nd argument auto-requested a template_name, and it will default to the templates folder as the root



def display_all_jobs(request):
    all_jobs = JobPosting.objects.all()
    context = {'job_postings_list': all_jobs}  # we are declaring, not pulling variables here
    return render(request, 'job_catalog/all_jobs.html' ,context)


def job_details(request, job_id):
    job_instance = get_object_or_404(JobPosting, pk=job_id)
    user_has_applied = False
    application = None

    if request.user.is_authenticated:
        try:
            application = JobApplication.objects.get(job_posting=job_instance, user=request.user)
            user_has_applied = True
        except JobApplication.DoesNotExist:
            user_has_applied = False

    context = {
        'job_instance': job_instance,
        'user_has_applied': user_has_applied,
        'application': application,  # Optional: Only if you need more details from the application itself
    }
    return render(request, 'job_catalog/job_details.html', context)

def company_details(request, company_id):
    company_instance = get_object_or_404(EmployerOrganization, pk=company_id)
    total_job_postings = JobPosting.objects.filter(organization=company_instance).count()
    active_job_postings = JobPosting.objects.filter(organization=company_instance, is_active=True).count()
    job_postings = JobPosting.objects.filter(organization=company_instance, is_active=True)

    context = {
        'company_instance': company_instance,
        'job_postings': job_postings,
        'total_job_postings': total_job_postings,  # Total number of jobs posted
        'active_job_postings': active_job_postings,  # Number of active jobs
    }
    return render(request, 'job_catalog/company_details.html', context)


def create_organization(request):
    # Check if the user is logged in and doesn't already belong to an organization
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to create an organization.")
        return redirect('core:login_start')

    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.organization:
        org_name = user_profile.organization.employer_org_name
        messages.error(request,
                       f"You cannot create a company since you are currently representing {org_name} for hiring.")
        return redirect('job_catalog:index')  # Adjust as needed

    if request.method == 'POST':
        form = EmployerOrganizationForm(request.POST)
        if form.is_valid():
            new_organization = form.save()
            user_profile.organization = new_organization
            user_profile.save()
            messages.success(request, "Organization created successfully.")
            return redirect('job_catalog:index')  # Redirect to an appropriate page
    else:
        form = EmployerOrganizationForm()

    return render(request, 'job_catalog/create_organization_form.html', {'form': form})