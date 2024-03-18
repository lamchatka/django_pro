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

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES['upload']
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "ecommerce/addProduct.html")
