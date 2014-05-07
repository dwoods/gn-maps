from django.conf.urls import patterns, url
from .views import MediaItemList, LocationList, MediaItemDetail, VideoItemDetail

urlpatterns = patterns('',
    url(r'^$', LocationList.as_view(), name='location_list'),
    url(r'^locations/$', LocationList.as_view(), name='location_list_alt'),
    url(r'^location_media/(\d+)/$', MediaItemList.as_view(), name='mediaitem_list'),
    url(r'^media/(?P<pk>\d+)/$', MediaItemDetail.as_view(), name='mediaitem_detail'),
    url(r'^video/(?P<pk>\d+)/$', VideoItemDetail.as_view(), name='videoitem_embed'),
)