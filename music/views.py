# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Track
from music.models import Artist

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
    artists = Artist.objects.all()
    return render_to_response('artists.html', locals(), context_instance=RequestContext(request))