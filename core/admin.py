from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile  # Ensure UserProfile is imported from models

# Your existing custom UserAdmin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groups'

# Unregister the original User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Modified ModelAdmin for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'employer_org', 'get_groups', 'is_staff_member')

    def employer_org(self, obj):
        return obj.organization.employer_org_name if obj.organization else None
    employer_org.short_description = 'Employer Org'
    employer_org.admin_order_field = 'organization__employer_org_name'

    def get_groups(self, obj):
        return ", ".join(group.name for group in obj.user.groups.all()) or None
    get_groups.short_description = 'Groups'

    def is_staff_member(self, obj):
        return obj.user.is_staff
    is_staff_member.short_description = 'Is staff member'
    is_staff_member.boolean = True

    search_fields = ('user__username', 'organization__employer_org_name')

# Register the modified UserProfileAdmin
admin.site.register(UserProfile, UserProfileAdmin)
