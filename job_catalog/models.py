#TODO: plan for industry tags, maybe so that users can only find orgs in their preferred industry


from django.db import models
from django.utils import timezone  #need this or we can't auto-set dates of job posting originations
# Create your models here.

class EmployerOrganization(models.Model):
    employer_org_name = models.CharField(max_length = 50)
    employer_org_description_box = models.TextField(
        default = 'Describe your organization, but not a specific role or requirements',
        blank = False  #we do not allow job posters to create employer orgs without a description
        )
    def __str__(self):
        return self.employer_org_name


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    role_overview = models.TextField()
    role_requirements_and_preferences = models.TextField()
    action_steps = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=90))
    is_active = models.BooleanField(default=True)

    # in django, save function is always called when you make a new job. we just overwrote it to make it more expansive in responsibility
    def save(self, *args, **kwargs):  #technical debt, as this check is only going to run when a fresh job is created
        if self.expiration_date < timezone.now():
            self.is_active = False
        super().save(*args, **kwargs)