from decimal import Decimal
from django.db import models
from rest_framework.serializers import ValidationError

from .inventory import Inventory


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
    ]
    inventory_item = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (
            self.transaction_type == "SELL"
            and self.quantity > self.inventory_item.quantity
        ):
            raise ValidationError("Cannot sell more items than available in inventory.")

    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.quantity) * self.price_per_unit
        self.clean()
        super().save(*args, **kwargs)
        if self.transaction_type == "BUY":
            self.inventory_item.quantity += self.quantity
        elif self.transaction_type == "SELL":
            self.inventory_item.quantity -= self.quantity
            if self.inventory_item.quantity == 0:
                self.inventory_item.status = "SOLD"
        self.inventory_item.save()

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.inventory_item.fruit_name} on {self.date}"
