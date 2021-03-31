from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import SearchForm
# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        return render(request, 'store/product/category.html', {'category': category, 'categories': categories, 'products': products})
    else:
        return render(request, 'store/index.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product/category.html', {'product': product, 'cart_product_form': cart_product_form})


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.annotate(
                search=SearchVector('name', 'description'),).filter(search=query)
    return render(request, 'store/product/search_products.html', {'query': query, 'results': results})

# def category_list(request, category_slug):
#     categories = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=categories)
#     return render(request, 'store/product/category.html', {'cat': categories, 'products': products})
