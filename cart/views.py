from django.shortcuts import render
from store.models import Product
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def get_cart(request):
    """Returns the cart content"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """View adding a given product to the Cart"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_to = request.POST.get('redirect_url')

    messages.success(request, f"Added {quantity} {product} to your cart")

    cart = request.session.get('cart', {})

    if product_id in cart.keys():
        cart[product_id] = cart[product_id] + quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_to)
