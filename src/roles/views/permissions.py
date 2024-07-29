from rest_framework import generics

from roles.models.permissions import Permissions
from roles.serializers import PermissionsSerializer


class PermissionsView(generics.ListCreateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer


class PermissionsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    lookup_field = "pk"
