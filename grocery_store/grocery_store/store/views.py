from django.shortcuts import render, redirect

# Create your views here.
from grocery_store.store.forms import ProductCreateForm
from grocery_store.store.models import Category, Product


def index(request):
    context = {
    }
    return render(request, 'grocery/index.html', context)


def list_products(request):

    products = Product.objects.all()

    context = {
        'products': products,

    }
    return render(request, 'grocery/items-list.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list products')
    else:
        form = ProductCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'grocery/add-product.html', context)


def details_product(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
    }
    return render(request, 'grocery/product-details.html', context)


def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProductCreateForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'grocery/edit-product.html', context)


def delete_products(request, pk):
    pass
