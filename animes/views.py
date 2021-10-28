from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404

from .serializers import NoteSerializer


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")


@api_view(['GET', 'POST'])
def api_note(request, anime_id):
    try:
        anime = Anime.objects.get(id=anime_id)
    except Anime.DoesNotExist:
        raise Http404()
    serialized_anime = NoteSerializer(anime)
    return Response(serialized_anime.data)