from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from OnlineAgecy.models import *
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyUser, AuthorAdmin)



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



class ActSource(resources.ModelResource):
    class Meta:
        model = Act
@admin.register(Act)
class ActModelAdmin(ImportExportModelAdmin):
    resource_class = ActSource



class BillSource(resources.ModelResource):
    class Meta:
        model = Bill
@admin.register(Bill)
class BillModelAdmin(ImportExportModelAdmin):
    resource_class = BillSource