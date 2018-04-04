from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


def homepage(request):

    return render(request, 'Index/homepage.html')


def dashboard(request):

    return render(request, 'Index/dashboardContent.html')

