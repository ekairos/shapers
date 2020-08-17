from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User


@login_required
def profile(request):
    """View returning Profile page"""

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

    profile_form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
    }

    return render(request, 'profile/profile.html', context=context)


@login_required()
def delete_account(request):
    """Deletes a user account"""

    user = request.user

    User.objects.get(username=user.username).delete()

    return redirect(reverse('home'))
