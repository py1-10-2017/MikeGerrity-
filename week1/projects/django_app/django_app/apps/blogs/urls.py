from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    #home page
    url(r'^new$', views.create),  # calls create function
    url(r'^(?P<number>\d+)$', views.show),  # displays blogs
    url(r'^(?P<number>\d+)/edit$', views.edit), #calls edit
    url(r'^(?P<number>\d+)/delete$', views.delete), #calls delete
]