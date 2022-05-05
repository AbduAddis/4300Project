from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import CustomerForm, OrderForm, registerUserForm, companyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request,'accounts/main.html')

def contact(request):
    return HttpResponse('Contact Page')

def aboutPage(request):
    company = Company.objects.filter(user = request.user).first()
    context={'company':company}
    return render(request,'accounts/aboutus.html',context)

def customer(request, pk):
    customer = truckCustomer.objects.get(name=pk)
    name = customer.name
    company = Company.objects.filter(user = request.user).first()
    orders = customer.order_set.all() 
    total_orders = orders.count()
    context = {'name':name, 'customer':customer,'orders':orders,'total_orders':total_orders,'company':company}
    return render(request,'accounts/customer.html',context)

def company(request,pk):
    comp = Company.objects.get(name=pk)
    compName = comp.name
    company = Company.objects.filter(user = request.user).first()
    customers = comp.truckcustomer_set.all()
    orders = Order.objects.filter(orderCustomer__in=truckCustomer.objects.filter(orderCompany=comp))
    total_orders = orders.count()
    delivered = orders.filter(status='Arrived').count()
    pending = orders.filter(status='Shipping').count()
    context = {'name':compName,'comp':comp,'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'delivered':delivered,'pending':pending, 'company':company}
    return render(request,'accounts/trucking.html',context)


def createOrder(request,pk):
    cust = truckCustomer.objects.get(name=pk)
    redirectURL = f"/customer/{cust.name}"
    company = Company.objects.filter(user = request.user).first()
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirectURL)
 
    context = {'form':form,'company':company}
    return render(request, 'accounts/order_form.html', context)

def createCompany(request):
    print("\n\nTHE RIGHT SHIT HAS IN")
    form = companyForm(initial={'user':request.user})
    if request.method == 'POST':
        print(str(form.errors))
        form = companyForm(request.POST)
        if form.is_valid():
            form.save()
            company = Company.objects.filter(user = request.user).first()
            redirectURL = f"/company/{company.name}"
            return redirect(redirectURL)
    context = {'form':form}
    return render(request,'accounts/company_form.html',context)

def createCustomer(request,pk):
    cust = Company.objects.get(name=pk)
    redirectURL = f"/company/{cust.name}"
    company = Company.objects.filter(user = request.user).first()

    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirectURL)
    context = {'form':form,'company':company}
    return render(request,'accounts/customer_form.html',context)

def updateCustomer(request,pk):
    company = Company.objects.filter(user = request.user).first()
    cust = truckCustomer.objects.get(name=pk)
    custComp = cust.orderCompany
    redirectURL=f"/customer/{cust.name}"
    form = CustomerForm(instance=cust)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect(redirectURL)

    context = {'form':form,'company':company}
    return render(request,'accounts/customer_form.html',context)


def updateOrder(request,pk):
    order = Order.objects.get(orderID=pk)
    ordCust = order.orderCustomer
    redirectURL = f"/customer/{ordCust.name}"
    company = Company.objects.filter(user = request.user).first()
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect(redirectURL)
    context={'form':form,'company':company}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request,pk):
    order=Order.objects.get(orderID=pk)
    ordCust = order.orderCustomer
    ordCustName = ordCust.name
    redirectURL = f"/customer/{ordCust.name}"
    company = Company.objects.filter(user = request.user).first()


    if request.method == "POST":
        order.delete()
        return redirect(redirectURL) 
    context={'name':ordCustName, 'item':order,'company':company}
    return render(request, 'accounts/delete.html',context)


def deleteCustomer(request,pk):
    cust = truckCustomer.objects.get(name=pk)
    company = Company.objects.filter(user = request.user).first()
    parentComp = cust.orderCompany
    parentName = parentComp.name
    name = cust.name
    redirectURL = f"/company/{parentName}"
    if request.method == "POST":
        cust.delete()
        return redirect(redirectURL)
    context = {'name':name,'parentName':parentName,
    'parentComp':parentComp,'cust':cust,'company':company}
    return render(request, 'accounts/delete_customer.html',context)


def registerPage(request):
    form = registerUserForm()
    if request.method == 'POST':
        print("\n\nPOSTDATA IS GODO")
        form = registerUserForm(request.POST)
        print("\n IS FORM VALID? " + str(form.is_valid())
        )
        print(str(form.errors))
        if form.is_valid():
            print("\n\nFORM IS VALID")
            form.save()
            messages.success(request,'Account was created successfully!')
            return redirect('/login')

    context={'form':form}
    return render(request, 'accounts/register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    context={}
    return render(request, 'accounts/login.html',context)

def profilePage(request):
    name = request.user.username
    mail = request.user.email
    company = Company.objects.filter(user = request.user).first()
    context = {'name':name,'mail':mail,'company':company}
    return render(request,'accounts/profile.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

