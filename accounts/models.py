from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TruckLoad(models.Model):
    loadName = models.CharField(max_length = 30, null = True)
    loadPrice = models.FloatField(null = True)
    loadWeight = models.FloatField(null = True)
    
    def __str__(self): 
        return str(self.loadName)
    

class Company(models.Model):

    objects = models.Manager()
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30, null = True)
    email = models.CharField(max_length = 30, null = True)
    phone = models.CharField(max_length = 30, null = True)
    profile_pic = models.ImageField(default = "profile.png", null=True, blank=True)
    #currentOrders = models.

    def __str__(self):
        return str(self.name)


class Driver(models.Model):
    driverName = models.CharField(max_length = 30, null = True)
    driverLocation = models.CharField(max_length = 30, null = True)
    STATUS = (
            ('Ready', 'Ready'),
            ('Driving', 'Driving'),
            ('Off', 'Off'),
         )
    driverStatus = models.CharField(max_length = 50, null = True, choices = STATUS)
    def __str__(self):
        return str(self.driverName)


class truckCustomer(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length = 30, null = True)
    email = models.CharField(max_length = 30, null = True)
    phone = models.CharField(max_length = 30, null = True)
    profile_pic = models.ImageField(default = "profile.png", null=True, blank=True)
    orderCompany = models.ForeignKey(Company, null = True, on_delete= models.SET_NULL)
    #currentOrders = models.

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    orderID = models.CharField(max_length = 10, null = True)
    origin = models.CharField(max_length = 50, null = True)
    destination = models.CharField(max_length = 50, null = True)
    dateLeft = models.DateField(auto_now=False, auto_now_add=False)
    dateArrived = models.DateField(auto_now=False, auto_now_add=False)
    STATUS = (
            ('Pending', 'Pending'),
            ('Shipping', 'Shipping'),
            ('Arrived', 'Arrived'),
         )
    status = models.CharField(max_length = 50, null = True, choices = STATUS)
    orderCustomer = models.ForeignKey(truckCustomer, null = True, on_delete= models.SET_NULL)
    load = models.ForeignKey(TruckLoad, null = True, on_delete= models.SET_NULL)
    trucker = models.ForeignKey(Driver, null = True, on_delete= models.SET_NULL)
    def __str__(self): 
        return str(self.orderID)


class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    products = models.ManyToManyField(Order)

    def __str__(self):
        return self.name


