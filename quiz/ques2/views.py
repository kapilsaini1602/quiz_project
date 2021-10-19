from django.shortcuts import render,HttpResponse,redirect
from index.models import Name
# Create your views here.
def ques2(request,id):
    if request.method=="POST":
        radio = request.POST.get('radio1')
        obj = Name.objects.filter(id=id).update(question1=radio)
    return render(request,'ques2/ques2.html',{'id':id})





