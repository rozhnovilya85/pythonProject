from django.urls import path, include
from mainapp import views as mainapp

app_name = 'products'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    # path('products/modern/', mainapp.products_modern, name='products_modern'),
    # path('products/office/', mainapp.products_office, name='products_office'),
    # path('products/classic/', mainapp.products_classic, name='products_classic'),
]