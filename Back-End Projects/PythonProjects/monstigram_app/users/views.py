from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from users.models import Profile


# Create your views here.
def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid Password or Username'})

    return render(request, 'users/login.html')


@login_required()
def logout_view(request):

    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']

        passwd_confirmation = request.POST['passwd_confirmation']
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'The Password Confirmation Does Not Match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'The Username Already Exists'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


def update_profile(request):
    return render(request, 'users/update_profile.html')
