from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from grocery_store.store.forms import ProductCreateForm
from grocery_store.store.models import Category, Product


def index(request):
    context = {}
    return render(request, 'grocery/index.html', context)


def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products,

    }
    return render(request, 'grocery/items-list.html', context)


@login_required
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


@login_required
def product_details(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
    }
    return render(request, 'grocery/product-details.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product details', pk)
    else:
        form = ProductCreateForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'grocery/edit-product.html', context)


@login_required
def delete_products(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'product': product,
        }

        return render(request, 'grocery/delete-product.html', context)

    else:
        product.delete()
        return redirect('list products')
