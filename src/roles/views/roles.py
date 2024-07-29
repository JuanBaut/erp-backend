from rest_framework import generics

from roles.models.roles import Roles
from roles.serializers import RolesSerializer


class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


# class RolesUpdate(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Roles.objects.all()
#    serializer_class = RolesSerializer
#    lookup_field = "pk"
