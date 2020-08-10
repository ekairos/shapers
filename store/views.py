from django.shortcuts import render, get_object_or_404
from .models import Product


def store(request):
    """View returning the Store landing page"""

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'store/store.html', context=context)


def product_details(request, product_id):
    """View returning a product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'store/product_details.html', context=context)
