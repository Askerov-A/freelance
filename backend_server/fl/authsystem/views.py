from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def authentificate(request):
    return render(request, 'auth/auth.html')

def login(request):
    username = request.POST['name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect('/works')
    else:
        return render(request, 'auth/auth.html', {'message': 'WRONG'})

def register(request):
    username = request.POST['name']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user = authenticate(request, username=username, password=password)
    return HttpResponseRedirect('/works')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/works')
