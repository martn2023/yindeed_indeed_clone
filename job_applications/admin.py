from django.contrib import admin
from .models import JobApplication


class JobApplicationsAdmin(admin.ModelAdmin):

    def get_employer_organization_name(self, obj):
        # This method will return the employer organization name related to the job posting.
        return obj.job_posting.organization.employer_org_name

    get_employer_organization_name.short_description = 'Employer Organization'  # Sets column name

    list_display = ('id', 'get_employer_organization_name', 'user', 'linkedin_url', 'submit_date')

    search_fields = ('user__username', 'job_posting__organization__employer_org_name', 'job_posting__title')


admin.site.register(JobApplication, JobApplicationsAdmin)
