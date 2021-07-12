from django.contrib import admin

from grocery_store.store.models import Category, Product, Like

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Like)
