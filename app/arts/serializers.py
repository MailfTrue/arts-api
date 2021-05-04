from rest_framework import serializers
from app.arts.models import ArtWork


class ArtWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtWork
        fields = 'id', 'title', 'description', 'type', 'image'
