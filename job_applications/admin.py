from django.contrib import admin
from .models import JobApplication

class JobApplicationsAdmin(admin.ModelAdmin):

    def get_job_posting_title(self, obj):
        # This method will return the title of the job posting.
        return obj.job_posting.title
    get_job_posting_title.short_description = 'Job Title'

    def get_employer_organization_name(self, obj):
        # This method will return the employer organization name related to the job posting.
        return obj.job_posting.organization.employer_org_name
    get_employer_organization_name.short_description = 'Employer Organization'

    def get_job_posting_id(self, obj):
        # This method will return the ID of the job posting.
        return obj.job_posting.id
    get_job_posting_id.short_description = 'Job Posting ID'

    def get_employer_organization_id(self, obj):
        # This method will return the ID of the employer organization related to the job posting.
        return obj.job_posting.organization.id
    get_employer_organization_id.short_description = 'Employer Org ID'

    list_display = (
        'id',

        'get_employer_organization_name',
        'get_employer_organization_id',

        'get_job_posting_title',
        'get_job_posting_id',

        'user',
        'submit_date',
        'linkedin_url'
    )
    search_fields = (
        'user__username',
        'job_posting__title',
        'job_posting__organization__employer_org_name'
    )

admin.site.register(JobApplication, JobApplicationsAdmin)
