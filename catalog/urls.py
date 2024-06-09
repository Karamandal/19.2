from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductsDetailView, ProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products_detail')
]