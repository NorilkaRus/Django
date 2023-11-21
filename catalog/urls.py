from django.urls import path
from django.contrib import admin
from catalog.views import index, home, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home', home),
    path('contacts', contacts),
]