from django.urls import path
from .views import ListDataTableView, RetrieveUpdateDestroyDataTableAPIView


urlpatterns = [
    path("list-data/", ListDataTableView.as_view(), name="list-data"),
    path(
        "rud-data/<str:code>",
        RetrieveUpdateDestroyDataTableAPIView.as_view(),
        name="rud-data",
    ),
]
