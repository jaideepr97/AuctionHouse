# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserLoginForm


# Create your views here.


def loginSuccessful(request):
    user_name = request.user.first_name
    context = {

        "user_name": user_name
    }
    #return render(request, 'Login/homepage.html', context)
    return redirect('Index:dashboard')


class UserFormView(View):
    form_class = UserLoginForm
    template_name = 'Login/loginForm.html'
    title = "Login"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Index:dashboard')

            return render(request, "Login/loginForm.html", {"form": form, "title": title})
        return render(request, "Login/loginForm.html", {"form": form})


def logoutView(request):
    logout(request)
    return redirect('Index:homepage')


