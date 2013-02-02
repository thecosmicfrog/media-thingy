from django.conf.urls import patterns, include, url
from music.views import base
from music.views import home
from music.views import music

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaThingy.views.home', name='home'),
    (r'^base/$', base),
    (r'^home/$', home),
    (r'^music/$', music),
)
