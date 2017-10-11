# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

def index(request): 
    try: 
        request.session['attempt'] += 1
    except: 
        if not 'count' in request.session:
            request.session['attempt'] = 0
    context = {
        "word": get_random_string(length=14)
    }

    return render(request, 'word/index.html', context, request.session['attempt'])

def generate(request): 
    return redirect('/')

def reset(request): 
    del request.session['attempt']
    return redirect('/')


