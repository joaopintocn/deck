from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm


def index_user(request):
    return render(request, 'authenticate/index.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('index')
        else:
            messages.warning(request, ('Error Login In - Please try agian.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})    


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out.'))
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered.'))
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)        


def edit_user(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have edited your profile.'))
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}   
    return render(request, 'authenticate/edit.html', context)            