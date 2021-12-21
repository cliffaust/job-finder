from company.models import CompanyProfile, CompanyProfileImages
from rest_framework import serializers


class CompanyProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfileImages
        exclude = ["company_profile"]


class CompanyProfileSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    company_images = CompanyProfileImageSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyProfile
        fields = "__all__"
