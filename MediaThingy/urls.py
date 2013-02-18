from django.conf.urls import patterns, include
from music.models import Artist
from music.views import home, music, test_weezer, artists, artist_name, artist_album_title
from picture.views import pictures

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#artist_detail_info = {
#    "queryset" : Artist.objects.all(),
#    "template_object_name" : "author",
#}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaThingy.views.home', name='home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', home),
    (r'^music/$', music),
    (r'^pictures/$', pictures),
    (r'^test_weezer/$', test_weezer),
    (r'^music/artists/$', artists),
    (r'^music/artists/([\w\W]+)/([\w\W]+)/$', artist_album_title),
    (r'^music/artists/([\w\W]+)/$', artist_name),
)

#if DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'static'}),
#)