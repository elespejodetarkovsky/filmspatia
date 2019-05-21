'''
Created on 21 may. 2019

@author: sebas
'''
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]