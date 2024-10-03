# store/cart.py
from .models import Product  # Import Product model

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'name': product.name  # Store the product name
            }
        self.cart[product_id]['quantity'] += quantity
        self.save()


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def get_items(self):
        return self.cart.items()  # This should yield (product_id, item) pairs


    def get_total_items(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(details['price']) * details['quantity'] for details in self.cart.values())
    def clear(self):
        self.cart = {}
        self.save()
