# Generated by Django 5.0.3 on 2024-04-02 08:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_applications', '0002_rename_application_email_jobapplication_email_address'),
        ('job_catalog', '0011_alter_jobposting_expiration_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together={('user', 'job_posting')},
        ),
    ]
