from django.db import models
from django.conf import settings
from job_catalog.models import JobPosting

class JobApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    submit_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    linkedin_url = models.URLField(max_length=250, blank=True)
    portfolio_url = models.URLField(max_length=250, blank=True)
    email_address = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'Application by {self.user} for {self.job_posting}'

    class Meta:
        unique_together = ('user', 'job_posting')  # Ensures a user can only apply once per job posting
