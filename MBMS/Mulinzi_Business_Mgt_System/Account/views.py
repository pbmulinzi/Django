from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'Account/Dashboard.html')

def products(request):
    return render(request, 'Account/Products.html')

def customers(request):
    return render(request, 'Account/Customer.html')