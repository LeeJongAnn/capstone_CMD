from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [


    path('',views.index),
    path('postcreate', views.postcreate,name='postcreate'),
    path('index',views.index,name = 'index'),
    path('login',views.login,name = 'login'),
    path('detail/<int:question_id>',views.detail,name = 'detail')

]