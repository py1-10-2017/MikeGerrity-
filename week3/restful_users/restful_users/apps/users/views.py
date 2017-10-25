from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

def index(request): 
    context = {
        'users':User.objects.all()
    }
    return render(request, 'users/index.html', context)

def create(request):
    return render(request, 'users/add.html')

def add(request): 
    User.objects.create(
        first_name = request.POST['f_name'], 
        last_name = request.POST['l_name'],
        email = request.POST['email']
    )
    return redirect('/users')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'users/edit.html', context)

def update(request, user_id):
    update_user = User.objects.get(id = user_id)
    update_user.first_name = request.POST['f_name']
    update_user.last_name = request.POST['l_name']
    update_user.email = request.POST['email']
    update_user.save()
    return redirect('/users')

def show(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'users/user.html', context)

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')