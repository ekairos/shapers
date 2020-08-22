from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from profile.models import UserProfile
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import OrderLineProduct


@login_required
def checkout(request):
    """View returning checkout page and processing payment logic"""

    if request.user.is_anonymous:
        messages.error(request, 'You need to be logged in to proceed.')
        return redirect('account_login')

    cart_content = request.session.get('cart', {})

    if not cart_content:
        messages.error(request, "Your cart is empty ! Add something in ;)")
        return redirect(reverse('store'))

    if request.POST:
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_process = order_form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            order_process.user_profile = user_profile
            order_process.save()
            for product_id, quantity in cart_content.items():
                try:
                    product = Product.objects.get(id=product_id)
                    OrderLineProduct.objects.create(
                        order=order_process,
                        product=product,
                        quantity=quantity,
                    )
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We couldn't process your order. You have not "
                        "been charged. Please try again or contact us.")
                    )
                    order_process.delete()
                    return redirect(reverse('get_cart'))

    else:
        user_profile = UserProfile.objects.get(user=request.user)
        order_form = OrderForm(initial={
            'full_name': f'{user_profile.user.first_name} '
                         f'{user_profile.user.last_name}',
            'email': request.user.email,
            'phone_number': user_profile.profile_phone_number,
            'street_address1': user_profile.profile_street_address1,
            'street_address2': user_profile.profile_street_address2,
            'postcode': user_profile.profile_postcode,
            'town_or_city': user_profile.profile_town_or_city,
            'country': user_profile.profile_country,
        })

    context = {
        'order_form': order_form,
        'cart_content': cart_content
    }

    return render(request, 'checkout/checkout.html', context=context)
