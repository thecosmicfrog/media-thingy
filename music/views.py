# Create your views here.
from django.shortcuts import render_to_response
from models import Track

def base(request):
    return render_to_response('base.html', locals())

def home(request):
    return render_to_response('home.html', locals())

def music(request):
    tracks = Track.objects.all()
    return render_to_response('music.html', locals())