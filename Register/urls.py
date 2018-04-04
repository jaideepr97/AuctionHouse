from django.conf.urls import url
from . import views

app_name = 'Register'
urlpatterns = [

    url(r'^$', views.UserFormView.as_view(), name='registerView'),
    url(r'^registerSuccessful$', views.registerSuccessful, name='registerSuccessful'),
]
