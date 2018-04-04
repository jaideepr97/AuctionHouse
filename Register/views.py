from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import View
from .forms import UserForm
from Register.models import Credits


User = get_user_model()
userCredits = Credits()
# Create your views here.


def registerSuccessful(request):
    user_name = request.user.first_name
    context = {
        "user_name": user_name
    }
    #return render(request, 'Register/registerSuccessful.html', context)
    return redirect('Index:dashboard')


class UserFormView(View):
    form_class = UserForm
    template_name = 'Register/registerForm.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            username = form.cleaned_data['username']
            user.save()
            userCredits.name = user
            userCredits.save()
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Register:registerSuccessful')

        return render(request, self.template_name, {'form': form})