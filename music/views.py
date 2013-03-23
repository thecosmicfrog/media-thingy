import eyed3
import os
import shutil
from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Artist, Album, Track
from MediaThingy.settings import MEDIA_ROOT, MEDIA_URL, SITE_URL

def base(request):
    return render_to_response('base.html', locals())

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def music(request):
    return render_to_response('music.html', locals(), context_instance=RequestContext(request))

def upload(request):
    return render_to_response('upload.html', locals(), context_instance=RequestContext(request))

def upload_handler(request):
    if request.method == 'POST':
        f = request.FILES['upload']
        filename = str(f)
        f_ext = os.path.splitext(filename)[1]
        
        # If file is a compatible music file, build a filesystem structure for
        # it (media/artist-name/album-name), then write it to that location and
        # add details of the file to the database.
        if f_ext in ['.mp3']:
            with open(MEDIA_ROOT + str(f), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
                
                filename = eyed3.load(MEDIA_ROOT + filename)
                dir_struct = MEDIA_ROOT + 'music' + '/' + filename.tag.artist + '/' + filename.tag.album + '/'
                
                try:
                    if not os.path.isdir(dir_struct):
                        os.makedirs(dir_struct)
                    shutil.move(MEDIA_ROOT + str(f), dir_struct)
                except OSError as ose:
                    if ose.errno != 17:
                        raise
                    # Need to pass on Errno 17, due to race conditions caused
                    # by making directories that already exist.
                    pass
            
            # If the artist or album doesn't exist in the database, create
            # table(s) for them. If they already exists, perform a query to
            # obtain an Artist or Album object for use as a foreign key.
            if not Artist.objects.filter(name=filename.tag.artist).exists():
                artist = Artist(name=filename.tag.artist)
                artist.save()
            else:
                artist_set = Artist.objects.filter(name=filename.tag.artist)
                artist = [a for a in artist_set][0]
    
            if not Album.objects.filter(title=filename.tag.album).exists():
                album = Album(title=filename.tag.album, artist=artist)
                album.save()
            else:
                album_set = Album.objects.filter(title=filename.tag.album)
                album = [a for a in album_set][0]
            
            if not Track.objects.filter(title=filename.tag.title).exists():
                track = Track(title=filename.tag.title, \
                           album=album, \
                           artist=artist, \
                           fspath=dir_struct + str(f), \
                           media_url=MEDIA_URL + (dir_struct + str(f)).split(MEDIA_ROOT)[1])
                track.save()
                print 'Added to DB: ' + filename.tag.title
            
                return render_to_response('upload_success.html', locals(), context_instance=RequestContext(request))
        
        # TODO: Picture uploads
        elif f_ext in ['.jpg']:
            with open(MEDIA_ROOT + 'pictures/' + filename, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
                
                return render_to_response('upload_success.html', locals(), context_instance=RequestContext(request)) 
        
        # TODO: Video uploads
        elif f_ext in ['.mp4']:
            with open(MEDIA_ROOT + 'videos/' + filename, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
                return render_to_response('upload_success.html', locals(), context_instance=RequestContext(request)) 

    return render_to_response('upload_failure.html', locals(), context_instance=RequestContext(request))

def artists(request):
    artists = Artist.objects.order_by('name')
    return render_to_response('music/artists.html', locals(), context_instance=RequestContext(request))

def artist_name(request, artist_name):
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name.html', locals(), context_instance=RequestContext(request))

def artist_name_albums(request, artist_name):
    albums = Album.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name/albums.html', locals(), context_instance=RequestContext(request))

def artist_name_albums_album_title_track_title(request, artist_name, album_title, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/artist/name/albums/album_title_track_title.html', locals(), context_instance=RequestContext(request))

def artist_name_songs(request, artist_name):
    tracks = Track.objects.filter(artist__name=artist_name).order_by('title')
    return render_to_response('music/artist/name/songs.html', locals(), context_instance=RequestContext(request))

def artist_name_songs_track_title(request, artist_name, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/artist/name/songs/track_title.html', locals(), context_instance=RequestContext(request))

def artist_album_title(request, artist_name, album_title):
    artist_name_split = artist_name.split('/albums')[0]
    album_tracks = Track.objects.filter(album__title=album_title)
    return render_to_response('music/artist/album_title.html', locals(), context_instance=RequestContext(request))

def albums(request):
    albums = Album.objects.all().order_by('title')
    return render_to_response('music/albums.html', locals(), context_instance=RequestContext(request))

def album_title(request, album_title):
    album_tracks = Track.objects.filter(album__title=album_title).order_by('title')
    artist_set = Artist.objects.filter(album__title=album_title)
    artist_name = [a.name for a in artist_set]
    return render_to_response('music/album/title.html', locals(), context_instance=RequestContext(request))

def album_title_track_title(request, album_title, track_title):
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    return render_to_response('music/album/track_title.html', locals(), context_instance=RequestContext(request))

def songs(request):
    tracks = Track.objects.all().order_by('title')
    return render_to_response('music/songs.html', locals(), context_instance=RequestContext(request))

def track(request, track_title):
    site_url = SITE_URL
    track_set = Track.objects.filter(title=track_title)
    track = [t for t in track_set][0] # Assign the first element in the list to track_url
    
    return render_to_response('music/track.html', locals(), context_instance=RequestContext(request))

