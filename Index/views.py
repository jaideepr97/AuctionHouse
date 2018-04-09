from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import get_user_model
from Register.models import Credits

# Create your views here.
User = get_user_model()
credit = Credits()

def homepage(request):

    return render(request, 'Index/homepage.html')


def dashboard(request):
    cur_user = request.user
    all_credits = Credits.objects.all()
    my_creds = all_credits.filter(name=cur_user)
    # print(my_creds)
    creds = my_creds.values_list('credit', flat=True)
    username = cur_user.username
    context = {
        "username": username,
        "credits": creds,
    }
    return render(request, 'Index/dashboardContent.html', context)

