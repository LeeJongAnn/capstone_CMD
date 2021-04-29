from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer,CMD_Information
from .forms import QuestionForm, AnswerForm,CMD_TravelForm,CMD_AnswerForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index2(request):
    cmd_list = CMD_Information.objects.order_by('-create_date')
    context = {'cmd_list': cmd_list}
    return render(request, 'pybo/drive_list.html', context)

def cmd_detail(request, cmd_id):
    cmd= get_object_or_404(CMD_Information, pk=cmd_id)
    context = {'cmd': cmd}
    return render(request, 'pybo/drive_detail.html', context)



@login_required(login_url='common:login')
def cmd_question_create(request):
    if request.method == 'POST':
        form = CMD_TravelForm(request.POST)
        if form.is_valid():
            cmd_question = form.save(commit=False)
            cmd_question.create_date = timezone.now()
            cmd_question.author = request.user
            cmd_question.save()
            return redirect('pybo:index2')
    else:
        form = CMD_TravelForm()
    context = {'form': form}
    return render(request, 'pybo/question_form2.html', context)


@login_required(login_url='common:login')
def cmd_answer_create(request, cmd_id):
    cmd_list = get_object_or_404(CMD_Information, pk=cmd_id)
    if request.method == "POST":
        form = CMD_AnswerForm(request.POST)
        if form.is_valid():
            cmd_list = form.save(commit=False)
            cmd_list.create_date = timezone.now()
            cmd_list.author = request.user
            cmd_list.cmd_list = cmd_list
            cmd_list.save()
            return redirect('pybo:cmd_detail', cmd_id=cmd_list.id)
    else:
        form = CMD_AnswerForm()
    context = {'cmd_list': cmd_list, 'form': form}
    return render(request, 'pybo/drive_detail.html', context)

