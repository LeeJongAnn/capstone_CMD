from django.shortcuts import render,redirect
from .forms import Postform
from .models import Write,Answer
# Create your views here.


def index(request):
    question_list = Write.objects.order_by('-create_date')
    return render(request, 'index.html', {'question_list': question_list})

def login(request):
    return render(request,'login.html')


def postcreate(request):

    if request.method == 'POST' or request.method == 'FILES':
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = Postform()

    return render(request,'post_form.html',{'form' : form})
