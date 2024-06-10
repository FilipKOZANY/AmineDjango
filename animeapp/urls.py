from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime-list/', views.anime_list, name='anime_list'),
    path('anime/<int:anime_id>/characters/', views.characters, name='characters'),
    path('character/<int:character_id>/voice-actors/', views.voice_actors, name='voice_actors'),
]
