from django.db import models

# Create your models here.

class gi_videogame(models.Model):
    gamename = models.CharField(max_length=255)
    releaseURL = models.CharField(max_length=255)
    releaseDate = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('gamename', 'releaseURL', 'releaseDate')



class gi_videogame_release(models.Model):
    game_fk = models.ForeignKey(gi_videogame,on_delete=models.CASCADE,default = None)
    platform = models.CharField(max_length=255)
    no_of_player = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    industry_rating = models.CharField(max_length=255)
    gameImage = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

