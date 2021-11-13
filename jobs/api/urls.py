from .views import SeekerCreateView, CompanyCreateView, SeekerDetailView, SeekerListView, CompanyDetailView, \
    CompanyListView
from django.urls import path


urlpatterns = [
    path('companies/', CompanyListView.as_view(), name="companies"),
    path('create-company/', CompanyCreateView.as_view(), name="create-company"),
    path('companies/<slug>/', CompanyDetailView.as_view(), name="company"),
    path('seekers/', SeekerListView.as_view(), name="seekers"),
    path('create-seeker/', SeekerCreateView.as_view(), name="create-seeker"),
    path('seekers/<slug>/', SeekerDetailView.as_view(), name="seeker"),
]
