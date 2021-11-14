from company.models import CompanyProfile, Company, CompanyProfileImages
from rest_framework import serializers


class CompanyProfileImageSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CompanyProfileImages
        fields = '__all__'


class CompanyProfileSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)
    company_images = CompanyProfileImageSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyProfile
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    company_profile = CompanyProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        exclude = ['user']
