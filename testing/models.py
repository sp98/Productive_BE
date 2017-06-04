from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=12)
    username = models.CharField(max_length=10, unique=True)
    createdOn = models.DateTimeField('date published')

    def __str__(self) :
        return self.email

class Daily_Tasks(models.Model):
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=230)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.taskName

class Monthly_tasks(models.Model):
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=230)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskName

class Weekly_tasks(models.Model):
    taskName = models.CharField(max_length=230)
    taskDescription = models.TextField()
    taskStatus = models.CharField(max_length=230)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskName
