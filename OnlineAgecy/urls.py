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
    url(r'^clients/sevices/$', views.clients_services_count, name='clients_services_count'),
    url(r'^clients/bills/(?P<id>\d+)/$', views.all_clients_bills, name='all_clients_bills'),
    url(r'^clients/bills/$', views.fresh_clients, name='fresh_clients'),
    url(r'^clients/del/(?P<id>\d+)/$', views.delete_client, name='delete_client'),

    url(r'^contracts/$', views.contracts, name='contracts'),
    url(r'^contracts/(?P<id>\d+)/$', views.contract_detail, name='contract_detail'),
    url(r'^contracts/new/$', views.contract_new, name='contract_new'),
    url(r'^contracts/(?P<id>\d+)/edit/$', views.contract_edit, name='contract_edit'),
    url(r'^contracts/list/(?P<id>\d+)/$', views.all_clients_contracts, name='all_clients_contracts'),
    url(r'^contracts/list/$', views.contracts_services, name='contracts_services'),
    url(r'^contracts/del/(?P<id>\d+)/$', views.delete_contract, name='delete_contract'),

    url(r'^manager/$', views.managers, name='managers'),
    url(r'^manager/(?P<id>\d+)/$', views.manager_detail, name='manager_detail'),
    url(r'^manager/new/$', views.manager_new, name='manager_new'),
    url(r'^manager/(?P<id>\d+)/edit/$', views.manager_edit, name='manager_edit'),
    url(r'^manager/clients/$', views.managers_clients_count, name='managers_clients_count'),
    url(r'^managers/del/(?P<id>\d+)/$', views.delete_manager, name='delete_manager'),

    url(r'^briefs/$', views.brief, name='briefs'),
    url(r'^briefs/(?P<id>\d+)/$', views.brief_detail, name='brief_detail'),
    url(r'^briefs/new/$', views.brief_new, name='brief_new'),
    url(r'^briefs/(?P<id>\d+)/edit/$', views.brief_edit, name='brief_edit'),
    url(r'^briefs/del/(?P<id>\d+)/$', views.delete_brief, name='delete_brief'),
    url(r'^briefs/list/(?P<id>\d+)/$', views.all_clients_briefs, name='all_clients_briefs'),

    url(r'^services/$', views.services, name='services'),
    url(r'^services/(?P<id>\d+)/$', views.service_detail, name='service_detail'),
    url(r'^services/new/$', views.services_new, name='services_new'),
    url(r'^services/(?P<id>\d+)/edit/$', views.service_edit, name='service_edit'),
    url(r'^services/table/(?P<id>\d+)/$', views.service_all_clients, name='service_all_clients'),
    url(r'^services/del/(?P<id>\d+)/$', views.delete_service, name='delete_service'),

    url(r'^contractors/$', views.contractors, name='contractors'),
    url(r'^contractors/(?P<id>\d+)/$', views.contractor_detail, name='contractor_detail'),
    url(r'^contractors/new/$', views.contractors_new, name='contractors_new'),
    url(r'^contractors/(?P<id>\d+)/edit/$', views.contractor_edit, name='contractor_edit'),
    url(r'^contractors/newest/$', views.newest_contractors, name='newest_contractors'),
    url(r'^contractors/del/(?P<id>\d+)/$', views.delete_contractor, name='delete_contractor'),

    url(r'^acts/$', views.acts, name='acts'),
    url(r'^acts/(?P<id>\d+)/$', views.act_detail, name='act_detail'),
    url(r'^acts/new/$', views.act_new, name='act_new'),
    url(r'^acts/(?P<id>\d+)/edit/$', views.act_edit, name='act_edit'),
    url(r'^acts/del/(?P<id>\d+)/$', views.delete_act, name='delete_act'),

    url(r'^bills/$', views.bills, name='bills'),
    url(r'^bills/(?P<id>\d+)/$', views.bills_detail, name='bills_detail'),
    url(r'^bills/new/$', views.bills_new, name='bills_new'),
    url(r'^bills/(?P<id>\d+)/edit/$', views.bills_edit, name='bills_edit'),
    url(r'^bill/del/(?P<id>\d+)/$', views.delete_bill, name='delete_bill'),
]
