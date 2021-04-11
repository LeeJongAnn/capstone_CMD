from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

class CMD_Information(models.Model):

    Car_num = models.CharField(max_length=15)
    Car_variety = models.CharField(max_length=10)
    Car_manager = models.CharField(max_length=10)
    time_start = models.DateTimeField(null=True,blank=True)
    time_end= models.DateTimeField(null=True,blank=True)
    position_start = models.TextField()
    position_end = models.TextField()

    modify_date = models.DateTimeField(verbose_name="수정날짜",null=True, blank=True)
    user_num = models.IntegerField(verbose_name="사번")
