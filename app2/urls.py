#coding=utf-8
from django.urls import path
from . import views
app_name='app2'
urlpatterns=[
    path('<int:question_id>/',views.details,name='details'),
]