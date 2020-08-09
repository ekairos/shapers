from django.shortcuts import render
from .models import Product


def store(request):
    """View returning the Store landing page"""

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'store/store.html', context=context)
