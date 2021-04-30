from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm,CMD_QuestionForm
from .models import CMD_Question,CMD_Answer


def CMD_index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = CMD_Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/drive_list.html', context)


def CMD_detail(request, question_id):
    question = get_object_or_404(CMD_Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/drive_detail.html', context)


def CMD_answer_create(request, question_id):
    question = get_object_or_404(CMD_Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('pybo:CMD_detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/drive_detail.html', context)


def CMD_question_create(request):

    if request.method == 'POST':
        form = CMD_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:CMD_index')
    else:
        form = CMD_QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form2.html', context)
