from django.db import models
# Create your models here.

class EmployerOrganization(models.Model):
    employer_org_name = models.CharField(max_length = 50)
    employer_org_description_box = models.CharField(
        max_length = 1000,
        default = 'Describe your organization, but not a specific role or requirements',
        blank = False  #we do not allow job posters to create employer orgs without a description
        )