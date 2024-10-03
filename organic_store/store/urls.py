# store/urls.py
from django.urls import path
from .views import product_list, add_to_cart, cart_view, remove_from_cart
from .views import cart_view, remove_all_from_cart, checkout, checkout_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/remove_all/', remove_all_from_cart, name='remove_all_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('checkout_product/<int:product_id>/', checkout_product, name='checkout_product'),
]
