from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "ecommerce/index.html", context=context)

def indexProduct(request, product_id):
    return HttpResponse("Your product id is: " + str(product_id))

def contacts(request):
    return render(request, "ecommerce/contacts.html")
