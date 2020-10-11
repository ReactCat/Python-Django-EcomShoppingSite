"""Store URL Configuration"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name="store"),
    path('category/<slug:category_slug>', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.productPage, name='product_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('thankyou/<int:order_id>', views.thankyou_page, name='thankyou_page'),
    path('contact', views.contact, name="contact"),
]
