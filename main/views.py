from django.http.response import HttpResponse
from django.shortcuts import render





def homepage(request):
    return HttpResponse("Hello world")

def test(request):
    return render(request, "test.html")    


def second(request):
    return HttpResponse("test2")