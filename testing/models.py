from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from datetime import datetime

# Create your models here.
class Users(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=10, unique=True)
    #createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.username

class Daily_Tasks(models.Model):
    permission_classes = (IsAuthenticated,)
    taskName = models.CharField(max_length=230, default='')
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=20, default='pending')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')
    taskCadence = models.CharField(max_length=20, default='Daily')
    taskDate = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.taskName
