# job_applications/forms.py

from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'user', 'linkedin_url']  # Adjust fields as needed
