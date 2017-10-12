
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

def index(request):
    return render(request, 'words/index.html')

def add(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        if key == "big":
            new_word['big'] = "big"
        if key != "big":
            new_word[key] = value
        else:
            new_word['big'] = ""

    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['word']
    except KeyError:
        request.session['word'] = []

    temp_list = request.session['word']
    temp_list.append(new_word)
    request.session['word'] = temp_list
   
    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')