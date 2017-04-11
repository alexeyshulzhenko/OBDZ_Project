from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import CheckboxSelectMultiple, SelectDateWidget

from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('Name', 'Contractor_id', 'Price_per_item', 'Count_item')




class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Name', 'Registration_adress', 'Office_adress', 'Phone', 'Personal_Discount', 'Software', 'Mail', 'Payment_info')


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('Date', 'Start_date', 'End_date', 'Manager_id', 'Brief_id', 'Client_id', 'Services')
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields["Services"].widget = CheckboxSelectMultiple()
        self.fields["Services"].queryset = Service.objects.all()
        self.fields["Date"].widget = SelectDateWidget()
        self.fields["Start_date"].widget = SelectDateWidget()
        self.fields["End_date"].widget = SelectDateWidget()


class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('Name', 'Birthday_date')
    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)

        self.fields["Birthday_date"].widget = SelectDateWidget()


class BriefForm(forms.ModelForm):

    class Meta:
        model = Brief
        fields = ('Date', 'Start_date', 'End_date', 'Client_id')
    def __init__(self, *args, **kwargs):
        super(BriefForm, self).__init__(*args, **kwargs)

        self.fields["Date"].widget = SelectDateWidget()
        self.fields["Start_date"].widget = SelectDateWidget()
        self.fields["End_date"].widget = SelectDateWidget()


class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        fields = ('Name', 'Payment_info')

