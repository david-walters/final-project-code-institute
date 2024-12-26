from django.db import models
from django.contrib.auth.models import User
from shop.models import Perfume


class CartItem(models.Model):
    """
    Represents an item in the user's shopping cart.

    This model associates a user with a specific perfume item, its selected size, 
    and the quantity added to the cart. It also stores the calculated total price 
    for the item based on the quantity and base price.

    Attributes:
        user (ForeignKey): The user who owns this cart item. Linked to the User model.
        perfume (ForeignKey): The perfume item being added to the cart. Linked to the Perfume model.
        size (CharField): The size variant of the perfume (e.g., '25 ml', '50 ml').
        quantity (PositiveIntegerField): The quantity of this item in the cart. Defaults to 1.
        total_price (DecimalField): The calculated total price for this item. Updated on save.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=24.00)

    def save(self, *args, **kwargs):
        """
        Override the save method to dynamically calculate and update the total price.

        The total price is calculated as the product of the quantity and a fixed
        base price (24). This ensures the price reflects any changes in the quantity.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.total_price = 24 * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the cart item.

        The string includes the name of the perfume, its size, and quantity 
        for easy identification.

        Returns:
            str: A readable representation of the cart item.
        """
        return f"{self.perfume.name} ({self.size}) x {self.quantity}"