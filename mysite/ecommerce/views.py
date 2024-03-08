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
    """
    Детальная страница продукта

    """
    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "ecommerce/detail.html", context=context)

def contacts(request):
    """
    Страница с контактными данными
    
    """
    return render(request, "ecommerce/contacts.html")
