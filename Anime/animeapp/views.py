from django.shortcuts import render, get_object_or_404
from .models import Anime, Character

def index(request):
    animes = Anime.objects.all()
    context = {
        'animes': animes,
    }
    return render(request, 'animeapp/index.html', context)
def anime_list(request):
    animes = Anime.objects.all()
    context = {'animes': animes}
    return render(request, 'animeapp/anime_list.html', context)

def characters(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    characters = Character.objects.filter(anime=anime)
    context = {
        'anime': anime,
        'characters': characters,
    }
    return render(request, 'animeapp/characters.html', context)

def voice_actors(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    voice_actors = character.voiceactor_set.all()
    context = {'character': character, 'voice_actors': voice_actors}
    return render(request, 'animeapp/voice_actors.html', context)
