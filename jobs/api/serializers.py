from rest_framework import serializers

from jobs.models import Job, Seeker


class SeekerSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField(read_only=True)
    slug = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Seeker
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    seekers = SeekerSerializer(many=True, read_only=True)
    date_posted = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"
