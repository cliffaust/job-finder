# Generated by Django 3.2.9 on 2021-12-24 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_rename_values_companyprofile_val'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyprofile',
            old_name='val',
            new_name='company_values',
        ),
    ]
