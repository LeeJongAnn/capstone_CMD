from django.db import models
from django.conf import settings
# Create your models here.


class Question(models.Model):

    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):

    answer = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
