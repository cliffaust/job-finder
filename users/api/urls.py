from django.urls import path
from .views import UserProfileDetailView, UserProfileView, CompanyProfileDetailView, CompanyProfileView

urlpatterns = [
    path("company/", UserProfileView.as_view(), name="user"),
    path("company/<int:pk>/", UserProfileDetailView.as_view(), name="user-detail"),
    path("user/", UserProfileView.as_view(), name="user"),
    path("user/<int:pk>/", UserProfileDetailView.as_view(), name="user-detail")
]
