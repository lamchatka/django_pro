from django.urls import path
from .views import add_product, index, contacts, indexProduct

app_name="ecommerce"

urlpatterns = [
    #  http://127.0.0.1:8000/
    path('', index),

    #  http://127.0.0.1:8000/1/
    path('<int:product_id>/', indexProduct, name="detail"),

    #  http://127.0.0.1:8000/contacts/
    path('contacts/', contacts),

    path('addproduct/', add_product)
]
