from django.http.response import HttpResponse
# from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Goal_for_month
from .models import ToDo



def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")    


def second(request):
    return HttpResponse("test2")


def news(request):
    Goal_list = Goal_for_month.objects.all()
    return render(request,"news.html", {"Goal_list":Goal_list})

    
def test(request):
    todo_list = ToDo.objects.all(),
    return render(request,"test.html",{"todo_list":todo_list})