# Generated by Django 4.1.1 on 2023-06-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_jobs_job_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
