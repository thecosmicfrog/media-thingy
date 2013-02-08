from django.conf.urls import patterns, include, url
from MediaThingy.settings import DEBUG
from music.views import base
from music.views import home
from music.views import music
from music.views import test_weezer
from music.views import artists

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaThingy.views.home', name='home'),
    (r'^base/$', base),
    (r'^home/$', home),
    (r'^music/$', music),
    (r'^test_weezer/$', test_weezer),
    (r'^music/artists/$', artists),
)

#if DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'static'}),
#)