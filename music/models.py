from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    record_label = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist)
    year_released = models.IntegerField()
    length = models.CharField(max_length=5)
    genre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title
    
class Track(models.Model):
    title = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    length = models.CharField(max_length=8)
    url = models.URLField(max_length=200)
    
    def __unicode__(self):
        return self.title