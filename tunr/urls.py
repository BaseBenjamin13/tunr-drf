from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    # path('artists/', views.artist_list, name='artist_list'),
    # path('artists/<int:pk>/', views.artist_detail, name='artist_detail'),
    # # path('artists/new', views.artist_create, name='artist_create'),
    # path('artists/new', views.ArtistCreate.as_view(), name='artist_create'),
    # path('artists/<int:pk>/update', views.ArtistUpdate.as_view(), name='artist_update'),
    # path('artists/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist_delete'),
    # path('songs/', views.song_list, name='song_list'),
    # path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    # path('songs/new', views.SongCreate.as_view(), name='song_create'),
    # path('songs/<int:pk>/update', views.SongUpdate.as_view(), name='song_update'),
    # path('songs/<int:pk>/delete', views.SongDelete.as_view(), name='song_delete'),
]
