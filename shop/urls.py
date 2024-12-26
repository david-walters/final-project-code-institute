from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfume/<int:pk>/', views.perfume_detail, name='perfume_detail'),
    path('cart/', views.cart, name='cart'),
]