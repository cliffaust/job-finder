from rest_framework import serializers

from jobs.models import Company, Seeker


class SeekerSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True)
    slug = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Seeker
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    seekers = SeekerSerializer(many=True)
    date_posted = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"
