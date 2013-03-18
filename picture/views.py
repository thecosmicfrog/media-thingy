from django.shortcuts import render_to_response
from django.template import RequestContext
from picture.models import Picture
from MediaThingy.settings import MEDIA_ROOT

def pictures(request):
    pictures = Picture.objects.order_by('name')
#    url_set = Picture.objects.all()
#    picture_url_full = [u.url for u in url_set]
#    picture_media_urls = [p.split(MEDIA_ROOT)[1] for p in picture_url_full]
#    folder_struct = []
#    for picture in pictures:
#        folder_struct.append(picture.url.split(MEDIA_ROOT + 'pictures/')[1].split('/'))
#    print picture_media_urls
        
    return render_to_response('pictures/pictures.html', locals(), context_instance=RequestContext(request))

def picture_name(request, picture_name):
    url_set = Picture.objects.filter(name=picture_name)
    picture_url_full = [u.url for u in url_set][0]
    picture_media_url = picture_url_full.split(MEDIA_ROOT)[1]
    return render_to_response('pictures/picture/name.html', locals(), context_instance=RequestContext(request))