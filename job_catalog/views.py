from django.shortcuts import render
from django.http import HttpResponse

from .models import EmployerOrganization #have to pull from the models to list them all

def index(request):
    return HttpResponse("Job Catalog app section")

def display_all_companies(request):  #not sure where "request" comes from
    all_organizations = EmployerOrganization.objects.all()
    context = {'organizations_list': all_organizations}  # we are declaring, not pulling variables here
    return render(request, 'jobs_catalog/all_companies.html' ,context)  #the 2nd argument auto-requested a template_name, and it will default to the templates folder as the root