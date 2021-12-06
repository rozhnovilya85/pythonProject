from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    context = {
        'basket_list': Basket.objects.filter(user=request.user)
    }
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user, product=product_item).first()
    if not basket_item:
        basket_item = Basket(
            user=request.user,
            product=product_item
        )
    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))