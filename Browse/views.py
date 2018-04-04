from __future__ import unicode_literals
from UploadItems.models import Items, Bought, Expired
from Register.models import Credits
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.

User = get_user_model()



def displayItems(request):
    exp = Expired()
    bt = Bought()
    for i in Items.objects.all():
        if i.cur_highest_bid != 0 and i.expiration < timezone.now():
            item = Items.objects.get(pk=i.item_id)
            bt.seller = item.seller
            bt.item_id = item.item_id
            bt.item_name = item.item_name
            bt.item_desc = item.item_desc
            bt.buyer = item.cur_highest_bidder
            bt.sell_price = item.cur_highest_bid
            bt.save()
            exp.seller = item.seller
            exp.item_id = item.item_id
            exp.item_name = item.item_name
            exp.item_desc = item.item_desc
            exp.created_on = item.created_on
            exp.min_price = item.min_price
            exp.buy_now_price = item.buy_now_price
            exp.save()
            item.delete()

        elif i.expiration < timezone.now():
            item = Items.objects.get(pk=i.item_id)
            exp.seller = item.seller
            exp.item_id = item.item_id
            exp.item_name = item.item_name
            exp.item_desc = item.item_desc
            exp.created_on = item.created_on
            exp.min_price = item.min_price
            exp.buy_now_price = item.buy_now_price
            exp.save()
            item.delete()

    all_items_list = Items.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_items_list, 8)
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        all_items = paginator.page(1)
    except EmptyPage:
        all_items = paginator.page(paginator.num_pages)

    context = {
        'all_items': all_items,
    }
    return render(request, 'Browse/DisplayItems.html', context)


def bought(request):
    all_bought = Bought.objects.all()
    my_bought = all_bought.filter(buyer=User.objects.get(username=request.user.username))
    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(all_items_list, 8)
    # try:
    #     all_items = paginator.page(page)
    # except PageNotAnInteger:
    #     all_items = paginator.page(1)
    # except EmptyPage:
    #     all_items = paginator.page(paginator.num_pages)
    context = {
        'all_items': my_bought,
    }
    return render(request, 'Browse/bought.html', context)


def details(request, item_id):
    cur_item = Items.objects.get(pk=item_id)
    context = {
        'cur_item': cur_item
    }
    return render(request, 'Browse/details.html', context)


def bought_details(request, item_id):
    cur_item = Bought.objects.get(pk=item_id)
    if cur_item.buyer == request.user:
        context = {
            'cur_item': cur_item
        }
    else:
        context = { }
    return render(request, 'Browse/bought_details.html', context)


def update(request, item_id):
    all_items = Items.objects.all()
    cur_item = Items.objects.get(pk=item_id)
    bought = Bought()
    bid = request.POST['bid_value']
    cred = Credits.objects.get(name=request.user)
    cred_sell = Credits.objects.get(name=cur_item.seller)
    score = cred.credit
    if int(bid) < score:
        if int(bid)in range(int(cur_item.cur_highest_bid), int(cur_item.buy_now_price)):

            cur_item.cur_highest_bid = bid
            cur_item.cur_highest_bidder = User.objects.get(email=request.user.email)
            cur_item.save()
            context = {
                'all_items': all_items,
            }
            return render(request, 'Browse/displayItems.html', context)
            #return redirect('Browse:displayItems')

        elif int(bid) >= int(cur_item.buy_now_price):                       # BUY NOW

            bought.seller = cur_item.seller
            bought.item_id = cur_item.item_id
            bought.item_logo = cur_item.item_logo
            bought.item_name = cur_item.item_name
            bought.desc = cur_item.item_desc
            bought.buyer = request.user
            bought.sell_price = int(bid)
            bought.save()
            cred.credit = score - int(bid)
            cred_sell.credit += int(bid)
            cred_sell.save()
            cred.save()
            cur_item.delete()

            # cur_item.cur_highest_bid = bid
            # cur_item.cur_highest_bidder = User.objects.get(email=request.user.email)
            # cur_item.save()

            messages.error(request, 'Congrats, you won!.')
            all_items = Items.objects.all()
            context = {
                'all_items': all_items,
                'ret_val': 1
            }

            return render(request, 'Browse/displayItems.html', context)

        elif int(cur_item.cur_highest_bid) > int(bid) or int(cur_item.min_price) > int(bid):

            messages.error(request, 'Bid rejected.')
            cur_item = Items.objects.get(pk=item_id)
            context = {
                'cur_item': cur_item
            }
            #return redirect('Browse:detail')
            return render(request, 'Browse/details.html', context)
    else:
        messages.error(request, 'Insufficient funds')
        cur_item = Items.objects.get(pk=item_id)
        context = {
            'cur_item': cur_item
        }
        #return redirect('Browse:detail')
        return render(request, 'Browse/details.html', context)

