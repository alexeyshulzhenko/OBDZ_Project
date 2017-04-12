#!python
#OnlineAgesy/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url="login/")
def home(request):
	return render(request, "static_pages/home.html")



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
            return redirect('client_detail', id=id)
    else:
        form = ClientForm()
    return render(request, 'layouts/form.html', {'form': form})


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
            return redirect('client_detail', id=id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'layouts/form.html', {'form': form})

@login_required(login_url="login/")
def all_clients_contracts(request, id):
	# get the blog clients that are published
	items = Contract.objects.raw('SELECT * FROM OnlineAgecy_contract WHERE Client_id_id =' + id)
	# now return the rendered template
	return render(request, "clients/allUserContracts.html", {'items': items}, {'client': id})

@login_required(login_url="login/")
def clients_documents(request, id):
    item = Client.objects.raw('SELECT OnlineAgecy_client.id, OnlineAgecy_client.Name AS Name, OnlineAgecy_act.Client_id_id AS id  '
                                'from OnlineAgecy_client join OnlineAgecy_act using (id) WHERE OnlineAgecy_client.id =' + id)
    return render(request, 'clients/clients_documents.html', {'item': item})




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
            return redirect('contract_detail', id=id)
    else:
        form = ContractForm()
    return render(request, 'layouts/form.html', {'form': form})


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
            return redirect('contract_detail', id=id)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'layouts/form.html', {'form': form})


#--------------------Manager Views------------------------------#
#################################################################



@login_required(login_url="login/")
def managers(request):
	# get the blog clients that are published
	managers = Manager.objects.all()
	# now return the rendered template
	return render(request, "manager/manager_list.html", {'managers': managers})


@login_required(login_url="login/")
def manager_new(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager = form.save(commit=False)
            manager.save()
            return redirect('manager_detail', id=id)
    else:
        form = ManagerForm()
    return render(request, 'layouts/form.html', {'form': form})


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
            return redirect('manager_detail', id=id)
    else:
        form = ManagerForm(instance=manager)
    return render(request, 'layouts/form.html', {'form': form})



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
            return redirect('brief_detail', id=id)
    else:
        form = BriefForm()
    return render(request, 'layouts/form.html', {'form': form})


@login_required(login_url="login/")
def brief_detail(request, id):
    brief = get_object_or_404(Brief, id=id)
    return render(request, 'briefs/brief_detail.html', {'brief': brief})

@login_required(login_url="login/")
def brief_edit(request, id):
    brief = get_object_or_404(Brief, id=id)
    if request.method == "POST":
        form = BriefForm(request.POST, instance=brief)
        if form.is_valid():
            brief = form.save(commit=False)
            brief.save()
            return redirect('brief_detail', id=id)
    else:
        form = ManagerForm(instance=brief)
    return render(request, 'layouts/form.html', {'form': form})




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
            return redirect('service_detail', id=id)
    else:
        form = ServiceForm()
    return render(request, 'layouts/form.html', {'form': form})


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
            return redirect('service_detail', id=id)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'layouts/form.html', {'form': form})

@login_required(login_url="login/")
def service_all_clients(request, id):
	# get the blog clients that are published
	services = Contract.objects.raw('SELECT OnlineAgecy_contract.id, OnlineAgecy_contract_Services.contract_id AS id, Online_Agecy_service.id, Online_Agecy_service.Name, OnlineAgecy_contract_Services.service_id AS id'
                                    'from (OnlineAgecy_contract join OnlineAgecy_contract_Services using (id)) join OnlineAgecy_contract_Services using (id)')

    # 'SELECT OnlineAgecy_client.Name OnlineAgecy_service.Name AS ServiceName FROM OnlineAgecy_contract JOIN OnlineAgecy_client USING (id)')
    #SELECT table.id, other_table.name AS name from table join other_table using (id)
	return render(request, "services/allClientServices.html", {'services': services})





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
            return redirect('contractor_detail', id=id)
    else:
        form = ContractorForm()
    return render(request, 'layouts/form.html', {'form': form})


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
            return redirect('contractor_detail', id=id)
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'layouts/form.html', {'form': form})



#--------------------Act Views------------------------------#
#####################################################################


@login_required(login_url="login/")
def acts(request):
    acts = Act.objects.all()

    return render(request, "acts/act_list.html", {'acts': acts})


@login_required(login_url="login/")
def act_new(request):
    if request.method == "POST":
        form = ActForm(request.POST)
        if form.is_valid():
            acts = form.save(commit=False)
            acts.save()
            return redirect('act_detail', id=id)
    else:
        form = ActForm()
    return render(request, 'layouts/form.html', {'form': form})


@login_required(login_url="login/")
def act_detail(request, id):
    act = get_object_or_404(Act, id=id)
    return render(request, 'acts/act_detail.html', {'act': act})

@login_required(login_url="login/")
def act_edit(request, id):
    act = get_object_or_404(Act, id=id)
    if request.method == "POST":
        form = ActForm(request.POST, instance=act)
        if form.is_valid():
            act = form.save(commit=False)
            act.save()
            return redirect('act_detail', id=id)
    else:
        form = ActForm(instance=act)
    return render(request, 'layouts/form.html', {'form': form})

#--------------------Bill Views------------------------------#
#####################################################################


@login_required(login_url="login/")
def bills(request):
    bills = Bill.objects.all()

    return render(request, "bills/bills_list.html", {'bills': bills})


@login_required(login_url="login/")
def bills_detail(request, id):
    bill = get_object_or_404(Bill, id=id)
    return render(request, 'bills/bill_detail.html', {'bill': bill})


