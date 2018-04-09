from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def profilepage(request, username):
    cur_user = User.objects.get(username=username)
    #user_name = request.user.first_name
    #print(User.username)
    context = {
        "first_name": cur_user.first_name,
        "username": cur_user.username,
        "email": cur_user.email,
    }
    return render(request, 'Profile/profile.html', context)


def rating(request):
    print("HIII")
    print(request.POST)
    if request.method == 'POST':
        if ('star1') in request.POST:
            rating = request.POST.get('star5')
            print(rating)
            print("star1")
        elif ('star2') in request.POST:
            rating = request.POST.get('star5')
            print(rating)
            print("star2")
        elif ('star3') in request.POST:
            rating = request.POST.get('star5')
            print(rating)
            print("star3")
        elif ('star4') in request.POST:
            rating = request.POST.get('star5')
            print(rating)
            print("star4")
        elif ('star5') in request.POST:
            rating = request.POST.get('star5')
            print(rating)
            print("star5")
    context = {
        "rating": rating
    }

    return render(request, 'Profile/profilepage.html', context)