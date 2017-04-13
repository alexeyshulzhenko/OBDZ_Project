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
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })



class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('Name', 'Registration_adress', 'Office_adress', 'Phone', 'Personal_Discount', 'Software', 'Mail', 'Payment_info')
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields["Mail"] = forms.EmailField()
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('Date', 'Start_date', 'End_date', 'Manager_id', 'Brief_id', 'Client_id', 'Services')

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields["Services"].widget = CheckboxSelectMultiple()
        self.fields["Services"].queryset = Service.objects.all()

# TODO Autopopulated fields
#http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/
# self.fields["Brief_id"].queryset = Service.objects.raw('SELECT * FROM OnlineAgecy_brief WHERE Client_id_id =' + context['Client_id'])


        self.fields["Date"].widget = forms.DateInput(attrs={'id': 'datetimepicker12'})

        self.fields["Start_date"].widget = forms.DateInput(attrs={'id': 'datetimepicker2'})

        self.fields["End_date"].widget = forms.DateInput(attrs={'id': 'datetimepicker3'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class ManagerForm(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('Name', 'Birthday_date')
    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)

        self.fields["Birthday_date"].widget = forms.DateInput(attrs={'id': 'datetimepicker12'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class BriefForm(forms.ModelForm):

    class Meta:
        model = Brief
        fields = ('Date', 'Start_date', 'End_date', 'Client_id')
    def __init__(self, *args, **kwargs):
        super(BriefForm, self).__init__(*args, **kwargs)

        self.fields["Date"].widget = forms.DateInput(attrs={'id': 'datetimepicker12'})

        self.fields["Start_date"].widget = forms.DateInput(attrs={'id': 'datetimepicker2'})

        self.fields["End_date"].widget = forms.DateInput(attrs={'id': 'datetimepicker3'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        fields = ('Name', 'Payment_info')
    def __init__(self, *args, **kwargs):
        super(ContractorForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class ActForm(forms.ModelForm):

    class Meta:
        model = Act
        fields = ('Contract_id', 'Date', 'Manager_id')
    def __init__(self, *args, **kwargs):
        super(ActForm, self).__init__(*args, **kwargs)

        self.fields["Date"].widget = forms.DateInput(attrs={'id': 'datetimepicker12'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = ('Act_id', 'Date', 'Manager_id')
    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)

        self.fields["Date"].widget = forms.DateInput(attrs={'id': 'datetimepicker3'})
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'class': "form-control myfont"
                })
