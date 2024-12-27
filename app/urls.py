from django.urls import path
from .views import ListDataTableView



urlpatterns = [
    path('list-data/', ListDataTableView.as_view(), name="list-data"),
]
