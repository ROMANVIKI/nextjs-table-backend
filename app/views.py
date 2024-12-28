from django.shortcuts import render
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


class RetrieveUpdateDestroyDataTableAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    permission_classes = [AllowAny]
