from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from grocery_store.product.forms import ProductCreateForm, DiscountProductForm
from grocery_store.product.models import Product, Category, DiscountProduct


def product_details(request, pk):
    is_discounted = False
    discounted_product = DiscountProduct.objects.filter(product_id=pk)
    if discounted_product:
        product = discounted_product[0]
        is_discounted = True
    else:
        product = Product.objects.get(pk=pk)

    context = {
        'categories': Category.objects.all(),
        'product': product,
        'is_discounted': is_discounted,
        'can_edit': request.user.has_perm('auth.change_product'),
        'can_delete': request.user.has_perm('auth.delete_product'),
    }
    return render(request, 'grocery/product/product-details.html', context)


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'grocery/product/add-product.html'
    success_url = reverse_lazy('list products')
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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


class AddDiscountProduct(LoginRequiredMixin, CreateView):
    model = DiscountProduct
    form_class = DiscountProductForm
    template_name = 'grocery/product/add-discounted_product.html'
    success_url = reverse_lazy('landing page')



