from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, default='no name')
    nationality = models.CharField(max_length=100, default='no name')
    photo_url = models.TextField(default='no img')
    genre = models.CharField(max_length=100, default='no genre')

    def __str__(self):
        return self.name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, default='no song title')
    album = models.CharField(max_length=100, default='no album title')
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title