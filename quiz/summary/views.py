from django.shortcuts import render,HttpResponse
from index.models import Name
# Create your views here.
def summary(request,id):

    if request.method=="POST":
        color = request.POST.getlist('checks[]')
        color = str(color)
        color = color.translate({ord(i): None for i in "['']"})
        obj = Name.objects.filter(id=id).update(question2=color)
        user = Name.objects.filter(id=id)
        print(user)
        return render(request, 'summary/summary.html',{'user':user})



    return render(request,'summary/summary.html')








