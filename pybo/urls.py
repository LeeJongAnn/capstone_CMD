from django.urls import path

from . import views
from . import views_drive
from . import views_business

app_name = 'pybo'

urlpatterns = [

    # <--------------- 공용차량등록일지 관련 ---------------- >
    path('drive_list/', views_drive.CMD_index, name='CMD_index'),
    path('drive_list/<int:cmd_question_id>/', views_drive.CMD_detail, name='CMD_detail'),
    path('drive_list/answer/create/<int:cmd_question_id>/', views_drive.CMD_answer_create, name='CMD_answer_create'),
    path('drive_list/question/create/', views_drive.CMD_question_create, name='CMD_question_create'),
    path('static/', views.static, name='static'),
    path('', views.index, name='index'),
    # <--------------- 직원등록 --------------------->

    path('apply/', views_business.employee_apply, name='employee'),
    path('apply/<int:business_list_id>/', views_business.employee_detail, name='employee_detail'),
    path('apply/apply_create', views_business.employee_create, name='employee_create'),
    path('apply/employee_answer', views_business.employee_answer, name='employee_answer'),

    # <---------------- 공용차량 등록관련 화면 ------------------->
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
