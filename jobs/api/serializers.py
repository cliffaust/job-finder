from rest_framework import serializers

from jobs.models import Company, Seeker


class CompanySerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    seekers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = "__all__"


class SeekerSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Seeker
        fields = "__all__"
