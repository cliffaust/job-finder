from .views import SeekerCreateView, JobCreateView, SeekerDetailView, SeekerListView, JobDetailView, \
    JobListView
from django.urls import path


urlpatterns = [
    path('jobs/', JobListView.as_view(), name="companies"),
    path('create-job/', JobCreateView.as_view(), name="create-company"),
    path('jobs/<slug>/', JobDetailView.as_view(), name="company"),
    path('seekers/', SeekerListView.as_view(), name="seekers"),
    path('create-seeker/', SeekerCreateView.as_view(), name="create-seeker"),
    path('seekers/<slug>/', SeekerDetailView.as_view(), name="seeker"),
]
