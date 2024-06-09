from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='list'),
    path('<slug:slug>/', views.BlogPostDetailView.as_view(), name='detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='create'),
    path('<slug:slug>/update/', views.BlogPostUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.BlogPostDeleteView.as_view(), name='delete'),
]