from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionForm , AnswerForm
from .models import Write,Answer
from django.utils import timezone
# Create your views here.

# 첫화면
def index(request):
    question_list = Write.objects.order_by('-create_date')
    return render(request, 'index.html', {'question_list': question_list})


# 디테일 페이지 추가
def detail(request,question_id):

    question_id = get_object_or_404(Write,pk = question_id)
    context = {'question_id':question_id}
    return render(request,'detail.html',context)


# 로그인 사이트 연결
def login(request):
    return render(request,'login.html')

# 질문등록


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'post_form.html', context)


def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Write, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
# ---------------------------------- [edit] ---------------------------------- #
    return redirect('detail', question_id=question.id)

