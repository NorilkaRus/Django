from django.urls import path
from catalog.views import index, home, contacts

urlpatterns = [
    path('', index),
    path('home', home),
    path('contacts', contacts),
]