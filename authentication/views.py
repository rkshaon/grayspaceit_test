from django.http import Http404
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm

# LOGIN VIEW ENDPOINT

def login(request):
    return render(request, 'login.html')


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
