from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeliveryAddress
from .forms import DeliveryAddressForm
from django.contrib import messages 

@login_required
def delivery_address(request):
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

@login_required
def edit_delivery_address(request):
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
