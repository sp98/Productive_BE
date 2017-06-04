
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from . import models

# Create your views here.

# List all the users
# Class based API Views.
class ListUsers(APIView):
    def get(self, request, format=None):
        users = models.Users.objects.all()
        serializer = serializers.User_Serializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)

class CreateUser(APIView):
    def post(self, request, format=None):
        print("Hi Everyone")

# Generic Views.
# ListCreateAPIView helps to list and Create API Views.
class ListCreateUsers(generics.ListCreateAPIView):
    queryset = models.Users.objects.all()
    serializer_class = serializers.User_Serializer

class RetrieveUpdateDestroyUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Users.objects.all()
    serializer_class = serializers.User_Serializer

class ListCreateDailyTasks(generics.ListCreateAPIView):
    queryset = models.Daily_Tasks.objects.all()
    serializer_class = serializers.Daily_Task_Serializer

    def get_queryset(self):
        return self.queryset.filter(users_id=self.kwargs.get('user_id'))

class RetrieveUpdateDestroyDailyTasks(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Daily_Tasks.objects.all()
    serializer_class = serializers.Daily_Task_Serializer
