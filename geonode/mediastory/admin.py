__author__ = 'dwoods'

from django.contrib import admin
from django.forms import ModelForm, Media
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import MediaItem, ImageMediaItem, TextMediaItem, Location
from suit_redactor.widgets import RedactorWidget


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
        js = ('filebrowser/js/FB_CKEditor.js', 'filebrowser/js/FB_Redactor.js')
        css = {
            'all': ('filebrowser/css/suit-filebrowser.css',)
        }



class LocationAdmin(admin.ModelAdmin):
    model = Location



class MediaItemAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = MediaItem

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    base_form = MediaItemEditor
    base_fieldsets = (
    )

class TextMediaItemAdmin(MediaItemAdmin):
    # define custom features here
    model = TextMediaItem

class ImageMediaItemAdmin(MediaItemAdmin):
    # define custom features here
    model = ImageMediaItem


class MediaItemParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = MediaItem
    child_models = (
        (TextMediaItem, TextMediaItemAdmin),
        (ImageMediaItem, ImageMediaItemAdmin),
    )

# Only the parent needs to be registered:
admin.site.register(Location, LocationAdmin)
admin.site.register(MediaItem, MediaItemParentAdmin)
