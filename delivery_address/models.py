from django.db import models
from django.contrib.auth.models import User

class DeliveryAddress(models.Model):
    """
A model representing a user's delivery address.

Attributes:
    user (OneToOneField): A one-to-one relationship with the User model, linking each delivery address to a specific user.
    street_address (CharField): The street and house/building information for the delivery address.
    city (CharField): The city name associated with the delivery address.
    postal_code (CharField): The postal code or ZIP code of the delivery address.
    country (CharField): The country name for the delivery address.
    phone_number (CharField): An optional phone number for the user, allowing for contact related to deliveries.

Methods:
    __str__: Returns a string representation of the delivery address, showing the username and their address information.
"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="delivery_address")
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Delivery Address"
