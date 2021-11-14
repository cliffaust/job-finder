from .models import CustomUser, Company

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        exclude = []

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        exclude = []

    def clean_password(self):

        return self.initial["password"]


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("first_name", "last_name", "email", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("Personal info", {"fields": ["profile_pic"]}),
        ("Permissions", {"fields": ("is_admin", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "profile_pic",
                    "password1",
                    "password2",
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email", "first_name", "last_name")
    filter_horizontal = ()


class CompanyChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Company
        exclude = []

    def clean_password(self):

        return self.initial["password"]


class CompanyAdmin(BaseUserAdmin):

    form = CompanyChangeForm
    add_form = UserCreationForm

    list_display = ("company_name", "email")
    list_filter = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "company_name")}),
        ("Personal info", {"fields": ["profile_pic"]})),

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "company_name",
                    "email",
                    "profile_pic",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email", "company_name")
    ordering = ("email", "company_name")
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)

admin.site.register(CustomUser, CompanyAdmin)
