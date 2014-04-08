from django.conf.urls import patterns, url
from .views import MediaItemList, LocationList, MediaItemDetail

urlpatterns = patterns('',
    url(r'^locations/$', LocationList.as_view(), name='location_list'),
    url(r'^location_media/(\d+)/$', MediaItemList.as_view(), name='mediaitem_list'),
    url(r'^media/(?P<pk>\d+)/$', MediaItemDetail.as_view(), name='mediaitem_detail'),
)