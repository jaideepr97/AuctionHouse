
from __future__ import unicode_literals
from UploadItems.models import Items, Bought
from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
User = get_user_model()


def showListings(request):
    all_items = Items.objects.all()
    items = all_items.filter(seller=User.objects.get(username=request.user.username))

    context = {
        'items': items
    }

    return render(request, 'Bids/bidItems.html', context)


def showBids(request):
    all_items = Items.objects.all()
    items = all_items.filter(cur_highest_bidder=User.objects.get(username=request.user.username))

    context = {
        'items': items
    }

    return render(request, 'Bids/bidItems.html', context)


def showBought(request):
    all_items = Bought.objects.all()
    items = all_items.filter(buyer=User.objects.get(username=request.user.username))

    context = {
        'items': items
    }

    return render(request, 'Bids/bidItems.html', context)