from django.conf.urls import url
from . import views

app_name = 'Index'
urlpatterns = [

    url(r'^$', views.homepage, name='homepage'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),

]