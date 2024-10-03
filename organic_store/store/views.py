from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart  # Ensure you have your Cart class implemented

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = Cart(request)  # Initialize the cart from the session
    product = get_object_or_404(Product, id=product_id)  # Get the product

    # Add product to the cart
    cart.add(product)  # Ensure your Cart class has an add method

    return redirect('product_list')  # Redirect to the correct view name

def cart_view(request):
    cart = Cart(request)
    cart_items = cart.get_items()  # Should return an iterable of (key, value)
    total_items = cart.get_total_items()
    total_price = cart.get_total_price()
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price,
    })
def remove_from_cart(request, product_id):
    cart = Cart(request)  # Initialize the cart
    product = get_object_or_404(Product, id=product_id)  # Get the product object
    cart.remove(product)  # Now pass the product object
    return redirect('cart_view')  # Redirect to the cart view

def remove_all_from_cart(request):
    if request.method == "POST":
        cart = Cart(request)  # Initialize the cart
        cart.clear()  # Assuming your Cart class has a clear method
        return redirect('cart_view')  # Redirect to the cart view

def checkout(request):
    # Implement your checkout logic here
    return render(request, 'store/checkout.html')

def checkout_product(request, product_id):
    # Logic for checking out the product
    cart = Cart(request)  # Initialize the cart
    product = get_object_or_404(Product, id=product_id)  # Get the product object
    cart.remove(product) 
    return redirect('checkout')  # Change to your actual checkout URL name