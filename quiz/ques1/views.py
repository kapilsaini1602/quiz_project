from django.shortcuts import render,HttpResponse,redirect
from index.models import Name
# Create your views here.
def ques1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        obj = Name.objects.create(name=name)
        obj.save()
        return redirect(f"question1/{obj.id}")

def question1(request,id):

    return render(request, 'ques1/ques1.html',{'id':id})

