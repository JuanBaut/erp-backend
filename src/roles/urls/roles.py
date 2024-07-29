from django.urls import path
from roles.views import roles

urlpatterns = [
    path(
        "create/",
        roles.RolesView.as_view(),
        name="roles_create_view",
    ),
    # path(
    #    "update/",
    #    roles.RolesUpdate.as_view(),
    #    name="roles_update_view",
    # ),
]
