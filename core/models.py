from django.db import models  #This line is only needed if you're defining models in this file.

from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

def auto_add_to_job_seekers_group(sender, instance, created, **kwargs):
    if created:
        job_seekers_group, _ = Group.objects.get_or_create(name='Job Seekers')
        instance.groups.add(job_seekers_group)

# Connect the signal handling function to the post_save signal of the User model
post_save.connect(auto_add_to_job_seekers_group, sender=User)
