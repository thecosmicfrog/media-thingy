from django.conf.urls import patterns, include
from music.views import home, music
from music.views import artists, artist_name, artist_album_title
from music.views import albums, album_title
from music.views import songs, track
from picture.views import pictures

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaThingy.views.home', name='home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', home),
    (r'^music/$', music),
    (r'^pictures/$', pictures),
    (r'^music/artists/$', artists),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/(?P<album_title>[\w\W]+)/$', artist_album_title),
    (r'^music/artists/(?P<artist_name>[\w\W]+)/$', artist_name),
    (r'^music/albums/(?P<album_title>[\w\W]+)/$', album_title),
    (r'^music/albums/$', albums),
    (r'^music/songs/$', songs),
    (r'^music/songs/(?P<track_title>[\w\W]+)/$', track),
)

#if DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'static'}),
#)