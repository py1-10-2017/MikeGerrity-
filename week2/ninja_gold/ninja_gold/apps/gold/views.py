from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random

from models import *

def index(request):
    try: 
        context = {
        'activities' : request.session['activity'],
        'myGold' : request.session['myGold']
        }    
    except KeyError:
        context = {
        'activities' : '',
        'myGold' : 0
        }  
   
    return render(request, 'gold/index.html', context)


def income(request):
    timeofday = strftime("%Y-%m-%d %H:%M", gmtime())
    try: 
        request.session['activity']
    except KeyError:
        request.session['activity']=[]    
    
    if request.POST['building'] == 'farm': 
        result = random.randint(10,21)

    elif request.POST['building'] == 'cave': 
        result = random.randint(5,11)

    elif request.POST['building'] == 'house': 
        result = random.randint(2,6)

    elif request.POST['building'] == 'casino': 
        result = random.randint(-50,51)

    if result >= 0:
        try:
            request.session['myGold'] = int(request.session['myGold']) + result
        except KeyError:
            request.session['myGold'] = 0 + result    

        temp = request.session['activity']
        temp.append("You earned " + str(result) + " Gold at the " + request.POST['building'] + " " + timeofday)
        request.session['activity'] = temp

    elif result < 0:
        try:
            request.session['myGold'] = int(request.session['myGold']) + result
        except KeyError:
            request.session['myGold'] = 0 + result  

        temp = request.session['activity']
        temp.append("You lost " + str(result) + " Gold at the " + request.POST['building'] + " " + timeofday)
        request.session['activity'] = temp
    
    return redirect('/')

def reset(request):
    for key in request.session.keys(): 
        del request.session[key]
    return redirect('/')
