from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.anime.title} - {self.rating}'

class VoiceActor(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
