from rest_framework import generics

from roles.models.employees import Employees
from roles.serializers import EmployeesSerializer


class EmployeesView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    lookup_field = "pk"
