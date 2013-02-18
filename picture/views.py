from django.shortcuts import render_to_response
from django.template import RequestContext
from picture.models import Picture
from os import listdir
import os
import shutil
from MediaThingy.settings import STATIC_ROOT

def pictures(request):
    images = listdir(STATIC_ROOT + 'images')
    
    for image in images:
        pass

    
#    pictures = Picture.objects.all()
    return render_to_response('pictures.html', locals(), context_instance=RequestContext(request))