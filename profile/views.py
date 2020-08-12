from django.shortcuts import render


def profile(request):
    """View returning Profile page"""

    return render(request, 'profile/profile.html')
