from django.db import models
from roles.models.permissions import Permissions


class Roles(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField(Permissions)

    def __str__(self):
        return self.name
