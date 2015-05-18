from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.AdsIndex.as_view(), name="index"),
    url(r'^post-ad/$', views.ad_new, name='ad_new'),
)