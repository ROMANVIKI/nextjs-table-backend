from asyncio import wait
from django.db import models
from django.contrib.auth.models import User
from django.utils import choices
# Create your models here.

    # code: "TASK-7393",
    # title: "We need to program the redundant EXE array!",
    # status: "todo",
    # priority: "medium",
    # archived: false,
    # createdAt: new Date("Thu Dec 26 2024 07:54:59 GMT+0530")

class DataTable(models.Model):
    STATUS_CHOICES = {

        "Done":"Done", 
        "Todo":"Todo",
        "In-Progress":"In-Progress",
        "Canceled":"Canceled",
    } 
    PRIORITY_CHOICES = {
        "Low":"Low",
        "Medium":"Medium", 
        "High":"High",
    }


    
    code = models.CharField(max_length=50, unique=True)
    title = models.TextField(max_length=100)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES)
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    

