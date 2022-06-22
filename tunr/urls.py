from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    # path('artists/new', views.artist_create, name='artist_create'),
    path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
]
