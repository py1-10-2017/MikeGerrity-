from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Users page"
    return HttpResponse(response)

def new(request): 
    response = "placeholder to register"
    return HttpResponse(response)

def show(request): 
    return HttpResponse("placeholder to display list of users")

def login(request): 
    return HttpResponse("placeholder to login")

