from rest_framework import generics
from .serializers import CompanySerializer, CompanyProfileSerializer, CompanyProfileImageSerializer
from company.models import Company, CompanyProfile, CompanyProfileImages
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserInstance, IsCompanyInstanceProfile, IsCompanyInstanceProfileImage


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def perform_create(self, serializer):
        if not self.request.user.is_company:
            raise PermissionDenied("Your account isn't a company account, please create one to proceed")
        return serializer.save(user=self.request.user)


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsUserInstance]
    lookup_field = "slug"

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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        company_slug = self.kwargs.get("company_slug")
        company = generics.get_object_or_404(Company, slug=company_slug)

        if company.user != self.request.user:
            raise PermissionDenied("You can't add to profile to this Company")
        return serializer.save(company=company)


class CompanyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated, IsCompanyInstanceProfile]
    lookup_field = "slug"

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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        company_profile_slug = self.kwargs.get("company_profile_slug")
        company_profile = generics.get_object_or_404(CompanyProfile, slug=company_profile_slug)

        if company_profile.company.user != self.request.user:
            raise PermissionDenied("You can't add to image profile to this Company")

        return serializer.save(company_profile=company_profile)


class CompanyProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileImageSerializer
    permission_classes = [IsAuthenticated, IsCompanyInstanceProfileImage]

    def get_queryset(self):
        queryset = CompanyProfileImages.objects.all()
        return queryset
