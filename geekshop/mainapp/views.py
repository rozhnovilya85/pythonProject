
from django.conf import settings
from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.



def index(request):

    products_list = Product.objects.all()[:4]
    context = {
        'products': products_list
    }

    return render(request, 'mainapp/index.html', context)

# links_menu = [
#
#     {'link_name': 'home', 'name': 'Дом'},
#     {'link_name': 'modern', 'name': 'Модерн'},
#     {'link_name': 'office', 'name': 'Офис'},
#     {'link_name': 'classic', 'name': 'Классика'},
# ]

def products(request, pk=None):
    links_menu = ProductCategory.objects.all()

    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, 'mainapp/products.html', context)






def contact(request):
    return render(request, 'mainapp/contact.html')

