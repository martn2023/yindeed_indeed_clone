# Generated by Django 5.0.3 on 2024-04-03 16:27

import job_applications.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_applications', '0003_alter_jobapplication_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=job_applications.models.JobApplication.resume_upload_path),
        ),
    ]
