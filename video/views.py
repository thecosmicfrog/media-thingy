from django.shortcuts import render_to_response
from django.template import RequestContext
from video.models import Video

def videos(request):
    videos = Video.objects.order_by('title')
    return render_to_response('videos/videos.html', locals(), context_instance=RequestContext(request))

def video_title(request, video_title):
    video_set = Video.objects.filter(title=video_title)
    video = [v for v in video_set][0]
    return render_to_response('videos/video/title.html', locals(), context_instance=RequestContext(request))