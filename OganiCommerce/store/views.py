from django.shortcuts import render

from .models import Category, Product


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/base.html', context)
