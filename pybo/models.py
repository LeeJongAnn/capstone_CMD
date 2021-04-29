from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
import datetime

class Question(models.Model):
    Car_num = models.CharField(max_length=15)
    Car_variety = models.CharField(max_length=10)
    Car_manager = models.CharField(max_length=10)
    bussiness_num = models.CharField(max_length=15)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


def __str__(self):
    return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class CMD_Information(models.Model):

    Car_num = models.CharField(max_length=15)
    Car_variety = models.CharField(max_length=10)
    Car_manager = models.CharField(max_length=10)
    cmd_bussiness_num = models.CharField(max_length=15)
    start_date = models.DateTimeField(null=True, blank=True)

    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    position_start = models.CharField(max_length=10)
    position_end = models.CharField(max_length=10)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
         return self.Car_num



class CMD_Answer(models.Model):
    question = models.ForeignKey(CMD_Information, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

