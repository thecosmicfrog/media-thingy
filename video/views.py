import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video
from MediaThingy.settings import MEDIA_ROOT, SITE_URL

def videos(request):
    videos = Video.objects.order_by('title')
    return render_to_response('videos/videos.html', locals(), context_instance=RequestContext(request))

def video_title(request, video_title):
    site_url = SITE_URL
    url_set = Video.objects.filter(title=video_title)
    video_url_full = [u.url for u in url_set][0]            # Assign the first element in the list to track_url
    video_media_url = video_url_full.split(MEDIA_ROOT)[1]  # Split on STATIC_ROOT to find the relative URL 
    return render_to_response('videos/video/title.html', locals(), context_instance=RequestContext(request))