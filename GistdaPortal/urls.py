from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *
home_url = url(
    r'^/?$', TemplateView.as_view(template_name='site_index.html'),
    name='home')
home2_url = url(
    r'^index2/$', TemplateView.as_view(template_name='index2.html'),
    name='home2')
urlpatterns = patterns('', home_url, home2_url,) + urlpatterns
