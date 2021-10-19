from django.shortcuts import render
from index.models import Name
# Create your views here.
def history(request):
    obj = Name.objects.all()
    return render(request,"history/history.html",{'obj':obj})