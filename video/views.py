from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video
from MediaThingy.settings import MEDIA_ROOT

def videos(request):
    return render_to_response('videos/videos.html', locals(), context_instance=RequestContext(request))