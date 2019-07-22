#coding=utf-8
from django.urls import path
from . import views
app_name='polls'
urlpatterns=[
    path('',views.IndexView.as_view()),
    path('<int:pk>/',views.DetailsView.as_view(),name='details'),
    path('<int:question_id>/results',views.results,name='result'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('<int:year>/<int:month>/<int:day>',views.date),
]