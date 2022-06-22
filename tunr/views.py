from django.shortcuts import render, redirect
from .models import Artist, Song
# from .forms import ArtistForm
from django.views.generic.edit import CreateView

# Create your views here.

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'photo_url', 'nationality']
    template_name = 'tunr/artist_form.html'
    success_url = '/artists/'

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})

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