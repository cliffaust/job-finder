from rest_framework import generics
from .serializers import CompanySerializer, CompanyProfileSerializer, CompanyProfileImageSerializer
from company.models import Company, CompanyProfile, CompanyProfileImages


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyProfileListView(generics.ListAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()

    def perform_create(self, serializer):
        company_slug = self.kwargs.get("company_slug")
        company = generics.get_object_or_404(Company, slug=company_slug)

        serializer.save(company=company)


class CompanyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileImageListView(generics.ListAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()


class CompanyProfileImageCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()

    def perform_create(self, serializer):
        company_profile_slug = self.kwargs.get("company_profile_slug")
        company_profile = generics.get_object_or_404(CompanyProfile, slug=company_profile_slug)


class CompanyProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()
