from rest_framework import generics

from base.serializers import InventorySerializer
from base.models.inventory import Inventory


class InventoryView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "pk"
