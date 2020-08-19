from django.shortcuts import get_object_or_404
from store.models import Product


def cart_content(request):
    """
    Return the cart context variables

    :return dictionary
    """

    cart_products = []
    cart_total = 0
    cart_count = 0
    cart = request.session.get('cart', {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_total += product.base_price * quantity
        cart_count += quantity
        cart_products.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_products': cart_products,
        'cart_total': cart_total,
        'cart_count': cart_count,
    }

    return context
