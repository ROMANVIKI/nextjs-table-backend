from django.shortcuts import get_object_or_404, render, get_list_or_404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import DataTableSerializer
from .models import DataTable
from rest_framework.permissions import IsAdminUser, AllowAny


class ListDataTableView(ListAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    permission_classes = [AllowAny]


class CreateDataTableAPIView(CreateAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    permission_classes = [AllowAny]


class RetrieveUpdateDestroyDataTableAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return get_object_or_404(DataTable, code=self.kwargs["code"])
