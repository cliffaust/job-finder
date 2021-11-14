from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.company_name


class CompanyProfile(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    num_of_employees = models.PositiveIntegerField(blank=True, null=True)
    year_started = models.PositiveIntegerField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company.company_name


class CompanyProfileImages(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    image = ProcessedImageField(
        processors=[Resize(1000, 760)],
        format="JPEG",
        options={"quality": 60},
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company.company_name
