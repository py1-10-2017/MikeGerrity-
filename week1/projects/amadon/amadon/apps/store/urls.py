from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon$', views.amadon),
    url(r'^checkout$', views.checkout),
    url(r'^clear$', views.clear),
]