# Generated by Django 3.2.9 on 2022-01-08 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_job_current_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='number_of_applicant',
        ),
    ]
