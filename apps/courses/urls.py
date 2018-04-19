from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^courses/create$', views.create),
    url(r'^courses/(?P<number>\d)/remove$', views.remove),
    url(r'^process$', views.process),
    
    url(r'^courses/(?P<number>\d)/destroy$', views.destroy),
    ]
