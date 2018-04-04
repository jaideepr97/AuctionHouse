from django.conf.urls import url
from . import views

app_name = 'Browse'
urlpatterns = [

    url(r'^$', views.displayItems, name='displayItems'),

    url(r'^(?P<item_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<item_id>[0-9]+)/updated$', views.update, name='update'),
    url(r'^bought$', views.bought, name='bought'),
    url(r'^(?P<item_id>[0-9]+)/bought$', views.bought_details, name='bought_details'),
]
