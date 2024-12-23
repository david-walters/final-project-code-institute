from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_address, name='delivery_address'),
    path('edit/', views.edit_delivery_address, name='edit_delivery_address'),
]
