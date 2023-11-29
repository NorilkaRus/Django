from django.urls import path
from django.contrib import admin
from catalog.views import IndexListView, ContactsPageView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]