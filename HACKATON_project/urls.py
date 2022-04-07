from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('admin/', admin.site.urls),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)