from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def store(request):
    """View returning the Store landing page"""

    products = Product.objects.all()

    query_string = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

        if 'q' in request.GET:
            query_string = request.GET['q']
            queries = Q(name__icontains=query_string) | Q(
                description__icontains=query_string)
            products = products.filter(queries)

    context = {
        'products': products,
        'query_string': query_string,
    }

    return render(request, 'store/store.html', context=context)


def product_details(request, product_id):
    """View returning a product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'store/product_details.html', context=context)
