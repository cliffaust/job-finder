from rest_framework import generics
from .serializers import CompanySerializer, CompanyProfileSerializer, CompanyProfileImageSerializer
from company.models import Company, CompanyProfile, CompanyProfileImages


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyProfileListView(generics.ListAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileImageListView(generics.ListAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()


class CompanyProfileImageCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()


class CompanyProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()
