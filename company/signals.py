from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CompanyProfile
from django.utils.text import slugify
from core.utils import generate_random_string


@receiver(pre_save, sender=CompanyProfile)
def create_company_profile_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.company_name)
        random_string = generate_random_string(length=24)
        instance.slug = slug + "-" + random_string
