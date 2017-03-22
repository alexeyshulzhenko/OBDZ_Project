#!python
#OnlineAgesy/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OnlineAgecy.models import Client

@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

@login_required(login_url="login/")
def clients(request):
	# get the blog posts that are published
	clients = Client.objects.all()
	# now return the rendered template
	return render(request,"clients_list.html", {'clients': clients})



@login_required(login_url="login/")
def clients_contracts(request):
	# get the blog posts that are published
	contracts = Client.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
	# now return the rendered template
	return render(request,"contracts_list.html", {'contracts': contracts})

