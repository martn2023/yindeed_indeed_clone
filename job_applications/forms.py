from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'user', 'linkedin_url', 'phone_number', 'email_address', 'resume']

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

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        job_posting = cleaned_data.get('job_posting')

        if user and job_posting and JobApplication.objects.filter(user=user, job_posting=job_posting).exists():
            # This will add a non-field error, you can change it to a field error if preferred
            raise forms.ValidationError("You have already applied for this job.")
        return cleaned_data
