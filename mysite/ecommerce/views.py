from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    items = Product.objects.all()
    return HttpResponse(items)

def contacts(request):
    return render(request, "ecommerce/contacts.html")
