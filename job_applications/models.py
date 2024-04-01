from django.db import models
from django.conf import settings
from job_catalog.models import JobPosting  # We need this because we are tying apps to specific postings

class JobApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    submit_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    linkedin_url = models.URLField(max_length=250, blank=True)  # Optional LinkedIn profile URL
    portfolio_url = models.URLField(max_length=250, blank=True)  # Optional portfolio website URL
    email_address = models.EmailField(max_length=50)  # Required email address for the application
    phone_number = models.CharField(max_length=20)  # Required phone number

    def __str__(self):
        return f'Application by {self.user} for {self.job_posting}'
