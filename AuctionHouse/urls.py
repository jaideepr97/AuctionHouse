"""AuctionHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Index.urls')),
    url(r'^Register/', include('Register.urls')),
    url(r'^Login/', include('Login.urls')),
    url(r'^Browse/', include('Browse.urls')),
    url(r'^UploadItems/', include('UploadItems.urls')),
    url(r'^ShowBids/', include('Bids.urls')),
    #url(r'^Profile/', include('Profile.urls')),
]
