from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Artist, Album, Track
from MediaThingy.settings import MEDIA_ROOT

def base(request):
    crumbs = make_crumbs(request)
    crumb_urls = []
    crumb_urls.append(crumbs[0])
    crumb_urls.append(crumbs[0] + '/' + crumbs[1])
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))

def home(request):
    crumbs = make_crumbs(request)
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def music(request):
    crumbs = make_crumbs(request)
    return render_to_response('music.html', locals(), context_instance=RequestContext(request))

def artists(request):
    crumbs = make_crumbs(request)
    artists = Artist.objects.order_by('name')
    return render_to_response('artists.html', locals(), context_instance=RequestContext(request))

def artist_name(request, artist_name):
    crumbs = make_crumbs(request)
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('artist_name.html', locals(), context_instance=RequestContext(request))

def artist_name_albums(request, artist_name):
    crumbs = make_crumbs(request)
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('artist_name_albums.html', locals(), context_instance=RequestContext(request))

def artist_name_albums_album_title_track_title(request, artist_name, album_title, track_title):
    crumbs = make_crumbs(request)
    url_set = Track.objects.filter(title=track_title)
    track_url_full = [u.url for u in url_set][0]              # Assign the first element in the list to track_url
    track_media_url = track_url_full.split(MEDIA_ROOT)[1]    # Split on STATIC_ROOT to find the relative URL
    return render_to_response('artist_name_songs_track_title.html', locals(), context_instance=RequestContext(request))

def artist_name_songs(request, artist_name):
    crumbs = make_crumbs(request)
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('artist_name_albums_album_title_track_title.html', locals(), context_instance=RequestContext(request))

def artist_name_songs_track_title(request, artist_name, track_title):
    crumbs = make_crumbs(request)
    url_set = Track.objects.filter(title=track_title)
    track_url_full = [u.url for u in url_set][0]              # Assign the first element in the list to track_url
    track_media_url = track_url_full.split(MEDIA_ROOT)[1]    # Split on STATIC_ROOT to find the relative URL
    return render_to_response('artist_name_songs_track_title.html', locals(), context_instance=RequestContext(request))

def artist_album_title(request, artist_name, album_title):
    crumbs = make_crumbs(request)
    album_tracks = Track.objects.filter(album__title=album_title)
    return render_to_response('artist_album_title.html', locals(), context_instance=RequestContext(request))

def albums(request):
    crumbs = make_crumbs(request)
    albums = Album.objects.all().order_by('title')
    return render_to_response('albums.html', locals(), context_instance=RequestContext(request))

def album_title(request, album_title):
    crumbs = make_crumbs(request)
    album_tracks = Track.objects.filter(album__title=album_title).order_by('title')
    artist_set = Artist.objects.filter(album__title=album_title)
    artist_name = [a.name for a in artist_set][0]
    return render_to_response('album_title.html', locals(), context_instance=RequestContext(request))

def album_title_track_title(request, album_title, track_title):
    crumbs = make_crumbs(request)
    url_set = Track.objects.filter(title=track_title)
    track_url_full = [u.url for u in url_set][0]            # Assign the first element in the list to track_url
    track_media_url = track_url_full.split(MEDIA_ROOT)[1]  # Split on STATIC_ROOT to find the relative URL
    return render_to_response('album_title_track_title.html', locals(), context_instance=RequestContext(request))

def songs(request):
    crumbs = make_crumbs(request)
    tracks = Track.objects.all().order_by('title')
    return render_to_response('songs.html', locals(), context_instance=RequestContext(request))

def track(request, track_title):
    crumbs = make_crumbs(request)
    url_set = Track.objects.filter(title=track_title)
    track_url_full = [u.url for u in url_set][0]            # Assign the first element in the list to track_url
    track_media_url = track_url_full.split(MEDIA_ROOT)[1]  # Split on STATIC_ROOT to find the relative URL 
    return render_to_response('track.html', locals(), context_instance=RequestContext(request))

def make_crumbs(request):
    crumbs = request.get_full_path().split('/')
    del crumbs[0]
    del crumbs[len(crumbs)-1]
    return crumbs

