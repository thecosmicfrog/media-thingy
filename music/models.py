from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist)
    
    def __unicode__(self):
        return self.title
    
class Track(models.Model):
    title = models.CharField(max_length=400)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    url = models.URLField(max_length=600)
    
    def __unicode__(self):
        return self.title