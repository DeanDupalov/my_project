from django.contrib import admin

from grocery_store.product.models import Category, Product, DiscountProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscountProduct)
class DiscountProductAdmin(admin.ModelAdmin):
    pass


