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
    url(r'^clients/(?P<id>\d+)/edit/$', views.client_edit, name='client_edit'),

    url(r'^contracts/$', views.contracts, name='contracts'),
    url(r'^contracts/(?P<id>\d+)/$', views.contract_detail, name='contract_detail'),
    url(r'^contracts/new/$', views.contract_new, name='contract_new'),
    url(r'^contracts/(?P<id>\d+)/edit/$', views.contract_edit, name='contract_edit'),

    url(r'^manager/$', views.managers, name='managers'),
    url(r'^manager/(?P<id>\d+)/$', views.manager_detail, name='manager_detail'),
    url(r'^manager/new/$', views.manager_new, name='manager_new'),
    url(r'^manager/(?P<id>\d+)/edit/$', views.manager_edit, name='manager_edit'),

    url(r'^briefs/$', views.briefs, name='briefs'),
    url(r'^briefs/(?P<id>\d+)/$', views.brief_detail, name='brief_detail'),
    url(r'^briefs/new/$', views.brief_new, name='brief_new'),
    url(r'^briefs/(?P<id>\d+)/edit/$', views.brief_edit, name='brief_edit'),


]
