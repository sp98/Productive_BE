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
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField(default='')
    taskStatus = models.CharField(max_length=10, default='pending')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')
    taskCadence = models.CharField(max_length=20)
    taskDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.taskName

class Monthly_tasks(models.Model):
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=230)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskName

class Weekly_tasks(models.Model):
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=230)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskName
