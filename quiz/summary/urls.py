from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [

    path('summary/<int:id>',views.summary,name="summary"),
]