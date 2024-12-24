from django.db import models
from django.contrib.auth.models import User

class DeliveryAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="delivery_address")
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Delivery Address"
