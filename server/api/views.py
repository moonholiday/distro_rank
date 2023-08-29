from rest_framework import viewsets
from .models import LinuxDistribution
from .serializers import LinuxDistributionSerializer


class LinuxDistributionViewSet(viewsets.ModelViewSet):
    queryset = LinuxDistribution.objects.all()
    serializer_class = LinuxDistributionSerializer
