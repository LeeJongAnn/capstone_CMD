from django.shortcuts import render,redirect
from .models import Question,Answer
# Create your views here.



def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'index.html', context)