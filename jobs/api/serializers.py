from rest_framework import serializers

from jobs.models import Job, Seeker


class SeekerSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Seeker
        exclude = ["job"]


class JobSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    # seekers = SeekerSerializer(many=True, read_only=True)
    date_posted = serializers.StringRelatedField(read_only=True)
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
