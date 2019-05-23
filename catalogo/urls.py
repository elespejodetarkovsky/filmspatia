'''
Created on 21 may. 2019

@author: sebas
'''
from django.conf.urls import url

from . import views

print("Hola Flavia")

urlpatterns = [
#     url('', views.index, name='index'),
#     url('films/', views.FilmListView.as_view(), name='films'),
#     url('film/(<int:pk>)', views.FilmDetailView.as_view(), name='film-detail'),
#     url('directores/', views.DirectorListView.as_view(), name='directores'),
#     url('^director/(<int:pk>)', views.DirectorListView.as_view(), name='persona-detail'),
    url(r'^$', views.index, name='index'),
    url(r'^films/$', views.FilmListView.as_view(), name='films'),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'^directores/$', views.DirectorListView.as_view(), name='directores'),
    url(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director-detail'),
]

urlpatterns += [   
    url(r'^misfilms/$', views.prestamosByUserListView.as_view(), name='mis-films'),
]