from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from webhook.models import Destination
from webhook.serializers import DestinationSerializer


class DestinationModelApiViewSet(ModelViewSet):
    """Api viewset for Destination model"""

    serializer_class = DestinationSerializer
    queryset = Destination.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["account"]
