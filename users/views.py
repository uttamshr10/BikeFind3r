from django.shortcuts import render, redirect
from django.contrib.auth import logout
from users import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def log_out(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method != 'POST':
        form = forms.UserForm()
    else:
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login/')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)