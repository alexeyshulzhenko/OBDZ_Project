from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# Client block

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Registration_adress =models.CharField(max_length=200)
    Office_adress = models.CharField(max_length=200)
    Phone = models.CharField(max_length=14)
    Personal_Discount = models.IntegerField()
    Software = models.CharField(max_length=40)
    Mail = models.CharField(max_length=40)
    Payment_info = models.CharField(max_length=255)
    def __str__(self):
        return self.id


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Birth_date = models.DateField(max_length=100)
    Position = models.CharField(max_length=40)
    def __str__(self):
        return self.Category


class Brief(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField( max_length=100)
    Start_date = models.DateField(max_length=100)
    End_date = models.DateField(max_length=100)
    Client_id = models.ForeignKey(Client)
    def __str__(self):
        return self.Subcategory

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField(max_length=100)
    Start_date = models.DateField( max_length=100)
    End_date = models.DateField(max_length=100)
    Manager_id = models.ForeignKey(Staff)
    Brief_id = models.ForeignKey(Brief)
    Client_id = models.ForeignKey(Client)
    def __str__(self):
        return self.id

class Act(models.Model):
    id = models.AutoField(primary_key=True)
    Client_id = models.ForeignKey(Client)
    Date = models.DateField(max_length=100)
    Manager_id = models.ForeignKey(Staff)
    def __str__(self):
        return self.Product

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    Act_id = models.ForeignKey(Act)
    Date = models.DateField(max_length=100)
    Manager_id = models.ForeignKey(Staff)
    def __str__(self):
        return self.Product

class Contractor(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Payment_info = models.CharField(max_length=255)
    def __str__(self):
        return self.ClipId

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Contractor_id = models.ForeignKey(Contractor)
    Price_per_item = models.IntegerField()
    Count_item = models.IntegerField()
    def __str__(self):
        return self.Channel
