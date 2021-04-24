from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone

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
    author = models.ForeignKey(User,on_delete=models.CASCADE)
#
# class CMD_Information(models.Model):
#
#     Car_num = models.CharField(max_length=15)
#     Car_variety = models.CharField(max_length=10)
#     Car_manager = models.CharField(max_length=10)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     # time_start = models.DateTimeField()
#     # time_end= models.DateTimeField()
#     # position_start = models.TextField()
#     # position_end = models.TextField()
#     user_num = models.CharField(verbose_name="사번",max_length=20)
#     # def __str__(self):
#     #     return self.subject
#
