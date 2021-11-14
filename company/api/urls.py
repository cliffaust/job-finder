from django.urls import path
from .views import CompanyListView, CompanyCreateView, CompanyDetailView, CompanyProfileListView, \
    CompanyProfileCreateView, CompanyProfileDetailView, CompanyProfileImageListView, CompanyProfileImageCreateView, \
    CompanyProfileImageDetailView


urlpatterns = [
    path('companies', CompanyListView.as_view(), name="companies"),
    path('com')
]
