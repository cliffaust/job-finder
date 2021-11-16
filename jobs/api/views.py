from .serializers import JobSerializer, SeekerSerializer
from jobs.models import Job, Seeker
from rest_framework import generics
from company.models import Company
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        company_slug = self.kwargs.get("company_slug")
        company = generics.get_object_or_404(Company, slug=company_slug)

        if company.user == self.request.user:
            raise PermissionDenied("You can't add a job to this home")

        serializer.save(company=company)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Job.objects.filter(slug=slug)
        return queryset


class SeekerListView(generics.ListAPIView):
    serializer_class = SeekerSerializer

    def get_queryset(self):
        queryset = Seeker.objects.all()

        job_slug = self.kwargs.get("job_slug")
        if job_slug is not None:
            job = generics.get_object_or_404(Job, slug=job_slug)
            queryset = Seeker.objects.filter(job=job)

        return queryset


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
