from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField(max_length=700)
    
    def __unicode__(self):
        return self.title