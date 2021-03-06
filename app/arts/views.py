import django_filters.rest_framework
from rest_framework import viewsets, permissions
from app.arts.models import ArtWork
from app.arts.serializers import ArtWorkSerializer


class ArtWorkViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = []
    serializer_class = ArtWorkSerializer
    queryset = ArtWork.objects.filter(show=True)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = 'type',
    pagination_class = None
