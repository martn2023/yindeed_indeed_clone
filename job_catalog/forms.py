# job_catalog/forms.py

from django import forms
from .models import EmployerOrganization

class EmployerOrganizationForm(forms.ModelForm):
    class Meta:
        model = EmployerOrganization
        fields = ['employer_org_name', 'employer_org_description_box', 'representative_claim_token']
        # Add any additional fields you'd like to include in the form
