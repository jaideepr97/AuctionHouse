# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ItemUploadForm
from .models import Items
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.timezone import localtime, now

# Create your views here.
User = get_user_model()
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def uploadItemSuccessful(request):
    return render(request, 'UploadItems/UploadItemSuccessful.html')


class ItemUploadFormView(View):
    form_class = ItemUploadForm
    template_name = 'UploadItems/UploadItemForm.html'

    def get(self, request):
        currentUser = request.user
        #print(currentUser)
        # user = authenticate(username=username, password=password)
        if request.user.is_anonymous:
            return redirect('Login:loginView')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            item = Items()
            item.item_name = form.cleaned_data['item_name']
            item.item_desc = form.cleaned_data['item_desc']
            item.min_price = form.cleaned_data['min_price']
            item.buy_now_price = form.cleaned_data['buy_now_price']
            item.expiration = form.cleaned_data['expiration']
            item.seller = User.objects.get(email=request.user.email)
            item.created_on = localtime(now())

            item.item_logo = request.FILES['item_logo']
            file_type = item.item_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {

                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, self.template_name, context)

            item.save()
            context = {

                'user_name': request.user.first_name
            }
            # return render(request, 'UploadItems/UploadItemSuccessful.html', context)
            return redirect('Browse:displayItems')
        return render(request, self.template_name, {'form': form})


