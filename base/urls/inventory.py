from django.urls import path
from base.views import inventory

urlpatterns = [
    path(
        "create/",
        inventory.InventoryView.as_view(),
        name="inventory_create_view",
    ),
    path(
        "update/",
        inventory.InventoryUpdate.as_view(),
        name="inventory_update_view",
    ),
]
