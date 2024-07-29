from rest_framework import generics

from .serializers import InventorySerializer, TransactionSerializer
from .models.inventory import Inventory
from .models.transactions import Transaction


class InventoryView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    lookup_field = "pk"


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
