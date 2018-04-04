from django.conf.urls import url
from . import views

app_name = 'UploadItems'
urlpatterns = [

    url(r'^$', views.ItemUploadFormView.as_view(), name='UploadItems'),
    url(r'^uploadItemSuccessful$', views.uploadItemSuccessful, name='uploadItemSuccessful'),

]
