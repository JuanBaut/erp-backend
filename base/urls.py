from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/",
        views.InventoryView.as_view(),
        name="inventory_create_view",
    ),
    path(
        "update/<int:pk>/",
        views.InventoryDelete.as_view(),
        name="inventory_delete_view",
    ),
]
