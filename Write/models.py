from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Write(models.Model):

    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class Answer(models.Model):

    answer = models.ForeignKey(Write,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
