from django.urls import path
from base.views import transactions

urlpatterns = [
    path(
        "create/",
        transactions.TransactionView.as_view(),
        name="transactions_create_view",
    ),
]
