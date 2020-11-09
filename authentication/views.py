from django.http import Http404
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# LOGIN VIEW ENDPOINT

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts')
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration for ' + user + ' is successfully done.')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
