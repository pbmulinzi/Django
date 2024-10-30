from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, "account/Dashboard.html")

def customers(request):
    return render(request, "account/Customers.html")

def products(request):
    return render(request, "account/Products.html")