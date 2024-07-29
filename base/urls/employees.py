from django.urls import path
from base.views import employees

urlpatterns = [
    path(
        "create/",
        employees.EmployeesView.as_view(),
        name="employees_create_view",
    ),
]
