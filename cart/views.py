from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Sum
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from shop.models import Perfume

@login_required(login_url='register')
def cart(request):
    """
    Display the cart page with all items added by the authenticated user.

    The function retrieves all cart items associated with the currently logged-in user.
    It calculates the total price for each cart item and the overall cart total.
    The results are passed to the 'cart.html' template for rendering.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered 'cart.html' template with the user's cart items and total price.
    """
    cart_items = CartItem.objects.filter(user=request.user).annotate(
        calculated_total_price=F('quantity') * F('perfume__price')
    )
    
    total_cart_price = cart_items.aggregate(total=Sum(F('quantity') * F('perfume__price')))['total'] or 0.00

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_price': total_cart_price})


@login_required
def add_to_cart(request, perfume_id):
    """
    Add a perfume item to the user's cart or update its quantity if already present.

    The function retrieves the selected perfume and checks if it exists in the user's cart.
    If the item exists, its quantity is updated. Otherwise, a new cart item is created.
    After the operation, the user is redirected to the cart page.

    Args:
        request: The HTTP request object.
        perfume_id: The ID of the perfume being added.

    Returns:
        A redirect to the 'cart' view.
    """
    perfume = get_object_or_404(Perfume, id=perfume_id)
    size = request.POST.get('size')
    quantity = int(request.POST.get('quantity', 1))

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        perfume=perfume,
        size=size
    )
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    """
    Remove an item from the authenticated user's cart.

    The function checks if the user is authenticated and attempts to delete the
    specified cart item. If successful, the user is redirected to the cart page.

    Args:
        request: The HTTP request object.
        cart_item_id: The ID of the cart item to be removed.

    Returns:
        A redirect to the 'cart' view.
    """
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()

    return redirect('cart')