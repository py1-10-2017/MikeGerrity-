from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

def index(request): 
    request.session['items'] = [
        {'prod_id':1,'item_name':'Dojo Tshirt', 'price': 19.99},
        {'prod_id':2, 'item_name':'Dojo Sweater', 'price': 29.99}, 
        {'prod_id':3, 'item_name':'Dojo Cup', 'price': 4.99}, 
        {'prod_id':4, 'item_name':'Algorithim Book', 'price': 49.99}
    ]
    context = {
    "items": request.session['items']
    }

    return render(request, 'store/index.html', context)

def amadon(request):
    try: 
        request.session['item_count']
        request.session['grand_total']
    except: 
        if not "item_count" in request.session: 
            request.session['item_count'] = 0
        if not "grand_total" in request.session: 
            request.session['grand_total'] = 0
    for item in request.session['items']:
        if int(item['prod_id']) == int(request.POST['prod_id']):
            request.session['subtotal'] = int(request.POST['quantity']) * float(item['price'])
    request.session['item_count'] += int(request.POST['quantity'])
    request.session['grand_total'] += float(request.session['subtotal'])

    return redirect('/checkout')

def checkout(request):
    context = {
        'item_count' : request.session['item_count'], 
        'subtotal' : request.session['subtotal'], 
        'grand_total' : request.session['grand_total']
    }

    return render(request, "store/checkout.html", context)

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')