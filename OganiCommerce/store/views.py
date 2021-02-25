from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)
    return render(request, 'store/index.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'store/product/detail.html', {'product': product})


# def category_list(request, category_slug):
#     categories = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=categories)
#     return render(request, 'store/product/category.html', {'cat': categories, 'products': products})
