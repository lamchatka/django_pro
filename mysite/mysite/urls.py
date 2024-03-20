from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),

    #  http://127.0.0.1:8000/
    path("", include("ecommerce.urls", namespace="ecommerce")),
    path("", include("users.urls", namespace="users")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
