# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # The home page
    url(r'addquiz/$' , views.addquiz , name='addquiz'),
    url(r'addkey/$', views.addkey, name='addkey'),
    url(r'signup/$', views.apiregister, name='apiregister'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.apilogin, name='apilogin'),

    url(r'', views.intro, name='intro'),

]


