from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from Write.forms import UserForm

def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')

        else:

            return render(request,'common/bad_login.html')
    else:
        return render(request, 'common/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

