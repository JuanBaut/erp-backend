from django.db import models
from django.contrib.auth.models import User
from roles.models.roles import Roles


class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role.name if self.role else 'No Role'}"

    def has_permission(self, model, action):
        if self.role:
            return self.role.permissions.filter(model=model, action=action).exists()
        return False
