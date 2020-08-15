from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import UserProfile


@login_required
def profile(request):
    """View returning Profile page"""

    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user_profile': user_profile
    }

    return render(request, 'profile/profile.html', context=context)
