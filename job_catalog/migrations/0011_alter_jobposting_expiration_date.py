# Generated by Django 5.0.3 on 2024-04-02 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_catalog', '0010_alter_jobposting_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 8, 46, 47, 73126, tzinfo=datetime.timezone.utc)),
        ),
    ]
