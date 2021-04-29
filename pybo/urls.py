from django.urls import path

from . import views
from . import views_drive

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('drive_list/', views_drive.index2, name='index2'),
    path('drive_list/request/', views_drive.cmd_question_create, name='cmd_question_create'),
    path('drive_list/<int:cmd_id>/', views_drive.cmd_detail, name='cmd_detail'),
    path('drive_list/create/<int:cmd_id>/', views_drive.cmd_answer_create, name='cmd_answer_create'),


    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
