from django.conf import settings
from django.db import models
from embed_video.backends import detect_backend, UnknownBackendException
from embed_video.fields import EmbedVideoField
from polymorphic import PolymorphicModel, ShowFieldType, ShowFieldTypeAndContent
from filebrowser.settings import ADMIN_THUMBNAIL
from geoposition.fields import GeopositionField
from filebrowser.fields import FileBrowseField


class Location(models.Model):
    name = models.CharField("Name", max_length=100, blank=False, null=False)
    description = models.TextField("Description", blank=True, null=True)
    population = models.IntegerField("Population", blank=True, null=True)
    position = GeopositionField()

    def __unicode__(self):
        return self.name

class MediaItem(ShowFieldTypeAndContent, PolymorphicModel):
    title = models.CharField("Title", max_length=100, blank=False, null=False)
    description = models.TextField("Description")
    location = models.ForeignKey(Location)

    attribution = models.CharField("Attribution", max_length=200, blank=True, null=True)

    order = models.IntegerField("Sort Order", default=0, blank=True, null=False)

    class Meta:
        verbose_name = "Media Item"
        ordering = ('order',)

    def __unicode__(self):
        return self.title

    def thumbnail(self):
        return ''


class TextMediaItem(MediaItem):

    text = models.TextField(help_text='Story text')

    class Meta:
        verbose_name = "Text"

    @property
    def thumnail_url(self):
        return settings.STATIC_URL + 'mediastory/images/text-icon.png'

    def thumbnail(self):
        return '<img src="%s" />' % self.thumnail_url
    thumbnail.allow_tags = True


class ImageMediaItem(MediaItem):

    image = FileBrowseField("Image", max_length=200, format="image", blank=False, null=False)
    text = models.TextField(help_text='Story text', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Image"

    @property
    def thumbnail_url(self):
        if self.image and self.image.filetype == "Image":
            self.image.url_thumbnail
        else:
            return ""

    def thumbnail(self):
        return '<img src="%s" />' % self.thumbnail_url
    thumbnail.allow_tags = True

class AudioMediaItem(MediaItem):

    audio_file = FileBrowseField("Audio File", max_length=200, format="Audio", blank=False, null=False)
    text = models.TextField(help_text='Story text', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Audio"

    @property
    def thumnail_url(self):
        return settings.STATIC_URL + 'mediastory/images/music-icon.png'

    def thumbnail(self):
        return '<img src="%s" />' % self.thumnail_url
    thumbnail.allow_tags = True



class ExternalVideoMediaItem(MediaItem):

    video = EmbedVideoField("Video", max_length=200, blank=False, null=False)
    text = models.TextField(help_text='Story text', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "External Video"

    @property
    def thumbnail_url(self):
        try:
            backend = detect_backend(self.video)
            return backend.get_thumbnail_url()
        except UnknownBackendException:
            return ''

    def thumbnail(self):
        return '<img src="%s" style="height: 60px;" />' % self.thumbnail_url
    thumbnail.allow_tags = True

class VideoMediaItem(MediaItem):

    # video_file = FileBrowseField("Video File", max_length=200, format="Video", blank=False, null=False)
    video_file_webm = FileBrowseField("Video File (webm)", max_length=200, format="Video", blank=False, null=True)
    video_file_mp4 = FileBrowseField("Video File (mp4)", max_length=200, format="Video", blank=False, null=True)
    text = models.TextField(help_text='Story text', blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Video"

    @property
    def thumbnail_url(self):
        return ''

    def thumbnail(self):
        return ''
    thumbnail.allow_tags = True








