from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from core.clen_up import clean_image_files
from grocery_store.store.forms import ProductCreateForm, ContactForm
from grocery_store.store.models import Category, Product, DiscountProduct


class IndexView(TemplateView):
    template_name = 'grocery/index.html'

    def get_context_data(self, **kwargs):
        products = list(Product.objects.order_by('id'))[-3:]

        return {
            'categories': Category.objects.all(),
            'products': products,
            'discounted_products': DiscountProduct.objects.all(),
        }


class ListAllProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'grocery/items-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context




def list_category_products(request, pk):
    category = Category.objects.get(pk=pk)

    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category__id=category.id)

    }
    return render(request, 'grocery/items-list.html', context)


class ListCategoryProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'grocery/items-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    # fields = '__all__'
    template_name = 'grocery/product/add-product.html'
    success_url = reverse_lazy('list products')
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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


@login_required
def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }

            message = "\n".join(body.values())

            try:
                send_mail(subject, message, '', ['cantacts.groceryproject@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.info(request, "Your message has been sent!")
            return redirect('contact')

    context = {
        'form': ContactForm(),
    }

    return render(request, 'grocery/contact.html', context)
