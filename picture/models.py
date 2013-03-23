from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=250)
    filename = models.CharField(max_length=250)
    fspath = models.URLField(max_length=600)
    media_url = models.URLField(max_length=500)
    
    def __unicode__(self):
        return self.name