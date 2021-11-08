from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    first_name = models.CharField(max_length=150, required=True)
    last_name = models.CharField(max_length=150, required=True)
    name = models.CharField(max_length=255, required=True)
    job_title = models.CharField(max_length=255, required=True)
    work_email = models.EmailField(max_length=255, unique=True)
    phonenumber = PhoneNumberField(blank=True)
