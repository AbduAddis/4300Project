from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Company)
admin.site.register(TruckLoad)
admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(truckCustomer)
admin.site.register(Category)