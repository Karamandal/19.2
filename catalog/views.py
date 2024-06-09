from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def form_valid(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
        return super().get(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'


