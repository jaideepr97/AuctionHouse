from django.shortcuts import render, redirect

# Create your views here.


def profilepage(request, username):
    #user_name = request.user.first_name
    #print(User.username)
    context = {
    #    "first_name": first_name,
        "username": username,
    #    "email": email,
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