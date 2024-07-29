from rest_framework import generics

from base.serializers import EmployeesSerializer
from base.models.employees import Employees


class EmployeesView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
