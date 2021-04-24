from django import forms
from pybo.models import Question,Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['Car_num','bussiness_num','Car_variety','Car_manager']
        labels = {

            'Car_num':'차량번호',
            'Car_variety':'차량종류',
            'Car_manager':'차량책임자',
            'bussiness_num': '사번'

        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

