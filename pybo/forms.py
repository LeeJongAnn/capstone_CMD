from django import forms
from pybo.models import Question,Answer,CMD_Information


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


# 공용차량등록폼

class CMDForm(forms.ModelForm):
    class Meta:
        model = CMD_Information
        fields = ['Car_num','Car_variety','Car_manager','user_num']
        labels = {
            'Car_num':'차량번호',
            'Car_variety':'차종',
            'Car_manager':'차량관리자',
            'user_num':'사번'
        }