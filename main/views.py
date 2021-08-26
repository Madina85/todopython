
from django.http.response import HttpResponse
# from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Goal_for_month
from .models import ToDo
from .models import ToMeet
from .forms import HabitsForm



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
    todo_list = ToDo.objects.all()
    return render(request,"test.html", {"todo_list":todo_list})

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request,"meeting.html", {"tomeet_list":tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)   


def habits(request):
    if request.method == 'POST':
        form = HabitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(habits)
     

    form = HabitsForm()
    data = {
        'form':form,
        
    }
    
    return render(request, "habits.html", data)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)    



def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def mark_undo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)



def delete_tomeet(request, id):
    meet = ToMeet.objects.get(id=id) 
    meet.delete()
    return redirect(meeting)   


