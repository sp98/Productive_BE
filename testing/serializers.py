from rest_framework import serializers
from . import models

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Users
        fields=('id', 'email', 'username', 'createdOn')

class Daily_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('taskName', 'taskDescription', 'taskStatus', 'user')

class Weekly_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('taskName', 'taskDescription', 'taskStatus', 'user')

class Monthly_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('taskName', 'taskDescription', 'taskStatus', 'user')
