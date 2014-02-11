from django.db import models
from polymorphic import PolymorphicModel

# Create your models here.
from filebrowser.fields import FileBrowseField


class Location(models.Model):
    name = models.CharField("Name", max_length=100, blank=False, null=False)

    def __unicode__(self):
        return self.name

class MediaItem(PolymorphicModel):
    title = models.CharField("Title", max_length=100, blank=False, null=False)
    description = models.TextField("Description")
    location = models.ForeignKey(Location)


class TextMediaItem(MediaItem):

    text = models.TextField(help_text='Editor Redactor')


class ImageMediaItem(MediaItem):
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)








