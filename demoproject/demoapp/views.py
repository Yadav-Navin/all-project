from django.shortcuts import render,redirect
from django.contrib.auth import login as login_user,logout as logout_user,authenticate
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login_user(request,user)
            return redirect('/')
        else:
            return render(request,'login',{"message":"Invalid creadentials"})
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{"message": 'User is alredy exists'})
        elif User.objects.filter(email=email).exists():
            return render(request,'register.html',{"message": 'Email is alredy exists'})
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
    else:
        return render(request,'register.html')

def logout(request):
    logout_user(request)
    return redirect('/')