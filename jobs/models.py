from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from core.utils import cv_thumbnail


class Company(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    work_email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True)
    current_role = models.CharField(max_length=100, blank=True)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.company_name)


class Seeker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="seekers"
    )
    cv = models.FileField(
        upload_to=cv_thumbnail,
        blank=True,
        null=True,
    )
    phone_number = PhoneNumberField(blank=True)
    other_comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_cv = self.cv
            self.cv = None
            super(Seeker, self).save(*args, **kwargs)

            self.cv = saved_cv
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")

        super(Seeker, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)
