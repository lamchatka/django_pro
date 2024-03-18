from django.urls import path
from .views import add_product, index, contacts, indexProduct, update_product, delete_product

app_name="ecommerce"

urlpatterns = [
    #  http://127.0.0.1:8000/
    path('', index, name="index"),

    #  http://127.0.0.1:8000/1/
    path('<int:product_id>/', indexProduct, name="detail"),

    #  http://127.0.0.1:8000/contacts/
    path('contacts/', contacts),

    #  http://127.0.0.1:8000/addproduct/
    path('addproduct/', add_product, name='add_product'),

    #  http://127.0.0.1:8000/updateproduct/1/
    path('updateproduct/<int:product_id>/', update_product, name='update_product'),

    #  http://127.0.0.1:8000/deleteproduct/1/
    path('deleteproduct/<int:product_id>/', delete_product, name='delete_product'),

]
