from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Artist, Album, Track

def base(request):
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def music(request):
    return render_to_response('music.html', locals(), context_instance=RequestContext(request))

def test_weezer(request):
    tracks = Track.objects.all()
    return render_to_response('test_weezer.html', locals(), context_instance=RequestContext(request))

def artists(request):
    artists = Artist.objects.order_by('name')
    return render_to_response('artists.html', locals(), context_instance=RequestContext(request))

def artist_name(request, artist_name):
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('artist_name.html', locals(), context_instance=RequestContext(request))

def artist_album_title(request, artist_name, album_title):
    album_tracks = Track.objects.filter(album__title=album_title)
    return render_to_response('artist_album_title.html', locals(), context_instance=RequestContext(request))