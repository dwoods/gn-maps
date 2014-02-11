from django.db import models
from embed_video.backends import detect_backend, UnknownBackendException
from embed_video.fields import EmbedVideoField
from polymorphic import PolymorphicModel, ShowFieldType, ShowFieldTypeAndContent
from filebrowser.settings import ADMIN_THUMBNAIL

# Create your models here.
from filebrowser.fields import FileBrowseField


class Location(models.Model):
    name = models.CharField("Name", max_length=100, blank=False, null=False)

    def __unicode__(self):
        return self.name

class MediaItem(ShowFieldTypeAndContent, PolymorphicModel):
    title = models.CharField("Title", max_length=100, blank=False, null=False)
    description = models.TextField("Description")
    location = models.ForeignKey(Location)

    class Meta:
        verbose_name = "Media Item"

    def __unicode__(self):
        return self.title

    def thumbnail(self):
        return 'BASE'

class TextMediaItem(MediaItem):

    text = models.TextField(help_text='Editor Redactor')

    class Meta:
        verbose_name = "Text"

    def thumbnail(self):
        return 'TEXT'
    thumbnail.allow_tags = True



class ImageMediaItem(MediaItem):

    image = FileBrowseField("Image", max_length=200, format="image", blank=False, null=False)

    class Meta:
        verbose_name = "Image"

    def thumbnail(self):
        if self.image and self.image.filetype == "Image":
            return '<img src="%s" style="height: 100px; width: 130px;"/ />' % self.image.version_generate('thumbnail').url
        else:
            return "blah"
        return "blah"
    thumbnail.allow_tags = True


class ExternalVideoMediaItem(MediaItem):

    video = EmbedVideoField("Video", max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = "External Video"

    def thumbnail(self):
        try:
            backend = detect_backend(self.video)
            return '<img src="%s" style="height: 100px; width: 130px;"/>' % backend.get_thumbnail_url()
        except UnknownBackendException:
            return '';
    thumbnail.allow_tags = True








