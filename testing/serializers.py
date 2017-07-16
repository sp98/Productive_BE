from rest_framework import serializers
from . import models

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Users
        fields=('id', 'email', 'username', 'password')

class Daily_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('id', 'taskName', 'taskDescription', 'taskStatus', 'user', 'taskDate', 'taskCadence')

class Weekly_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('id', 'taskName', 'taskDescription', 'taskStatus', 'user')

class Monthly_Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Daily_Tasks
        fields=('id', 'taskName', 'taskDescription', 'taskStatus', 'user')
