from rest_framework import serializers

from jobs.models import Job, Seeker


class SeekerSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Seeker
        exclude = ["job"]


class JobSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    num_applicants = serializers.SerializerMethodField()
    company = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"

    def get_num_applicants(self, instance):
        return instance.seekers.count()
