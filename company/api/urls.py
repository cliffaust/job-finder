from django.urls import path
from .views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyProfileListView, \
    CompanyProfileCreateView, CompanyProfileDetailView, CompanyProfileImageListView, CompanyProfileImageCreateView, \
    CompanyProfileImageDetailView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name="companies"),
    path('companies/<slug>/', CompanyDetailView.as_view(), name="company"),
    path('create-company/', CompanyCreateView.as_view(), name="create-company"),
    path('company-profiles/', CompanyProfileListView.as_view(), name="company-profiles"),
    path('company-profiles/<slug>/', CompanyProfileDetailView.as_view(), name="company-profile"),
    path('companies/<company_slug>/create-company-profile/', CompanyProfileCreateView.as_view(), name="create-company-profile"),
    path('company-profile-images/', CompanyProfileImageListView.as_view(), name="company-profile-images"),
    path('company-profile-images/<int:pk>/', CompanyProfileImageDetailView.as_view(), name="company-profile-image"),
    path('company-profiles/<company_profile_slug>/create-company-profile-image/', CompanyProfileImageCreateView.as_view(),
         name="create-company-profile-image")
]
# As part of our culture we believe in good work practices, and that's what we do.
