#!python
#OnlineAgesy/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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


@login_required(login_url="login/")
def all_clients_contracts(request, clientId):
	# get the blog clients that are published
	contracts = Contract.objects.raw('SELECT * FROM OnlineAgecy_contract WHERE Client_id_id =' + clientId)
	# now return the rendered template
	return render(request, "contracts/allUserContracts.html", {'contracts': contracts})



#--------------------Clients Views------------------------------#
#################################################################


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
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'clients/new_client.html', {'form': form})


@login_required(login_url="login/")
def client_detail(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'clients/client_detail.html', {'client': client})

@login_required(login_url="login/")
def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/new_client.html', {'form': form})



#--------------------Contracts Views------------------------------#
###################################################################


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
            return redirect('contracts')
    else:
        form = ContractForm()
    return render(request, 'contracts/new_contract.html', {'form': form})


@login_required(login_url="login/")
def contract_detail(request, id):
    contract = get_object_or_404(Contract, id=id)
    return render(request, 'contracts/contract_detail.html', {'contract': contract})

@login_required(login_url="login/")
def contract_edit(request, id):
    contract = get_object_or_404(Contract, id=id)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect('contracts')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/new_contract.html', {'form': form})


#--------------------Manager Views------------------------------#

@login_required(login_url="login/")
def managers(request):
	# get the blog clients that are published
	manager = Manager.objects.all()
	# now return the rendered template
	return render(request, "manager/manager_list.html", {'contracts': contracts})


@login_required(login_url="login/")
def manager_new(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.save()
            return redirect('manager')
    else:
        form = ManagerForm()
    return render(request, 'manager/new_manager.html', {'form': form})


@login_required(login_url="login/")
def manager_detail(request, id):
    manager = get_object_or_404(Manager, id=id)
    return render(request, 'manager/manager_detail.html', {'manager': manager})

@login_required(login_url="login/")
def manager_edit(request, id):
    manager = get_object_or_404(Manager, id=id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.save()
            return redirect('manager')
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'manager/new_manager.html', {'form': form})



#--------------------Brief Views------------------------------#
###############################################################

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
            return redirect('briefs')
    else:
        form = BriefForm()
    return render(request, 'briefs/new_brief.html', {'form': form})


@login_required(login_url="login/")
def brief_detail(request, id):
    brief = get_object_or_404(Brief, id=id)
    return render(request, 'brief/brief_detail.html', {'brief': brief})

@login_required(login_url="login/")
def brief_edit(request, id):
    brief = get_object_or_404(Brief, id=id)
    if request.method == "POST":
        form = BriefForm(request.POST, instance=brief)
        if form.is_valid():
            brief = form.save(commit=False)
            brief.save()
            return redirect('brief_detail')
    else:
        form = ManagerForm(instance=brief)
    return render(request, 'brief/new_brief.html', {'form': form})




#--------------------Services Views------------------------------#
##################################################################

@login_required(login_url="login/")
def services(request):
    services = Service.objects.all()

    return render(request, "services/services_list.html", {'services': services})


@login_required(login_url="login/")
def services_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            services = form.save(commit=False)
            services.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'services/new_service.html', {'form': form})


@login_required(login_url="login/")
def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required(login_url="login/")
def service_edit(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/new_service.html', {'form': form})



#--------------------contractors Views------------------------------#
#####################################################################


@login_required(login_url="login/")
def contractors(request):
    contractors = Contractor.objects.all()

    return render(request, "contractors/contractors_list.html", {'contractors': contractors})


@login_required(login_url="login/")
def contractors_new(request):
    if request.method == "POST":
        form = ContractorForm(request.POST)
        if form.is_valid():
            contractors = form.save(commit=False)
            contractors.save()
            return redirect('contractors')
    else:
        form = ContractorForm()
    return render(request, 'contractors/new_contractor.html', {'form': form})


@login_required(login_url="login/")
def contractor_detail(request, id):
    contractor = get_object_or_404(Contractor, id=id)
    return render(request, 'contractors/contractor_detail.html', {'contractor': contractor})

@login_required(login_url="login/")
def contractor_edit(request, id):
    contractor = get_object_or_404(Contractor, id=id)
    if request.method == "POST":
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.save()
            return redirect('contractors')
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'contractors/new_contractor.html', {'form': form})


