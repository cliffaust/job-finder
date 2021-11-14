from django.contrib import admin
from .models import Company, CompanyProfile, CompanyProfileImages


admin.site.register(Company)
admin.site.register(CompanyProfile)
admin.site.register(CompanyProfileImages)
