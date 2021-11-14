from .serializers import JobSerializer, SeekerSerializer
from jobs.models import Job, Seeker
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


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
