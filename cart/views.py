from django.shortcuts import render


def get_cart(request):
    """Returns the cart content"""

    context = {
        'key': 'value',
    }

    return render(request, 'cart/cart.html', context=context)
