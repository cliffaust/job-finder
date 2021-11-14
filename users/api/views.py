from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserProfile
from .serializer import UserSerializer, CompanySerializer
from users.models import CustomUser, Company


class UserProfileView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.email

        return CustomUser.objects.filter(email=user)


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserProfile]

    def get_queryset(self):
        user = self.request.user.email

        return CustomUser.objects.filter(email=user)


class CompanyProfileView(generics.ListAPIView):
    serializer_class = CompanySerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.email

        return Company.objects.filter(email=user)


class CompanyProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsUserProfile]

    def get_queryset(self):
        user = self.request.user.email

        return Company.objects.filter(email=user)
