from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.AdsIndex.as_view(), name="index"),
    url(r'^post-ad/$', views.ad_new, name='ad_new'),
    url(r'^ads/$', views.AdsList.as_view(), name='list_ads'),
    url(r'^ads-view/(?P<slug>[\w-]+)/$', views.ad_details, name='ad_details'),
)
