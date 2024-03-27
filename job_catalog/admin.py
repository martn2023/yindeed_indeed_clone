#TODO: plan for mass-importing of company names + descriptions



from django.contrib import admin
from .models import EmployerOrganization, JobPosting

class EmployerOrganizationAdmin(admin.ModelAdmin):
    list_display = ('employer_org_name','employer_org_description_box')  #need to be what's in the models currently, not what you want the naked eye to see
    search_fields = ['employer_org_name']

admin.site.register(EmployerOrganization, EmployerOrganizationAdmin)  #need this to tie whats in the models (1st arg) to what shows up in admin panel (2nd arg)



class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'organization', 'post_date', 'expiration_date', 'is_active')
    list_filter = ('organization', 'post_date', 'expiration_date', 'is_active')
    search_fields = ('title', 'organization__name')  # Assuming organization has a name field

admin.site.register(JobPosting, JobPostingAdmin)
