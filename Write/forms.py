from django import forms
from .models import Write


class Postform(forms.ModelForm):
    class Meta:
        model = Write
        fields = '__all__'
       # fields = ['subject','content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }