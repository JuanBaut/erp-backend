from django.db import models


class Permissions(models.Model):
    MODELS = [
        ("inventory", "Inventory"),
        ("transaction", "Transaction"),
        ("employee", "Employee"),
    ]
    ACTIONS = [
        ("create", "Create"),
        ("read", "Read"),
        ("update", "Update"),
        ("delete", "Delete"),
    ]

    model = models.CharField(max_length=20, choices=MODELS)
    action = models.CharField(max_length=10, choices=ACTIONS)

    class Meta:
        unique_together = ["model", "action"]

    def __str__(self):
        return f"{self.get_action_display()} {self.get_model_display()}"  # type: ignore
