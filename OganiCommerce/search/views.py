from django.shortcuts import get_object_or_404, render
from django.contrib.postgres.search import SearchVector
from store.models import Product
from .forms import SearchForm

# Create your views here.


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    print(request.GET)
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            results = Product.objects.annotate(
                search=SearchVector('name', 'description'),).filter(search=query)
    return render(request, 'store/product/search_products.html', {'query': query, 'results': results})
