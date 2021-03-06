from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('grocery_store.grocery_auth.urls')),
    path('', include('grocery_store.store.urls')),
    path('product/', include('grocery_store.product.urls')),
    path('profiles/', include('grocery_store.profiles.urls')),
    path('cart/', include('grocery_store.cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
