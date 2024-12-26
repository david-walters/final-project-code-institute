from django.db import models

class Perfume(models.Model):
    """
    Represents a perfume product with attributes for name, size, price, description, image URL, and gender.

    Attributes:
        SIZE_CHOICES: Available sizes for the perfume (25 ml, 50 ml, 75 ml).
        GENDER_CHOICES: Gender options for the perfume (Male, Female).
        name: The name of the perfume.
        size: The size of the perfume bottle, chosen from SIZE_CHOICES.
        price: The price of the perfume, determined by its size.
        description: A text description of the perfume.
        image_url: A URL to an image of the perfume.
        gender: The target gender for the perfume, chosen from GENDER_CHOICES.

    Methods:
        save: Overrides the save method to automatically set the price based on the selected size.
        __str__: Returns a string representation of the perfume including its name, gender, and size.
    """
    SIZE_CHOICES = [
        ("25 ml", "25 ml"),
        ("50 ml", "50 ml"),
        ("75 ml", "75 ml"),
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default="25 ml")
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=24.00)
    description = models.TextField()
    image_url = models.URLField(default="https://ibb.co/YLWps0V")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        """Set the price based on size before saving."""
        size_price_map = {
            "25 ml": 24.00,
            "50 ml": 36.00,
            "75 ml": 60.00,
        }
        self.price = size_price_map[self.size]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()}) - {self.get_size_display()}"
