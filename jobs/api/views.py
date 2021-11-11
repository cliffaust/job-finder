from .serializers import CompanySerializer, SeekerSerializer
from jobs.models import Company, Seeker
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Company.objects.filter(slug=slug)
        return queryset


class SeekerListView(generics.ListAPIView):
    serializer_class = SeekerSerializer
    queryset = Seeker.objects.all()


class SeekerCreateView(generics.CreateAPIView):
    serializer_class = SeekerSerializer
    queryset = Seeker.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SeekerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SeekerSerializer

    def get_queryset(self):
        queryset = Seeker.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Seeker.objects.filter(slug=slug)
        return queryset
