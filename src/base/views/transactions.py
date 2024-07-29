from rest_framework import generics

from base.serializers import TransactionSerializer
from base.models.transactions import Transaction


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
