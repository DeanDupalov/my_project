from django.contrib import admin

from grocery_store.store.models import Category, Product, Like, DiscountProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscountProduct)
class DiscountProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Product)
# admin.site.register(Like)
# admin.site.register(Category)
