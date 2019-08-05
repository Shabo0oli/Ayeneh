# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # The home page
    url(r'addquiz/$' , views.addquiz , name='addquiz'),
    url(r'addkey/$', views.addkey, name='addkey'),

]


