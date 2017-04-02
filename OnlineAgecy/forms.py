from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Name', 'Registration_adress', 'Office_adress', 'Phone', 'Personal_Discount', 'Software', 'Mail', 'Payment_info')


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('Date', 'Start_date', 'End_date', 'Manager_id', 'Brief_id', 'Client_id', 'Services')

class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('Name', 'Birthday_date')

class BriefForm(forms.ModelForm):

    class Meta:
        model = Brief
        fields = ('Date', 'Start_date', 'End_date', 'Client_id')