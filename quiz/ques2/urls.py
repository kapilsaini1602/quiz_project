from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('question2/<int:id>', views.ques2,name="ques2"),
]
