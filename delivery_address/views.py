from django.shortcuts import render

def delivery_address(request):
    return render(request, 'delivery_address/delivery_address.html')

def edit_delivery_address(request):
    return render(request, 'delivery_address/edit_delivery_address.html')
