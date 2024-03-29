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
    representative_claim_token = models.CharField(max_length = 16, default = "join")
    def __str__(self):
        return self.employer_org_name


class JobPosting(models.Model):
    organization = models.ForeignKey(EmployerOrganization, on_delete=models.CASCADE, default = 1)  #we wanted cascaded deletion but FYI django requires explicit selection of on_delete
    title = models.CharField(max_length=100)
    role_overview = models.TextField()
    role_requirements_and_preferences = models.TextField()
    action_steps = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=90))
    is_active = models.BooleanField(default=True)

    # Override the save method to check expiration date and set is_active
    def save(self, *args, **kwargs):
        if self.expiration_date < timezone.now():
            self.is_active = False
        super().save(*args, **kwargs)