from django.contrib import admin
from .models import JobApplication

class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_posting', 'user', 'linkedin_url', 'submit_date')
    search_fields = ('user__username', 'job_posting__organization__employer_org_name', 'job_posting__title')

admin.site.register(JobApplication, JobApplicationsAdmin)
