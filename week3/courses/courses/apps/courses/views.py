# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import error
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

def index(request): 
    context = {
           'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request): 
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
        name = request.POST['name'], 
        description = request.POST['description']
    )
    return redirect('/courses')

def remove(request, course_id): 
    context = {
        'courses': Course.objects.get(id=course_id)
    }    
    return render(request, 'courses/destroy.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')