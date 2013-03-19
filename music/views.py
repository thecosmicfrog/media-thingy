from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Artist, Album, Track
from MediaThingy.settings import SITE_URL

def base(request):
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def music(request):
    return render_to_response('music.html', locals(), context_instance=RequestContext(request))

def artists(request):
    artists = Artist.objects.order_by('name')
    return render_to_response('music/artists.html', locals(), context_instance=RequestContext(request))

def artist_name(request, artist_name):
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name.html', locals(), context_instance=RequestContext(request))

def artist_name_albums(request, artist_name):
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name/albums.html', locals(), context_instance=RequestContext(request))

def artist_name_albums_album_title_track_title(request, artist_name, album_title, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/artist/name/albums/album_title_track_title.html', locals(), context_instance=RequestContext(request))

def artist_name_songs(request, artist_name):
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name/songs.html', locals(), context_instance=RequestContext(request))

def artist_name_songs_track_title(request, artist_name, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/artist/name/songs/track_title.html', locals(), context_instance=RequestContext(request))

def artist_album_title(request, artist_name, album_title):
    album_tracks = Track.objects.filter(album__title=album_title)
    return render_to_response('music/artist/album_title.html', locals(), context_instance=RequestContext(request))

def albums(request):
    albums = Album.objects.all().order_by('title')
    return render_to_response('music/albums.html', locals(), context_instance=RequestContext(request))

def album_title(request, album_title):
    album_tracks = Track.objects.filter(album__title=album_title).order_by('title')
    artist_set = Artist.objects.filter(album__title=album_title)
    artist_name = [a.name for a in artist_set][0]
    return render_to_response('music/album/title.html', locals(), context_instance=RequestContext(request))

def album_title_track_title(request, album_title, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/album/track_title.html', locals(), context_instance=RequestContext(request))

def songs(request):
    tracks = Track.objects.all().order_by('title')
    return render_to_response('music/songs.html', locals(), context_instance=RequestContext(request))

def track(request, track_title):
    site_url = SITE_URL
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    
    return render_to_response('music/track.html', locals(), context_instance=RequestContext(request))

