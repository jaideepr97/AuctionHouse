
 #   url(r'^$', views.display, name='bidItems'),

from django.conf.urls import url
from . import views

app_name = 'Bids'
urlpatterns = [

    url(r'^showListings$', views.showListings, name='showListings'),
    url(r'^showBids$', views.showBids, name='showBids'),
    url(r'^showBought$', views.showBought, name='showBought'),
]
