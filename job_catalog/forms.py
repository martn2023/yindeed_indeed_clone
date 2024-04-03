# job_catalog/forms.py

from django import forms
from .models import EmployerOrganization, JobPosting

class EmployerOrganizationForm(forms.ModelForm):
    class Meta:
        model = EmployerOrganization
        fields = ['employer_org_name', 'employer_org_description_box', 'representative_claim_token']
        # Add any additional fields you'd like to include in the form

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'role_overview', 'role_requirements_and_preferences', 'action_steps',]
        # Exclude 'expiration_date' from the form