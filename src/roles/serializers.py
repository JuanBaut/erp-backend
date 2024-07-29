from rest_framework import serializers

from .models.roles import Roles
from .models.employees import Employees
from .models.permissions import Permissions


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = "__all__"
