from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product, Version


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        products = context['products']
        product_version = {}
        for product in products:
            active_version = Version.objects.filter(product=product, is_active=True).first()
            product_version[product.id] = active_version
        context['product_version'] = product_version
        return context


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'
    context_object_name = 'product'


