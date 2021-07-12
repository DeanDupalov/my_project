from django.shortcuts import render


# Create your views here.
from grocery_store.store.models import Category, Product


def index(request):
    context = {
    }
    return render(request, 'grocery/index.html', context)


def list_products(request):
    first_product = Product.objects.first()
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'grocery/items-list.html', context)
