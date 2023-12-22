from django.shortcuts import render
from catalog.models import Product, Version
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404



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

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     # queryset = queryset.filter(public_sign=True)
    #     return queryset

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:  # для зарегистрированных пользователей
            if user.is_staff or user.is_superuser:  # для работников и суперпользователя
                queryset = super().get_queryset().order_by('pk')

            else:  # для остальных пользователей
                # Получаем queryset, результат фильтрации по условию owner=user
                queryset_1 = super().get_queryset().filter(owner=self.request.user).order_by('pk')
                # Получаем queryset, результат фильтрации по условию is_published=True
                queryset_2 = super().get_queryset().filter(is_published=True).order_by('pk')
                # Объединяем два queryset с использованием метода union()
                queryset = queryset_2.union(queryset_1)
                # queryset = super().get_queryset().filter(owner=user).order_by('pk')

        else:  # для незарегистрированных пользователей
            queryset = super().get_queryset().filter(
                is_published=True).order_by('-pk')
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.all()
        return context


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
            'object': product,
            'title': f'{product.title}'
        }
        return render(request, 'catalog/product.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


    def get_form_class(self):
        return super().get_form_class()


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog_app.set_is_published',
            'catalog_app.set_category',
            'catalog_app.set_description',
        )

        if _user == _instance.user:
            return True
        elif _user.groups.filter(name='moders') and _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
