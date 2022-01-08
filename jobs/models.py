from django.db import models
from django.conf import settings
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from core.utils import cv_thumbnail
from company.models import CompanyProfile


class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    remote = models.BooleanField(default=False)
    salary = models.PositiveIntegerField()
    work_email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    current_role = models.CharField(max_length=255, blank=True)
    is_closed = models.BooleanField(default=False)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.company.company_name)


class Seeker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="seekers")
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
