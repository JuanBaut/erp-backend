from rest_framework import generics

from .serializers import InventorySerializer
from .models.inventory import Inventory as Inventory


class InventoryView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "pk"
