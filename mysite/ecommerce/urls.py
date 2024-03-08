from django.urls import path
from .views import index, contacts
urlpatterns = [
    #  http://127.0.0.1:8000/
    path('', index),

    #  http://127.0.0.1:8000/contacts/
    path('contacts/', contacts),
]