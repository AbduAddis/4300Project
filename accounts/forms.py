from django.forms import ModelForm
from .models import *
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = truckCustomer
        fields = '__all__'

class registerUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class companyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'