from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from OnlineAgecy.models import *

class ClientsSource(resources.ModelResource):
    class Meta:
        model = Client

@admin.register(Client)
class ClientModelAdmin(ImportExportModelAdmin):
    resource_class = ClientsSource

class ContractsSource(resources.ModelResource):
    class Meta:
        model = Client

@admin.register(Contract)
class ContractModelAdmin(ImportExportModelAdmin):
    resource_class = ContractsSource