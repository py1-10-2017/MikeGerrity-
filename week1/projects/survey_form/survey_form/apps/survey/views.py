# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.


def index(request): 
    return render(request, 'survey/index.html')

def process(request): 
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    try: 
        request.session['count'] += 1
    except: 
        if not 'count' in request.session:
            request.session['count'] = 0
    
    context = {
        'name': request.session['name'], 
        'location': request.session['location'], 
        'language': request.session['language'], 
        'comment': request.session['comment']
    }

    return render(request, 'survey/result.html', context, request.session['count'])

def back(request): 
    return redirect('/')
    


