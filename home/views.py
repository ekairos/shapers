from django.shortcuts import render


def home(request):
    """View returning Home page"""

    return render(request, 'home/index.html')


def about_us(request):
    """View returning About Us page"""

    return render(request, 'home/about_us.html')


def privacy_policy(request):
    """View returning Shapers Privacy Policy"""

    return render(request, 'home/privacy_policy.html')
