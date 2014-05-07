from embed_video.admin import AdminVideoMixin
from leaflet.admin import LeafletGeoAdmin

__author__ = 'dwoods'

from django.contrib import admin
from django.forms import ModelForm, Media
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import MediaItem, ImageMediaItem, TextMediaItem, AudioMediaItem, Location, ExternalVideoMediaItem, \
    VideoMediaItem
from suit_redactor.widgets import RedactorWidget



class LocationEditor(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en', 'minHeight': 100}),
            }

    class Media:
        js = ('filebrowser/js/FB_Redactor.js',)
        css = {
            'all': ('filebrowser/css/suit-filebrowser.css',)
        }

class MediaItemEditor(ModelForm):
    class Meta:
        widgets = {
            #'ckeditor': CKEditorWidget(editor_options={'startupFocus': True}),
            'text': RedactorWidget(editor_options={
                'lang': 'en',
                'plugins': ['filebrowser']
            }),
        }

    class Media:
        js = ('filebrowser/js/FB_Redactor.js',)
        css = {
            'all': ('filebrowser/css/suit-filebrowser.css',)
        }


class MediaItemInline(admin.TabularInline):
    model = MediaItem
    fields = ('title', 'thumbnail')
    readonly_fields = ('title', 'thumbnail')
    extra = 0



class LocationAdmin(admin.ModelAdmin):
    model = Location
    form = LocationEditor


class MediaItemAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = MediaItem

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    base_form = MediaItemEditor
    base_fieldsets = (
    )


class TextMediaItemAdmin(MediaItemAdmin):

    model = TextMediaItem

    list_display = ('title', 'order', 'thumbnail')
    # list_editable = ('order',)

class ImageMediaItemAdmin(MediaItemAdmin):

    model = ImageMediaItem
    list_display = ('title', 'order', 'thumbnail')
    # list_editable = ('order',)

class AudioMediaItemAdmin(MediaItemAdmin):

    model = AudioMediaItem
    list_display = ('title', 'order', 'thumbnail')
    # list_editable = ('order',)

class ExternalVideoMediaItemAdmin(AdminVideoMixin, MediaItemAdmin):

    model = ExternalVideoMediaItem
    list_display = ('title', 'order', 'thumbnail')
    # list_editable = ('order',)

class VideoMediaItemAdmin(MediaItemAdmin):

    model = VideoMediaItem
    list_display = ('title', 'order', 'thumbnail')
    # list_editable = ('order',)

class MediaItemParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = MediaItem
    child_models = (
        (TextMediaItem, TextMediaItemAdmin),
        (ImageMediaItem, ImageMediaItemAdmin),
        (AudioMediaItem, AudioMediaItemAdmin),
        (ExternalVideoMediaItem, ExternalVideoMediaItemAdmin),
        (VideoMediaItem, VideoMediaItemAdmin),
    )
    polymorphic_list = True
    readonly_fields = ('thumbnail',)
    list_display = ('title', 'location', 'order', 'thumbnail')
    list_editable = ('order',)
    list_filter = ('location',)

# Only the parent needs to be registered:
admin.site.register(Location, LocationAdmin)
admin.site.register(MediaItem, MediaItemParentAdmin)
