from django.urls import path
from .views import (
    ListDataTableView,
    RetrieveUpdateDestroyDataTableAPIView,
    CreateDataTableAPIView,
)


urlpatterns = [
    path("create/", CreateDataTableAPIView.as_view(), name="create"),
    path("list-data/", ListDataTableView.as_view(), name="list-data"),
    path(
        "rud-data/<str:code>",
        RetrieveUpdateDestroyDataTableAPIView.as_view(),
        name="rud-data",
    ),
]
