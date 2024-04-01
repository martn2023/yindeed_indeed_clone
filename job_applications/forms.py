from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'user', 'linkedin_url', 'phone_number', 'email_address','resume']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['email_address'].required = False

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        if resume:
            # Check if the file size is greater than 10 megabytes
            if resume.size > 10 * 1024 * 1024:  # 10 megabytes in bytes
                raise forms.ValidationError("File size cannot exceed 10 megabytes.")

            # Check if the file is not a PDF based on the filename extension
            if not resume.name.lower().endswith('.pdf'):
                raise forms.ValidationError("Please upload a PDF file.")
        return resume
