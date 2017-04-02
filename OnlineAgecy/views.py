#!python
#OnlineAgesy/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url="login/")
def home(request):
	return render(request, "static_pages/home.html")



@login_required(login_url="login/")
def clients_contracts(request):
	# get the clients that are published
	contracts = Client.objects.raw('SELECT id, date,  FROM Contract WHERE id_client = "Client_id"')
	# now return the rendered template
	return render(request, "contracts/contracts_list.html", {'contracts': contracts})


#--------------------Clients Views------------------------------#

@login_required(login_url="login/")
def clients(request):
	# get the blog clients that are published
	clients = Client.objects.all()
	# now return the rendered template
	return render(request, "clients/clients_list.html", {'clients': clients})


@login_required(login_url="login/")
def client_new(request):
    if request.method == "client":
        form = ClientForm(request.client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('new_client', id=client.id)
    else:
        form = ClientForm()
    return render(request, 'clients/new_client.html', {'form': form})


@login_required(login_url="login/")
def client_detail(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'clients/client_detail.html', {'client': client})


#--------------------Contracts Views------------------------------#

@login_required(login_url="login/")
def contract_new(request):
    form = ContractForm()
    return render(request, 'contracts/new_contract.html', {'form': form})