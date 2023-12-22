from django.urls import path
from django.contrib import admin
from catalog.views import IndexListView, ContactsPageView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
