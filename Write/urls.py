from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [


    path('',views.index),
    path('question_create', views.question_create,name='question_create'),
    path('index',views.index,name = 'index'),
    # path('login',views.login,name = 'login'),
    path('detail/<int:question_id>',views.detail,name = 'detail'),
    path('answer_create/<int:question_id>',views.answer_create,name='answer_create')
]