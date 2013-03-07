from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video
from MediaThingy.settings import MEDIA_ROOT

def videos(request):
    url_set = Video.objects.all()
    video_url_full = [u.url for u in url_set][0]
    print video_url_full
    video_media_url = video_url_full.split(MEDIA_ROOT)[1]
    print video_media_url
    return render_to_response('videos/videos.html', locals(), context_instance=RequestContext(request))