from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404

from .serializers import AnimeSerializer


@api_view(['GET', 'POST', 'DELETE'])
def api_anime(request, anime_id):
    try:
        anime = Anime.objects.get(id=anime_id)
    except Anime.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_anime_data = request.data
        anime.title = new_anime_data['title']
        anime.img = new_anime_data['img']
        anime.mal_id = new_anime_data['mal_id']
        anime.save()

    elif request.method == 'DELETE':
        anime = Anime()
        anime.id = anime_id
        anime.delete()

    serialized_anime = AnimeSerializer(anime)
    return Response(serialized_anime.data)


@api_view(['GET', 'POST'])
def api_anime_list(request):
    if request.method == 'POST':
        new_anime_data = request.data
        anime = Anime()
        anime.title = new_anime_data["title"]
        anime.img = new_anime_data['img']
        anime.mal_id = new_anime_data['mal_id']
        anime.save()

    animes = Anime.objects.all()
    serialized_animes = AnimeSerializer(animes, many=True)
    return Response(serialized_animes.data)


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.POST.get('img')
        mal_id = request.POST.get('mal_id')
        
        anime = Anime()

        
        anime.title = title
        anime.img = img
        anime.mal_id = mal_id
        anime.save()

        
        serialized_animes = AnimeSerializer(animes, many=True)
        return Response(serialized_animes.data)

