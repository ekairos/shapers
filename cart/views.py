from django.shortcuts import render
from store.models import Product
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib import messages


def get_cart(request):
    """Returns the cart content"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """View adding a given product to the Cart"""

    redirect_to = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))

    try:

        messages.success(request, f"Added {quantity} {product} to your cart")

        cart = request.session.get('cart', {})

        if product_id in cart.keys():
            cart[product_id] = cart[product_id] + quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart

    except Exception:
        messages.error(request, f'Sorry, couldn\'t add {product}'
                                f'to your cart.')
    return redirect(redirect_to)


def remove_from_cart(request, product_id):
    """View removing a product from the cart"""

    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)

    try:
        cart.pop(product_id)
        request.session['cart'] = cart

        messages.success(request, f"Removed {product} from your cart")
    except Exception:
        messages.error(request, f'Sorry, we couldn\'t remove {product}'
                                f'from your cart.')
    return redirect(reverse('get_cart'))


def update_cart(request, product_id):
    """View updating the quantity of a given product in the cart"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart')

    try:
        if quantity > 0:
            cart[product_id] = quantity
            request.session['cart'] = cart
            messages.success(request, f"You have now {quantity} of {product} "
                                      f"in your cart")
        else:
            cart.pop(product_id)
            messages.success(request, f"Removed {product} from your cart")

    except Exception:
        messages.error(request, f'Error while updating your {product}')

    return redirect(reverse('get_cart'))


def decrement_cart_product(request, product_id):
    """View decrementing the quantity of a given product in the cart"""

    product = get_object_or_404(Product, pk=product_id)

    try:
        cart = request.session.get('cart')

        if cart[product_id] > 1:
            cart[product_id] -= 1
            request.session['cart'] = cart
            messages.success(request, f"You have now {cart[product_id]} of "
                                      f"{product} in your cart")
        else:
            cart.pop(product_id)
            request.session['cart'] = cart
            messages.success(request, f"{product} has been removed from "
                                      f"your cart")
    except Exception:
        messages.error(request, f'Error while updating your {product}')
    return redirect(reverse('get_cart'))


def increment_cart_product(request, product_id):
    """View incrementing the quantity of the given product in the cart"""

    product = get_object_or_404(Product, pk=product_id)
    try:
        cart = request.session.get('cart')

        cart[product_id] += 1
        request.session['cart'] = cart
        messages.success(request, f"You have now {cart[product_id]} of "
                                  f"{product} in your cart")
    except Exception:
        messages.error(request, f'Error while updating your {product}')
    return redirect(reverse('get_cart'))
