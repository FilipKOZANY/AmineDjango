from django.contrib import admin
from .models import Anime, Character, VoiceActor, Review

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title', 'description')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'anime')
    search_fields = ('name', 'description')
    list_filter = ('anime',)

@admin.register(VoiceActor)
class VoiceActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'character')
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('anime', 'rating')
    search_fields = ('review_text',)
    list_filter = ('anime', 'rating')
