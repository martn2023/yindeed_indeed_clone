from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    organization = models.ForeignKey('job_catalog.EmployerOrganization', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profiles')
    # Include other fields for your UserProfile model here

# Function to handle adding new users to the JobSeekers group
def auto_add_to_job_seekers_group(sender, instance, created, **kwargs):
    if created:
        job_seekers_group, _ = Group.objects.get_or_create(name='JobSeekers')
        instance.groups.add(job_seekers_group)

# Function to handle creating or updating a user profile
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()

# Connect signals
post_save.connect(auto_add_to_job_seekers_group, sender=User)
post_save.connect(create_or_update_user_profile, sender=settings.AUTH_USER_MODEL)
