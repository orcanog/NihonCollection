from django.db import models

# Create your models here.
class AnimeInfos(models.Model):
    titre = models.CharField(max_length=100)
    image = models.URLField(max_length=200, default=None)
    id_anime = models.IntegerField(primary_key=True)


class FavoriDb(models.Model):
    pseudo = models.CharField(max_length=100)
    id_anime_key = models.ForeignKey(AnimeInfos, blank=True, null=True, on_delete=models.CASCADE)
