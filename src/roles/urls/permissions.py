from django.urls import path
from roles.views import permissions

urlpatterns = [
    path(
        "create/",
        permissions.PermissionsView.as_view(),
        name="permissions_create_view",
    ),
    path(
        "update/",
        permissions.PermissionsUpdate.as_view(),
        name="permissions_update_view",
    ),
]
