# shop/urls.py
from django.urls import path
from .views import (
    CategoryListCreateAPIView, CategoryDetailView,
    ProductListCreateAPIView, ProductDetailView
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
