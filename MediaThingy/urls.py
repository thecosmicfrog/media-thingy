from django.conf.urls import patterns, include
from music.views import home, music, upload_handler
from music.views import artists, artist_name, artist_album_title, artist_name_albums, \
                        artist_name_songs, artist_name_songs_track_title, \
                        artist_name_albums_album_title_track_title
from music.views import albums, album_title, album_title_track_title
from music.views import songs, track
from picture.views import pictures, picture_name
from video.views import videos, video_title

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaThingy.views.home', name='home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', home),
    (r'^music/$', music),
    
    (r'^music/artists/$', artists),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/albums/(?P<album_title>[\w\W]+)/(?P<track_title>[\w\W]+)/$', \
                artist_name_albums_album_title_track_title),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/songs/(?P<track_title>[\w\W]+)/$', artist_name_songs_track_title),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/albums/$', artist_name_albums),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/songs/$', artist_name_songs),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/(?P<album_title>[\w\W]+)/$', artist_album_title),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/$', artist_name),
    
    (r'^music/albums/(?P<album_title>[\w\W]+)/(?P<track_title>[\w\W]+)/$', album_title_track_title),
    (r'^music/albums/(?P<album_title>[\w\W]+)/$', album_title),
    (r'^music/albums/$', albums),
    
    (r'^music/songs/$', songs),
    (r'^music/songs/(?P<track_title>[\w\W]+)/$', track),
    
    (r'^pictures/(?P<picture_name>[\w\W]+)/$', picture_name),
    (r'^pictures/$', pictures),
    
    (r'^videos/(?P<video_title>[\w\W]+)/$', video_title),
    (r'^videos/$', videos),
    
    (r'^upload_handler/$', upload_handler),
)