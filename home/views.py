from django.shortcuts import render


def home(request):
    """View returning Home page"""

    return render(request, 'home/index.html')
