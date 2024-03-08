from django.urls import path
from .views import index, contacts, indexProduct
urlpatterns = [
    #  http://127.0.0.1:8000/
    path('', index),

    #  http://127.0.0.1:8000/1/
    path('<int:product_id>/', indexProduct),

    #  http://127.0.0.1:8000/contacts/
    path('contacts/', contacts),

]