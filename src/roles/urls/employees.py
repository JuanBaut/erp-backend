from django.urls import path
from roles.views import employees

urlpatterns = [
    path(
        "create/",
        employees.EmployeesView.as_view(),
        name="employees_create_view",
    ),
    path(
        "update/",
        employees.EmployeesUpdate.as_view(),
        name="employees_update_view",
    ),
]
