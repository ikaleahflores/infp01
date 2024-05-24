from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages 
from .models import *
# Create your views here.


def home(request):
    records = Record.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})
 

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
    