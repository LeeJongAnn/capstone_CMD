from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,redirect
from .forms import business_applyform
from django.utils import timezone
from .models import business_apply


def employee_apply(request):
    business_list = business_apply.objects.order_by('-create_date')
    context = {'business_list': business_list}
    return render(request,'pybo/apply_form.html')



def employee_list(request,business_list_id):
    business_list = get_object_or_404(business_apply, pk=business_list_id)
    context = {'business_list': business_list}
    return render(request, 'pybo/apply_detail.html', context)



def employee_create(request):

    if request.method == 'POST':
        form = business_applyform(request.POST)
        if form.is_valid():
            employee_question = form.save(commit=False)
            employee_question.create_date = timezone.now()
            employee_question.author = request.user
            employee_question.save()
            return redirect('pybo:employee')
    else:
        form = business_applyform()
    context = {'form': form}
    return render(request, 'pybo/apply_form.html', context)
