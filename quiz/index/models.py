from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    question1 = models.CharField(max_length=50,default=0)
    question2 = models.CharField(max_length=50,default=0)
