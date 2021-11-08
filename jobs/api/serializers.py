from django.db.models import fields
from rest_framework import serializers

from jobs.models import Company, Seeker


class CompanySerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class SeekerSerializer(serializers.ModelSerializer):
    class Meat:
        model = Seeker
        fields = "__all__"
