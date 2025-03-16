from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DeliveryAddress
from .forms import DeliveryAddressForm
from django.contrib import messages 

@login_required(login_url='login')
def delivery_address(request):
    """
    Handle the addition of a new delivery address for the logged-in user.

    If the request method is POST, the function processes the submitted delivery 
    address form. If the form is valid, it associates the address with the 
    current user and saves it. For GET requests, it renders an empty form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered template for the delivery address form or a 
        redirect to the index page upon successful form submission.
    """
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('index')
    else:
        form = DeliveryAddressForm()

    return render(request, 'delivery_address/delivery_address.html', {'form': form})

@login_required(login_url='login')
def edit_delivery_address(request):
    """
    Handle the editing of an existing delivery address for the logged-in user.

    This function retrieves the delivery address associated with the current 
    user. If the address doesn't exist, it redirects to the delivery address 
    creation view. If the request method is POST, it updates the delivery 
    address with the submitted form data. Otherwise, it displays the form 
    pre-filled with the existing address information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered template for editing the delivery address form 
        or a redirect to the same page upon successful form submission.
    """
    try:
        address = DeliveryAddress.objects.get(user=request.user)
    except DeliveryAddress.DoesNotExist:
        return redirect('delivery_address')

    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your delivery address has been successfully updated!')
            return redirect('edit_delivery_address')
    else:
        form = DeliveryAddressForm(instance=address)

    return render(request, 'delivery_address/edit_delivery_address.html', {'form': form})
