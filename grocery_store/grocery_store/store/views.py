from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from core.clen_up import clean_image_files
from grocery_store.store.forms import ProductCreateForm
from grocery_store.store.models import Category, Product


def index(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'grocery/index.html', context)


def list_products(request):
    products = Product.objects.all()

    context = {
        'categories': Category.objects.all(),
        'products': products,

    }
    return render(request, 'grocery/items-list.html', context)


def list_category_products(request, pk):
    category = Category.objects.get(pk=pk)

    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category__id=category.id)

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
        'categories': Category.objects.all(),
        'form': form,
    }

    return render(request, 'grocery/product/add-product.html', context)


@login_required
def product_details(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'categories': Category.objects.all(),
        'product': product,
        'can_edit': request.user.has_perm('auth.change_product'),
        'can_delete': request.user.has_perm('auth.delete_product'),
    }
    return render(request, 'grocery/product/product-details.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        # old_image = product.image
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # if old_image:
            #     clean_image_files(old_image.path)
            form.save()
            return redirect('product details', pk)
    else:
        form = ProductCreateForm(instance=product)

    context = {
        'categories': Category.objects.all(),
        'form': form,
        'product': product,
    }

    return render(request, 'grocery/product/edit-product.html', context)


@login_required
def delete_products(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'categories': Category.objects.all(),
            'product': product,
        }

        return render(request, 'grocery/product/delete-product.html', context)

    else:
        product.delete()
        return redirect('list products')
