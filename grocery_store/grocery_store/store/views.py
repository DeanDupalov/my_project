from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from grocery_store.product.models import Product, Category, DiscountProduct
from grocery_store.store.forms import ContactForm


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
        'categories': Category.objects.all(),
    }

    return render(request, 'grocery/contact.html', context)
