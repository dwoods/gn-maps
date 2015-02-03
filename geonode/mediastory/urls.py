from django.conf.urls import patterns, url
from djgeojson.views import GeoJSONLayerView
from .views import MediaItemList, LocationList, MediaItemDetail, VideoItemDetail, MapView
from geonode.mediastory.models import Location

urlpatterns = patterns('',
   url(r'^$', MapView.as_view(), name='location_list'),
   url(r'^locations/$', MapView.as_view(), name='location_list_alt'),
   url(r'^location_media/(\d+)/$', MediaItemList.as_view(), name='mediaitem_list'),
   url(r'^media/(?P<pk>\d+)/$', MediaItemDetail.as_view(), name='mediaitem_detail'),
   url(r'^video/(?P<pk>\d+)/$', VideoItemDetail.as_view(), name='videoitem_embed'),
   url(r'^data.locations$', GeoJSONLayerView.as_view(model=Location, properties=('id', 'name', 'description', 'population', 'media_url')),
       name='location_geodata'),

)