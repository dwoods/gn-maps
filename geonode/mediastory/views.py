# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Location, MediaItem

class MediaItemList(ListView):

    template_name = 'mediastory/location_media.html'
    context_object_name = 'media_items'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MediaItemList, self).get_context_data(**kwargs)
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