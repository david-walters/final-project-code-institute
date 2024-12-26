import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from cart.models import CartItem

"""
Handles the finalization of purchases and the redirection for success or cancellation.

Functions:
    finalise_purchase(request):
        - Validates user authentication and cart contents.
        - Creates a Stripe Checkout session with line items derived from cart items.
        - Redirects the user to the Stripe Checkout page for payment processing.

    success(request):
        - Renders a success page upon successful payment completion.

    cancel(request):
        - Renders a cancellation page if the user cancels the payment.

Stripe Integration:
    - Utilizes Stripe API for secure payment processing.
    - Creates dynamic line items based on the user's cart and calculates total prices.
    - Redirects to custom success or cancellation URLs after payment.
"""

stripe.api_key = settings.STRIPE_SECRET_KEY

def finalise_purchase(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    line_items = [
        {
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': item.perfume.name,
                },
                'unit_amount': int(item.perfume.price * 100),
            },
            'quantity': item.quantity,
        }
        for item in cart_items
    ]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/finalise_purchase/success/'),
        cancel_url=request.build_absolute_uri('/finalise_purchase/cancel/'),
    )

    return redirect(session.url, code=303)

def success(request):
    return render(request, 'finalise_purchase/success.html')

def cancel(request):
    return render(request, 'finalise_purchase/cancel.html')
