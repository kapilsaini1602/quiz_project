from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('queston1', views.ques1,name="ques1"),
    path('question1/<int:id>', views.question1,name="question1"),
]
