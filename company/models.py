from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize


class CompanyProfile(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    num_of_employees = models.PositiveIntegerField(blank=True, null=True)
    year_started = models.PositiveIntegerField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    company_values = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.user}"


class CompanyProfileImages(models.Model):
    company_profile = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, related_name="company_images"
    )
    image = ProcessedImageField(
        processors=[Resize(1000, 760)],
        format="JPEG",
        options={"quality": 60},
    )
    comment = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return str(self.company_profile)
