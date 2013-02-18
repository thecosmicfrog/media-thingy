from django.db import models

class Picture(models.Model):
    url = models.URLField(max_length=200)
    
    def __unicode__(self):
        return self.url