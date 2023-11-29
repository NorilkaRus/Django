from django.shortcuts import render
from catalog.models import Product
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.

# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list' : product_list
#     }
#     return render(request, 'catalog/index.html', context)

class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'index'
    }

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'catalog/contacts.html')

class ContactsPageView(View):
    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)

# def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     product = get_object_or_404(Product, pk=pk)
#     ctx = {
#         "object": product
#     }
#     return render(request, template_name='catalog/product.html', context=ctx)

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'title': f'{product.name}'
        }
        return render(request, 'catalog/product_detail.html', context)