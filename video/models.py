from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=400)
    filename = models.CharField(max_length=400)
    fspath = models.URLField(max_length=700)
    media_url = models.URLField(max_length=600)
    
    def __unicode__(self):
        return self.title