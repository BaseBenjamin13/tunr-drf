from ast import Delete
from django.shortcuts import render, redirect
from .models import Artist, Song
# from .forms import ArtistForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import JsonResponse

from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer
# Create your views here.

#Artist
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

#Song
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer





class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'photo_url', 'nationality']
    template_name = 'tunr/artist_form.html'
    success_url = '/artists/'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'photo_url', 'nationality']
    template_name = 'tunr/artist_update_form.html'
    success_url = '/artists/'

class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'tunr/artist_delete_form.html'
    success_url = '/artists/'

class SongCreate(CreateView):
    model = Song
    fields = ['artist', 'title', 'album', 'preview_url']
    template_name = 'tunr/song_form.html'
    success_url = '/songs/'

class SongUpdate(UpdateView):
    model = Song
    fields = ['artist', 'title', 'album', 'preview_url']
    template_name = 'tunr/song_update_form.html'
    success_url = '/songs/'

class SongDelete(DeleteView):
    model = Song
    template_name = 'tunr/song_delete_form.html'
    success_url = '/songs/'

def artist_list(request):
    artists = Artist.objects.all().values('name', 'nationality', 'photo_url',)
    artists = list(artists)
    return JsonResponse(artists, safe=False)
    # return render(request, 'tunr/artist_list.html', {'artists': artists})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'tunr/song_detail.html', {'song': song})

# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             artist = form.save()
#             return redirect('artist_detail', pk=artist.pk)
#     else:
#         form = ArtistForm()
#     return render(request, 'tunr/artist_form.html', {'form': form})