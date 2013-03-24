from django.shortcuts import render_to_response
from django.template import RequestContext
from picture.models import Picture

def pictures(request):
    pictures = Picture.objects.order_by('name')
    return render_to_response('pictures/pictures.html', locals(), context_instance=RequestContext(request))

def picture_name(request, picture_name):
    picture_set = Picture.objects.filter(name=picture_name)
    picture = [p for p in picture_set][0] # Assign the first element in the list to picture
    return render_to_response('pictures/picture/name.html', locals(), context_instance=RequestContext(request))