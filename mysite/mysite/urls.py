from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),

    #  http://127.0.0.1:8000/
    path("", include("ecommerce.urls", namespace="ecommerce"))
]
