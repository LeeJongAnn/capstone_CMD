from django import forms
from pybo.models import Question,Answer,CMD_Information,CMD_Answer


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

class CMD_TravelForm(forms.ModelForm):
    class Meta:
        model = CMD_Information
        fields = ['Car_num','cmd_bussiness_num','start_date',
                  'time_end','time_start','position_start','position_end']

        labels = {

            'Car_num':'차량번호',
            'cmd_bussiness_num': '사번',
            'start_date': '운행날짜',
            'time_start': '시작시간',
            'time_end': '종료시간',
            'position_start': '시작장소',
            'position_end':'도착장소'

        }

class CMD_AnswerForm(forms.ModelForm):
    class Meta:
        model = CMD_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


