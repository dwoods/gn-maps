# Create your views here.
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Location, MediaItem, TextMediaItem, ImageMediaItem, ExternalVideoMediaItem, AudioMediaItem, \
    VideoMediaItem


class MediaItemList(ListView):

    template_name = 'mediastory/location_media.html'
    context_object_name = 'media_items'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MediaItemList, self).get_context_data(**kwargs)
        context['location'] = self.location

        queryset = context['media_items']

        context['text_items'] = queryset.filter(polymorphic_ctype=ContentType.objects.get_for_model(TextMediaItem))
        context['image_items'] = queryset.filter(polymorphic_ctype=ContentType.objects.get_for_model(ImageMediaItem))
        context['audio_items'] = queryset.filter(polymorphic_ctype=ContentType.objects.get_for_model(AudioMediaItem))
        context['video_items'] = queryset.filter(Q(polymorphic_ctype=ContentType.objects.get_for_model(ExternalVideoMediaItem)) |
                                                 Q(polymorphic_ctype=ContentType.objects.get_for_model(VideoMediaItem)))

        return context


    def get_queryset(self):
        self.location = get_object_or_404(Location, pk=self.args[0])
        return MediaItem.objects.filter(location=self.location)


class LocationStoriesList(ListView):

    template_name = 'mediastory/location_stories.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LocationStoriesList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['location'] = self.location
        return context


    def get_queryset(self):
        self.location = get_object_or_404(Location, name=self.args[0])
        return MediaItem.objects.filter(location=self.location)

class LocationList(ListView):

    template_name = 'mediastory/location_list.html'
    context_object_name = 'locations'

    queryset = Location.objects.all()



class MediaItemDetail(DetailView):

    template_name = 'mediastory/mediaitem_detail.html'
    context_object_name = 'mediaitem'
    queryset = MediaItem.objects.all()


class VideoItemDetail(DetailView):
    template_name = 'mediastory/videoplayer.html'
    context_object_name = 'videoitem'
    queryset = VideoMediaItem.objects.all()


class MapView(TemplateView):
    template_name = "mediastory/main.html"


class LocationsLayer(GeoJSONLayerView):
    # Options
    properties = {
        'name': 'name',
        'description': 'description',
        'population': 'population'
    }


