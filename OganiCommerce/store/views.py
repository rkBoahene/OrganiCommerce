from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def product_list(request):
    categories = Category.objects.all()

    return render(request, 'store/index.html', {'categories': categories})
