from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def store(request):
    """View returning the Store landing page"""

    products = Product.objects.all()

    query_string = None
    query_categories = None
    query_sorting = None

    if request.GET:

        if 'category' in request.GET:
            query_categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=query_categories)

        if 'q' in request.GET:
            query_string = request.GET['q']
            queries = Q(name__icontains=query_string) | Q(
                description__icontains=query_string)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            sort_by = sort
            if sort_by == 'price':
                sort_by = 'base_price'
            elif sort_by == 'date':
                sort_by = 'date_version'

            if 'direction' in request.GET:
                sort_direction = request.GET['direction']
                if sort_direction == 'desc':
                    sort_by = f'-{sort_by}'
                query_sorting = f'{sort}_{sort_direction}'
            products = products.order_by(sort_by)

    context = {
        'products': products,
        'query_string': query_string,
        'query_categories': query_categories,
        'query_sorting': query_sorting,
    }

    return render(request, 'store/store.html', context=context)


def product_details(request, product_id):
    """View returning a product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'store/product_details.html', context=context)
