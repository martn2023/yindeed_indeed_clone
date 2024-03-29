from django.shortcuts import render
from django.shortcuts import get_object_or_404  #test this to see error message

from django.http import HttpResponse

from .models import EmployerOrganization, JobPosting #have to pull from the models to list them all

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
    job_instance = get_object_or_404(JobPosting, pk = job_id)  #where is job_id coming from? django built in language? i think it's drawing from the URL
    context = {'job_instance': job_instance}  # we are declaring, not pulling variables here
    return render(request, 'job_catalog/job_details.html' ,context)

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
