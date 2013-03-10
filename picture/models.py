from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=600)
    
    def __unicode__(self):
        return self.name