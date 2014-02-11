from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField("Name", max_length=100, blank=False, null=False)

    def __unicode__(self):
        return self.name

class MediaItem(models.Model):
    title = models.CharField("Title", max_length=100, blank=False, null=False)
    description = models.TextField("Description")
