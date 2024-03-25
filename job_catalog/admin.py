from django.contrib import admin
from .models import EmployerOrganization

class EmployerOrganizationAdmin(admin.ModelAdmin):
    list_display = ('employer_org_name','employer_org_description_box')  #need to be what's in the models currently, not what you want the naked eye to see
    search_fields = ['employer_org_name']

admin.site.register(EmployerOrganization, EmployerOrganizationAdmin)  #need this to tie whats in the models (1st arg) to what shows up in admin panel (2nd arg)