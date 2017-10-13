from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    #home page
    url(r'^surveys$', views.index),  # calls create function
    url(r'^surveys/new$', views.new),  # calls create function
]