from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')


def login_fun(request):
    return render(request,'login.html')


def register_fun(request):
    return render(request,'register.html')


def read_register(request):
    email = request.POST['tbemail']
    password = request.POST['tbpwd']
    username = request.POST['tbname']
    user = User.objects.create_superuser(username=username, email=email, password=password)
    user.save()
    return render(request, 'login.html', {'msg':
                                              f'User Created Successfully'})


def read_login(request):
    username = request.POST["tbname"]
    password = request.POST["tbpwd"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('displaystudent')
    else:
        return render(request, 'login.html')


def logout_fun(request):
    logout(request)
    return redirect('login')