from rest_framework import serializers
from .models import Anime


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title', 'img', 'mal_id']