#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),


    url(r'^clients/$', views.clients, name='clients'),
    url(r'^clients/(?P<id>\d+)/$', views.client_detail, name='client_detail'),
    url(r'^clients/new/$', views.client_new, name='client_new'),

    url(r'^contracts/new/$', views.contract_new, name='contract_new'),
]
