from django.contrib import admin
from .models import JobApplication


class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id','job_posting', 'user', 'linkedin_url', 'submit_date')
    #list_filter = ('organization', 'post_date', 'is_active')
    search_fields = ('user',)  # Assuming organization has a name field

admin.site.register(JobApplication, JobApplicationsAdmin)
