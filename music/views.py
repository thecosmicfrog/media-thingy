from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Artist, Album, Track

def base(request):
    crumbs = make_crumbs(request)
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

def artist_album_title(request, artist_name, album_title):
    crumbs = make_crumbs(request)
    album_tracks = Track.objects.filter(album__title=album_title)
    return render_to_response('artist_album_title.html', locals(), context_instance=RequestContext(request))

def albums(request):
    crumbs = make_crumbs(request)
    albums = Album.objects.all()
    return render_to_response('albums.html', locals(), context_instance=RequestContext(request))

def album_title(request, album_title):
    crumbs = make_crumbs(request)
    album_tracks = Track.objects.filter(album__title=album_title).order_by('title')
    artist_set = Artist.objects.filter(album__title=album_title)
    for a in artist_set:
        artist_name = a
    return render_to_response('album_title.html', locals(), context_instance=RequestContext(request))

def songs(request):
    crumbs = make_crumbs(request)
    songs = Track.objects.all()
    return render_to_response('songs.html', locals(), context_instance=RequestContext(request))    

def make_crumbs(request):
    crumbs = request.get_full_path().split('/')
    del crumbs[0]
    del crumbs[len(crumbs)-1]
#    del crumbs[len(crumbs)-2]
    return crumbs

