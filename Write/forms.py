from django import forms
from .models import Write,Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'
       # fields = ['subject','content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:

        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }