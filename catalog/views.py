from django.shortcuts import render
from catalog.models import Product
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list' : product_list
    }
    return render(request, 'catalog/index.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

def product(request: HttpRequest, pk: int) -> HttpResponse:
    path("product/<int:pk>", product, name="product"),
    product = get_object_or_404(Product, pk=pk)
    ctx = {
        "product": product
    }
    return render(request, template_name="product.html", context=ctx)