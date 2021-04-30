from django import forms
from pybo.models import Question,Answer,CMD_Question


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

class CMD_QuestionForm(forms.ModelForm):
    class Meta:
        model = CMD_Question
        fields = [ 'Car_num','bussiness_num','bussiness_manager','start_date',
                   'start_pos','destination_pos','depart_date','arrive_date']

        labels = {
            'Car_num':'선택차량번호',
            'bussiness_num':'사번',
            'bussiness_manager':'운행 책임자',
            'start_pos':'출발위치',
            'destination_pos':'도착위치',
            'start_date':'운행날짜',
            'depart_date':'출발시간',
            'arrive_date':'도착시간'
        }

# class CMD_AnswerForm(forms.ModelForm):
#     class Meta:
#         model = CMD_Answer
#         fields = ['content']
#         labels = {
#             'content': '답변내용',
#         }


