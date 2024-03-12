from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # authenticate the user
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'login was successfull')
            return redirect('home')
        else:
            messages.success(request, 'Log in Error, Please try again....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


#logout user
def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out....')
    return redirect('home')
    
# registering new user
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate the user and then log them in
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, email=email, password=password)
            # after authentication log them in
            login(request, user)
            messages.success(request, "You have succesfully registered welcome...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    