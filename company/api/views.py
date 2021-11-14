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

    def get_queryset(self):
        queryset = Company.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Company.objects.filter(slug=slug)
        return queryset


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

    def get_queryset(self):
        queryset = CompanyProfile.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = CompanyProfile.objects.filter(slug=slug)
        return queryset


class CompanyProfileImageListView(generics.ListAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()


class CompanyProfileImageCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()

    def perform_create(self, serializer):
        company_profile_slug = self.kwargs.get("company_profile_slug")
        company_profile = generics.get_object_or_404(CompanyProfile, slug=company_profile_slug)

        serializer.save(company_profile=company_profile)


class CompanyProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileImageSerializer

    def get_queryset(self):
        queryset = CompanyProfileImages.objects.all()
        return queryset
