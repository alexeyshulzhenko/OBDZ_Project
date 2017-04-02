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
    if request.method == "POST":
        form = ClientForm(request.POST)
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

def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', id=client.id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/new_client.html', {'form': form})

#--------------------Contracts Views------------------------------#

@login_required(login_url="login/")
def contracts(request):
	# get the blog clients that are published
	contracts = Contract.objects.all()
	# now return the rendered template
	return render(request, "contracts/contracts_list.html", {'contracts': contracts})


@login_required(login_url="login/")
def contract_new(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('new_contract', id=contract.id)
    else:
        form = ContractForm()
    return render(request, 'contracts/new_contract.html', {'form': form})


@login_required(login_url="login/")
def contract_detail(request, id):
    contract = get_object_or_404(Contract, id=id)
    return render(request, 'contracts/contract_detail.html', {'contract': contract})

def contract_edit(request, id):
    contract = get_object_or_404(Contract, id=id)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('contract_detail', id=contract.id)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/new_contract.html', {'form': form})


#--------------------Manager Views------------------------------#

@login_required(login_url="login/")
def managers(request):
	# get the blog clients that are published
	contracts = Contract.objects.all()
	# now return the rendered template
	return render(request, "contracts/contracts_list.html", {'contracts': contracts})


@login_required(login_url="login/")
def manager_new(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.save()
            return redirect('new_manager', id=manager.id)
    else:
        form = ManagerForm()
    return render(request, 'managers/new_manager.html', {'form': form})


@login_required(login_url="login/")
def manager_detail(request, id):
    manager = get_object_or_404(Contract, id=id)
    return render(request, 'managers/manager_detail.html', {'manager': manager})

def manager_edit(request, id):
    manager = get_object_or_404(Manager, id=id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.save()
            return redirect('manager_detail', id=manager.id)
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'manager/new_manager.html', {'form': form})

#--------------------Brief Views------------------------------#

@login_required(login_url="login/")
def brief(request):
	# get the blog clients that are published
	briefs = Brief.objects.all()
	# now return the rendered template
	return render(request, "briefs/briefs_list.html", {'briefs': briefs})


@login_required(login_url="login/")
def brief_new(request):
    if request.method == "POST":
        form = BriefForm(request.POST)
        if form.is_valid():
            brief = form.save(commit=False)
            brief.save()
            return redirect('new_brief', id=brief.id)
    else:
        form = BriefForm()
    return render(request, 'brief/new_brief.html', {'form': form})


@login_required(login_url="login/")
def brief_detail(request, id):
    brief = get_object_or_404(Brief, id=id)
    return render(request, 'brief/brief_detail.html', {'brief': brief})

def brief_edit(request, id):
    brief = get_object_or_404(Manager, id=id)
    if request.method == "POST":
        form = BriefForm(request.POST, instance=brief)
        if form.is_valid():
            brief = form.save(commit=False)
            brief.save()
            return redirect('manager_detail', id=brief.id)
    else:
        form = ManagerForm(instance=brief)
    return render(request, 'brief/new_brief.html', {'form': form})