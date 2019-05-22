'''
Created on 21 may. 2019

@author: sebas
'''
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^films/$', views.FilmListView.as_view(), name='films'),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
#     url(r'^directores/$', views.DirectoresListView.as_view(), name='directores'),
#     url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='directores-detail'),
]