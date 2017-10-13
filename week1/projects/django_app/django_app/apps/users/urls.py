from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    #home page
    url(r'^register$', views.new),  # calls create function
    url(r'^login$', views.login),  # displays blogs
    url(r'^users/new$', views.new), #calls edit
    url(r'^users$', views.show), #calls delete
]