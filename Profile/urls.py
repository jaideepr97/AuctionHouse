from django.conf.urls import url
from . import views

app_name = 'Profile'
urlpatterns = [
    url(r'^(?P<username>[a-zA-Z]+)/$', views.profilepage, name='profilepage'),
    url(r'^rating/', views.rating, name='rating'),
    #url(r'^$', views.profilepage, name='profilepage'),
]
