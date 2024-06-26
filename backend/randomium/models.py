from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

RATINGS_CHOICES = [
    ("good", "Good"),
    ("average", "Average"),
    ("poor", "Poor"),
]


class Bank(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=63, choices=RATINGS_CHOICES)
    address = models.ForeignKey(
        "Address", on_delete=models.CASCADE, related_name="banks"
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, blank=True, null=True)

    def clean(self):
        super().clean()
        if self.postal_code is not None and len(self.postal_code) < 5:
            raise ValidationError(_("Postal code must be at least 5 characters long."))

    class Meta:
        unique_together = [["street", "city", "country"]]

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
