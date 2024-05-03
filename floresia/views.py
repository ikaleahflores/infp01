from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages 
# Create your views here.


def home(request):
    #do something
    return render(request, 'home.html')    

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #authenticate
            username = request.POST('username')
            password = request.POST('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

            return render('home.html')
    else:
        form = SignUpForm()
        return render(request,'register.html', {'form':form})


    return render(request, 'register.html', {'form':form})
    