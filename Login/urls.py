from django.conf.urls import url
from . import views

app_name = 'Login'
urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='loginView'),
    url(r'^loginSuccessful$', views.loginSuccessful, name='loginSuccessful'),
    url(r'^logout$', views.logoutView, name="logoutView"),
]
