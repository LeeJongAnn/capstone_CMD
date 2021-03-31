from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionForm
from .models import Write,Answer
from django.utils import timezone
# Create your views here.


def index(request):
    question_list = Write.objects.order_by('-create_date')
    return render(request, 'index.html', {'question_list': question_list})


def detail(request,question_id):

    question_id = get_object_or_404(Write,pk = question_id)
    context = {'question_id':question_id}
    return render(request,'detail.html',context)

def login(request):
    return render(request,'login.html')


def question_create(request):
    """
    pybo 질문등록
    """
# ---------------------------------- [edit] ---------------------------------- #
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
# ---------------------------------------------------------------------------- #

