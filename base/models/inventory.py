from django.db import models


class Inventory(models.Model):
    fruit_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ("IN_WAREHOUSE", "In Warehouse"),
        ("SOLD", "Sold"),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="IN_WAREHOUSE"
    )

    def __str__(self):
        return f"{self.fruit_name} (QTY: {self.quantity})"
