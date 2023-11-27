from django.urls import path
from django.contrib import admin
from catalog.views import index, contacts, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path("product/<int:pk>/", product_detail, name="product-detail"),
]