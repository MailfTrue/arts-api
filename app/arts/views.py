import django_filters.rest_framework
from rest_framework import viewsets
from app.arts.models import ArtWork
from app.arts.serializers import ArtWorkSerializer


class ArtWorkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArtWorkSerializer
    queryset = ArtWork.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = 'type',
