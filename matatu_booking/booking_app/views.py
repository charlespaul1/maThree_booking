from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home(request):
    # check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
            messages.success(request, 'Log in Error, Please try again....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


#logout user
def logout_user(request):
    pass
    