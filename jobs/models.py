from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from core.utils import cv_thumbnail


class Company(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=150, required=True)
    last_name = models.CharField(max_length=150, required=True)
    company_name = models.CharField(max_length=255, required=True)
    job_title = models.CharField(max_length=255, required=True)
    work_email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True)
    current_role = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.company_name)


class Seeker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="seeker"
    )
    cv = models.FileField(
        upload_to=cv_thumbnail,
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(blank=True)
    other_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
