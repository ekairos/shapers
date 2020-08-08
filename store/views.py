from django.shortcuts import render


def store(request):
    """View returning the Store landing page"""

    return render(request, 'store/store.html')
