from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'display/index.html', context)
