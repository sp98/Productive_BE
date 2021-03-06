import json
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404
from django.contrib.auth import authenticate

from . import serializers
from . import models
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your views here.

# List all the users
# Class based API Views.

class CreateUser(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        print(request.data)
        return(Response("hi"))

class validateUserName(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        #print(request.data)
        user = request.data.get('username')
        email = request.data.get('email')
        print('Check for user {}'.format(user))
        if(models.Users.objects.filter(username__iexact=user).exists()):
            return Response("This User Name is Taken")
        else:
            return Response("User Validated Successfully")

# Generic Views.
# ListCreateAPIView helps to list and Create API Views.
class ListUsers(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Users.objects.all()
    serializer_class = serializers.User_Serializer

class SignUpUsers(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Users.objects.all()
    serializer_class = serializers.User_Serializer

class loginUser(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print(password)
        user = models.Users.objects.all().filter(email=email, password=password)
        #print(user[0].id)
        if user.count() > 0:
            print(user[0])
            token, created = Token.objects.get_or_create(user=user[0])
            print(token.key)
            return Response({'token': token.key , 'user_id': user[0].id } )
        else:
            return Response("Invalid email or password")


class logoutUser(APIView):
    def post(self, request, format=None):
        print(request.user)
        request.user.auth_token.delete()
        #models.Users.objects.all().filter(id=request.data.get('user_id')).auth_token_delete()
        return Response("Logged Out successfully");

class RetrieveUpdateDestroyUsers(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Users.objects.all()
    serializer_class = serializers.User_Serializer

class ListCreateDailyTasks(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Daily_Tasks.objects.all()
    serializer_class = serializers.Daily_Task_Serializer

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs.get('user_id'))

   # Right when the object is created by the view:
    def perform_create(self, serializer):
        user = get_object_or_404(models.Users, pk=self.kwargs.get('user_id'))
        serializer.save(user=user)

class fetchTasks(APIView):
    def post(self, request, format=None):
        tasks =models.Daily_Tasks.objects.all().filter(user=request.user, taskCadence=request.data.get('cadence'), taskDate=request.data.get('date'))
        serializer = serializers.Daily_Task_Serializer(tasks, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        print(request.user)

class RetrieveUpdateDestroyDailyTasks(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = models.Daily_Tasks.objects.all()
    serializer_class = serializers.Daily_Task_Serializer

    def get_object(self):
        return get_object_or_404(
        self.get_queryset(),
        user_id=self.kwargs.get('user_id'),
        pk= self.kwargs.get('pk')
        )

class CreateFetchDeleteUpdateTasks(APIView):

    def post(self, request, format=None):
        task = request.data
        task['user'] = request.user  # adding user to the task dict
        models.Daily_Tasks(**task).save() #saving the new task
        print(task.get('taskCadence'))
        updated_tasks = models.Daily_Tasks.objects.all().filter(user=request.user,
                                taskCadence=task.get('taskCadence'), taskDate=task.get('taskDate'))
        serializer = serializers.Daily_Task_Serializer(updated_tasks, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        print(request.GET)
        return Response('hi get')
    def put(self, request, format=None):
        return Repsonse('hi put')
    def delete(self, request, format=None):
        print(request.data);
        for task in request.data:
            print(task.get('id'))
            to_be_deleted = models.Daily_Tasks.objects.all().filter(user=request.user, id=task.get('id'))
            if not to_be_deleted:
                return Http404('Task Not found')
            else:
                to_be_deleted.delete();
        updated_tasks = models.Daily_Tasks.objects.all().filter(user=request.user,
                                taskCadence=task.get('taskCadence'), taskDate=task.get('taskDate'))
        serializer = serializers.Daily_Task_Serializer(updated_tasks, many=True)
        return Response(serializer.data)
