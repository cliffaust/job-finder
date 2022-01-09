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
    company_name = serializers.SerializerMethodField()
    company_profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

    def get_num_applicants(self, instance):
        return instance.seekers.count()

    def get_company_name(self, instance):
        return instance.company.company_name

    def get_company_profile_image(self, instance):
        return instance.company.user.profile_pic
