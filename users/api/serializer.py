from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from users.models import CustomUser, Company


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_company', 'profile_pic']


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name",
            'is_company',
            "profile_pic",
            "password1",
            "password2",
        ]

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address.", )
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(("The two password fields didn't match.", ))
        return data

    def get_cleaned_data(self):
        return {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "is_company": self.validated_data.get("is_company", ""),
            "profile_pic": self.validated_data.get("profile_pic", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        if self.cleaned_data.get("profile_pic"):
            user.profile_pic = self.cleaned_data.get("profile_pic")
        setup_user_email(request, user, [])
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'email', 'company_name', 'profile_pic']


class RegisterCompanySerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "company_name",
            "profile_pic",
            "password1",
            "password2",
        ]

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address.", )
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(("The two password fields didn't match.", ))
        return data

    def get_cleaned_data(self):
        return {
            "company_name": self.validated_data.get("company_name", ""),
            "profile_pic": self.validated_data.get("profile_pic", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        if self.cleaned_data.get("profile_pic"):
            user.profile_pic = self.cleaned_data.get("profile_pic")
        setup_user_email(request, user, [])
        user.save()
        return user

