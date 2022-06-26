from pyexpat import model
from rest_framework import serializers
from .models import Artist, Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        many=False,
        read_only=True
    )
    class Meta:
        model = Song
        fields = ('artist', 'title', 'album', 'preview_url', 'artist_id',)

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'nationality', 'name', 'genre', 'songs',)